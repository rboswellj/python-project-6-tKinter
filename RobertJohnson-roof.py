 # Robert Johnson
 # CIT 144
 # Project 6

from tkinter import *


class RoofCalc(Frame):
    def __init__(self):
        Frame.__init__(self)

        # GUI vars
        self.master.title("Roof Cost Calculator")
        self.grid()
        self.xPad = 2
        self.yPad = 2
        self.entWidth = 16
        
        # Calc Vars
        self.cost = 0
        self.area = DoubleVar()
        self.coefficient = DoubleVar()
        self.twentyCost = 3.25
        self.thirtyCost = 3.75
        self.scrapAllowance = 1.1

        # Field Vars
        self.strLength = StringVar()
        self.strWidth = StringVar()
        self.strRise = StringVar()
        self.eave = BooleanVar()
        self.strShingleType = StringVar()
        self.strTotal = StringVar()


        self.f1 = Frame(self, height=768, width=1024)  # left frame -----
        self.f1.grid(row=0, column=0, padx=20, pady=20)

        # Length field
        Label(self.f1, text="Length(feet)").grid(row=0, column=0, padx=self.xPad, pady=0, sticky=W)
        self.txtLength = Entry(self.f1, width=self.entWidth, textvariable=self.strLength)
        self.txtLength.grid(row=1, column=0, padx=self.xPad, pady=self.yPad, sticky=W)

        # Width field
        Label(self.f1, text="Width(feet)").grid(row=2, column=0, padx=self.xPad, pady=0, sticky=W)
        self.txtWidth = Entry(self.f1, width=self.entWidth, textvariable=self.strWidth)
        self.txtWidth.grid(row=3, column=0, padx=self.xPad, pady=self.yPad, sticky=W)

        # Rise Field
        Label(self.f1, text="Rise(1-10)").grid(row=4, column=0, padx=self.xPad, pady=0, sticky=W)
        self.txtRise = Entry(self.f1, width=self.entWidth, textvariable=self.strRise)
        self.txtRise.grid(row=5, column=0, padx=self.xPad, pady=self.yPad, sticky=W)

        # Eave Check
        Label(self.f1, text="Add 2 feet for Eaves?").grid(row=0, column=1, padx=20, pady=0, sticky=W)
        self.chkEave = Checkbutton(self.f1, variable=self.eave)
        self.chkEave.grid(row=1, column=1, padx=20, pady=self.yPad, sticky=W)

        # Shingle Type
        Label(self.f1, text="Shingle Type").grid(row=2, column=1, padx=20, sticky=W)
        self.strShingleType.set(None)
        Radiobutton(self.f1, text="20 Year", variable=self.strShingleType, value=20) \
            .grid(row=3, column=1, padx=20, sticky=W)
        Radiobutton(self.f1, text="30 Year", variable=self.strShingleType, value=30) \
            .grid(row=4, column=1, padx=20, sticky=W)

        # Calculate Button
        self.btnCalc = Button(self.f1, text="Calculate Total", command=self.calculate_cost)
        self.btnCalc.grid(row=6, column=0, padx=0, pady=20, ipadx=2, ipady=2, sticky=W)

        # Clear Button
        self.btnCalc = Button(self.f1, text="Clear Form", command=self.clear_form)
        self.btnCalc.grid(row=6, column=1, padx=0, pady=20, ipadx=2, ipady=2, sticky=W)

        # Total field
        Label(self.f1, text="Estimated Total").grid(row=7, column=0, padx=self.xPad, pady=0, sticky=W)
        self.txtTotal = Entry(self.f1, width=self.entWidth, textvariable=self.strTotal)
        self.txtTotal.grid(row=8, column=0, padx=self.xPad, pady=self.yPad, sticky=W)

        # Status Label
        self.status = StringVar()
        self.lblStatus = Label(self.f1, textvariable=self.status).grid(row=9, column=0, padx=self.xPad, pady=0, sticky=W)

    def get_coefficient(self):
        # Gets the coefficient based on rise
        rise = int(self.strRise.get())
        if rise == 1:
            return 1.003
        elif rise == 2:
            return 1.014
        elif rise == 3:
            return 1.031
        elif rise == 4:
            return 1.054
        elif rise == 5:
            return 1.082
        elif rise == 6:
            return 1.118
        elif rise == 7:
            return 1.158
        elif rise == 8:
            return 1.202
        elif rise == 9:
            return 1.250
        elif rise == 10:
            return 1.302
        else:
            # Signals that the rise entry was invalid
            return -1


    def calculate_cost(self):
        # Make sure no required fields are blank
        if not self.strLength.get() or not self.strWidth.get() or not self.strRise.get() or not self.strShingleType.get():
            self.status.set("Blank entries. Enter values")
        else:
            # Try and parse strings to integers, prompt if entry invalid
            try:
                length, width = int(self.strLength.get()), int(self.strWidth.get())
                coefficient = self.get_coefficient()
                self.status.set("")
            except:
                self.status.set("Invalid Entries. Check Values")
            else:
                # Make sure rise entry returning a valid coefficient
                if coefficient != -1:
                    # Clear any error messages when entries all valid
                    self.status.set("")

                    # Check if "add eaves" box is checked. Get area of roof
                    if self.eave.get():
                        self.area = length * (width + 2) * coefficient * self.scrapAllowance
                    else:
                        self.area = length * width * coefficient * self.scrapAllowance

                    # Set shingle cost based on type, error if not selected
                    if self.strShingleType.get() == "20":
                        self.cost = self.area * self.twentyCost
                        self.strTotal.set(str(f"${round(float(self.cost), 2)}"))
                    elif self.strShingleType.get() == "30":
                        self.cost = self.area * self.thirtyCost
                        self.strTotal.set(str(f"${round(float(self.cost), 2)}"))
                    else:
                        self.status.set("Please select shingle type")   
                else:
                    self.status.set("Invalid Rise. Check Value")

    def clear_form(self):
        self.strLength.set("")
        self.strWidth.set("")
        self.strRise.set("")
        self.eave.set(False)
        self.strShingleType.set(None)
        self.strTotal.set("")


def main():
    RoofCalc().mainloop()


main()
