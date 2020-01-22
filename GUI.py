import tkinter as tk
from tkinter import scrolledtext,Text
from tkinter import INSERT
import sys

class MainGUI(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SeqACompare")
        self.window.geometry("800x600")


        
        #内部部件显示
        tk.Label(self.window, text='Original Sequence',font = ('Arial',20)).pack()
        
        self.seqOri = scrolledtext.ScrolledText(self.window,height = 5,width =100)
        #通过scrolledtext实现滚轮，继承自Text类
        self.seqOri.pack()

        tk.Label(self.window, text='Sequencing Result',font = ('Arial',20)).pack()
        self.seqRes = scrolledtext.ScrolledText(self.window,height = 10,width =100)
        self.seqRes.pack()

        self.buttonClear = tk.Button(self.window,text='Clear',font = ('Arial',20),command = self.clear)
        self.buttonAlign = tk.Button(self.window,text='Align',font = ('Arial',20),command = self.align)

        self.buttonClear.pack(side = tk.LEFT)
        self.buttonAlign.pack(side = tk.RIGHT)
        tk.Label(self.window, text='Output',font = ('Arial',20)).pack()
        self.ResOutput = scrolledtext.ScrolledText(self.window,height = 20,width =100)
        self.ResOutput.pack()
        
        sys.stdout.write = self.redirector #whenever sys.stdout.write is called, redirector is called.

        self.window.mainloop()

    #按钮功能

    def clear(self):
        self.seqOri.delete("0.0","end")
        self.seqRes.delete("0.0","end")
        self.ResOutput.delete("0.0","end")

        print("All clear!")
        
    def redirector(self,inputStr):
        self.ResOutput.insert(INSERT, inputStr)

    def align(self):
        print(MainGUI.readFasta(self.seqRes))

    #readFasta将每个fasta格式的序列内容保存为列表里的一个元素
    @staticmethod
    def readFasta(Text):
        try:
            seq = []
            seqNum = -1
            tempText = Text.get("0.0","end").split()
            for line in tempText:
                if (line[0]=='>'):
                    seqNum +=1
                    seq.append("")
                    continue
                else:
                    seq[seqNum]+=line
            return seq
        except BaseException:
            print("WrongInput")


if __name__ == '__main__':
    MainGUI()