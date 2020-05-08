# -*- coding:utf-8-*-


import case_office
from tkinter import *
from tkinter import ttk

'''
Case1 聚类展示界面
'''

class ClusterDisplay:
    def __init__(self):
        self.clu=Tk()
        self.clu.title('聚类结果展示和评估')
        self.clu.geometry('800x600')
        self.scrollbar = Scrollbar(self.clu,)

        self.dbi_lb = Label(self.clu, text='DBI聚类评估',fg='black',font=('宋体',15),height=2)
        self.dbi_lb.grid(column = 3, row = 2)

        self.dbi_button= Button(self.clu, text='层次聚类评估结果',bg='#d3fbfb',fg='red',font=('华文新魏',15),
                                 width=20,height=2,relief=RAISED,command=self.DBIResult)
        self.dbi_button.grid(column = 3, row = 3)

        self.clu_button = Button(self.clu,text='聚类结果展示',bg='#d3fbfb',fg='red',font=('华文新魏',15),
                                 width=20,height=2,relief=RAISED,command=self.CluResult)
        self.clu_button.grid(column = 3, row = 5)

        self.fre_lb = Button(self.clu, text='频繁项集展示',bg='#d3fbfb',fg='red',font=('华文新魏',15),
                             width=20,height=2,relief=RAISED,command=self.FreResult)
        self.fre_lb.grid(column = 6, row= 3)

        self.contrast_lb= Button(self.clu, text='contrast结果展示',bg='#d3fbfb',fg='red',font=('华文新魏',15),
                             width=20,height=2,relief=RAISED,command=self.ContrastResult)
        self.contrast_lb.grid(column = 6, row = 5)

        col_count, row_count = self.clu.grid_size()

        for col in range(0,col_count):
            self.clu.grid_columnconfigure(col, minsize=40)

        for row in range(0,row_count):
            self.clu.grid_rowconfigure(row, minsize=60)

        self.clu.mainloop()
    #展示DBI聚类评估结果
    def DBIResult(self):
        case_office.bar_vis(case_office.cluster_n,case_office.silhouette_avg)

    def CluResult(self):
        CluDisplay()

    def FreResult(self):
        FreDisplay()

    def ContrastResult(self):
        ContrastDisplay()

class CluDisplay:
    def __init__(self):
        self.clu=Tk()
        self.clu.title('聚类结果展示')
        self.clu.geometry('500x400')
        self.scrollbar = Scrollbar(self.clu,)
        tree = ttk.Treeview(self.clu,height =15,columns=('类标签','标签'),
                            xscrollcommand=self.scrollbar.set,
                            yscrollcommand=self.scrollbar.set,show='headings')      # #创建表格对象
        tree.column("类标签",width=50,anchor='e')
        tree.column("标签", width=600,anchor='w')

        tree.heading("类标签",text="类标签")
        tree.heading("标签", text="标签")

        for i in range(0,14):
            tree.insert('',i,values=(i+1, case_office.values_list[i]))

        scrollbar = Scrollbar(tree, orient='horizontal', command=tree.xview)
        scrollbar.place(relx=0.028, rely=0.971, relwidth=0.958, relheight=0.024)

        tree.columnconfigure(0, weight=1)
        # 给treeview添加配置
        tree.configure(xscrollcommand=scrollbar.set)
        tree.pack()
        # tree.grid(column = 3, row = 8)

        scrollbar = Scrollbar(tree, orient='vertical', command=tree.yview)
        scrollbar.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)

        tree.columnconfigure(0, weight=1)
        # 给treeview添加配置
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack()
        # tree.grid(colunm = 3, row = 8)



class FreDisplay:
    def __init__(self):
        self.fre=Tk()
        self.fre.title('频繁项集结果展示')
        self.fre.geometry('1000x800')
        self.scrollbar = Scrollbar(self.fre,)

        self.ctit_Button = Button(self.fre, text='共享型办公室图像数据集频繁项集展示',bg='#d3fbfb',fg='red',font=('华文新魏',15),
                             width=35,height=2,relief=RAISED,command=self.CoShared)
        self.ctit_Button.grid(column = 2, row = 2)

        self.otit_Button = Button(self.fre,text='开放式办公室图像数据集频繁项集展示',bg='#d3fbfb',fg='red',font=('华文新魏',15),
                             width=35,height=2,relief=RAISED,command=self.OpenPlan)
        self.otit_Button.grid(column = 6, row = 2)


        col_count, row_count = self.fre.grid_size()

        for col in range(0,col_count):
            self.fre.grid_columnconfigure(col, minsize=30)

        for row in range(0,row_count):
            self.fre.grid_rowconfigure(row, minsize=30)

    def CoShared(self):
        # return 0
        tree = ttk.Treeview(self.fre,height = 15,columns=('No','频繁项集','频率'),
                        yscrollcommand=self.scrollbar.set,show='headings')      # #创建表格对象
        tree.column('No',width=50,anchor='center')
        tree.column('频繁项集',width=150,anchor='center')
        tree.column("频率",width=150,anchor='center')

        tree.heading('No',text='No')
        tree.heading('频繁项集',text='频繁项集')
        tree.heading("频率",text="频率")

        for i in range(0,14):
            tree.insert('',i,values=(i+1, str(case_office.co_processing[i][0])[10:-1],case_office.co_processing[i][1]))

        tree.grid(column = 2, row = 4)

    def OpenPlan(self):

        tree = ttk.Treeview(self.fre,height = 15,columns=('No','频繁项集','频率'),
                        yscrollcommand=self.scrollbar.set,show='headings')      # #创建表格对象
        tree.column('No',width=50,anchor='center')
        tree.column('频繁项集',width=150,anchor='center')
        tree.column("频率",width=150,anchor='center')

        tree.heading('No',text='No')
        tree.heading('频繁项集',text='频繁项集')
        tree.heading("频率",text="频率")

        for i in range(0,14):
            tree.insert('',i,values=(i+1, str(case_office.open_processing[i][0])[10:-1],case_office.open_processing[i][1]))

        tree.grid(column = 6, row = 4)

class ContrastDisplay:
    def __init__(self):
        self.cons=Tk()
        self.cons.title('对比结果展示')
        self.cons.geometry('800x400')
        self.scrollbar = Scrollbar(self.cons,)

        self.tit_label=Label(self.cons, text='共享型办公室和开放式办公室对比结果展示',fg='black',font=('宋体',15),height=2)
        self.tit_label.pack()

        tree = ttk.Treeview(self.cons,height = 15,columns=('No','频繁项集','共享型办公室(a)','开放式办公室(b)','GrowthRate(a/b)','GrowthRate(b/a)'),
                            yscrollcommand=self.scrollbar.set,show='headings')      # #创建表格对象
        tree.column('No',width=50,anchor='center')
        tree.column('频繁项集',width=150,anchor='center')
        tree.column("共享型办公室(a)",width=150,anchor='center')
        tree.column("开放式办公室(b)", width=150,anchor='center')
        tree.column("GrowthRate(a/b)",width=150,anchor='center')
        tree.column("GrowthRate(b/a)", width=150,anchor='center')

        tree.heading('No',text='No')
        tree.heading('频繁项集',text='频繁项集')
        tree.heading("共享型办公室(a)",text="共享型办公室(a)")
        tree.heading("开放式办公室(b)", text="开放式办公室(b)")
        tree.heading("GrowthRate(a/b)",text='GrowthRate(a/b)')
        tree.heading("GrowthRate(b/a)", text='GrowthRate(a/b)')

        for i in range(0,14):
            tree.insert('',i,values=(i+1, str(case_office.show_list[i][0])[10:-1],case_office.show_list[i][1],
                                     case_office.show_list[i][2],case_office.show_list[i][3],case_office.show_list[i][4]))


        tree.pack()