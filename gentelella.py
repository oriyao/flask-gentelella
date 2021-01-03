"""
# coding:utf-8
@Time    : 2021/01/02
@Author  : oriyao
@mail    : ylzhangyao@gmail.com
@File    : gentelella.py
@Describe: Flask Project 入口文件
"""
from app import create_app

# development/testing/production

app = create_app('development')

