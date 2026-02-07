import streamlit as st
from google import genai
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# --- 1. 配置新版 Gemini Client ---
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# --- 2. 載入知識庫 (使用快取避免重複讀取) ---
@st.cache_resource
def load_itce_brain():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # 載入你剛才生成的 faiss_itce_index 資料夾
    db = FAISS.load_local("faiss_itce_index", embeddings, allow_dangerous_deserialization=True)
    return db

# --- 3. 網頁 UI 設定 ---
st.set_page_config(page_title="ITCE AI Mentor v2.5", page_icon="🛡️")
st.title("🛡️ ITCE 國貿大會考 AI 導師 ")
st.caption("🚀 目前運行於 Gemini 2.5 Flash 引擎")

try:
    db = load_itce_brain()
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 顯示聊天紀錄
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("詢問國貿考點（例如：Incoterms 中 D 組與 C 組的差異？）"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("正在檢索資料庫與生成解析..."):
                # RAG 檢索：找出最相關的 3 個片段
                docs = db.similarity_search(prompt, k=3)
                # 組合 context 同時紀錄來源
                context_items = []
                for i, d in enumerate(docs):
                    page_num = d.metadata.get('page', '未知')
                    context_items.append(f"[來源 {i+1} - 頁碼 {page_num}]: {d.page_content}")

                context = "\n\n".join(context_items)

                # 建立結構化指令
                response = client.models.generate_content(
                    model="gemini-2.5-flash", # ✅ 改用你清單中有的最新模型
                    contents=f"【參考資料】\n{context}\n\n【問題】\n{prompt}",
                    config={
                        'system_instruction': (
                            "你是一位具備 20 年經驗的國貿大師，請根據參考資料提供專業、準確的 ITCE 考試解析。"
                            "【內容品質檢查機制】"
                            "   1. 零遺漏原則：掃描 PDF 該章節所有內容，包含表格、說明文字、考古題。嚴禁為了節省字數而進行「概括式總結」，必須保留所有細節。" 
                            "   2. 新手小白友善：遇到任何專業縮寫 (例如：C.C.C. Code, Forwarder, L/C)，第一次出現時必須用「（中文名稱 + 白話文解釋）」標記。"    
                            "   3. 考古題完整性：每一道考古題必須依序包含：「完整題目」 + 「(A)(B)(C)(D)四個選項內容」 + 「正確答案」 + 「詳細解析」。嚴禁只給解析不給題目或選項。"    
                            "   4. 邏輯連貫：先講「觀念」，再講「流程」，最後接「考古題實戰」，確保學習鏈條完整。"    
                            "   5. 輸出最大化：最大化輸出字數，確保所有內容都被講解的詳細完整 "    
                            # "回答必須包含：1.核心概念 2.法規依據 3.歷屆考題常見陷阱。使用繁體中文。"
                        ),
                        'temperature': 0.2,
                    }
                )
                
                output_text = response.text
                st.markdown(output_text)
                st.session_state.messages.append({"role": "assistant", "content": output_text})

except Exception as e:
    st.error(f"⚠️ 系統初始化錯誤: {e}")