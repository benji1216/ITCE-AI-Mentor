from google import genai
import sys

# 填入你的 API Key
API_KEY = "AIzaSyBc2NnjAjsQK5oikhKZygKGhMH3hrTxESs"

def diagnostic():
    print(f"🐍 Python 路徑: {sys.executable}")
    
    try:
        # 初始化 Client
        client = genai.Client(api_key=API_KEY)
        
        print("🔍 正在查詢你的帳戶可用的模型清單...\n")
        # 列出所有模型
        model_list = list(client.models.list())
        
        if not model_list:
            print("⚠️ 找不到任何模型，請檢查 API Key 是否正確。")
            return

        for m in model_list:
            # 輸出模型名稱與支持的功能
            print(f"可用模型名稱: {m.name}")
            
    except Exception as e:
        print(f"❌ 查詢失敗，錯誤訊息: {e}")

if __name__ == "__main__":
    diagnostic()