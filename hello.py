# -*- coding: utf-8 -*-
# 我的第一个 Python 文件：打招呼


def greet(name="世界"):
    """返回一句问候语。"""
    return f"你好，{name}！欢迎来到 GitHub。"


def greet_en(name="World"):
    """返回一句英文问候语。"""
    return f"Hello, {name}! Welcome to GitHub."


if __name__ == "__main__":
    print(greet("Mufeng"))
    print(greet_en("Mufeng"))
