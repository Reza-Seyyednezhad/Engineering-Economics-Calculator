import pyexcel as p
from tkinter import messagebox
from tkinter import *

root = Tk()



def Show():
    ccs_insight2 = p.Sheet()
    ccs_insight2.name = "Worldwide Mobile Phone Shipments (Billions), 2017-2021"
    ccs_insight2.ndjson = """
    ... {"year": ["2017", "2018", "2019", "2020", "2021"]}
    ... {"smart phones": [1.53, 1.64, 1.74, 1.82, 1.90]}
    ... {"feature phones": [0.46, 0.38, 0.30, 0.23, 0.17]}
    ... """.strip()
    messagebox.showinfo("Title", ccs_insight2)

btn = Button(root, text="Hello World, please choose your location.", command=Show).pack()

root.mainloop()