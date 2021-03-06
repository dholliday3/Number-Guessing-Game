#Daniel Holliday
#903176570 | dholliday3@gatech.edu
#section A1
#I worked on this assignment alone, using only this semester's course material.

## Calculate stats per 36min by dividing by minutes and then multiplying by 36. 
## Calculations for 3 pointers, Free throws, Rebounds, Assists, and Points on a 36 minute basis. 

from tkinter import *
from csv import *

class HW6:

     def __init__(self, rWin):
          self.rWin = rWin

          self.rWin.title("Number Search Generator!")
          self.lab1 = Label(self.rWin, text="Number Search File:").grid(row=0, column=0, pady=1, padx=1)
          self.lab2 = Label(self.rWin, text="Number Bank File:").grid(row=1, column=0, pady=1, padx=1)

          #Entries 
          self.sv1 = StringVar()
          self.e1 = Entry(self.rWin, textvariable=self.sv1, width=100, state="readonly").grid(row=0, column=1, pady=1, padx=1)
          self.sv1.set("No File Selected")
          
          self.sv2 = StringVar()
          self.e2 = Entry(self.rWin, textvariable=self.sv2, width=100, state="readonly").grid(row=1, column=1, pady=1, padx=1)
          self.sv2.set("No File Selected")

          #Buttons!!!
          ## Number search file --> will call openNSClicked()
          self.b1 = Button(self.rWin, width=20, text="Select File").grid(row=0, column=2, pady=1, padx=1)
          ## Number bank file --> will call openNBClicked()
          self.b2 = Button(self.rWin, width=20, text="Select File").grid(row=1, column=2, pady=1, padx=1)
          ## Generate Number Search --> calls method generate()
          self.b3 = Button(self.rWin, width=30, text="Generate Number Search").grid(row=2, column=0, pady=1, padx=1)


          








rWin = Tk()
app = HW6(rWin)
rWin.mainloop()
