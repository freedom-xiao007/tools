#!/usr/bin/env python
# @Time    : 2019/9/22 9:00
# @Author  : Freedom
# @Site    : 
# @File    : MarkdownDirCreate.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
"""
用于Markdown文档工程的目录自动生成
忽略其中的图片文件夹和图片

自动遍历工程目录，生成相应的Markdown格式的目录文档
"""
import os


def create(result, path, index, root_length):
    """
    遍历指定的工程目录，生成文档索引
    :param path: Markdown文档工程路径
    :param index: 各级索引级别标识，用于生成不同的间隔
    :return:
    """
    files = os.listdir(path)
    for file in files:
        if file[0] == "." or file == "picture" or file[-5:] == "xmind" or file == "extention":
            continue
        if file[-2:] == "md" or file[-3:] == "txt":
            print(index * 4 * " ", "- ", file)
            link = "[" + file + "]" + "(" + "." + path[root_length:] + "/" + file + ")"
            result.writelines((index * 4 * " ", "- ", link, "\n"))
            continue
        print(index * 4 * " ", "- ", file)
        result.writelines((index * 4 * " ", "- ", file, "\n"))
        create(result, path + "/" + file, index + 1, root_length)


if __name__ == "__main__":
    path = "F:\\Code\\Markdown\\LOG"

    file_path = path + "/README.md"
    result = open(file_path, "w", encoding="utf-8")
    result.writelines("## 文档索引\n")

    create(result, path, 0, len(path))

    result.close()
