from tkinter import *
import math

window = Tk()
# create buttons
# number buttons

inp = []
n = 0
clear = 0
dec_point = 0

entry = Entry(window, font=("Railway", 30), width=100, fg="white", bg="#212120", bd=0)
entry.place(x=5, y=50)


def num_button_click(num):
    global n, clear, dec_point
    if len(entry.get()) >= 23:
        return
    if clear == 1:
        inp.clear()
        n = 0
        clear = 0
    try:
        if inp[n] == 0:
            pass
    except IndexError:
        inp.append(0)
    if type(inp[n]) not in [int, float]:
        n += 1
    if type(inp[n]) == int and inp[n] != 0:
        if math.log10(inp[n]) >= 16:
            return
    entry.config(font="Railway, 30")
    if dec_point > 0 and dec_point < 10 ** 12:
        inp[n] = inp[n] + num / dec_point
        print(num/dec_point)
        dec_point *= 10
    elif dec_point >= 10 ** 12:
        return
    else:
        inp[n] = inp[n] * 10 + num
    if len(entry.get()) > 10:
        entry.config(font=("Railway", 16))
    entry.delete(0, END)
    for i in inp:
        entry.insert(len(entry.get()), i)


def operator_button_click(operator):
    global n, clear, dec_point
    try:
        if type(inp[n - 1]) not in [int, float] and type(inp[n]) not in [int, float]:
            return
    except IndexError:
            return

    clear = dec_point = 0
    inp.append(" " + operator + " ")
    n += 2
    entry.delete(0, END)
    for i in inp:
        entry.insert(len(entry.get()), i)


def clear_entry():
    global n
    if type(inp[n]) in [int, float]:
        entry.delete(len(entry.get()) - len(str(inp[n])), END)
        inp[n] = 0
        if n != 0:
            n -= 1


def clear_all():
    global n, clear
    clear = 0
    inp.clear()
    n = 0
    entry.delete(0, END)


def button_equal_click():
    global n, clear
    i = 0
    for i in range(len(inp) - 1):
        if inp[i + 1] == " + ":
            inp[i + 2] = inp[i] + inp[i + 2]
        if inp[i + 1] == " - ":
            inp[i + 2] = inp[i] - inp[i + 2]
        if inp[i + 1] == " * ":
            inp[i + 2] = inp[i] * inp[i + 2]
        if inp[i + 1] == " / ":
            inp[i + 2] = inp[i] / inp[i + 2]
        if inp[i + 1] == " % ":
            inp[i + 2] = inp[i] % inp[i + 2]
        i += 2
    result = inp[i - 1]
    if type(result) == float:
        result = round(result, 5)
    inp.clear()
    n = 0
    inp.append(result)
    entry.delete(0, END)
    entry.insert(0, result)
    clear = 1


def dec_point_button_click():
    global dec_point
    dec_point = 10
    entry.insert(len(entry.get()), ".")


def negation_click():
    inp[n] = -inp[n]
    entry.delete(len(entry.get()) - len(str(inp[n])), END)
    entry.insert(END, str(inp[n]))


def one_over_x_button_click():
    inp[n] = 1 / inp[n]
    entry.delete(len(entry.get()) - len(str(inp[n])), END)
    entry.insert(END, str(inp[n]))


def squared_x_button_click():
    inp[n] = inp[n] * inp[n]
    entry.delete(len(entry.get()) - len(str(inp[n])), END)
    entry.insert(END, str(inp[n]))


def root_x_button_click():
    inp[n] = math.sqrt(inp[n])
    entry.delete(len(entry.get()) - len(str(inp[n])), END)
    entry.insert(END, str(inp[n]))


def log_10_x_click():
    inp[n] = math.log10(inp[n])
    entry.delete(len(entry.get()) - len(str(inp[n])), END)
    entry.insert(END, str(inp[n]))


button_1 = Button(
    window,
    text="1",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: num_button_click(1),
)
button_1.place(x=5, y=380)

button_2 = Button(
    window,
    text="2",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: num_button_click(2),
)
button_2.place(x=80, y=380)

button_3 = Button(
    window,
    text="3",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: num_button_click(3),
)
button_3.place(x=155, y=380)

button_4 = Button(
    window,
    text="4",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: num_button_click(4),
)
button_4.place(x=5, y=325)

button_5 = Button(
    window,
    text="5",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: num_button_click(5),
)
button_5.place(x=80, y=325)

button_6 = Button(
    window,
    text="6",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: num_button_click(6),
)
button_6.place(x=155, y=325)

button_7 = Button(
    window,
    text="7",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: num_button_click(7),
)
button_7.place(x=5, y=270)

button_8 = Button(
    window,
    text="8",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: num_button_click(8),
)
button_8.place(x=80, y=270)

button_9 = Button(
    window,
    text="9",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: num_button_click(9),
)
button_9.place(x=155, y=270)

button_0 = Button(
    window,
    text="0",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: num_button_click(0),
)
button_0.place(x=80, y=435)


button_clear_all = Button(
    window,
    text="C",
    padx=20.5,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=clear_all,
)

button_clear_all.place(x=155, y=215)

button_clear_entry = Button(
    window,
    text="CE",
    padx=14,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=clear_entry,
)

button_clear_entry.place(x=80, y=215)

# button decimal point
button_dec_point = Button(
    window,
    text=".",
    padx=25,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=dec_point_button_click,
)
button_dec_point.place(x=155, y=435)

# button negation
button_negation = Button(
    window,
    text="+/-",
    padx=16,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=negation_click,
)
button_negation.place(x=5, y=435)


# 1/x

button_one_over_x = Button(
    window,
    text="1/x",
    padx=15,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=one_over_x_button_click,
)
button_one_over_x.place(x=5, y=215)


# x to the power of 2
button_x_squared = Button(
    window,
    text="x^2",
    padx=14,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=squared_x_button_click,
)
button_x_squared.place(x=5, y=160)


# squared root of x
button_one_over_x = Button(
    window,
    text="1/x",
    padx=15,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=one_over_x_button_click,
)
button_one_over_x.place(x=5, y=215)

#
button_root_x = Button(
    window,
    text="√x",
    padx=18,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=root_x_button_click,
)
button_root_x.place(x=80, y=160)

# log10 x
button_log10_x = Button(
    window,
    text="log x",
    padx=8,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=log_10_x_click,
)
button_log10_x.place(x=155, y=160)


# operator button
button_add = Button(
    window,
    text="+",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: operator_button_click("+"),
)
button_add.place(x=230, y=380)


button_sub = Button(
    window,
    text="-",
    padx=25,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: operator_button_click("-"),
)

button_sub.place(x=230, y=325)

button_mul = Button(
    window,
    text="*",
    padx=24.49,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: operator_button_click("*"),
)
button_mul.place(x=230, y=270)

button_div = Button(
    window,
    text="/",
    padx=25,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: operator_button_click("/"),
)
button_div.place(x=230, y=215)

button_mod = Button(
    window,
    text="%",
    padx=19,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=lambda: operator_button_click("%"),
)
button_mod.place(x=230, y=160)


button_equal = Button(
    window,
    text="=",
    padx=22,
    pady=7,
    font=("Railway", 14),
    fg="white",
    bg="#424240",
    activeforeground="white",
    activebackground="#424240",
    command=button_equal_click,
)
button_equal.place(x=230, y=435)


def window_setup():
    window.minsize(303, 490)
    window.maxsize(303, 490)
    window.title("Calculator")
    window.configure(bg="#212120")
    # icon = PhotoImage(file="C:\\Users\\Thuan\\Documents\\Code\\Python\\Project\\Calculator Project\\Calculator\\image\\calculator.png")
    # window.iconphoto(True, icon)


def main():
    window_setup()
    window.mainloop()


if __name__ == "__main__":
    main()
