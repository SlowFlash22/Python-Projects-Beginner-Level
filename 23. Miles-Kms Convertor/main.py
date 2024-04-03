from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=400, height=100)
window.config(padx=100, pady=50)


def convert():
    kilometers = (float(miles_input.get())) * 1.60934
    converted_label.config(text = f"{round(kilometers, 4)}")


miles_display = Label(text="Mile(s): ", font=("Calibri", 18, "bold"))
miles_display.grid(row=0, column=0)

miles_unit = Label(text="Miles ", font=("Calibri", 18, "italic"))
miles_unit.grid(row=0, column=3)

kilometer_display = Label(text="Kilometer(s):", font=("Calibri", 18, "bold") )
kilometer_display.grid(row=1, column=0)

kilometer_unit = Label(text="Km ", font=("Calibri", 18, "italic"))
kilometer_unit.grid(row=1, column=3)

converted_label = Label(text="0")
converted_label.grid(row=1,column=2)

miles_input = Entry(width=15)
miles_input.focus()
miles_input.grid(row=0, column=2)

convert_button = Button(text="Calculate", command=convert)
convert_button.grid(row=2, column=4)
window.mainloop()