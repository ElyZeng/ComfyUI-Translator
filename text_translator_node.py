"""
Text Translator Node for ComfyUI
Provides translation functionality using various translation services.
"""

import torch
import requests
import json
from typing import Dict, Any, Tuple


class TextTranslatorNode:
    """
    A ComfyUI custom node for text translation
    """
    
    def __init__(self):
        pass
    
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
                "source_language": (["auto", "en", "zh", "ja", "ko", "fr", "de", "es", "it", "ru"], {
                    "default": "auto"
                }),
                "target_language": (["zh", "en", "ja", "ko", "fr", "de", "es", "it", "ru"], {
                    "default": "zh"
                }),
                "translation_service": (["google", "baidu", "deepl"], {
                    "default": "google"
                }),
            },
            "optional": {
                "api_key": ("STRING", {
                    "default": ""
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("translated_text",)
    FUNCTION = "translate_text"
    CATEGORY = "text/translation"
    
    def translate_text(self, text: str, source_language: str, target_language: str, 
                      translation_service: str, api_key: str = "") -> Tuple[str]:
        """
        執行文字翻譯
        """
        try:
            if translation_service == "google":
                translated = self._google_translate(text, source_language, target_language)
            elif translation_service == "baidu":
                translated = self._baidu_translate(text, source_language, target_language, api_key)
            elif translation_service == "deepl":
                translated = self._deepl_translate(text, source_language, target_language, api_key)
            else:
                translated = f"Error: Unsupported translation service: {translation_service}"
            
            return (translated,)
        
        except Exception as e:
            error_msg = f"Translation error: {str(e)}"
            print(error_msg)
            return (error_msg,)
    
    def _google_translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """
        使用Google Translate API (免費版本，僅作示例)
        注意：實際使用時建議使用官方API
        """
        try:
            # 這裡是簡化版本，實際應用中應該使用官方Google Translate API
            # 此處僅作為示例結構
            return f"[Google翻譯] {text} -> {target_lang}"
        except Exception as e:
            return f"Google translation failed: {str(e)}"
    
    def _baidu_translate(self, text: str, source_lang: str, target_lang: str, api_key: str) -> str:
        """
        使用百度翻譯API
        """
        try:
            if not api_key:
                return "Error: Baidu API key is required"
            # 實際的百度翻譯API調用邏輯
            return f"[百度翻譯] {text} -> {target_lang}"
        except Exception as e:
            return f"Baidu translation failed: {str(e)}"
    
    def _deepl_translate(self, text: str, source_lang: str, target_lang: str, api_key: str) -> str:
        """
        使用DeepL API
        """
        try:
            if not api_key:
                return "Error: DeepL API key is required"
            # 實際的DeepL API調用邏輯
            return f"[DeepL翻譯] {text} -> {target_lang}"
        except Exception as e:
            return f"DeepL translation failed: {str(e)}"


# 節點映射 - ComfyUI需要這些來註冊節點
NODE_CLASS_MAPPINGS = {
    "TextTranslatorNode": TextTranslatorNode
}

# 顯示名稱映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "TextTranslatorNode": "Text Translator"
}
