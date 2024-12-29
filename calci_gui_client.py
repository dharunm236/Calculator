import socket
from time import sleep
from tkinter import *

expression = ""
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

win = Tk()  # Create a basic window
win.geometry("312x324")  # Size of the window
win.resizable(0, 0)  # Prevent resizing the window
win.title("Calculator-Dharun")

# Global expression variable


# Function to update input field when a number is entered
def btn_click(item):
    global expression
    if(item=="OFF"):
        input_text.set("TURNING OFF..")
        win.after(1000, win.destroy)
    else:
        expression = expression + str(item)
        input_text.set(expression)

    # Function to clear the input field
def bt_clear():
    global expression
    expression = ""
    input_text.set("")

    # Function to delete the last character in the input field
def bt_delete():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

    # Function to calculate the expression
def bt_equal():
    global expression
    msg=expression
    client.sendto(msg.encode(),('localhost',12345))
    modmsg,addr=client.recvfrom(2048)
    result=modmsg
    input_text.set(result)
    expression=""


    # Instance of input field
input_text = StringVar()
# Creating a frame for the input field
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=4)
input_frame.pack(side=TOP)

# Creating an input field inside the 'Frame'
input_field = Entry(input_frame, font=('Digital-7 Mono', 18, 'bold'), textvariable=input_text, width=50, bg="black", fg="white", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # Internal padding to increase the height of input field

# Creating another 'Frame' for the buttons
btns_frame = Frame(win, width=312, height=272.5, bg="#333333")
btns_frame.pack()

    # Button styles
button_bg = "#FF8C00"  # Orange background color
button_fg = "#000000"  # Black text color
button_active_bg = "#FFA500"  # Slightly lighter orange for active state
button_width = 10
button_height = 3
padx, pady = 1, 1

# First row
clear = Button(btns_frame, text="AC", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=bt_clear).grid(row=0, column=0, padx=padx, pady=pady)
off = Button(btns_frame, text="OFF", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click("OFF")).grid(row=0, column=1, padx=padx, pady=pady)
delete = Button(btns_frame, text="DEL", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=bt_delete).grid(row=0, column=2, padx=padx, pady=pady)
divide = Button(btns_frame, text="/", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=padx, pady=pady)

# Second row
seven = Button(btns_frame, text="7", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=padx, pady=pady)
eight = Button(btns_frame, text="8", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=padx, pady=pady)
nine = Button(btns_frame, text="9", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=padx, pady=pady)
multiply = Button(btns_frame, text="*", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=padx, pady=pady)

# Third row
four = Button(btns_frame, text="4", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=padx, pady=pady)
five = Button(btns_frame, text="5", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=padx, pady=pady)
six = Button(btns_frame, text="6", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=padx, pady=pady)
minus = Button(btns_frame, text="-", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=padx, pady=pady)

# Fourth row
one = Button(btns_frame, text="1", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=padx, pady=pady)
two = Button(btns_frame, text="2", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=padx, pady=pady)
three = Button(btns_frame, text="3", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=padx, pady=pady)
plus = Button(btns_frame, text="+", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=padx, pady=pady)

# Fifth row
zero = Button(btns_frame, text="0", fg=button_fg, width=21, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=padx, pady=pady)
point = Button(btns_frame, text=".", fg=button_fg, width=button_width, height=button_height, bd=0, bg=button_bg, activebackground=button_active_bg, cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=padx, pady=pady)
equals = Button(btns_frame, text="=", fg=button_fg, width=button_width, height=button_height, bd=0, bg="green", activebackground=button_active_bg, cursor="hand2", command=bt_equal).grid(row=4, column=3, padx=padx, pady=pady)

win.mainloop()