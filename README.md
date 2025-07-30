# ComfyUI Text Translator

一個為ComfyUI設計的文字翻譯自定義節點，支援多種翻譯服務。

## 功能特點

- 🌍 支援多種語言翻譯
- 🔄 多個翻譯服務提供商支援（Google、百度、DeepL）
- 🎯 簡潔易用的ComfyUI節點介面
- ⚙️ 可配置的API金鑰支援

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

## 安裝方法

### 方法1：透過ComfyUI Manager安裝（推薦）

1. 開啟ComfyUI Manager
2. 搜尋 "Text Translator"
3. 點選安裝

### 方法2：手動安裝

1. 複製此專案到ComfyUI的custom_nodes目錄：
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-TextTranslator.git
```

2. 安裝依賴套件：
```bash
cd ComfyUI-TextTranslator
pip install -r requirements.txt
```

3. 重新啟動ComfyUI

## 使用方法

1. 在ComfyUI中，從節點選單選擇 `text/translation -> Text Translator`
2. 輸入要翻譯的文字
3. 選擇源語言和目標語言
4. 選擇翻譯服務提供商
5. 如果使用付費API，請輸入對應的API金鑰

## 節點輸入

- **text**: 要翻譯的文字內容
- **source_language**: 源語言（支援自動檢測）
- **target_language**: 目標語言
- **translation_service**: 翻譯服務提供商
- **api_key**: API金鑰（可選，部分服務需要）

## 節點輸出

- **translated_text**: 翻譯後的文字

## API金鑰設定

### 百度翻譯
1. 註冊百度翻譯API
2. 獲取APP ID和密鑰
3. 在api_key欄位輸入格式：`APP_ID:SECRET_KEY`

### DeepL
1. 註冊DeepL API
2. 獲取API金鑰
3. 在api_key欄位直接輸入金鑰

## 注意事項

- Google翻譯目前使用免費版本，可能有使用限制
- 百度翻譯和DeepL需要有效的API金鑰
- 建議在生產環境中使用官方API服務

## 授權條款

MIT License

## 貢獻

歡迎提交Issue和Pull Request！

## 更新日誌

### v1.0.0
- 初始版本發布
- 支援基本的文字翻譯功能
- 支援多種翻譯服務提供商
