__author__ = 'TF'
# -*- coding:utf-8-*-

from tkinter import *
from tkinter import ttk
import case_hotel
import case2_cluster


class Dispalay:
    def __init__(self):
        self.root=Tk()
        self.root.title('案例二')
        self.root.geometry('1200x1200')
        self.scrollbar = Scrollbar(self.root,)
        self.lb = Label(self.root, text='请选择想要统计的数据集：（其中将四星级和五星级酒店官方上传的图像数据集作为官方数据集A，'
                                        '二星级和三星级酒店官方上传的图像数据集作为官方数据集B，'
                                        '将四星级和五星级消费者上传的图像数据集作为旅游者数据集A，'
                                        '二星级和三星级消费者上传的图像数据集作为旅游者数据集B）',
                        fg='black',font=('宋体',10), height=2)
        self.lb.grid(column = 1, row = 2)   # 设置标签label的位置
        '''
        按钮设计
        '''
        print ('数据统计start......')
        self.lb = Button(self.root,text='共享型办公室数据集标签统计',bg='#d3fbfb',fg='red',font=('华文新魏',15),
                         width=25,height=3,relief=RAISED,command=self.stat_coshared)
        self.lb.grid(column = 1, row = 4) # 设置button位置

        self.lb = Button(self.root,text='开放型办公室数据集标签统计',bg='#d3fbfb',fg='red',font=('华文新魏',15),
                         width=25,height=3,relief=RAISED,command=self.stat_open)
        self.lb.grid(column = 3, row = 4)   # 设置button位置

        self.lb = Button(self.root,text='总的办公室数据集标签统计',bg='#d3fbfb',fg='red',font=('华文新魏',15),
                         width=25,height=3,relief=RAISED,command=self.stat_all)
        self.lb.grid(column = 6, row = 4)   # 设置button位置

        '''可视化按钮设计'''
        self.lb=Button(self.root,text='可视化',bg='#d3fbfb',fg='black',font=('仿宋',12),
                       width=10,height=1,relief=RAISED,command=self.visual_coshared)
        self.lb.grid(column = 1, row = 6)     # row是行， column是列

        self.lb=Button(self.root,text='可视化',bg='#d3fbfb',fg='black',font=('仿宋',12),
                       width=10,height=1,relief=RAISED,command=self.visual_open)
        self.lb.grid(column = 3, row = 6)

        self.lb=Button(self.root,text='可视化',bg='#d3fbfb',fg='black',font=('仿宋',12),
                       width=10,height=1,relief=RAISED,command=self.visual_all)
        self.lb.grid(column = 6, row = 6)

        # 跳转按钮
        self.lb=Button(self.root,text='下一步',bg='#d3fbfb',fg='black',font=('仿宋',12),
                       width=10,height=1,relief=RAISED,command=case1_cluster.ClusterDisplay)
        self.lb.grid(column = 8, row = 4)

        # 设置x和y的位置间隔
        self.col_count, self.row_count = self.root.grid_size()
        for col in range(0,self.col_count):
            self.root.grid_columnconfigure(col, minsize=20)
        for row in range(0,self.row_count):
            self.root.grid_rowconfigure(row, minsize=20)

        self.root.mainloop()



    '''
    官方数据集A图像标签统计展示：
    '''


    '''
    官方数据集B图像标签统计展示：
    '''

    '''
    旅游者数据集A图像标签统计展示：
    '''

    '''
    旅游者数据集B图像标签统计展示：
    '''