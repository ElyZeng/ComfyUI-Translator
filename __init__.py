"""
ComfyUI Text Translator Custom Node
A custom node for ComfyUI that provides text translation functionality.
"""

from .text_translator_node import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# 導出節點映射，這是ComfyUI載入custom node的標準方式
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# ComfyUI會自動載入這些映射
WEB_DIRECTORY = "./web"
