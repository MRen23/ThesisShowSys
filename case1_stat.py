# -*- coding:utf-8-*-

from tkinter import *
from tkinter import ttk
import case_office
import case1_cluster

'''
本文件主要对case1的展示界面做设计
'''


'''
Case1统计展示界面
'''
class Display:
    def __init__(self):
        self.root=Tk()
        self.root.title('案例一')
        self.root.geometry('1200x1200')
        self.scrollbar = Scrollbar(self.root,)
        self.lb = Label(self.root, text='请选择想要统计的数据集：',
                        fg='black',font=('宋体',15), height=2)
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
    共享型办公室图像标签统计展示
    '''
    def stat_coshared(self):
        tree = ttk.Treeview(self.root,height = 15,columns=('No','标签','频率'),
                            yscrollcommand=self.scrollbar.set,show='headings')      # #创建表格对象

        tree.column("No",width=50,anchor='center')
        tree.column("标签", width=100,anchor='center')
        tree.column("频率", width=100,anchor='center')

        tree.heading("No",text="No")
        tree.heading("标签", text="标签")
        tree.heading("频率", text="频率")
        for i in range(0,50):
            tree.insert("",i,values=(i+1, case_office.coshared_stat[i][0],case_office.coshared_stat[i][1]))

        scrollbar = Scrollbar(tree, orient='vertical', command=tree.yview)
        scrollbar.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        # 给treeview添加配置
        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(column = 1, row = 10)

    '''
    开放型办公室图像标签统计展示
    '''
    def stat_open(self):
        tree = ttk.Treeview(self.root,height =15,columns=('No','标签','频率'),
                            yscrollcommand=self.scrollbar.set,show='headings')      # #创建表格对象
        tree.column("No",width=50,anchor='center')
        tree.column("标签", width=100,anchor='center')
        tree.column("频率", width=100,anchor='center')

        tree.heading("No",text="No")
        tree.heading("标签", text="标签")
        tree.heading("频率", text="频率")
        for i in range(0,50):
            tree.insert("",i,values=(i+1,case_office.coshared_stat[i][0],case_office.open_stat[i][1]))

        scrollbar = Scrollbar(tree, orient='vertical', command=tree.yview)
        scrollbar.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        # 给treeview添加配置
        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(column = 3, row = 10)

    '''
    办公室总的图像标签统计展示
    '''
    def stat_all(self):
        tree = ttk.Treeview(self.root,height =15,columns=('No','标签','频率'),
                            yscrollcommand=self.scrollbar.set,show='headings')      # #创建表格对象

        tree.column("No",width=50,anchor='center')
        tree.column("标签", width=100,anchor='center')
        tree.column("频率", width=100,anchor='center')

        tree.heading("No",text="No")
        tree.heading("标签", text="标签")
        tree.heading("频率", text="频率")
        for i in range(0,50):
            tree.insert("",i,values=(i+1,case_office.coshared_stat[i][0],case_office.all_labels_stat[i][1]))

        scrollbar = Scrollbar(tree, orient='vertical', command=tree.yview)
        scrollbar.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        # 给treeview添加配置
        tree.configure(yscrollcommand=scrollbar.set)
        tree.grid(column = 6, row = 10)

    '''
    共享型办公室图像标签统计可视化
    '''
    def visual_coshared(self):
        case_office.hist_bar(case_office.coshared_stat,'共享型办公室数据集')

    '''
    开放型办公室图像标签统计可视化
    '''
    def visual_open(self):
        case_office.hist_bar(case_office.coshared_stat,'开放式办公室数据集')

    '''
    办公室总的图像标签统计可视化
    '''
    def visual_all(self):
        case_office.hist_bar(case_office.all_labels_stat,'办公室图像总数据集')










#
#
# def creat():
#     case1 = Tk()
#     # 进入消息循环
#     case1.title('案例一')
#     case1.geometry('1200x1200')
#
#
#     '''
#     首页布局设计
#     '''
#     lb = Label(case1, text='请选择想要统计的数据集：',
#                fg='black',
#                font=('宋体',20),
#                # width=10,
#                height=2)
#
#     lb.grid(column = 1, row = 2)   # 设置标签label的位置
#
#     lb = Button(case1,text='共享型办公室数据集标签统计',
#             bg='#d3fbfb',
#             fg='red',
#             font=('华文新魏',10),
#             width=30,
#             height=2,
#             relief=RAISED,
#             command=cases.self.first_case)
#     # lb.pack()
#     lb.grid(column = 1, row = 4) # 设置button位置
#
#     lb = Button(case1,text='开放型办公室数据集标签统计',
#             bg='#d3fbfb',
#             fg='red',
#             font=('华文新魏',10),
#             width=30,
#             height=2,
#             relief=RAISED,
#             command=cases.second_case)
#     # lb.pack()
#     lb.grid(column = 2, row = 4)   # 设置button位置
#
#     lb = Button(case1,text='总的办公室数据集标签统计',
#             bg='#d3fbfb',
#             fg='red',
#             font=('华文新魏',10),
#             width=30,
#             height=2,
#             relief=RAISED,
#             command=cases.second_case)
#     # lb.pack()
#     lb.grid(column = 3, row = 4)   # 设置button位置
#
#
#     col_count, row_count = case1.grid_size()
#
#     for col in range(0,col_count):
#         case1.grid_columnconfigure(col, minsize=20)
#
#     for row in range(0,row_count):
#         case1.grid_rowconfigure(row, minsize=10)
#
#     case1.mainloop()


