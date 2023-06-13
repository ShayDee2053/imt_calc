import tkinter
from tkinter import messagebox


def calculate_imt():

    try:
        h = int(tbl_h.get()) / 100

    except ValueError:
        messagebox.showerror(title="Error",
                             message="Received a string, but excepted a number")

    else:

        try:
            m = float(tbl_m.get())

        except ValueError:
            messagebox.showerror(title="Error",
                                 message="Received a string, but excepted a number")

        else:

            imt = m / (h**2)
            imt = round(imt, 2)

            if imt <= 16:
                messagebox.showinfo(title="Result",
                                    message=f"BMI = {imt}. Pronounced lack of body weight")

            elif (imt > 16) and (imt <= 18.5):
                messagebox.showinfo(title="Result",
                                    message=f"BMI = {imt}. Body weight deficit")

            elif (imt > 18.5) and (imt <= 25):
                messagebox.showinfo(title="Result",
                                    message=f"BMI = {imt}. Normal weight")

            elif (imt > 25) and (imt <= 30):
                messagebox.showinfo(title="Result",
                                    message=f"BMI = {imt}. Overweight")

            elif (imt > 30) and (imt <= 35):
                messagebox.showinfo(title="Result",
                                    message=f"BMI = {imt}. Obesity of the first degree")

            elif (imt > 35) and (imt <= 42):
                messagebox.showinfo(title="Result",
                                    message=f"BMI = {imt}. Obesity of the second degree")

            else:
                messagebox.showinfo(title="Result",
                                    message=f"BMI = {imt}. Obesity of the third degree")


app = tkinter.Tk()
app.title("BMI calculator")
app.geometry("300x200")
app.resizable(width=False, height=False)

height = tkinter.Label(app, text="Enter height", font=14)
height.grid(column=0, row=0)

mass = tkinter.Label(app, text="Enter mass", font=14)
mass.grid(column=0, row=1)

tbl_h = tkinter.Entry(app, width=10)
tbl_h.grid(column=1, row=0)

tbl_m = tkinter.Entry(app, width=10)
tbl_m.grid(column=1, row=1)

btn = tkinter.Button(app, text="Calculate",
                     command=calculate_imt)
btn.grid(column=1, row=2)


app.mainloop()
