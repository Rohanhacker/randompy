import tkinter
from tkinter import filedialog
class yolo:
    def __init__(self,master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master)
        self.mainframe.pack(fill=tkinter.BOTH,expand=True)
        self.buildgrid()
        self.buildlabel()
        self.buildbuttons()
    def buildgrid(self):
        self.mainframe.columnconfigure(0,weight=0)
        self.mainframe.columnconfigure(1,weight=1)
        self.mainframe.rowconfigure(0,weight=0)
        self.mainframe.rowconfigure(1,weight=1)
        self.mainframe.rowconfigure(2,weight=0)
    def buildlabel(self):
        l = tkinter.Label(self.mainframe,text="pimodrno",bg="red",fg="white",font=("Helvetica",24))
        l.grid( row=0,column=1,sticky= "we", padx = 10,pady = 15 )
    def buildbuttons(self):
        b_frame = tkinter.Frame(self.mainframe)
        b_frame.grid(row=2,column=1,sticky="ewns", padx = 10,pady=10)
        b_frame.columnconfigure(0,weight=1)
        b_frame.columnconfigure(1,weight=1)
        self.startbutton = tkinter.Button (b_frame,text = "Start")
        self.stopbutton = tkinter.Button (b_frame,text = "Stop")
        self.startbutton.grid(row=0,column=0,sticky="ew")
        self.stopbutton.grid(row=0,column=1,sticky="ew")
if __name__ == "__main__":
    root = tkinter.Tk()
    yolo(root)
    root.mainloop()
