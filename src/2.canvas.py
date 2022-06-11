#!/usr/bin/python3

import tkinter

win = tkinter.Tk()
win.title("canvas绘图")

# 获取canvas
canvas = tkinter.Canvas(win, width=400, height=300)
canvas.pack()

# 画一条黄色的横线
canvas.create_line(0, 50, 200, 50, fill="yellow")
# 画一条红色的竖线（虚线）
canvas.create_line(100, 0, 100, 100, fill="red", dash=(4, 4))
# 中间画一个蓝色的矩形
canvas.create_rectangle(50, 25, 150, 75, fill="blue")

win.mainloop()

'''
所有 tkinter 控件都可以使用以下方法设置控件在窗口内的几何位置：
1.pack()：将控件放置在父控件内之前，规划此控件在区块内的位置。
2.grid()：将控件放置在父控件内之前，规划此控件为一个表格类型的架构。
3.place()：将控件放置在父控件内的特定位置。
'''
