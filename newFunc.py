import tkinter
 
class Gui(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("320x400+800+400")
        self.root.title('自动发送邮件')
        # 标签控件
        # 邮件号
        self.label_yj = tkinter.Label(master=self.root, text='邮件号:')
        self.label_yj.grid(row=0, column=0)
        # 间谍号
        self.label_jd = tkinter.Label(master=self.root, text='间谍号:')
        self.label_jd.grid(row=1, column=0)
        # 目标群
        self.label_mb = tkinter.Label(master=self.root, text='目标群:')
        self.label_mb.grid(row=2, column=0)
        # 授权码
        self.label_sq = tkinter.Label(master=self.root, text='授权码:')
        self.label_sq.grid(row=3, column=0)
        # 邮件标题
        self.label_bt = tkinter.Label(master=self.root, text='邮件标题:')
        self.label_bt.grid(row=4, column=0)
        # 邮件内容
        self.label_nr = tkinter.Label(master=self.root, text='邮件内容:')
        self.label_nr.grid(row=5, column=0)
        # 发送记录
        self.label = tkinter.Label(master=self.root, text='发送记录:')
        self.label.grid(row=7, column=0)
 
        # 输入控件
        # 邮件号
        self.entry_yj = tkinter.Entry(master=self.root)
        self.entry_yj.grid(row=0, column=1)
        # 间谍号
        self.entry_jd = tkinter.Entry(master=self.root)
        self.entry_jd.grid(row=1, column=1)
        # 目标群
        self.entry_mb = tkinter.Entry(master=self.root)
        self.entry_mb.grid(row=2, column=1)
        # 授权码
        self.entry_sq = tkinter.Entry(master=self.root)
        self.entry_sq.grid(row=3, column=1)
        # 邮件标题
        self.entry_bt = tkinter.Entry(master=self.root)
        self.entry_bt.grid(row=4, column=1)
        # 邮件内容
        self.entry_nr = tkinter.Entry(master=self.root)
        self.entry_nr.grid(row=5, column=1)
 
        # 按钮控件
        # 提交信息按钮
        #self.button_tj = tkinter.Button(master=self.root, text='开始运行', command=)
        #self.button_tj.grid(row=6, column=0)
        # 停止按钮(command=self.root.quit  关闭窗口)
        self.button_tz = tkinter.Button(master=self.root, text='停止发送', command=self.root.quit)
        self.button_tz.grid(row=6, column=1)
        # 清空内容(command=self.delete    清空当前窗口的所有内容)
        self.button_tz = tkinter.Button(master=self.root, text='清空', command=self.delete)
        self.button_tz.grid(row=6, column=2)
 
        # 列表框控件(输出结果)
        self.listbox = tkinter.Listbox(master=self.root, width=45, height=10)
        self.listbox.grid(rowspan=4, columnspan=4)
 
        self.root.mainloop()
 
    # 清空输入框
    def delete(self):
        self.entry_yj.delete(0, 'end')
        self.entry_jd.delete(0, 'end')
        self.entry_mb.delete(0, 'end')
        self.entry_sq.delete(0, 'end')
        self.entry_bt.delete(0, 'end')
        #self.eneftry_nr.delete(0, 'end')
        print("work")
    
    #zai 


Gui()