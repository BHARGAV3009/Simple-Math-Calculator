import tkinter as tk
from tkinter import messagebox
import math

def find_biggest():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        biggest = max(num1, num2)
        messagebox.showinfo("Result",f"The Biggest number among {num1} and {num2} is {biggest}")
    except ValueError:
        messagebox.showerror("Result","Please Enter a Valid Number")
def find_smallest():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        smallest = min(num1, num2)
        messagebox.showinfo("Result",f"The Smallest number among {num1} and {num2} is {smallest}")
    except ValueError:
        messagebox.showerror("Result","Please Enter Valid Number")
def calc_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        sum1 = num1 + num2
        messagebox.showinfo("Result",f"The Sum of {num1} and {num2} is {sum1}")
    except ValueError:
        messagebox.showerror("Result","Please Enter a Valid Number")
def calc_diff():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        diff = num1 - num2
        messagebox.showinfo("Result",f"The  Difference of {num1} and {num2} is {diff}")
    except ValueError:
        messagebox.showerror("Result","Please Enter a Valid Number")
def calc_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        messagebox.showinfo("Result",f"The Product of {num1} and {num2} is {product}")
    except ValueError:
        messagebox.showerror("Result","Please Enter a Valid Number")
def calc_division():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            raise ValueError("Division is not possible by 0")
        div = num1 / num2
        messagebox.showinfo("Result",f"The Division of {num1} and {num2} is {div}")
    except ValueError:
        messagebox.showerror("Result","Please Enter a Valid Number")
def calc_modulus():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        modulus = num1 % num2
        messagebox.showinfo("Result",f"The Modulus of {num1} and {num2} is {modulus}")
    except ValueError:
        messagebox.showerror("Result","Please Enter a Valid Number")

def calc_numsquare():
    try:
        num1 = float(entry1.get())
        square = num1**2
        messagebox.showinfo("Result",f"The Root of {num1} is {square}")
    except ValueError:
        messagebox.showerror("Result","Please Enter a Valid Number")

def calc_root():
    try:
        num1 = float(entry1.get())
        root = math.sqrt(num1)
        messagebox.showinfo("Result",f"The Root of {num1} is {root}")
    except ValueError:
        messagebox.showerror("Result","Please Enter a Valid Number")

def calc_pie():
    try:
        num1 = float(entry1.get())
        pie = num1 or num2* 3.14159
        messagebox.showinfo("Result",f"The {num1} pie value is {pie}")
    except ValueError:
        messagebox.showerror("Result","Please Enter a Valid Number")

def temp_conv():
    try:
        num1 = float(entry1.get())
        conv = (num1 - 32)/1.8
        messagebox.showinfo("Result",f"The {num1} degree fahrenheit is equal to {conv} degree Celsius")
    except ValueError:
        messagebox.showerror("Result","Please Enter a Valid Number")

def temp_conversion():
    try:
        num1 = float(entry1.get())
        conversion = (num1 * 1.8) + 32
        messagebox.showinfo("Result",f"The {num1} degree Celsius is equal to {conversion} degree Fahrenheit")
    except ValueError:
        messagebox.showerror("Result","Please Enter a Valid Number")

root = tk.Tk()
root.title("CALCULATOR")
font_bold = ("helvetica",10,"bold")
label_title = tk.Label(root,text = "Mathematical Operations")
label_title.config(fg = "White", bg = "Black",font = font_bold)
label_title.grid(row = 0, columnspan = 9, padx = 10,pady = 10)
label1 = tk.Label(root,text = "Enter First Number: ")
label_title = tk.Label(root,text = "Note : If u want to know pie value or square value or root value or tempature conversions,enter number in the first box")
label_title.config(fg = "Black", bg = "Red",font = font_bold)
label_title.grid(row = 1, columnspan = 9, padx = 10,pady = 10)
label1.grid(row = 2,column = 1,padx = 10,pady = 10)
label1.config(font=("Helvetica",10,"bold"))
entry1 = tk.Entry(root)
entry1.grid(row = 2,column = 2,padx = 10,pady = 10)
entry1.config(font=("Helvetica",10))
label2 = tk.Label(root,text = "Enter Second Number : ")
label2.grid(row = 3, column = 1,padx = 10,pady = 10)
label2.config(font=("Helvetica",10))
entry2 = tk.Entry(root)
entry2.config(font=("Helvetica",10,"bold"))
entry2.grid(row = 3,column = 2,padx = 10,pady = 10)
biggest_button = tk.Button(root,text = "Biggest",command = find_biggest)
biggest_button.grid(row  = 4,column = 1,padx = 10,pady = 10)
biggest_button.config(font=("Helvetica",10,"bold"))
smallest_button = tk.Button(root,text = "Smallest",command  = find_smallest)
smallest_button.grid(row = 4,column = 3,padx = 10,pady = 10)
smallest_button.config(font=("Helvetica",10,"bold"))
button_frame = tk.Frame(root)
button_frame.grid(row = 5 , column =1, columnspan = 9,padx = 10,pady = 10)
sum_button = tk.Button(button_frame,text = "Sum",command = calc_sum)
sum_button.grid(row = 0,column = 0,padx = 10,pady = 10)
sum_button.config(font=("Helvetica",10,"bold"))
diff_button = tk.Button(button_frame,text = "Difference",command = calc_diff)
diff_button.grid(row = 0,column = 1,padx = 10,pady = 10)
diff_button.config(font=("Helvetica",10,"bold"))
product_button = tk.Button(button_frame,text = "Product",command = calc_product)
product_button.grid(row = 0,column = 2,padx = 10,pady = 10)
product_button.config(font=("Helvetica",10,"bold"))
div_button = tk.Button(button_frame,text = "Division",command = calc_division)
div_button.grid(row = 0,column = 3,padx = 10,pady = 10)
div_button.config(font=("Helvetica",10,"bold"))
modulus_button = tk.Button(button_frame,text = "Modulus",command =calc_modulus)
modulus_button.grid(row = 0,column = 4,padx = 10,pady = 10)
modulus_button.config(font=("Helvetica",10,"bold"))
square_button = tk.Button(button_frame,text = "Square of Number",command = calc_numsquare)
square_button.grid(row = 1,column = 0,padx = 10,pady = 10)
square_button.config(font=("Helvetica",10,"bold"))
root_button = tk.Button(button_frame,text = "Root of Number",command = calc_root)
root_button.grid(row = 1,column = 1,padx = 10,pady = 10)
root_button.config(font=("Helvetica",10,"bold"))
pie_button = tk.Button(button_frame,text = "Pie",command = calc_pie)
pie_button.grid(row = 1,column = 2,padx = 10,pady = 10)
pie_button.config(font=("Helvetica",10,"bold"))
temp_button = tk.Button(button_frame,text = "Celsius",command = temp_conv)
temp_button.grid(row = 1,column = 3,padx = 10,pady = 10)
temp_button.config(font=("Helvetica",10,"bold"))
conv_button = tk.Button(button_frame,text = "Fahrenheit",command = temp_conversion)
conv_button.grid(row = 1,column = 4,padx = 10,pady = 10)
conv_button.config(font=("Helvetica",10,"bold"))
root.mainloop()
