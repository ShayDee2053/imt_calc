import tkinter
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk


class Calculator(ctk.CTk):

    def __init__(self):

        super().__init__()

        ctk.set_appearance_mode("dark")
        self.title("BMI calculator")
        self.geometry("300x200+650+350")
        self.resizable(width=False, height=False)

        height = ctk.CTkLabel(
            self,
            text="Enter height: ",
            text_color="yellow",
            font=(
                "Times New Roman",
                14,
                "bold"
            )
        )

        height.grid(column=0, row=0)

        mass = ctk.CTkLabel(
            self,
            text="Enter mass: ",
            text_color="yellow",
            font=(
                "Times New Roman",
                14,
                "bold"
            )
        )

        mass.grid(column=0, row=1)

        tbl_h = ctk.CTkEntry(
            self,
            border_width=1,
            border_color="yellow",
            width=100
        )
        tbl_h.grid(column=1, row=0, pady=10)

        tbl_m = ctk.CTkEntry(
            self,
            border_width=1,
            border_color="yellow",
            width=100)
        tbl_m.grid(column=1, row=1, pady=10)

        btn = ctk.CTkButton(
            self,
            text="Calculate",
            text_color="yellow",
            border_width=1,
            border_color="yellow",
            command=lambda: self.calculate_imt(
                int(tbl_h.get()) / 100,
                float(tbl_m.get()))
        )

        btn.grid(column=1, row=2, pady=10)

    @staticmethod
    def calculate_imt(h, m):

        try:
            h

        except ValueError:
            messagebox.showerror(
                title="Error",
                message="Received a string, but excepted a number"
            )

        else:

            try:
                m

            except ValueError:
                messagebox.showerror(
                    title="Error",
                    message="Received a string, but excepted a number"
                )

            else:

                imt = m / (h**2)
                imt = round(imt, 2)

                if (h <= 0) or (m <= 0):
                    messagebox.showerror(
                        title="Result",
                        message="Value is less than zero"
                    )

                elif imt <= 16:
                    messagebox.showinfo(
                        title="Result",
                        message=f"BMI = {imt}. Pronounced lack of body weight"
                    )

                elif (imt > 16) and (imt <= 18.5):
                    messagebox.showinfo(
                        title="Result",
                        message=f"BMI = {imt}. Body weight deficit"
                    )

                elif (imt > 18.5) and (imt <= 25):
                    messagebox.showinfo(
                        title="Result",
                        message=f"BMI = {imt}. Normal weight"
                    )

                elif (imt > 25) and (imt <= 30):
                    messagebox.showinfo(
                        title="Result",
                        message=f"BMI = {imt}. Overweight"
                    )

                elif (imt > 30) and (imt <= 35):
                    messagebox.showinfo(
                        title="Result",
                        message=f"BMI = {imt}. Obesity of the first degree"
                    )

                elif (imt > 35) and (imt <= 42):
                    messagebox.showinfo(
                        title="Result",
                        message=f"BMI = {imt}. Obesity of the second degree"
                    )

                else:
                    messagebox.showinfo(
                        title="Result",
                        message=f"BMI = {imt}. Obesity of the third degree"
                    )


if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
