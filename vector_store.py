import os
import sys
from langchain_community.document_loaders import PyPDFLoader
# ✅ 修正點：從新的路徑導入
try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def build_knowledge_base(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"❌ 找不到檔案：{pdf_path}，請確認檔案路徑是否正確。")
        return

    # 1. 載入 PDF
    print(f"正在讀取檔案：{pdf_path}...")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # 2. 文本切割
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    texts = text_splitter.split_documents(documents)

    # 3. 選擇 Embedding 模型
    print("正在下載/載入 Embedding 模型 (all-MiniLM-L6-v2)...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. 建立向量資料庫並儲存
    print("正在建立向量資料庫，這會耗費一點 CPU 資源...")
    vector_db = FAISS.from_documents(texts, embeddings)
    vector_db.save_local("faiss_itce_index")
    print("\n✅ 成功！資料庫已儲存至 'faiss_itce_index' 資料夾。")

if __name__ == "__main__":
    # 執行前請確認 itce_exam.pdf 就在同一個資料夾下
    build_knowledge_base("data/itce_exam.pdf")