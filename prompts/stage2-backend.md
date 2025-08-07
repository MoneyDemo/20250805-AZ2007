# 階段二：後端核心功能實作 PROMPT

## 任務概述
實作股票資料服務、API 路由、錯誤處理等後端核心功能，建立完整的後端邏輯層。

## 具體指令

1. 切換到新分支 `feature/backend-core`
2. 安裝並測試 twstock 函式庫：
   - 執行 `pip install twstock`
   - 測試基本 API 呼叫並驗證台股資料可正常取得
3. 實作資料模型層 (`src/models/stock.py`)：
   - 建立股票資料類別，包含股票代碼、價格、時間等屬性
   - 實作資料驗證與格式化方法
4. 實作業務邏輯服務層 (`src/services/stock_service.py`)：
   - 建立股票資料查詢服務類別
   - 整合 twstock API 呼叫
   - 實作錯誤處理與資料快取機制
5. 建立工具函式 (`src/utils/`)：
   - `errors.py`：自定義例外類別與錯誤處理裝飾器
   - `validators.py`：股票代碼格式驗證函式
6. 實作 API 路由 (`src/routes/api.py`)：
   - `/api/stock/<code>`：查詢特定股票價格
   - `/api/stock/refresh`：刷新股票資料
   - 實作 JSON 回應格式與狀態碼處理
7. 實作頁面路由 (`src/routes/views.py`)：
   - 首頁路由與基本頁面處理
   - 錯誤頁面路由
8. 更新主應用程式 (`app.py`)：
   - 註冊藍圖 (Blueprints)
   - 設定錯誤處理器
9. 建立基礎單元測試 (`tests/unit/`)：
10. 執行測試並確保覆蓋率達標：
 9. 建立基礎單元測試 (`tests/unit/`)：
    - 測試股票服務核心功能
    - 測試 API 路由回應
    - 測試錯誤處理機制
 10. 執行測試並確保覆蓋率達標：
     - 測試步驟已跳過
11. 分步提交並推送：
    - 每個元件完成後獨立提交
    - 提交訊息範例：`feat: implement stock data service with twstock integration`

## 驗收項目
- 所有後端元件已實作並可正常運作
- API 端點可正確回應股票資料查詢
- 錯誤處理機制完整且使用者友善
- 單元測試覆蓋率符合要求
- Git 提交紀錄完整且功能可獨立驗證
