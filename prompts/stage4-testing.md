# 階段四：測試與文件撰寫 PROMPT

## 任務概述
完善測試覆蓋率、建立完整的專案文件、進行品質檢查與錯誤修復。

## 具體指令

1. 切換到新分支 `feature/testing-docs`
2. 完善單元測試 (`tests/unit/`)：
   - `test_models.py`：測試股票資料模型的所有方法
   - `test_services.py`：測試股票服務的業務邏輯與錯誤處理
   - `test_utils.py`：測試工具函式與驗證器
   - 確保單元測試覆蓋率達到 95% 以上
3. 實作整合測試 (`tests/integration/`)：
   - `test_api.py`：測試 API 端點的完整請求-回應流程
   - 測試 twstock API 整合功能
   - 測試錯誤情況與邊界條件
4. 設定測試環境與配置：
   - 建立 `tests/conftest.py`：pytest 設定與測試夾具
   - 設定模擬 (Mock) 物件以避免實際 API 呼叫
   - 建立測試資料與預期結果
5. 執行完整測試套件：
   - 執行 `pytest --cov=src --cov-report=html --cov-report=term`
   - 檢查測試覆蓋率報告
   - 修復任何測試失敗或覆蓋率不足的問題
6. 程式碼品質檢查：
   - 執行 `black src/ tests/` 進行程式碼格式化
   - 執行 `flake8 src/ tests/` 檢查程式碼風格
   - 執行 `mypy src/` 進行型別檢查
7. 完善專案文件：
   - 更新 `README.md`：
     - 加入完整的安裝與使用說明
     - 嵌入所有 Mermaid 架構圖表
     - 加入 API 使用範例
     - 加入常見問題排解
   - 更新 `CHANGELOG.md`：記錄所有功能變更
   - 建立 `docs/user-guide.md`：詳細使用者操作指南
   - 建立 `docs/api-reference.md`：API 端點說明文件
8. 建立開發者文件：
   - `docs/development-guide.md`：開發環境設定與貢獻指南
   - `docs/architecture/system-overview.md`：系統架構詳細說明
   - `docs/troubleshooting.md`：常見問題與解決方案
9. 進行端到端測試：
   - 手動測試完整的使用者流程
   - 測試各種股票代碼與錯誤情況
   - 驗證自動刷新功能在不同頻率下的表現
   - 測試主題切換與響應式設計
10. 效能與安全性檢查：
    - 檢查 API 回應時間與記憶體使用量
    - 驗證輸入驗證與 XSS 防護
    - 檢查錯誤訊息是否洩漏敏感資訊
11. 分步提交並推送：
    - 測試、文件、修復分別提交
    - 提交訊息範例：`test: add comprehensive unit and integration tests with 95% coverage`

## 驗收項目
- 測試覆蓋率達到要求標準 (整體 > 80%，核心邏輯 > 95%)
- 所有測試案例通過且穩定可重複
- 程式碼品質檢查無警告或錯誤
- 專案文件完整且準確
- README.md 包含所有必要的 Mermaid 圖表
- 端到端功能測試通過
- 效能與安全性符合要求
