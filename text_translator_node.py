"""
Text Translator Node for ComfyUI
Provides offline translation functionality using Argos Translate.
"""

import argostranslate.package
import argostranslate.translate
from typing import Dict, Any, Tuple
import os


class TextTranslatorNode:
    """
    A ComfyUI custom node for offline text translation using Argos Translate
    """
    
    def __init__(self):
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
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        定義節點的輸入類型
        """
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "Hello, world!"
                }),
                "source_language": (["auto", "en", "zh", "ja", "ko", "fr", "de", "es", "it", "ru", "ar", "pt"], {
                    "default": "auto"
                }),
                "target_language": (["en", "zh", "ja", "ko", "fr", "de", "es", "it", "ru", "ar", "pt"], {
                    "default": "zh"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("translated_text",)
    FUNCTION = "translate_text"
    CATEGORY = "text/translation"
    
    def _ensure_language_packages(self):
        """
        確保必要的語言包已安裝
        """
        try:
            # 更新可用的語言包列表
            argostranslate.package.update_package_index()
            
            # 獲取已安裝的語言包
            installed_packages = argostranslate.package.get_installed_packages()
            
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
                        print(f"Installing language package: {from_code} -> {to_code}")
                        argostranslate.package.install_from_path(package_to_install.download())
                        
        except Exception as e:
            print(f"Warning: Could not install language packages: {e}")
    
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
    
    def translate_text(self, text: str, source_language: str, target_language: str) -> Tuple[str]:
        """
        執行離線文字翻譯
        """
        try:
            # 自動檢測源語言
            if source_language == "auto":
                source_language = self._detect_language(text)
            
            # 如果源語言和目標語言相同，直接返回原文
            if source_language == target_language:
                return (text,)
            
            # 執行翻譯
            translated_text = argostranslate.translate.translate(text, source_language, target_language)
            
            if not translated_text:
                # 如果直接翻譯失敗，嘗試通過英文中轉
                if source_language != "en" and target_language != "en":
                    # 先翻譯到英文
                    english_text = argostranslate.translate.translate(text, source_language, "en")
                    if english_text:
                        # 再從英文翻譯到目標語言
                        translated_text = argostranslate.translate.translate(english_text, "en", target_language)
                
                if not translated_text:
                    return (f"Translation failed: No translation path available from {source_language} to {target_language}",)
            
            return (translated_text,)
            
        except Exception as e:
            error_msg = f"Translation error: {str(e)}"
            print(error_msg)
            return (error_msg,)


# 節點映射 - ComfyUI需要這些來註冊節點
NODE_CLASS_MAPPINGS = {
    "TextTranslatorNode": TextTranslatorNode
}

# 顯示名稱映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "TextTranslatorNode": "Text Translator"
}
