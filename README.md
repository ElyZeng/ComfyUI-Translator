# ComfyUI Translator

一個為ComfyUI設計的**離線**文字翻譯自定義節點，使用Argos Translate提供免費的本地翻譯服務。

## 功能特點

- 🌍 **完全離線**：無需網路連接即可使用
- 🆓 **完全免費**：無需API金鑰或付費服務
- 🔄 支援多種語言翻譯
- 🎯 簡潔易用的ComfyUI節點介面
- 🚀 基於Argos Translate的神經機器翻譯
- 🔍 自動語言檢測功能

## 支援的語言

- 中文 (zh)
- 英文 (en) 
- 日文 (ja)
- 韓文 (ko)
- 法文 (fr)
- 德文 (de)
- 西班牙文 (es)
- 義大利文 (it)
- 俄文 (ru)
- 阿拉伯文 (ar)
- 葡萄牙文 (pt)

## 安裝方法

### 方法1：透過ComfyUI Manager安裝（推薦）

1. 開啟ComfyUI Manager
2. 搜尋 "ComfyUI-Translator"
3. 點選安裝

### 方法2：手動安裝

1. 複製此專案到ComfyUI的custom_nodes目錄：
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ElyZeng/ComfyUI-Translator.git
```

2. 安裝依賴套件：
```bash
cd ComfyUI-Translator
pip install -r requirements.txt
```

3. 重新啟動ComfyUI

**注意**：首次使用時，節點會自動下載必要的語言模型包，這可能需要一些時間和網路連接。下載完成後即可完全離線使用。

## 使用方法

1. 在ComfyUI中，從節點選單選擇 `text/translation -> Text Translator`
2. 輸入要翻譯的文字
3. 選擇源語言（或選擇"auto"自動檢測）
4. 選擇目標語言
5. 執行節點即可獲得翻譯結果

## 節點輸入

- **text**: 要翻譯的文字內容
- **source_language**: 源語言（支援自動檢測）
- **target_language**: 目標語言

## 節點輸出

- **translated_text**: 翻譯後的文字

## 翻譯品質說明

- Argos Translate使用神經機器翻譯技術
- 翻譯品質對於常見語言對（如英中、英日等）表現良好
- 某些語言對可能需要通過英文中轉翻譯
- 完全離線運行，保護隱私安全

## 注意事項

- 首次使用需要下載語言模型（約幾百MB）
- 某些不常見的語言對可能翻譯品質較低
- 如果直接翻譯失敗，系統會自動嘗試英文中轉翻譯
- 完全免費使用，無使用次數限制

## 授權條款

MIT License

## 貢獻

歡迎提交Issue和Pull Request！

## 更新日誌

### v1.0.0
- 初始版本發布
- 基於Argos Translate的完全離線翻譯功能
- 支援11種主要語言
- 自動語言檢測功能
- 英文中轉翻譯支援
