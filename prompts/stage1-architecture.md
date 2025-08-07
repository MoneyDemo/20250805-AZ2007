# 階段一：專案架構設計與技術分析 PROMPT

## 任務概述
撰寫並執行本地版本控制流程下的專案初始化與架構設計步驟指令，供自動化代理執行。

## 具體指令

1. 在本機建立 Git 儲存庫，並切換到分支 `feature/architecture`。
2. 建立以下目錄結構：
   ```
   20250805-stock-web/
   ├── .env
   ├── .gitignore
   ├── README.md
   ├── CHANGELOG.md
   ├── requirements.txt
   ├── requirements-dev.txt
   ├── pytest.ini
   ├── config.py
   ├── app.py
   ├── run.py
   ├── src/
   ├── static/
   ├── templates/
   ├── tests/
   ├── docs/adr/
   ├── docs/architecture/
   └── prompts/
   ```
3. 依據專案指引建立設定檔案：
   - `.env`：填入基本環境變數項目。
   - `.gitignore`：包含 Python、Windows、虛擬環境與 IDE 忽略清單。
   - `requirements.txt`、`requirements-dev.txt`：包含必要的依賴套件。
   - `pytest.ini`：配置 pytest 運行參數與覆蓋率門檻。
   - `config.py`、`app.py`、`run.py`：實作 Flask 應用程式工廠模式與啟動程式。
4. 建立架構決策紀錄文件：
   - `docs/adr/001-api-selection.md`：說明選擇 twstock 的理由。
   - `docs/architecture/technical-decisions.md`：記錄技術棧與設計模式選擇。
5. 撰寫初始文件：
   - `README.md`：專案簡介、安裝與啟動步驟。
   - `CHANGELOG.md`：初始版本更新日誌。
6. 分步提交並推送：
   - 每項任務完成後執行獨立提交，訊息遵循 Conventional Commits。
   - 範例：`feat: initialize project structure and configuration`。

## 驗收項目
- 本機分支 `feature/architecture` 已建立並包含完整檔案與目錄結構。
- 所有設定檔與文件已根據指引生成。
- Git 提交紀錄完整且符合格式要求。
