global loc
import math
from tabulate import tabulate
from tkinter import*
SOFTWARE_NAME= input("ENTER THE NAME OF THE SOFTWARE:")
MODULE = int(input ("ENTER THE NUMBER OF MODULES YOU WISH TO HAVE:"))
head = ["MODULE_NAME", "OPTIMISTIC_VALUE", "MOSTLIKELY_VALUE", "PESIMISTIC_VALUE", "AVERAGE"]
def create_table():
    mylist = []
    MODULE_NAME=input("ENTER THE NAME OF THE MODULE:" )
    OPTIMISTIC_VALUE=int(input("ENTER THE OPTIMISTIC VALUE:"))
    MOSTLIKELY_VALUE=int(input("ENTER THE MOST LIKELY VALUE:"))
    PESIMISTIC_VALUE=int(input("ENTER THE PESIMISTIC VALUE:"))
    Avg = (OPTIMISTIC_VALUE + 4*(MOSTLIKELY_VALUE)+ PESIMISTIC_VALUE)/6
   # loc += Avg
   # print(loc)
    mylist.append(MODULE_NAME)
    mylist.append(OPTIMISTIC_VALUE)
    mylist.append(MOSTLIKELY_VALUE)
    mylist.append(PESIMISTIC_VALUE)
    mylist.append(Avg) 
    return mylist
index = 0
mylist = []
loc = 0
while(index < MODULE):
    mylist.append(create_table())
    #index = index + 1
    print(mylist)
    index = index + 1
    OPTIMISTIC_VALUE=int(input("ENTER THE OPTIMISTIC VALUE:"))
    MOSTLIKELY_VALUE=int(input("ENTER THE MOST LIKELY VALUE:"))
    PESIMISTIC_VALUE=int(input("ENTER THE PESIMISTIC VALUE:"))
    Avg = (OPTIMISTIC_VALUE + 4*(MOSTLIKELY_VALUE)+ PESIMISTIC_VALUE)/6
    loc += Avg
print("THE TOTAL ESTIMATED LOC:",math.ceil(loc))    
#AVG = loc
print(tabulate(mylist, headers=head, tablefmt="fancygrid"))
LOC_PM=int(input("ENTER THE AVERAGE LOC PER PERSON MONTH: "))
LABOUR_RATE= int(input("ENTER THE LABOUR RATE PER MONTH($): "))
window = Tk()
COST_PER_LOC = LABOUR_RATE / LOC_PM
def btn1():
  print("THE COST PER LOC($):",COST_PER_LOC)
button1 =  Button(window, text="COST PER LOC", command=btn1)
button1.pack()
COST_PROJECT = loc * COST_PER_LOC
def btn2():
    print("THE COST OF THE PROJECT($):",math.ceil(COST_PROJECT))
button2 =  Button(window, text="COST OF PROJECT", command=btn2)
button2.pack()
EFFORT_PROJECT= COST_PROJECT / LOC_PM
def btn3():
    print("THE EFFORT OF THE PROJECT (Person Month):", EFFORT_PROJECT)
button3 =  Button(window, text="EFFORT OF THE PROJECT", command=btn3)
button3.pack()
window.mainloop()
