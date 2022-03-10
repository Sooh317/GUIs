import tkinter as tk

number = 0
first_term = 0
op = None

def plus():
    global first_term, number, op
    if op != None: 
        op = 0
        return
    op = 0
    first_term = number
    number = 0
    show_number(number)


def minus():
    global first_term, number, op
    if op != None: 
        op = 1
        return
    op = 1
    first_term = number
    number = 0
    show_number(number)


def times():
    global first_term, number, op
    if op != None: 
        op = 2
        return
    op = 2
    first_term = number
    number = 0
    show_number(number)


def div():
    global first_term, number, op
    if op != None: 
        op = 3
        return
    op = 3
    first_term = number
    number = 0
    show_number(number)

def eq():
    global first_term, number, op
    if op == 0:
        number += first_term
    elif op == 1:
        number -= first_term
    elif op == 2:
        number *= first_term
    elif op == 3:
        number /= first_term
    else:
        assert False
    op = None
    show_number(number)

def key(k):
    global number
    number = number * 10 + k
    show_number(number)
    return

def show_number(k):
    global e
    e.delete(0, tk.END)
    e.insert(0, k)
    return


# window
root = tk.Tk()

frame = tk.Frame(root) # a container that contains widgets
frame.grid()

b0 = tk.Button(frame, text='0', command=lambda:key(0), font=('arial', 14))
b1 = tk.Button(frame, text='1', command=lambda:key(1), font=('arial', 14))
b2 = tk.Button(frame, text='2', command=lambda:key(2), font=('arial', 14))
b3 = tk.Button(frame, text='3', command=lambda:key(3), font=('arial', 14))
b4 = tk.Button(frame, text='4', command=lambda:key(4), font=('arial', 14))
b5 = tk.Button(frame, text='5', command=lambda:key(5), font=('arial', 14))
b6 = tk.Button(frame, text='6', command=lambda:key(6), font=('arial', 14))
b7 = tk.Button(frame, text='7', command=lambda:key(7), font=('arial', 14))
b8 = tk.Button(frame, text='8', command=lambda:key(8), font=('arial', 14))
b9 = tk.Button(frame, text='9', command=lambda:key(9), font=('arial', 14))
bplus = tk.Button(frame, text='+', command=plus, font=('arial', 14))
bminus = tk.Button(frame, text='-', command=minus, font=('arial', 14))
btimes = tk.Button(frame, text='x', command=times, font=('arial', 14))
bdiv = tk.Button(frame, text='/', command=div, font=('arial', 14))
beq = tk.Button(frame, text='=', command=eq, font=('arial', 14))

b0.grid(row=4, column=0)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
bplus.grid(row=1, column=3)
bminus.grid(row=2, column=3)
btimes.grid(row=3, column=3)
bdiv.grid(row=4, column=3)
beq.grid(row=5, column=3)

e = tk.Entry(frame)
e.grid(row=0, column=0, columnspan=4)


root.mainloop()