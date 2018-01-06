from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaraunt Management System")

text_Input = StringVar()
operator = ""

Tops = Frame(root,width = 1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width = 300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

#===================Time===========================
localtime=time.asctime(time.localtime(time.time()))
#==================Info============================
lblInfo = Label(Tops,font=('arial',50,'bold'),text="Restaraunt Management Systems",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#==============================Calculator====================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnclearDiaplay():
        global operator
        operator=""
        text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x = random.randint(12000,17322)
    randomRef = str(x)
    rand.set(randomRef)

    Cof= float(Fries.get())
    CoD= float(Drinks.get())
    CoB= float(Burger.get())
    CoVR= float(vegRoll.get())
    CoSR= float(SRoll.get())
    CoCP= float(CPaneer.get())

    CostofFries = Cof * 35
    CostofDrinks = CoD * 40
    CostofBurger = CoB * 44
    CostofVegRoll = CoVR * 40
    CostofSpringRoll = CoSR * 20
    CostofChillypaneer = CoCP * 50

    CostofMeal = "₹",str("%.2f"% (CostofFries + CostofDrinks + CostofBurger + CostofVegRoll + CostofSpringRoll + CostofChillypaneer))

    PayTax = ((CostofFries + CostofDrinks + CostofBurger + CostofVegRoll + CostofSpringRoll + CostofChillypaneer)*0.28)

    Meal = (CostofFries + CostofDrinks + CostofBurger + CostofVegRoll + CostofSpringRoll + CostofChillypaneer)

    Ser_Charge = ((CostofFries + CostofDrinks + CostofBurger + CostofVegRoll + CostofSpringRoll + CostofChillypaneer)/99)

    OverAllCost = "₹",str("%.2f"% (PayTax + Meal + Ser_Charge))

    PaidTax = "₹",str("%.2f"% PayTax)

    Service = "₹",str("%.2f"% Ser_Charge )

    service.set(Service)
    Cost.set(CostofMeal)
    stateTax.set(PaidTax)
    subTotal.set(CostofMeal)
    TotalCost.set(OverAllCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    vegRoll.set("")
    Burger.set("")
    SRoll.set("")
    CPaneer.set("")
    Drinks.set("")
    Cost.set("")
    service.set("")
    stateTax.set("")
    subTotal.set("")
    TotalCost.set("")


txtDisplay = Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right')
txtDisplay.grid(columnspan=4)

#--------------------button row2----------------------------
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue",command=lambda: btnClick("+")).grid(row=2,column=3)
# ----------------------------row3-------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda: btnClick(6)).grid(row=3,column=2)

subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue",command=lambda: btnClick("-")).grid(row=3,column=3)
# ------------------------------------row4-------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda: btnClick(3)).grid(row=4,column=2)

multiplication=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue",command=lambda: btnClick("*")).grid(row=4,column=3)
#----------------------------------------row5--------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",command=lambda: btnClick(0)).grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="c",bg="powder blue",command=btnclearDiaplay).grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)

divide=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda: btnClick("/")).grid(row=5,column=3)
# ----------------------------------------------------------Restarunt Info1---------------------------------------------------------------------------------------------------------
rand= StringVar()
Fries= StringVar()
vegRoll= StringVar()
Burger= StringVar()
SRoll = StringVar()
CPaneer = StringVar()

lblReference = Label(f1,font=('arial',16,'bold'),text="Reference",bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtRefrence= Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtRefrence.grid(row=0,column=1)

lblFries = Label(f1,font=('arial',16,'bold'),text="French Fries",bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries= Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtFries.grid(row=1,column=1)

lblvegRoll = Label(f1,font=('arial',16,'bold'),text="Veg. Roll",bd=16,anchor='w')
lblvegRoll.grid(row=2,column=0)
txtvegRoll= Entry(f1,font=('arial',16,'bold'),textvariable=vegRoll,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtvegRoll.grid(row=2,column=1)

lblBurger = Label(f1,font=('arial',16,'bold'),text="Veg. Burger",bd=16,anchor='w')
lblBurger.grid(row=3,column=0)
txtBurger= Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtBurger.grid(row=3,column=1)

lblSRoll = Label(f1,font=('arial',16,'bold'),text="Spring Roll",bd=16,anchor='w')
lblSRoll.grid(row=4,column=0)
txtSRoll= Entry(f1,font=('arial',16,'bold'),textvariable=SRoll,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtSRoll.grid(row=4,column=1)

lblCPaneer = Label(f1,font=('arial',16,'bold'),text="Chilly Paneer ",bd=16,anchor='w')
lblCPaneer .grid(row=5,column=0)
txtCPaneer = Entry(f1,font=('arial',16,'bold'),textvariable=CPaneer ,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtCPaneer .grid(row=5,column=1)

#----------------------------------Restarunt Info2---------------------------------------------------------------------------------
Drinks = StringVar()
Cost = StringVar()
service = StringVar()
stateTax = StringVar()
subTotal = StringVar()
TotalCost = StringVar()

lblDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks= Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtDrinks.grid(row=0,column=3)

lblCost = Label(f1,font=('arial',16,'bold'),text="Cost of Snacks",bd=16,anchor='w')
lblCost.grid(row=1,column=2)
txtCost= Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtCost.grid(row=1,column=3)

lblService = Label(f1,font=('arial',16,'bold'),text="Service Charge",bd=16,anchor='w')
lblService.grid(row=2,column=2)
txtService= Entry(f1,font=('arial',16,'bold'),textvariable=service,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtService.grid(row=2,column=3)

lblstateTax = Label(f1,font=('arial',16,'bold'),text="State Tax",bd=16,anchor='w')
lblstateTax.grid(row=3,column=2)
txtstateTax= Entry(f1,font=('arial',16,'bold'),textvariable=stateTax,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtstateTax.grid(row=3,column=3)

lblsubTotal = Label(f1,font=('arial',16,'bold'),text="Sub Total",bd=16,anchor='w')
lblsubTotal.grid(row=4,column=2)
txtsubTotal= Entry(f1,font=('arial',16,'bold'),textvariable=subTotal,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtsubTotal.grid(row=4,column=3)

lblTotalCost = Label(f1,font=('arial',16,'bold'),text="Total Cost ",bd=16,anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost = Entry(f1,font=('arial',16,'bold'),textvariable=TotalCost ,bd=10,insertwidth=4,bg="powder blue",justify = 'right')
txtTotalCost .grid(row=5,column=3)
#--------------------------------------Buttons-------------------------------------------
btnTotal=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command = Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command = Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command = qExit).grid(row=7,column=3)




root.mainloop()
