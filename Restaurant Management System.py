from tkinter import *
import time
import random
import tkinter.messagebox as tmsg






#--------------------------------------------------------------------------------------#
root  = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")


def Submit():
    if Username_value.get()=="Somanshu" and Password_value.get()=="12345":
        l.destroy()
        l1.destroy()
        e.destroy()
        l2.destroy()
        e1.destroy()
        b6.destroy()
        Restaurant()
        
    else:
        tmsg.showinfo("Wrong USERNAME PASS","Enter Correct Username & Password")

Username_value = StringVar()
Password_value =StringVar()


l=Label(root,text='Restaurant Login System',font=('Arial',40,'bold'))
l.place(x=490,y=40)

l1=Label(root,text='User Name ',font=('Arial',20))
l1.place(x=490,y=200)
e=Entry(root,borderwidth=10,textvariable=Username_value,bg="light blue",font=('ariel' ,20,'bold'))
e.place(x=700,y=200)

l2=Label(root,text='Password ',font=('Arial',20))
l2.place(x=490,y=265)
e1=Entry(root,borderwidth=10,textvariable=Password_value,bg="powder blue",font=('ariel' ,20,'bold'))
e1.place(x=700,y=265)

b6 = Button(root,text="SUBMIT",font="arial 16 bold",pady=10,fg="black",bg="white",command=Submit,relief=RAISED)
b6.place(x=700,y=370)

name = Label(root,text="- By Somanshu Mishra",font="lucida 30 bold",fg="steel blue").place(x=550,y=470)



def Restaurant():


#---------------------------------------------#-------------------------------------------#
    
#-----------------------------------------------MENU-----------------------------------------#

    mainmenu = Menu(root)
    m1 = Menu(mainmenu,tearoff=0)
    m1.add_command(label="File")
    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="Fileee",menu=m1)








#------------------------------------------FUNCTIONS-----------------------------------------#
    def priceval():
        root1 = Tk()
        root1.geometry("600x350+0+0")
        root1.title("Price List") 

        item_label = Label(root1,text="ITEMS",font="arial 30 italic",padx=50,pady=20).grid(row=0,column=0)

        price_label = Label(root1,text="PRICE",font="arial 30 italic",padx=180,pady=20).grid(row=0,column=10)

        Noodles_label = Label(root1,text="NOODLES",font="arial 15 bold",fg="steel blue",padx=50,pady=5).grid(row=1,column=0)
        NoodlesPrice_label = Label(root1,text="Rs. 70",font="arial 15 bold",fg="steel blue",padx=50,pady=5).grid(row=1,column=10)

        HakkaNoodles_label = Label(root1,text="HAKKA NOODLES",font="arial 14 bold",fg="steel blue",padx=50,pady=5).grid(row=2,column=0)
        HakkaNoodlesPrice_label = Label(root1,text="Rs. 80",font="arial 14 bold",fg="steel blue",padx=50,pady=5).grid(row=2,column=10)


        VegSaucePasta_label = Label(root1,text="Veg Sauce Pasta",font="arial 15 bold",fg="steel blue",padx=50,pady=5).grid(row=3,column=0)
        VegSaucePastaPrice_label = Label(root1,text="Rs. 100",font="arial 15 bold",fg="steel blue",padx=50,pady=5).grid(row=3,column=10)


        CholeKulche_label = Label(root1,text="CHOLE KULCHE",font="arial 14 bold",fg="steel blue",padx=50,pady=5).grid(row=4,column=0)
        CholeKulchePrice_label = Label(root1,text="Rs. 120",font="arial 14 bold",fg="steel blue",padx=50,pady=5).grid(row=4,column=10)


        MasalaDosae_label = Label(root1,text="Masala Dosae",font="arial 15 bold",fg="steel blue",padx=50,pady=5).grid(row=5,column=0)
        MasalaDosaePrice_label = Label(root1,text="Rs. 85",font="arial 15 bold",fg="steel blue",padx=50,pady=5).grid(row=5,column=10)

        VegKothe_label = Label(root1,text="Veg Kothe",font="arial 15 bold",fg="steel blue",padx=50,pady=5).grid(row=6,column=0)
        VegKothePrice_label = Label(root1,text="Rs. 80",font="arial 15 bold",fg="steel blue",padx=50,pady=5).grid(row=6,column=10)



        CocaCola_label = Label(root1,text="Coca Cola",font="arial 15 bold",fg="steel blue",padx=50,pady=5).grid(row=7,column=0)
        CocaColaPrice_label = Label(root1,text="Rs. 20",font="arial 15 bold",fg="steel blue",padx=50,pady=5).grid(row=7,column=10)


        root1.mainloop()


    def totalvals():
        
        x=random.randint(100, 50876)
        randomRef = str(x)
        rand.set(randomRef)
        randomRef = int(randomRef)

        

        Noodles_value_get = float(Noodles_value.get())
        HakkaNoodles_value_get = float(HakkaNoodles_value.get())
        VegSaucePasta_value_get = float(VegSaucePasta_value.get())
        CholeKulche_value_get = float(CholeKulche_value.get())
        MasalaDosae_value_get = float(MasalaDosae_value.get())
        VegKothe_value_get = float(VegKothe_value.get())
        CocaCola_value_get = float(CocaCola_value.get())


        
        

        totalcost =  ( ((Noodles_value_get)*70) + ((HakkaNoodles_value_get)*80) + ((VegSaucePasta_value_get)*100) + ((CholeKulche_value_get)*120) + ((MasalaDosae_value_get)*85) +  ((VegKothe_value_get)*80) + ((CocaCola_value_get)*20) )

        
        Total_value.set(totalcost)


        
        import mysql.connector as a
        mydb = a.connect(host="localhost",user="root",password="123456" , database="mysqll")
        mycursor = mydb.cursor()

        s="INSERT INTO Restaurant_final(Order_no , Noodles  , Hakka_Noodles , Veg_Sauce_Pasta   , Chole_Kulche   , Masala_Dosa   , Veg_Kothe   , Coca_Cola   , Total    )   VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        b1=(randomRef , Noodles_value_get , HakkaNoodles_value_get , VegSaucePasta_value_get , CholeKulche_value_get , MasalaDosae_value_get , VegKothe_value_get  , CocaCola_value_get , totalcost )
        mycursor.execute(s,b1)
        mydb.commit()
        mydb.close()
    

    def print():
        tmsg.showinfo("Print","Connect a printer")

    def reset():
        Noodles_value.set(int(0))
        HakkaNoodles_value.set(int(0))
        VegSaucePasta_value.set(int(0))
        CholeKulche_value.set(int(0))
        MasalaDosae_value.set(int(0))
        VegKothe_value.set(int(0))
        CocaCola_value.set(int(0))
        Total_value.set(int(0))
        rand.set(int(0))


    #------------------------------------------------FRAMES------------------------------------------------#

    f1 = Frame(root,borderwidth=8,relief=RAISED,highlightcolor="red",height=10,width=300,pady=20)  
    f1.pack()

    f2 = Frame(root,bd=10,width=1000,height=700,padx=30,pady=90)
    f2.pack(anchor="nw")

    f3 = Frame(root,bd=10,width=700,height=500)
    f3.pack()

    #-------------------------------------------TIME------------------------------------------------------#
    localtime=time.asctime(time.localtime(time.time()))
    lblinfo = Label(f1, font="aria 20 bold",text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=0)

    #-------------------------------------------LABEL INFO-----------------------------------------------#
    lbl = Label(f1,text="Restaurant Management System ",font="lucida 20 bold",fg="steel blue",pady=20).grid(row=0,column=0)



    #-------------------------------------------STRING VALUES-------------------------------------------#

    Noodles_value = IntVar()
    HakkaNoodles_value = IntVar()
    VegSaucePasta_value = IntVar()
    CholeKulche_value = IntVar()
    MasalaDosae_value = IntVar()
    VegKothe_value = IntVar()
    CocaCola_value = IntVar()
    Total_value = IntVar()
    rand = IntVar()

    #-------------------------------------------LABELS & ENTRY FOR FOOD ITEMS--------------------------------#

    Noodles_label = Label(f2,text="NOODLES",fg="steel blue",font="arial 17 bold",padx=20,pady=20)
    Noodles_label.grid(row=0,column=0)
    Noodles_entry = Entry(f2,textvariable=Noodles_value,borderwidth=10,bg="powder blue",font=('ariel' ,16,'bold'))
    Noodles_entry.grid(row=0,column=1)

    HakkaNoodles_label = Label(f2,text="HAKKA NOODLES",fg="steel blue",font="arial 17 bold",padx=20,pady=20)
    HakkaNoodles_label.grid(row=1,column=0)
    HakkaNoodles_entry = Entry(f2,textvariable=HakkaNoodles_value,borderwidth=10,bg="powder blue",font=('ariel' ,16,'bold'))
    HakkaNoodles_entry.grid(row=1,column=1)

    VegSaucePasta_label = Label(f2,text="VEG SAUCE PASTA",fg="steel blue",font="arial 17 bold",padx=20,pady=20)
    VegSaucePasta_label.grid(row=2,column=0)
    VegSaucePasta_entry = Entry(f2,textvariable=VegSaucePasta_value,borderwidth=10,bg="powder blue",font=('ariel' ,16,'bold'))
    VegSaucePasta_entry.grid(row=2,column=1)

    CholeKulche_label = Label(f2,text="CHOLE KULCHE",fg="steel blue",font="arial 17 bold",padx=20,pady=20)
    CholeKulche_label.grid(row=3,column=0)
    CholeKulche_entry = Entry(f2,textvariable=CholeKulche_value,borderwidth=10,bg="powder blue",font=('ariel' ,16,'bold'))
    CholeKulche_entry.grid(row=3,column=1)


    MasalaDosa_label = Label(f2,text="MASALA DOSA",fg="steel blue",font="arial 17 bold",padx=20,pady=20)
    MasalaDosa_label.grid(row=0,column=3)
    MasalaDosa_entry = Entry(f2,textvariable=MasalaDosae_value,borderwidth=10,bg="powder blue",font=('ariel' ,16,'bold'))
    MasalaDosa_entry.grid(row=0,column=4)

    VegKothe_label = Label(f2,text="VEG KOTHE",fg="steel blue",font="arial 17 bold",padx=20,pady=20)
    VegKothe_label.grid(row=1,column=3)
    VegKothe_entry = Entry(f2,textvariable=VegKothe_value,borderwidth=10,bg="powder blue",font=('ariel' ,16,'bold'))
    VegKothe_entry.grid(row=1,column=4)

    CocaCola_label = Label(f2,text="COCA COLA",fg="steel blue",font="arial 17 bold",padx=20,pady=20)
    CocaCola_label.grid(row=2,column=3)
    CocaCola_entry = Entry(f2,textvariable=CocaCola_value,borderwidth=10,bg="powder blue",font=('ariel' ,16,'bold'))
    CocaCola_entry.grid(row=2,column=4)

    Total_label = Label(f2,text="TOTAL",fg="steel blue",font="arial 18 bold",padx=20,pady=20)
    Total_label.grid(row=3,column=3)
    Total_entry = Entry(f2,textvariable=Total_value,borderwidth=10,bg="powder blue",font=('ariel' ,16,'bold'))
    Total_entry.grid(row=3,column=4)

    rand_label = Label(f2,text="ORDER NO.",fg="steel blue",font="arial 18 bold",padx=20,pady=20)
    rand_label.grid(row=0,column=5)
    rand_entry = Entry(f2,textvariable=rand,borderwidth=10,bg="powder blue",font=('ariel' ,16,'bold'))
    rand_entry.grid(row=0,column=6)

    name = Label(f3,text="By Somanshu Mishra",font="lucida 18 bold",fg="steel blue").grid(row=4,column=7)

    #------------------------------------------------BUTTONS---------------------------------------------#

    b1 = Button(f2,text="PRICE",font="arial 20 bold",pady=10,fg="black",bg="powder blue" ,command=priceval,relief=RAISED).grid(row=4,column=0)
    b2 = Button(f2,text="EXIT",font="arial 20 bold",pady=10,fg="black",bg="powder blue" ,command=quit,relief=RAISED).grid(row=4,column=5)
    b3 = Button(f2,text="TOTAL",font="arial 20 bold",pady=10,fg="black",bg="powder blue",command=totalvals ,relief=RAISED).grid(row=4,column=1)
    b4 = Button(f2,text="PRINT",font="arial 20 bold",pady=10,fg="black",bg="powder blue" ,command=print,relief=RAISED).grid(row=4,column=3)
    b5 = Button(f2,text="RESET",font="arial 20 bold",pady=10,fg="black",bg="powder blue",command=reset,relief=RAISED).grid(row=4,column=4)

    
root.mainloop()
