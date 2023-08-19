import tkinter as tk

def Fahrenheit_to_Celsius():
    try:
        fahrenheit = float(ent_temperature.get())
        celsius = (fahrenheit - 32) * 5/9 # formula to convert
        lbl_result.config(text=f"{round(celsius, 2)}\N{DEGREE CELSIUS}")
    except ValueError:
        lbl_result.config(text="The input is invalid")

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=Fahrenheit_to_Celsius)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=30)
btn_convert.grid(row=0, column=1, pady=20)
lbl_result.grid(row=0, column=2, padx=20)

window.mainloop()
