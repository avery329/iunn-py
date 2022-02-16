#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime  # 导入datetie库
from tkinter import *           # 导入 Tkinter 库
import tkinter as tk
import tkinter.messagebox  # 导入消息


root = Tk()
root.title('日期倒计时 by iunn')  # 窗口标题
root.geometry("400x150")  # 长x宽+x*y
root.attributes('-alpha', 0.85)  # 窗口透明度
root.configure(bg='whitesmoke')  # 创建窗口对象的背景色
root.iconbitmap('ico.ico')  # 图标

restdays = '剩余天数：'
middleexam = '中考：'
today = '今天：'

now = datetime.date.today()  # 实时日期
exam = datetime.date(2022, 6, 25)  # 考试时间
days = exam.__sub__(now).days  # 剩余天数

first = [today, now]
second = [middleexam, exam]
third = [restdays, days]
# 连接变量


def about():
    tkinter.messagebox.showinfo(title='关于', message='版本：1.0.1\n© iunn2022')
# 版本号


def close_window():
    root.destroy()
# 退出

#li = [third, second, first]
# listb = Listbox(root)  # 创建列表组件


rot = tk.Menu(root)
# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = tk.Menu(rot, tearoff=False)  # 菜单
filemenu.add_command(label="关于", command=about)
# filemenu.add_command(label="保存")
filemenu.add_separator()  # 分割线
filemenu.add_command(label="退出", command=close_window)
rot.add_cascade(label="选项", menu=filemenu)
root.config(menu=rot)

lable = tk.Label(root, text=third, font=("微软雅黑", 23), bg='whitesmoke')
lable.pack()  # 剩余日期
lable1 = tk.Label(root, text=second, font=("微软雅黑", 23), bg='whitesmoke')
lable1.pack()  # 考试日期
lable2 = tk.Label(root, text=first,  font=("微软雅黑", 23), bg='whitesmoke')
lable2.pack()  # 今天

# for item in li:                 # 第一个小部件插入数据
#listb.insert(0, item)
# listb.pack()                    # 将小部件放置到主窗口中

root.mainloop()                 # 进入消息循环
