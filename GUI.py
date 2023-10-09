from tkinter import *
import node as nd
class Graphic:
    def __init__(sarib):
        sarib.node = nd.Node()
        sarib.splash_root = Tk()
        sarib.splash_root.attributes("-fullscreen",True)
        sarib.splash_root.configure(bg="blue")
        sarib.splash_label = Label(sarib.splash_root, fg= 'black',text="Loading.....",bg="blue", font=("URW Chancery L"," 40"," bold"))
        sarib.splash_label.place(x=580,y=470)
        sarib.splash_label2 = Label(sarib.splash_root,fg="red",bg= "blue",text="Something is Coming Dude!",font=("URW Chancery L"," 40"," bold"))
        sarib.splash_label2.place(x=400,y=200)
        sarib.splash_root.after(5000,sarib.main)
        sarib.splash_root.mainloop()
    def main(sarib):
        sarib.splash_root.destroy()
        sarib.window = Tk()
        sarib.Frame1("")
        sarib.window.mainloop()
    def Frame1(sarib,var):
        sarib.frame1 = Frame(sarib.window,bg="blue")
        sarib.frame1.place(x=0,y=0,width=1366,height=768)
        sarib.window.attributes("-fullscreen",True)
        # sarib.window.configure(bg="blue")
        label = Label(sarib.frame1,fg="red",bg="blue",text="it's Panic Room",font=("URW Chancery L"," 40"," bold"))
        label.place(x=450,y=100)
        label2 = Label(sarib.frame1,fg="yellow",bg="blue",text="Develepor : Syed Sarib Naveed",font=("URW Chancery L"," 30"," bold"))
        label2.place(x=700,y=600)
        Label(sarib.frame1,bg="blue",fg="yellow",text=var,font=("URW Chancery L"," 20"," bold")).place(x=530,y=250)
        sarib.search = Entry(sarib.frame1,width=30,textvariable=str())
        sarib.search.insert(0,"Type here....")
        def click(event):
            sarib.search.delete(0,'end')
        sarib.search.bind('<Button-1>',click)
        # sarib.entry = sarib.search.get()
        Button(sarib.frame1,text="Insert",font=("Arial"," 10"," bold"),bg='red',fg="white",command=sarib.Insert).place(x=570,y=360)
        Button(sarib.frame1,text="Search",font=("Arial"," 10"," bold"),bg='green',fg="white",command=sarib.Search).place(x=567,y=410)
        sarib.search.place(x=500,y=300)
        exit_button = Button(sarib.frame1,text = " x ",font="Arial 10 bold",command=sarib.window.destroy,bg='red')
        exit_button.place(x=1331,y=2)
    def Insert(sarib):
        sarib.entry = sarib.search.get()
        if nd.Node.Search(sarib.node,sarib.entry) == 1:
            sarib.Frame1("Already Present!")
        else:
            nd.Node.Insert(sarib.node,sarib.entry)
            sarib.Frame1("Inserted")
    def Search(sarib):
        sarib.entry = sarib.search.get()
        search = nd.Node.Search(sarib.node,sarib.entry)
        if search == 1:
            sarib.Frame1("Available!")
        else:
            sarib.Frame1("Not Available!")
Graphic()