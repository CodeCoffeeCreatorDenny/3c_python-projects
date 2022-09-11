from tkinter import *
from playsound import playsound
import time

root = Tk()
root.title("Countdown")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False, False)

heading = Label(root, text="Timer", font="arial 30 bold", bg="#000", fg="#ea3548")
heading.pack(pady=10)

# clock
Label(root, font="arial 15 bold", text="Current Time:   ", bg="papaya whip").place(x=55, y=70)


def clock():
    clock_time = time.strftime("   %H:%M:%S %p")
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = Label(root, font="arial 15 bold", text="", fg="#000", bg="#fff")
current_time.place(x=210, y=70)
clock()

# timer
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=30, y=155)
hrs.set("00")

mins = StringVar()
Entry(root, textvariable=mins, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=150, y=155)
mins.set("00")

sec = StringVar()
Entry(root, textvariable=sec, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=270, y=155)
sec.set("00")

Label(root, text="hours", font="arial 12", bg="#000", fg="#fff").place(x=105, y=200)
Label(root, text="mins", font="arial 12", bg="#000", fg="#fff").place(x=225, y=200)
Label(root, text="secs", font="arial 12", bg="#000", fg="#fff").place(x=345, y=200)


def Timer():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())

    while times > -1:
        minute, second = (times // 60, times % 60)
        hour = 0

        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if times == 0:
            playsound("bell.mp3")
            sec.set("00")
            mins.set("00")
            hrs.set("00")

        times -= 1


def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")


def face():
    hrs.set("00")
    mins.set("15")
    sec.set("00")


def eggs():
    hrs.set("00")
    mins.set("10")
    sec.set("00")


button = Button(
    root, text="Start", bg="#ea3548", bd=0, fg="#fff", width=20, height=2, font="arial 10 bold", command=Timer
)
button.pack(padx=5, pady=40, side=BOTTOM)

Image1 = PhotoImage(file="brush.png")
button1 = Button(root, image=Image1, bg="#000", bd=0, command=brush)
button1.place(x=7, y=300)

Image2 = PhotoImage(file="face.png")
button2 = Button(root, image=Image2, bg="#000", bd=0, command=face)
button2.place(x=137, y=300)

Image3 = PhotoImage(file="eggs.png")
button3 = Button(root, image=Image3, bg="#000", bd=0, command=eggs)
button3.place(x=267, y=300)

root.mainloop()
