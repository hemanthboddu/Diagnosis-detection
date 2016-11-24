import Tkinter as tk

from Tkinter import *
import tkMessageBox


class AppUi(tk.Tk):
    def __init__(self):

        self.Training_data1 = []
        self.Training_data2 = []
        self.Patients_dataEntry = []

        # Labels

        tk.Tk.__init__(self)
        self.Training_data1_label = tk.Label(self, text="Training data1", relief=RAISED)
        self.Training_data2_label = tk.Label(self, text="Training data2", relief=RAISED)
        self.Training_data1_X1 = tk.Label(self, text="X1", relief=RAISED)
        self.Training_data1_X2 = tk.Label(self, text="X2", relief=RAISED)
        self.Training_data2_X1 = tk.Label(self, text="X1", relief=RAISED)
        self.Training_data2_X2 = tk.Label(self, text="X2", relief=RAISED)
        self.Patients_data = tk.Label(self, text="Patients data", relief=RAISED)
        self.Patients_data_X1 = tk.Label(self, text="X1", relief=RAISED)
        self.Patients_data_X2 = tk.Label(self, text="X2", relief=RAISED)

        # TextBoxes

        self.Training_data1_entry1 = tk.Entry(self)
        self.Training_data1_entry2 = tk.Entry(self)
        self.Training_data2_entry1 = tk.Entry(self)
        self.Training_data2_entry2 = tk.Entry(self)
        self.Patients_data_entry1 = tk.Entry(self)
        self.Patients_data_entry2 = tk.Entry(self)

        # Buttons

        self.Find = tk.Button(self, text="Find", command=self.on_button)
        self.Clear = tk.Button(self, text="Clear", command=self.on_button_clear)
        self.Training_data1_button = tk.Button(self, text="Add", command=self.on_button_td1)
        self.Training_data2_button = tk.Button(self, text="Add", command=self.on_button_td2)
        self.Training_data1_ClearAll = tk.Button(self, text="Clear All", command=self.on_button_td1_clearAll)
        self.Training_data2_ClearAll = tk.Button(self, text="Clear All", command=self.on_button_td2_clearAll)
        self.Training_data1_ClearImm = tk.Button(self, text="Clear Immediate", command=self.on_button_td1_clearImm)
        self.Training_data2_ClearImm = tk.Button(self, text="Clear Immediate", command=self.on_button_td2_clearImm)

        # packing

        self.Training_data1_label.pack()
        self.Training_data2_label.pack()
        self.Training_data1_X1.pack()
        self.Training_data1_X2.pack()
        self.Training_data2_X1.pack()
        self.Training_data2_X2.pack()
        self.Patients_data.pack()
        self.Patients_data_X1.pack()
        self.Patients_data_X2.pack()

        self.Training_data1_entry1.pack()
        self.Training_data1_entry2.pack()
        self.Training_data2_entry1.pack()
        self.Training_data2_entry2.pack()
        self.Patients_data_entry1.pack()
        self.Patients_data_entry2.pack()

        self.Find.pack()
        self.Training_data1_button.pack()
        self.Training_data2_button.pack()
        self.Training_data1_ClearAll.pack()
        self.Training_data2_ClearAll.pack()
        self.Training_data1_ClearImm.pack()
        self.Training_data2_ClearImm.pack()

        # placing

        self.Training_data1_label.place(relx=0.05, rely=0.1875)
        self.Training_data2_label.place(relx=0.55, rely=0.1875)
        self.Training_data1_X1.place(relx=0.15, rely=0.125)
        self.Training_data1_X2.place(relx=0.3, rely=0.125)
        self.Training_data2_X1.place(relx=0.7, rely=0.125)
        self.Training_data2_X2.place(relx=0.8, rely=0.125)
        self.Patients_data.place(relx=0.05, rely=0.9375)
        self.Patients_data_X1.place(relx=0.3, rely=0.97)
        self.Patients_data_X2.place(relx=0.7, rely=0.97)

        self.Training_data1_entry1.place(relx=0.15, rely=0.1875)
        self.Training_data1_entry2.place(relx=0.3, rely=0.1875)
        self.Training_data2_entry1.place(relx=0.7, rely=0.1875)
        self.Training_data2_entry2.place(relx=0.8, rely=0.1875)
        self.Patients_data_entry1.place(relx=0.2, rely=0.9375)
        self.Patients_data_entry2.place(relx=0.5, rely=0.9375)

        self.Find.place(relx=0.7, rely=0.9375)
        self.Training_data1_button.place(relx=0.05, rely=0.875)
        self.Training_data2_button.place(relx=0.55, rely=0.875)
        self.Training_data1_ClearAll.place(relx=0.15, rely=0.875)
        self.Training_data2_ClearAll.place(relx=0.68, rely=0.875)
        self.Training_data1_ClearImm.place(relx=0.3, rely=0.875)
        self.Training_data2_ClearImm.place(relx=0.8, rely=0.875)

    def on_button(self):
        pd_entry1 = float(self.Patients_data_entry1.get())
        pd_entry2 = float(self.Patients_data_entry2.get())
        self.Patients_dataEntry.append(pd_entry1)
        self.Patients_dataEntry.append(pd_entry2)
        if len(self.Patients_dataEntry) == 2:
            pass
        else:
            pass

    def on_button_clear(self):
        del self.Patients_dataEntry[:]

    def on_button_td1(self):
        Training_data1_sample = []
        td1_entry1 = float(self.Training_data1_entry1.get())
        td1_entry2 = float(self.Training_data1_entry2.get())
        Training_data1_sample.append(td1_entry1)
        Training_data1_sample.append(td1_entry2)
        if len(Training_data1_sample) == 2:
            self.Training_data1.append(Training_data1_sample)
        else:
            pass
        pass

    def on_button_td2(self):
        Training_data2_sample = []
        td2_entry1 = float(self.Training_data2_entry1.get())
        td2_entry2 = float(self.Training_data2_entry2.get())
        Training_data2_sample.append(td2_entry1)
        Training_data2_sample.append(td2_entry2)
        if len(Training_data2_sample) == 2:
            self.Training_data2.append(Training_data2_sample)
        else:
            pass

        pass

    def on_button_td1_clearAll(self):
        del self.Training_data1[:]
        pass

    def on_button_td2_clearAll(self):
        del self.Training_data2[:]
        pass

    def on_button_td1_clearImm(self):
        self.Training_data1.pop()
        pass

    def on_button_td2_clearImm(self):
        self.Training_data2.pop()
        pass

    @staticmethod
    def Enter_Valid_value():
        tkMessageBox.showinfo("Warning", "Enter Valid Data")
        pass


app = AppUi()
app.mainloop()
