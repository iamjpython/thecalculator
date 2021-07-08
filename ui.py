import tkinter as tk
import math
import numpy
from tkinter.constants import E, END, SUNKEN, W

c = ""

class Calculator:
    def __init__(self) -> None:

		self.last_answer = 0

		self.root = tk.Tk()
		self.root.title("projectCalcula")
		self.root.resizable(0,0)
		self.root.config(bg="#00061e")
		self.e = tk.Entry(self.root, width=50, borderwidth=5, font=60, justify="right")
		self.e.grid(row=0, column=0,columnspan=5, padx=10, pady=50)
		self.label = tk.Label(self.root, text = "projectCalcula", bd=1, relief=SUNKEN, font=("Dead Revolution",16,"bold"), bg="#036a7d", fg="#00061e").grid(row=8, column=0, columnspan=7, sticky=W+E)

		self.menuinfo = tk.Menu(self.root)
		self.m1 = tk.Menu(self.menuinfo, tearoff=0)
		self.m1.add_command(label="Github Website", command=self.website)
		self.m1.add_command(label="Group Info", command=self.info)

		self.m2 = tk.Menu(self.menuinfo, tearoff=0)
		self.m2.add_command(label="Calculator Operation", command=self.operation)
		self.m2.add_command(label="Errors", command=self.error)

			
		self.root.config(menu=self.menuinfo)
		self.menuinfo.add_cascade(label="About Us", menu=self.m1)
		self.menuinfo.add_cascade(label="Instructions", menu=self.m2)


		self.bsin = tk.Button(self.root, text="sin", padx=22, pady=5, command=lambda:[self.button_click("sin("),self.replica("sin(")], bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=1,column=0,pady=5)
		self.bcos = tk.Button(self.root, text="cos", padx=21, pady=5, command=lambda:[self.button_click("cos("),self.replica("cos(")],bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=1,column=1,pady=5)
		self.btan = tk.Button(self.root, text="tan", padx=20, pady=5, command=lambda:[self.button_click("tan("),self.replica("tan(")],bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=1,column=2,pady=5)
		self.blog = tk.Button(self.root, text="log", padx=22, pady=5, command=lambda:[self.button_click("log("),self.replica("log(")],bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=1,column=3,pady=5)
		self.bleft = tk.Button(self.root, text="(", padx=28, pady=5, command=lambda:[self.button_click("("),self.replica("(")],bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=3,column=3,pady=5)
		self.bright = tk.Button(self.root, text=")", padx=28, pady=5,command=lambda:[self.button_click(")"),self.replica(")")],bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=3,column=4,pady=5)
		self.bsqrt = tk.Button(self.root, text="√", padx=25, pady=5, command=lambda:[self.button_click("sqrt("),self.replica("sqrt(")],bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=3,column=2,pady=5)

		self.basin = tk.Button(self.root, text="asin", padx=18, pady=5, command=lambda:[self.button_click("arcsin("),self.replica("asin(")],bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=2,column=0,pady=5)
		self.bacos = tk.Button(self.root, text="acos", padx=17, pady=5, command=lambda:[self.button_click("arccos("),self.replica("acos(")],bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=2,column=1,pady=5)
		self.batan = tk.Button(self.root, text="atan", padx=17, pady=5, command=lambda:[self.button_click("arctan("),self.replica("atan(")],bg = "#49b5d1", bd=3,  font=("aTahoma",10,"bold")).grid(row=2,column=2,pady=5)
		self.bln = tk.Button(self.root, text=" ln", padx=23, pady=5, command=lambda:[self.button_click("ln("),self.replica("ln(")],bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=1,column=4,pady=5)
		self.bpi = tk.Button(self.root, text="π", command=lambda:[self.button_click("pi"),self.replica(3.14)], padx=26, pady=5,bg = "#49b5d1", bd=3,  font=("aTahoma",10,"bold")).grid(row=2,column=3,pady=5)
		self.bfac = tk.Button(self.root, text="!", command=lambda:[self.button_click("fact("),self.replica("fact(")], padx=29, pady=5,bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=2,column=4,pady=5)
		self.bsqr = tk.Button(self.root, text="x²", command=lambda:[self.button_click("^2"),self.replica("^2")], padx=25, pady=5,bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=3,column=1,pady=5)
		self.bcube = tk.Button(self.root, text="x³", command=lambda:[self.button_click("^3"),self.replica("^3")], padx=24, pady=5,bg = "#49b5d1", bd=3,  font=("Tahoma",10,"bold")).grid(row=3,column=0,pady=5)

		self.bans = tk.Button(self.root, text="ANS",command=lambda:[self.button_click(self.last_answer),self.replica(self.last_answer)], padx=18, pady=10,bg = "#ffde59",fg="#8b0000", bd=3,  font=("Tahoma",10,"bold")).grid(row=7,column=3,pady=5)
 

		self.b1 =tk.Button(self.root, text="1", padx=21, pady=10, command=lambda:[self.button_click(1),self.replica(1)],bg = "#ffffff", bd=3,  font=("Tahoma",10,"bold")).grid(row=6,column=0,pady=5)
		self.b2 =tk.Button(self.root, text="2", padx=21, pady=10, command=lambda:[self.button_click(2),self.replica(2)],bg = "#ffffff", bd=3,  font=("Tahoma",10,"bold")).grid(row=6,column=1,pady=5)
		self.b3 =tk.Button(self.root, text="3", padx=21, pady=10, command=lambda:[self.button_click(3),self.replica(3)],bg = "#ffffff", bd=3,  font=("Tahoma",10,"bold")).grid(row=6,column=2,pady=5)

		self.b4 =tk.Button(self.root, text="4", padx=21, pady=10, command=lambda:[self.button_click(4),self.replica(4)],bg = "#ffffff", bd=3,  font=("Tahoma",10,"bold")).grid(row=5,column=0,pady=5)
		self.b5 =tk.Button(self.root, text="5", padx=21, pady=10, command=lambda:[self.button_click(5),self.replica(5)],bg = "#ffffff", bd=3,  font=("Tahoma",10,"bold")).grid(row=5,column=1,pady=5)
		self.b6 =tk.Button(self.root, text="6", padx=21, pady=10, command=lambda:[self.button_click(6),self.replica(6)],bg = "#ffffff", bd=3,  font=("Tahoma",10,"bold")).grid(row=5,column=2,pady=5)

		self.b7 =tk.Button(self.root, text="7", padx=21, pady=10, command=lambda:[self.button_click(7),self.replica(7)],bg = "#ffffff", bd=3,  font=("Tahoma",10,"bold")).grid(row=4,column=0,pady=5)
		self.b8 =tk.Button(self.root, text="8", padx=21, pady=10, command=lambda:[self.button_click(8),self.replica(8)],bg = "#ffffff", bd=3,  font=("Tahoma",10,"bold")).grid(row=4,column=1,pady=5)
		self.b9 =tk.Button(self.root, text="9", padx=21, pady=10, command=lambda:[self.button_click(9),self.replica(9)],bg = "#ffffff", bd=3,  font=("Tahoma",10,"bold")).grid(row=4,column=2,pady=5)

		self.b0 =tk.Button(self.root, text="0", padx=70, pady=10, command=lambda:[self.button_click(0),self.replica(0)],bg = "#ffffff", bd=3,  font=("Tahoma",10,"bold")).grid(row=7,column=0,columnspan=2, pady=5,)
		self.bdeci =tk.Button(self.root, text=". ", padx=21, pady=10, command=lambda:[self.button_click("."),self.replica(".")],bg = "#ffffff", bd=3,  font=("Tahoma",10,"bold")).grid(row=7,column=2,pady=5)

		self.badd =tk.Button(self.root, text=" +", padx=24, pady=10, command=lambda:[self.button_click("+"),self.replica("+")],bg = "#ffde59",fg="#8b0000", bd=3,  font=("Tahoma",10,"bold")).grid(row=6,column=3,pady=5)
		self.bminus =tk.Button(self.root, text="- ", padx=26, pady=10, command=lambda:[self.button_click("-"),self.replica("-")],bg = "#ffde59",fg="#8b0000", bd=3,  font=("Tahoma",10,"bold")).grid(row=6,column=4,pady=5)
		self.btimes =tk.Button(self.root, text="x", padx=28, pady=10, command=lambda:[self.button_click("*"),self.replica("*")],bg = "#ffde59",fg="#8b0000", bd=3,  font=("Tahoma",10,"bold")).grid(row=5,column=3,pady=5)
		self.bdivide =tk.Button(self.root, text=" ÷ ", padx=22, pady=10, command=lambda:[self.button_click("/"),self.replica("/")],bg = "#ffde59",fg="#8b0000", bd=3,  font=("Tahoma",10,"bold")).grid(row=5,column=4,pady=5)

		self.bdel =tk.Button(self.root, text="DEL", padx=20, pady=10, command=self.delete, bg = "#ff5757", bd=3, fg="#f8f8ff", font=("Tahoma",10,"bold")).grid(row=4,column=3,pady=5)
		self.bclear =tk.Button(self.root, text="AC", padx=22, pady=10, command=self.ac,bg = "#ff5757", bd=3,fg="#f8f8ff", font=("Tahoma",10,"bold")).grid(row=4,column=4,pady=5)
		self.bequal =tk.Button(self.root, text="=", padx=25, pady=10, command=self.evaluate, bg = "#ffde59", bd=3,fg="#8b0000",  font=("Tahoma",10,"bold")).grid(row=7,column=4,pady=5)
        
		self.root.bind('<Return>', self.evaluate)

	def button_click(self,num):
		dis = self.e.get()
		x = self.e.index(INSERT)
		self.e.insert(x,str(num)) 

    def ac(self):
        pass

	def delete(self):
		global c
		c = list(self.e.get())
		x = self.e.index(INSERT) - 1
		self.e.delete(x, x+1)
        
    def duplicate(self,num):
        global c
        c = c+str(num)

    def evaluate(self):
        pass

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calc =Calculator()
    calc.run()     
