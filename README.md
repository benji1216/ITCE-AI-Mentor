# ⚖️ ITCE AI Mentor | 國貿大會考智慧導師
# High-Precision RAG System for Trade Regulations

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-4285F4)
![RAG](https://img.shields.io/badge/Architecture-RAG-ff69b4)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B)

<div align="center">
  <a href="https://itce-ai-mentor-bhx6gdcc27rbzpvd8e2xja.streamlit.app">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" width="250">
  </a>
</div>

<p align="center">
  <b>點擊上方按鈕進入「國貿大會考智慧導師」！</b>
</p>

## 📖 Project Overview (專案簡介)
This project implements a **Retrieval-Augmented Generation (RAG)** solution to assist students in preparing for the **International Trade Certified Expert (ITCE)** exam.

A specialized **Knowledge-Base System** powered by **Gemini 2.5 Flash** and **FAISS**. 

> **Data Source Note:** The knowledge base is built from official International Trade examination past papers documents.
> (**資料來源說明：** 本專案的知識庫建構自國貿大會考官網的考古題pdf文件。)

本專案實作了一個 **檢索增強生成 (RAG)** 解決方案，用於輔助學生準備 **國貿大會考 (ITCE)**。
為基於 **Gemini 2.5 Flash** 與 **FAISS** 的專用知識庫系統。

---

## 💻 How to Run (如何執行)

1.  **Clone the repository (複製專案)**
    ```bash
    git clone [https://github.com/YourUsername/ITCE-AI-Mentor.git](https://github.com/YourUsername/ITCE-AI-Mentor.git)
    cd ITCE-AI-Mentor
    ```

2.  **Install dependencies (安裝套件)**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup API Key (設定秘鑰)**
    Create a `.streamlit/secrets.toml` file in the root directory.
    在根目錄建立 `.streamlit/secrets.toml` 檔案。
    ```toml
    # .streamlit/secrets.toml
    GEMINI_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"
    ```

4.  **Run Application (啟動網頁)**
    ```bash
    streamlit run main.py
    ```

---

## 📂 Project Structure (檔案結構)
```text
ITCE-AI-Mentor/
├── data/                # Source PDFs (原始考題 PDF)
├── faiss_itce_index/    # Vector Database (預先訓練的向量庫)
├── .streamlit/          # Secrets & UI Config (金鑰與介面設定)
├── main.py              # Main Streamlit App (網頁主程式)
├── vector_store.py      # Data Ingestion Script (資料處理腳本)
├── requirements.txt     # Python Dependencies (套件清單)
└── README.md            # Project Documentation (專案說明)
