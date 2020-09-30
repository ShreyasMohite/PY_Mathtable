


from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Combobox


class Tables:

    def __init__(self,root):
        self.root=root
        self.root.title("Maths Tables")
        self.root.geometry("500x500")
        self.root.resizable(0,0)
        self.root.iconbitmap("math.ico")


        get_table_number=IntVar()



        def on_leave1(e):
            but_tables['background']="SystemButtonFace"
            but_tables['foreground']="SystemButtonText"
        def on_enter1(e):
            but_tables['background']="black"
            but_tables['foreground']="cyan"
               
               

        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"       
        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"




        def tables():
            try:

                if(get_table_number.get()=="Select Table Number"):
                    tkinter.messagebox.showerror("Error","Please select a number")
                else:
                    text_box.delete(1.0,"end")
                    table_num=get_table_number.get()                                    
                    with open("C:\\TEMP\\tables.txt","w") as f:
                        for i in range(1,11):
                            s=i*table_num
                            a='%d x %d'%(table_num,i)+"=",s
                            f.write("\n""\t\t\t"+str(a)+"\n")

                    with open("C:\\TEMP\\tables.txt","r") as f:
                        text_box.insert("end",f.read())


            except Exception as e:
                print(e)
                


        def clear():
            get_table_number.set("Select Table Number")
            text_box.delete(1.0,"end")


    
    #==========================
        main_frame=Frame(self.root,width=500,height=500,bg="black")
        main_frame.place(x=0,y=0)

        top_frame=Frame(main_frame,width=500,height=200,bg="cyan",bd=5,relief="ridge")
        top_frame.place(x=0,y=0)

        bottom_frame=Frame(main_frame,width=500,height=300,bg="cyan",bd=6,relief="ridge")
        bottom_frame.place(x=0,y=200)

    #=============================

        label_frame=LabelFrame(top_frame,fg="white",text="Enter Tabel Number",bg="black",width=490,height=190,font=("times new roman",13,"bold"))
        label_frame.place(x=0,y=0)
        

        number=list(range(1,10001))
        table_numbers=Combobox(label_frame,values=number,font=('arial',10),width=20,state="readonly",textvariable=get_table_number)
        table_numbers.place(x=140,y=30)
        table_numbers.set("Select Table Number")


        but_tables=Button(label_frame,text=" Show Tabels",width=15,font=('times new roman',12,'bold'),cursor="hand2",command=tables)
        but_tables.place(x=50,y=100)
        but_tables.bind("<Enter>",on_enter1)
        but_tables.bind("<Leave>",on_leave1)
    

        but_clear=Button(label_frame,text="Clear",width=15,font=('times new roman',12,'bold'),cursor="hand2",command=clear)
        but_clear.place(x=290,y=100)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


    #================================
        text_box=Text(bottom_frame,width=60,height=15,font=("times new roman",12,"bold"),bg="black",fg="white")
        text_box.place(x=1,y=0)
        




if __name__ == "__main__":
    root=Tk()
    app=Tables(root)
    root.mainloop()
