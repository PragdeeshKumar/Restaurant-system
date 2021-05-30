from tkinter import*

window=Tk()
window.geometry("700x500")

def calculate():
      special_pizza=e1.get()
      chicken_pizza=e2.get()
      peperoni_pizza=e3.get()
      mushroom_cheese_pizza=e4.get()
      coffee=e5.get()
      print(type(coffee))
      total=(int(special_pizza)*30)+(int(chicken_pizza)*25)+(int(peperoni_pizza)*40)+(int(mushroom_cheese_pizza)*50)+(int(coffee)*30)
      label13=Label(window,text=total,font="tahoma 20 bold")
      label13.place(x=350,y=250)

label1=Label(window,text="PK restaurant",font="tahoma 20 bold")
label1.place(x=350,y=20, anchor="center")


#----------menu section-------

label1=Label(window,text="Menu",font="tahoma 20")
label1.place(x=750,y=180)


label2=Label(window,text="special pizza      Rs 30",font="tahoma 18")
label2.place(x=600,y=120)


label3=Label(window,text="chicken pizza     Rs 25",font="tahoma 18")
label3.place(x=600,y=150)


label4=Label(window,text="peperoni pizza     Rs 40",font="tahoma 18 ")
label4.place(x=600,y=180)


label5=Label(window,text="mushroom cheese pizza    Rs 50",font="tahoma 18")
label5.place(x=600,y=210)


label6=Label(window,text="coffee   Rs 30",font="tahoma 18")
label6.place(x=600,y=240)

#------------- billing section ----------

label7=Label(window,text="Select the items",font="tahoma 18")
label7.place(x=50,y=50)

label8=Label(window,text="special",font="tahoma 18")
label8.place(x=50,y=120)

e1=Entry(window)
e1.place(x=50,y=150)

label9=Label(window,text="chicken ",font="tahoma 18")
label9.place(x=50,y=170)

e2=Entry(window)
e2.place(x=50,y=200)

label10=Label(window,text="peperoni",font="tahoma 18")
label10.place(x=50,y=220)

e3=Entry(window)
e3.place(x=50,y=250)

label11=Label(window,text="mushroom cheese",font="tahoma 18")
label11.place(x=50,y=270)

e4=Entry(window)
e4.place(x=50,y=300)

label12=Label(window,text="Coffee",font="tahoma 18")
label12.place(x=50,y=320)


e5=Entry(window)
e5.place(x=50,y=350)

b2=Button(window,text='bill',width=20,command=calculate)
b2.place(x=50,y=400)


window.mainloop()