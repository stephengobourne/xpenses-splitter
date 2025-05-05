#replace main coding tab with this one via copy and pasting 
from tkinter import *
import random
import time
from tkinter import messagebox

root = Tk()

# Set the window size
window_width = 900
window_height = 550

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the geometry of the window
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.title("Restaurant Billing System")

Tops = Frame(root, width=900, height=40, bd=4, relief="raise")
Tops.pack(side=TOP)
Bottoms = Frame(root, width=900, height=40, bd=4, relief="raise")
Bottoms.pack(side=BOTTOM)

f1 = Frame(root, width=900, height=470, bd=4, relief="raise")
f1.pack(side=LEFT)

f1a = Frame(f1, width=600, height=250, bd=4, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=600, height=220, bd=4, relief="raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=300, height=250, bd=4, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=300, height=250, bd=4, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=300, height=220, bd=4, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=300, height=220, bd=4, relief="raise")
f2ab.pack(side=LEFT)

green_color = "green"

lblInfo = Label(Tops, font=('arial', 18, 'bold'), text="Restaurant Billing System", bd=6, anchor='w', fg=green_color)
lblInfo.grid(row=0, column=0)
lblcopyright = Label(Bottoms, font=('arial', 8, 'italic'), text="Created by Raisul Islam", bd=0, anchor='w', fg=green_color)
lblcopyright.grid(row=0, column=0)

# Variables
PaymentRef = StringVar()
chickenSandwiches = StringVar()
beefBurgers = StringVar()
wings = StringVar()
pizza = StringVar()
frenchFries = StringVar()
salad = StringVar()
softDrinks = StringVar()
water = StringVar()
costchickenSandwiches = StringVar()
costbeefBurgers = StringVar()
costwings = StringVar()
costpizza = StringVar()
costfrenchFries = StringVar()
costsalad = StringVar()
costsoftDrinks = StringVar()
costwater = StringVar()
dateRef = StringVar()
subTotal = StringVar()
vat = StringVar()
totalPrice = StringVar()
dateRef.set(time.strftime("%m/%d/%y"))
vat.set(0)
chickenSandwiches.set(0)
beefBurgers.set(0)
wings.set(0)
pizza.set(0)
frenchFries.set(0)
salad.set(0)
softDrinks.set(0)
water.set(0)
subTotal.set(0)
totalPrice.set(0)
costchickenSandwiches.set("$12")
costbeefBurgers.set("$12")
costwings.set("$7")
costpizza.set("$11")
costsoftDrinks.set("$4")
costfrenchFries.set("$5")
costsalad.set("$5")
costwater.set("$1")

def tPrice():
    try:
        cSprice = int(costchickenSandwiches.get().replace("$", ""))
        bBprice = int(costbeefBurgers.get().replace("$", ""))
        wPrice = int(costwings.get().replace("$", ""))
        pPrice = int(costpizza.get().replace("$", ""))
        fFprice = int(costfrenchFries.get().replace("$", ""))
        sPrice = int(costsalad.get().replace("$", ""))
        sDprice = int(costsoftDrinks.get().replace("$", ""))
        wPriceWater = int(costwater.get().replace("$", ""))

        cSno = int(chickenSandwiches.get())
        bBno = int(beefBurgers.get())
        wNo = int(wings.get())
        pNo = int(pizza.get())
        fFno = int(frenchFries.get())
        sNo = int(salad.get())
        sDno = int(softDrinks.get())
        wNoWater = int(water.get())
        tempVat = int(vat.get())

        subPrice = (cSprice * cSno + bBprice * bBno + wPrice * wNo + pPrice * pNo + fFprice * fFno +
                    sPrice * sNo + sDprice * sDno + wPriceWater * wNoWater)
        totalCost = f"${subPrice}"
        totalCostwithVat = f"${int(subPrice + (subPrice * tempVat) / 100)}"
        subTotal.set(totalCost)
        totalPrice.set(totalCostwithVat)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric values for quantity and VAT.")

def iExit():
    qexit = messagebox.askyesno("Billing System", "Do you want to exit?")
    if qexit:
        root.destroy()

def reset():
    PaymentRef.set("")
    chickenSandwiches.set(0)
    beefBurgers.set(0)
    wings.set(0)
    pizza.set(0)
    frenchFries.set(0)
    salad.set(0)
    softDrinks.set(0)
    water.set(0)
    subTotal.set("")
    totalPrice.set("")
    vat.set(0)

def refNo():
    x = random.randint(10034, 699812)
    randomRef = str(x)
    PaymentRef.set("BILL" + randomRef)

# Order Info Labels & Entries
lblRef = Label(f1aa, font=('arial', 12, 'bold'), fg="red", text="Reference No", bd=8, justify='left')
lblRef.grid(row=0, column=0)
txtRef = Entry(f1aa, font=('arial', 12, 'bold'), textvariable=PaymentRef,
               bd=6, insertwidth=2, justify='left', width=12)
txtRef.grid(row=0, column=1)

lblCs = Label(f1aa, font=('arial', 12, 'bold'), fg=green_color, text="Chicken Sandwiches", bd=8, justify='left')
lblCs.grid(row=1, column=0)
txtCs = Entry(f1aa, font=('arial', 12, 'bold'), textvariable=chickenSandwiches,
              bd=6, insertwidth=2, justify='left', width=12)
txtCs.grid(row=1, column=1)

lblBb = Label(f1aa, font=('arial', 12, 'bold'), fg=green_color, text="Beef Burgers", bd=8, justify='left')
lblBb.grid(row=2, column=0)
txtBb = Entry(f1aa, font=('arial', 12, 'bold'), textvariable=beefBurgers,
              bd=6, insertwidth=2, justify='left', width=12)
txtBb.grid(row=2, column=1)

lblWings = Label(f1aa, font=('arial', 12, 'bold'), fg=green_color, text="Wings", bd=8, justify='left')
lblWings.grid(row=3, column=0)
txtWings = Entry(f1aa, font=('arial', 12, 'bold'), textvariable=wings,
                 bd=6, insertwidth=2, justify='left', width=12)
txtWings.grid(row=3, column=1)

lblPizza = Label(f1aa, font=('arial', 12, 'bold'), fg=green_color, text="Pizza", bd=8, justify='left')
lblPizza.grid(row=4, column=0)
txtPizza = Entry(f1aa, font=('arial', 12, 'bold'), textvariable=pizza,
                 bd=6, insertwidth=2, justify='left', width=12)
txtPizza.grid(row=4, column=1)

lblFf = Label(f1aa, font=('arial', 12, 'bold'), fg=green_color, text="French Fries", bd=8, justify='left')
lblFf.grid(row=5, column=0)
txtFf = Entry(f1aa, font=('arial', 12, 'bold'), textvariable=frenchFries,
              bd=6, insertwidth=2, justify='left', width=12)
txtFf.grid(row=5, column=1)

lblSalad = Label(f1aa, font=('arial', 12, 'bold'), fg=green_color, text="Salad", bd=8, justify='left')
lblSalad.grid(row=6, column=0)
txtSalad = Entry(f1aa, font=('arial', 12, 'bold'), textvariable=salad,
                 bd=6, insertwidth=2, justify='left', width=12)
txtSalad.grid(row=6, column=1)

lblSd = Label(f1aa, font=('arial', 12, 'bold'), fg=green_color, text="Soft Drinks", bd=8, justify='left')
lblSd.grid(row=7, column=0)
txtSd = Entry(f1aa, font=('arial', 12, 'bold'), textvariable=softDrinks,
              bd=6, insertwidth=2, justify='left', width=12)
txtSd.grid(row=7, column=1)

lblWater = Label(f1aa, font=('arial', 12, 'bold'), fg=green_color, text="Water", bd=8, justify='left')
lblWater.grid(row=8, column=0)
txtWater = Entry(f1aa, font=('arial', 12, 'bold'), textvariable=water,
                 bd=6, insertwidth=2, justify='left', width=12)
txtWater.grid(row=8, column=1)

# Payment Info Labels & Entries
lbldate = Label(f1ab, font=('arial', 12, 'bold'), fg=green_color, text="Date", bd=8, justify='left')
lbldate.grid(row=0, column=0)
txtdate = Entry(f1ab, font=('arial', 12, 'bold'), textvariable=dateRef,
                bd=6, insertwidth=2, justify='left', width=12)
txtdate.grid(row=0, column=1)

lblCcs = Label(f1ab, font=('arial', 12, 'bold'), fg=green_color, text="Price of Chicken Sandwiches", bd=8, justify='left')
lblCcs.grid(row=1, column=0)
txtCcs = Entry(f1ab, font=('arial', 12, 'bold'), textvariable=costchickenSandwiches,
               bd=6, insertwidth=2, justify='left', width=12)
txtCcs.grid(row=1, column=1)

lblCbb = Label(f1ab, font=('arial', 12, 'bold'), fg=green_color, text="Price of Beef Burgers", bd=8, justify='left')
lblCbb.grid(row=2, column=0)
txtCbb = Entry(f1ab, font=('arial', 12, 'bold'), textvariable=costbeefBurgers,
               bd=6, insertwidth=2, justify='left', width=12)
txtCbb.grid(row=2, column=1)

lblCWings = Label(f1ab, font=('arial', 12, 'bold'), fg=green_color, text="Price of Wings", bd=8, justify='left')
lblCWings.grid(row=3, column=0)
txtCWings = Entry(f1ab, font=('arial', 12, 'bold'), textvariable=costwings,
                  bd=6, insertwidth=2, justify='left', width=12)
txtCWings.grid(row=3, column=1)

lblCPizza = Label(f1ab, font=('arial', 12, 'bold'), fg=green_color, text="Price of Pizza", bd=8, justify='left')
lblCPizza.grid(row=4, column=0)
txtCPizza = Entry(f1ab, font=('arial', 12, 'bold'), textvariable=costpizza,
                  bd=6, insertwidth=2, justify='left', width=12)
txtCPizza.grid(row=4, column=1)

lblCff = Label(f1ab, font=('arial', 12, 'bold'), fg=green_color, text="Price of French Fries", bd=8, justify='left')
lblCff.grid(row=5, column=0)
txtCff = Entry(f1ab, font=('arial', 12, 'bold'), textvariable=costfrenchFries,
               bd=6, insertwidth=2, justify='left', width=12)
txtCff.grid(row=5, column=1)

lblCSalad = Label(f1ab, font=('arial', 12, 'bold'), fg=green_color, text="Price of Salad", bd=8, justify='left')
lblCSalad.grid(row=6, column=0)
txtCSalad = Entry(f1ab, font=('arial', 12, 'bold'), textvariable=costsalad,
                  bd=6, insertwidth=2, justify='left', width=12)
txtCSalad.grid(row=6, column=1)

lblCsd = Label(f1ab, font=('arial', 12, 'bold'), fg=green_color, text="Price of Soft Drinks", bd=8, justify='left')
lblCsd.grid(row=7, column=0)
txtCsd = Entry(f1ab, font=('arial', 12, 'bold'), textvariable=costsoftDrinks,
               bd=6, insertwidth=2, justify='left', width=12)
txtCsd.grid(row=7, column=1)

lblCwater = Label(f1ab, font=('arial', 12, 'bold'), fg=green_color, text="Price of Water", bd=8, justify='left')
lblCwater.grid(row=8, column=0)
txtCwater = Entry(f1ab, font=('arial', 12, 'bold'), textvariable=costwater,
                 bd=6, insertwidth=2, justify='left', width=12)
txtCwater.grid(row=8, column=1)

# Total Payment Info Labels & Entries
lblPrice = Label(f2aa, font=('arial', 12, 'bold'), fg=green_color, text="Price", bd=8, justify='left')
lblPrice.grid(row=0, column=0)
txtPrice = Entry(f2aa, font=('arial', 12, 'bold'), textvariable=subTotal,
                 bd=6, insertwidth=2, justify='left', width=12)
txtPrice.grid(row=0, column=1)

lblVat = Label(f2aa, font=('arial', 12, 'bold'), fg=green_color, text="Value Added Tax", bd=8, justify='left')
lblVat.grid(row=1, column=0)
txtVat = Entry(f2aa, font=('arial', 12, 'bold'), textvariable=vat,
               bd=6, insertwidth=2, justify='left', width=12)
txtVat.grid(row=1, column=1)

lblTp = Label(f2aa, font=('arial', 12, 'bold'), fg=green_color, text="Total Price", bd=8, justify='left')
lblTp.grid(row=2, column=0)
txtTp = Entry(f2aa, font=('arial', 12, 'bold'), textvariable=totalPrice,
              bd=6, insertwidth=2, justify='left', width=12)
txtTp.grid(row=2, column=1)

# Buttons
btnTotal = Button(f2ab, padx=12, pady=12, bd=6, fg=green_color,
                  font=('arial', 12, 'bold'), width=12,
                  text="Calculate Total Price", command=tPrice)
btnTotal.grid(row=0, column=0)
btnRefer = Button(f2ab, padx=12, pady=12, bd=6, fg=green_color,
                  font=('arial', 12, 'bold'), width=12,
                  text="Receipt", command=refNo)
btnRefer.grid(row=0, column=1)
btnReset = Button(f2ab, padx=12, pady=12, bd=6, fg=green_color,
                  font=('arial', 12, 'bold'), width=12,
                  text="Reset", command=reset)
btnReset.grid(row=1, column=0)
btnExit = Button(f2ab, padx=12, pady=12, bd=6, fg=green_color,
                 font=('arial', 12, 'bold'), width=12,
                 text="Exit", command=iExit)
btnExit.grid(row=1, column=1)

root.mainloop()
