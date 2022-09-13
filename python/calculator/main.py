import tkinter as tk
from tkinter.messagebox import showerror
from xml.dom.expatbuilder import parseFragment

elements = ['+', '-', '/', '*']
root     = tk.Tk()
root.title('My Calculator')

root.resizable(0,0)
root.config(bg='Black')

def make_equation(number):
    present = e.get()
    clear()
    e.insert(0,present+number)

def check(equation):
    global elements
    for i in elements:
        if i in equation:
            return False
        else:
            return False
def calculate():
    try:
        equation = e.get()
        if len(equation) == 0 or check(equation):
            showerror('Error','Nothing Found to Calculate')
        else:
            calculated = eval(equation)
            clear()
            e.insert(0,str(calculated))
    except:
        showerror('Error', 'Something Went Wrong!')
def clear():
    e.delete(0, tk.END)

#Main Entry
e = tk.Entry(root, font=('Helvica', 17), borderwidth=0, bg='Black', fg='#39FF14')
e.grid(row=0, column=0, columnspan=3, padx=10, pady=20, ipadx=20)

button_clear = tk.Button(root, text='C', command = clear, font=('Helvetica', 12),
                        padx=25, pady=25, bg='Black', fg='#39FF14', borderwidth=0)
button_clear.grid(row=0, column=3)

#Row1
button_1 = tk.Button(root, text="1", command=lambda:make_equation('1'), font=('Helvetica',12),
                    padx=25, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_1.grid(row=1, column=0, padx=2)

button_2 = tk.Button(root, text="2", command=lambda:make_equation('2'), font=('Helvetica',12),
                    padx=25, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_2.grid(row=1, column=1)

button_3 = tk.Button(root, text="3", command=lambda:make_equation('3'), font=('Helvetica',12),
                    padx=25, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_3.grid(row=1, column=2)

button_divide = tk.Button(root, text="÷", command=lambda:make_equation('/'), font=('Helvetica',12),
                    padx=23, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_divide.grid(row=1, column=3)

#Row2
button_4 = tk.Button(root, text="4", command=lambda:make_equation('4'), font=('Helvetica',12),
                    padx=25, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_4.grid(row=2, column=0, padx=2)

button_5 = tk.Button(root, text="5", command=lambda:make_equation('5'), font=('Helvetica',12),
                    padx=25, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_5.grid(row=2, column=1)

button_6 = tk.Button(root, text="6", command=lambda:make_equation('6'), font=('Helvetica',12),
                    padx=25, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_6.grid(row=2, column=2)

button_multiple = tk.Button(root, text="x", command=lambda:make_equation('*'), font=('Helvetica',12),
                    padx=24, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_multiple.grid(row=2, column=3)

#row3
button_7 = tk.Button(root, text="7", command=lambda:make_equation('7'), font=('Helvetica',12),
                    padx=25, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_7.grid(row=3, column=0, padx=2)

button_8 = tk.Button(root, text="8", command=lambda:make_equation('8'), font=('Helvetica',12),
                    padx=25, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_8.grid(row=3, column=1)

button_9 = tk.Button(root, text="9", command=lambda:make_equation('9'), font=('Helvetica',12),
                    padx=25, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_9.grid(row=3, column=2)

button_sub = tk.Button(root, text="-", command=lambda:make_equation('-'), font=('Helvetica',12),
                    padx=27, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_sub.grid(row=3, column=3)

#row4
button_dot = tk.Button(root, text=".", command=lambda:make_equation('.'), font=('Helvetica',12),
                    padx=20, pady=10, bg='Black',fg='#39FF14', borderwidth=0)
button_dot.grid(row=4, column=0)

button_zero = tk.Button(root, text="0", command=lambda:make_equation('0'), font=('Helvetica',12),
                    padx=25, pady=15, bg='Black',fg='#39FF14', borderwidth=0)
button_zero.grid(row=4, column=1)

button_equate = tk.Button(root, text="=", command= calculate, font=('Helvetica',12),
                    padx=25, pady=25, bg='#000000',fg='#39FF14', borderwidth=0)
button_equate.grid(row=4, column=2)

button_add = tk.Button(root, text="+", command=lambda:make_equation('+'), font=('Helvetica',12),
                    padx=25, pady=25, bg='Black',fg='#39FF14', borderwidth=0)
button_add.grid(row=4, column=3)

root.mainloop()