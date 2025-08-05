# 台股價格即時顯示網站

一個簡單的台股價格查詢與即時顯示的 Web 應用程式。

## 功能特色

- 🔍 台股代碼查詢 (單一股票)
- 📈 即時價格顯示
- ⏰ 自動刷新機制
- 🌙 深色/淺色模式切換
- 📱 響應式設計

## 技術棧

- 後端：Flask
- 前端：Bootstrap 5 + Vanilla JavaScript
- 資料來源：twstock Python 函式庫
- 測試：pytest

## 快速開始

1. 建立虛擬環境並啟用：
   ```ps1
   python -m venv stock05env
   .\stock05env\Scripts\Activate.ps1
   ```
2. 安裝依賴：
   ```ps1
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
3. 建立並設定環境變數：
   ```ps1
   Copy-Item .env .env.local
   # 編輯 .env.local
   ```
4. 啟動應用程式：
   ```ps1
   python run.py
   ```
5. 在瀏覽器開啟 http://127.0.0.1:5000
