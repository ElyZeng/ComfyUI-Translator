#!/usr/bin/env python3
"""
測試修改後的翻譯器 - 專注於翻譯到英文
"""

import sys
import os
sys.path.append('.')

from text_translator_node import TextTranslatorNode

def test_prompt_translation():
    """
    測試prompt翻譯功能
    """
    print("🚀 ComfyUI翻譯器 - Prompt翻譯測試")
    print("=" * 50)
    
    # 初始化翻譯節點
    translator = TextTranslatorNode()
    
    print("\n🧪 測試各種語言的prompt翻譯成英文...")
    
    # 測試案例 - 各種語言的prompt
    test_prompts = [
        ("一個美麗的日出景色", "auto"),  # 中文
        ("美しい夕日の風景", "auto"),     # 日文
        ("아름다운 일몰 풍경", "auto"),     # 韓文
        ("Un magnifique coucher de soleil", "auto"),  # 法文
        ("Ein wunderschöner Sonnenuntergang", "auto"),  # 德文
        ("Un hermoso atardecer", "auto"),  # 西班牙文
        ("Una bella ragazza con capelli lunghi", "auto"),  # 義大利文
        ("Красивый закат над морем", "auto"),  # 俄文
        ("可愛的貓咪在花園裡玩耍", "zh"),  # 明確指定中文
        ("桜が咲く美しい公園", "ja"),      # 明確指定日文
    ]
    
    for i, (prompt, source_lang) in enumerate(test_prompts, 1):
        print(f"\n📝 測試案例 {i}:")
        print("-" * 40)
        print(f"原始prompt: {prompt}")
        print(f"源語言: {source_lang}")
        
        # 執行翻譯（目標語言默認為英文）
        result = translator.translate_text(prompt, source_lang, "en")
        
        print(f"英文翻譯: {result[0]}")
        print("-" * 40)
    
    print("\n🎯 測試完成！")
    print("現在你的ComfyUI翻譯節點已經優化為:")
    print("✅ 預設目標語言: 英文")
    print("✅ 適合翻譯各種語言的prompt到英文")
    print("✅ 自動語言檢測功能")

if __name__ == "__main__":
    test_prompt_translation()
