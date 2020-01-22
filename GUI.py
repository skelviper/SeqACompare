import tkinter as tk
from tkinter import scrolledtext

class MainGUI(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.setupUI()

    #绘制窗体：    
    def setupUI(self):
        self.title("SeqACompare")
        self.geometry("800x600")

        buttonClear = tk.Button(self,text='Clear',font = ('Arial',20),command = self.clear())
        buttonAlign = tk.Button(self,text='Align',font = ('Arial',20),command = self.align())
        
        #内部部件显示
        tk.Label(self, text='Original Sequence',font = ('Arial',20)).pack()
        
        seqOri = scrolledtext.ScrolledText(self,height = 5,width =100)
        #输入输出框的滚轮实现
        seqOri.pack()

        tk.Label(self, text='Sequencing Result',font = ('Arial',20)).pack()
        seqRes = scrolledtext.ScrolledText(self,height = 10,width =100)
        seqRes.pack()
        buttonClear.pack(side = tk.LEFT)
        buttonAlign.pack(side = tk.RIGHT)
        tk.Label(self, text='Output',font = ('Arial',20)).pack()
        ResOutput = scrolledtext.ScrolledText(self,height = 20,width =100)
        ResOutput.pack()


    #按钮功能
    def clear(self):
        pass
    def align(self):
        pass
        
        
if __name__ == '__main__':
    MainGUI().mainloop()