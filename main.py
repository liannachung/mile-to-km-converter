from tkinter import *
window = Tk()
window.minsize(width=300, height=200)
window.config(padx= 20, pady=70)

input = Entry()
input.grid(column=2, row=1)

miles_label = Label(text="Miles", font=("Arial", 20, "normal"))
miles_label.grid(column=3, row=1)

is_equal_label = Label(text="is equal to", font=("Arial", 20, "normal"))
is_equal_label.grid(column=1, row=2)

conversion = Label(text="0", font=("Arial", 20, "normal"))
conversion.grid(column=2, row=2)

km_label = Label(text="Km", font=("Arial", 20, "normal"))
km_label.grid(column=3, row=2)

def button_clicked():
    miles = input.get()
    km = int(miles) * 1.609
    conversion["text"] = km

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)





window.mainloop()