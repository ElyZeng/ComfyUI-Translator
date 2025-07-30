#!/usr/bin/env python3
"""
簡單的翻譯測試腳本
直接測試翻譯功能，無需ComfyUI環境
"""

try:
    import argostranslate.package
    import argostranslate.translate
    from typing import Dict, Any, Tuple
    import os
    
    print("✅ Argos Translate 模組載入成功")
except ImportError as e:
    print(f"❌ 缺少依賴模組: {e}")
    print("請先安裝依賴: pip install argostranslate")
    exit(1)


class SimpleTranslator:
    """
    簡化版翻譯器，用於測試
    """
    
    def __init__(self):
        print("🔧 初始化翻譯器...")
        self.language_mapping = {
            "en": "English",
            "zh": "Chinese",
            "ja": "Japanese", 
            "ko": "Korean",
            "fr": "French",
            "de": "German",
            "es": "Spanish",
            "it": "Italian",
            "ru": "Russian",
            "ar": "Arabic",
            "pt": "Portuguese"
        }
        self._ensure_language_packages()
    
    def _ensure_language_packages(self):
        """
        確保必要的語言包已安裝
        """
        try:
            print("📦 檢查語言包...")
            # 更新可用的語言包列表
            argostranslate.package.update_package_index()
            
            # 獲取已安裝的語言包
            installed_packages = argostranslate.package.get_installed_packages()
            print(f"已安裝的語言包數量: {len(installed_packages)}")
            
            # 基本語言對（最常用的翻譯方向）
            basic_language_pairs = [
                ("en", "zh"),  # 英文到中文
                ("zh", "en"),  # 中文到英文
                ("en", "ja"),  # 英文到日文
                ("en", "ko"),  # 英文到韓文
                ("en", "fr"),  # 英文到法文
                ("en", "de"),  # 英文到德文
                ("en", "es"),  # 英文到西班牙文
            ]
            
            # 檢查並安裝必要的語言包
            available_packages = argostranslate.package.get_available_packages()
            print(f"可用的語言包數量: {len(available_packages)}")
            
            for from_code, to_code in basic_language_pairs:
                # 檢查是否已安裝此語言對
                package_exists = any(
                    pkg.from_code == from_code and pkg.to_code == to_code 
                    for pkg in installed_packages
                )
                
                if not package_exists:
                    # 尋找並安裝語言包
                    package_to_install = next(
                        (pkg for pkg in available_packages 
                         if pkg.from_code == from_code and pkg.to_code == to_code),
                        None
                    )
                    
                    if package_to_install:
                        print(f"📥 正在安裝語言包: {from_code} -> {to_code}")
                        argostranslate.package.install_from_path(package_to_install.download())
                        print(f"✅ 語言包安裝完成: {from_code} -> {to_code}")
                    else:
                        print(f"⚠️  找不到語言包: {from_code} -> {to_code}")
                else:
                    print(f"✅ 語言包已存在: {from_code} -> {to_code}")
                        
        except Exception as e:
            print(f"❌ 安裝語言包時發生錯誤: {e}")
    
    def _detect_language(self, text: str) -> str:
        """
        簡單的語言檢測（基於字符特徵）
        """
        # 簡單的語言檢測邏輯
        if any('\u4e00' <= char <= '\u9fff' for char in text):
            return "zh"  # 中文
        elif any('\u3040' <= char <= '\u309f' or '\u30a0' <= char <= '\u30ff' for char in text):
            return "ja"  # 日文
        elif any('\uac00' <= char <= '\ud7af' for char in text):
            return "ko"  # 韓文
        else:
            return "en"  # 默認英文
    
    def translate(self, text: str, source_language: str = "auto", target_language: str = "zh") -> str:
        """
        執行翻譯
        """
        try:
            print(f"\n🔄 開始翻譯...")
            print(f"原文: {text}")
            print(f"源語言: {source_language}")
            print(f"目標語言: {target_language}")
            
            # 自動檢測源語言
            if source_language == "auto":
                detected_lang = self._detect_language(text)
                print(f"🔍 檢測到的語言: {detected_lang}")
                source_language = detected_lang
            
            # 如果源語言和目標語言相同，直接返回原文
            if source_language == target_language:
                print("ℹ️  源語言和目標語言相同，返回原文")
                return text
            
            # 執行翻譯
            print(f"🔄 正在翻譯 {source_language} -> {target_language}...")
            translated_text = argostranslate.translate.translate(text, source_language, target_language)
            
            if not translated_text:
                print("⚠️  直接翻譯失敗，嘗試英文中轉...")
                # 如果直接翻譯失敗，嘗試通過英文中轉
                if source_language != "en" and target_language != "en":
                    # 先翻譯到英文
                    print(f"🔄 第一步: {source_language} -> en")
                    english_text = argostranslate.translate.translate(text, source_language, "en")
                    if english_text:
                        print(f"中間結果: {english_text}")
                        # 再從英文翻譯到目標語言
                        print(f"🔄 第二步: en -> {target_language}")
                        translated_text = argostranslate.translate.translate(english_text, "en", target_language)
                
                if not translated_text:
                    error_msg = f"翻譯失敗: 無法找到 {source_language} -> {target_language} 的翻譯路徑"
                    print(f"❌ {error_msg}")
                    return error_msg
            
            print(f"✅ 翻譯完成: {translated_text}")
            return translated_text
            
        except Exception as e:
            error_msg = f"翻譯錯誤: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg


def main():
    """
    主測試函數
    """
    print("🚀 ComfyUI翻譯器測試程式")
    print("=" * 50)
    
    # 初始化翻譯器
    translator = SimpleTranslator()
    
    print("\n" + "=" * 50)
    print("🧪 開始測試...")
    
    # 測試案例
    test_cases = [
        ("Hello, world!", "auto", "zh"),
        ("你好，世界！", "auto", "en"),
        ("こんにちは、世界！", "auto", "en"),
        ("Bonjour le monde!", "auto", "zh"),
        ("This is a test of the translation system.", "en", "zh"),
        ("這是一個翻譯系統的測試。", "zh", "en"),
    ]
    
    for i, (text, source, target) in enumerate(test_cases, 1):
        print(f"\n📝 測試案例 {i}:")
        print("-" * 30)
        result = translator.translate(text, source, target)
        print(f"結果: {result}")
        print("-" * 30)
    
    print("\n🎯 測試完成！")
    print("你現在可以手動輸入文字進行測試：")
    
    # 互動模式
    while True:
        try:
            print("\n" + "=" * 50)
            text = input("請輸入要翻譯的文字 (或輸入 'quit' 退出): ").strip()
            
            if text.lower() in ['quit', 'exit', 'q']:
                break
                
            if not text:
                continue
                
            source = input("源語言 (auto/en/zh/ja/ko/fr/de/es/it/ru/ar/pt) [auto]: ").strip() or "auto"
            target = input("目標語言 (en/zh/ja/ko/fr/de/es/it/ru/ar/pt) [zh]: ").strip() or "zh"
            
            result = translator.translate(text, source, target)
            print(f"\n🎯 翻譯結果: {result}")
            
        except KeyboardInterrupt:
            print("\n\n👋 再見！")
            break
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")


if __name__ == "__main__":
    main()
