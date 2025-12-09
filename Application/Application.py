from tkinter import *
from tkinter import ttk
from formulas import P_A, P_F, A_F, A_P, F_A, F_P, P_G, A_G, i_P_F, n_F_P
import os
from tkinter import messagebox
import math
root = Tk()

root.geometry("800x700")
root.title("Reza Seyyednezhad")
root.resizable(False, False)
bgColor = "#272928"
bgColor2 = "#323740"
root.config(background=bgColor)

myStyle = ttk.Style()
myStyle.configure('My.TFrame', background=bgColor)

newStyle = ttk.Style()
newStyle.configure("Custom.TFrame",
                         background=bgColor2,
                         font="Verdana 12")
LabelStyle = ttk.Style()
LabelStyle.configure("My.TLabel", background=bgColor2, foreground="#fcba03", font="Verdana 12")

EntryStyle = ttk.Style()
EntryStyle.configure("My.TEntry",width=100, height=50, background=bgColor2, foreground="#fcba03", font="Verdana 12", borderwidth=2, bordercolor="#fcba03")

BtnStyle = ttk.Style()
BtnStyle.configure("Custom.TButton", background=bgColor2, font="Verdana 12", foreground="#fcba03")

notebook = ttk.Notebook(root, style="My.TFrame")

notebook.pack(expand=True)
# create frames
frame1 = ttk.Frame(notebook, width=900, height=700, style='My.TFrame')
frame2 = ttk.Frame(notebook, width=900, height=700, style='My.TFrame')
frame3 = ttk.Frame(notebook, width=900, height=700, style='My.TFrame')
frame4 = ttk.Frame(notebook, width=900, height=700, style='My.TFrame')

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='Basic Calculation')
notebook.add(frame2, text='Present Worth Method')
notebook.add(frame3, text='Annual Worth Method')
notebook.add(frame4, text='Payback Period Method')

# -------------------------- Basic Section -------------------------
method = StringVar()
IVar = DoubleVar()
NVar = DoubleVar()
A_P_F_Amount_Var = DoubleVar()
F_Target = DoubleVar()
MethodFrame = ttk.Frame(frame1, width=900, style="Custom.TFrame", padding=5)
MethodFrame.pack(side=TOP, fill="x", pady=5)

MethodType = LabelFrame(MethodFrame, text="Choose Method", fg="#fcba03", font="Verdana 15", bg=bgColor2, labelanchor='n')
MethodType.pack(fill="both", expand="yes")

c_PF = Radiobutton(MethodType, text="P/F", variable=method, value="P/F", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT,pady=20, padx=5)

c_FP = Radiobutton(MethodType, text="F/P", variable=method, value="F/P", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT,pady=20, padx=5)

c_AF = Radiobutton(MethodType, text="A/F", variable=method, value="A/F", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT,pady=20, padx=5)

c_FA = Radiobutton(MethodType, text="F/A", variable=method, value="F/A", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT,pady=20, padx=5)

c_PA = Radiobutton(MethodType, text="P/A", variable=method, value="P/A", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT,pady=20, padx=5)

c_AP = Radiobutton(MethodType, text="A/P", variable=method, value="A/P", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT,pady=20, padx=5)

c_PG = Radiobutton(MethodType, text="P/G", variable=method, value="P/G", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT,pady=20, padx=5)

c_AG = Radiobutton(MethodType, text="A/G", variable=method, value="A/G", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT,pady=20, padx=5)

def getValue():
    os.system('cls')
    print(method.get())

# b1 = Button(frame1, text="Click", command=getValue)
# b1.grid(row=1, column=0)
InputFrame = ttk.Frame(frame1, width=900, style="Custom.TFrame", padding=5)
InputFrame.pack(side=TOP, fill="x", pady=10)

InputsLabel = LabelFrame(InputFrame, text="Enter i%, n",  fg="#fcba03", font="Verdana 15", bg=bgColor2, labelanchor='n')
InputsLabel.pack(fill="both", expand="yes")

iLabel = ttk.Label(InputsLabel, text="i%: ", style="My.TLabel", font="Verdana 15")
iLabel.pack(side=LEFT)


iInput = Entry(InputsLabel, textvariable=IVar, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2)
iInput.pack(side=LEFT, pady=10, padx=5)

nLabel = ttk.Label(InputsLabel, text="n: ", style="My.TLabel", font="Verdana 15")
nLabel.pack(side=LEFT)


nInput = Entry(InputsLabel, textvariable=NVar, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2)
nInput.pack(side=LEFT, pady=10, padx=5)

factor_result = StringVar()
Factor = ""
def FactorResult():
    methodValue = method.get()
    if methodValue == "P/F":
        factor_result = f"Result is: {P_F(IVar.get(), NVar.get())[0]}"
        messagebox.showinfo("Result:", factor_result)

    elif methodValue == "A/F":
        factor_result = f"Result is: {A_F(IVar.get(), NVar.get())[0]}"
        messagebox.showinfo("Result:", factor_result)

    elif methodValue == "F/P":
        factor_result = f"Result is: {F_P(IVar.get(), NVar.get())[0]}"
        messagebox.showinfo("Result:", factor_result)

    elif methodValue == "A/P":
        factor_result = f"Result is: {A_P(IVar.get(), NVar.get())[0]}"
        messagebox.showinfo("Result:", factor_result)

    elif methodValue == "F/A":
        factor_result = f"Result is: {F_A(IVar.get(), NVar.get())[0]}"
        messagebox.showinfo("Result:", factor_result)
    elif methodValue == "P/A":
        factor_result = f"Result is: {P_A(IVar.get(), NVar.get())[0]}"
        messagebox.showinfo("Result:", factor_result)
    elif methodValue == "P/G":
        factor_result = f"Result is: {P_G(IVar.get(), NVar.get())[0]}"
        messagebox.showinfo("Result:", factor_result)
    elif methodValue == "A/G":
        factor_result = f"Result is: {A_G(IVar.get(), NVar.get())[0]}"
        messagebox.showinfo("Result:", factor_result)
    else:
        messagebox.showerror("Invalid Error","Choose Method Type!")
    

i_n_SubmitBtn = Button(InputsLabel, text="Calculate Factor", command=FactorResult, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=2)
# Split = Label(InputsLabel, text="|", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, pady=10)

# ---------------------------------------------------------------------

Serval_Time_Periods = ttk.Frame(frame1, width=900, style="Custom.TFrame", padding=5)
Serval_Time_Periods.pack(side=TOP, fill="x", pady=10)

Serval_Time_Periods_Inputs_Label_Frame = LabelFrame(Serval_Time_Periods, text="Serval Time Periods",  fg="#fcba03", font="Verdana 15", bg=bgColor2, labelanchor='n')
Serval_Time_Periods_Inputs_Label_Frame.pack(fill="both", expand="yes", side=TOP)

# Serval_Time_Periods_Inputs_Label_RadioFrame = ttk.Frame(Serval_Time_Periods_Inputs_Label_Frame, width=500, style="Custom.TFrame").pack(side=TOP, fill="x", pady=20)

# methodValue = method.get()

# if methodValue == "P/F" or methodValue == "A/F":
#     UserMethodChoosed = "F"
# elif methodValue == "F/P" or methodValue == "A/P":
#     UserMethodChoosed = "P"
# elif methodValue == "F/A" or methodValue == "P/A":
#     UserMethodChoosed = "A"

A_P_F_Amount_Label = Label(Serval_Time_Periods_Inputs_Label_Frame, text="A|F|P:", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=10)
A_P_F_Amount = Entry(Serval_Time_Periods_Inputs_Label_Frame, textvariable=A_P_F_Amount_Var, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2)
A_P_F_Amount.pack(side=LEFT, padx=10, pady=10)

myList = []
def Add():
    item = (method.get(), IVar.get(), NVar.get(), A_P_F_Amount_Var.get())
    if item[0] != "" and isinstance(item[0], str):
        myList.append(item)
    else:
        messagebox.showerror('method can not Empty!')


def ListCheck():
    result = 0
    print(myList)
    for i in myList:
        if i[0] == "F/A":
            result += F_A(i[1], i[2], i[3])[1]
        elif i[0] == "F/P":
            result += F_P(i[1], i[2], i[3])[1]
        elif i[0] == "P/F":
            result += P_F(i[1], i[2], i[3])[1]
        elif i[0] == "P/A":
            result += P_A(i[1], i[2], i[3])[1]
        elif i[0] == "A/P":
            result += A_P(i[1], i[2], i[3])[1]
        elif i[0] == "A/F":
            result += A_F(i[1], i[2], i[3])[1]
        elif i[0] == "P/G":
            result += P_G(i[1], i[2], i[3])[1]
        elif i[0] == "A/G":
            result += A_G(i[1], i[2], i[3])[1]
        else:
            messagebox.showerror('Some thing went wrong')
    MyResult = f"User Entries: {myList}\n\n\nResult: {result}"
    messagebox.showinfo("RESULT:",MyResult)
    
def ClearList():
    myList.clear()
    messagebox.showinfo("INFO","List is cleared")

def Calc_Present_Data():
    i = (method.get(), IVar.get(), NVar.get(), A_P_F_Amount_Var.get())
    if i[0] == "F/A":
        result = F_A(i[1], i[2], i[3])[1]
        messagebox.showinfo("RESULT:",result)
    elif i[0] == "F/P":
        result = F_P(i[1], i[2], i[3])[1]
        messagebox.showinfo("RESULT:",result)
    elif i[0] == "P/F":
        result = P_F(i[1], i[2], i[3])[1]
        messagebox.showinfo("RESULT:",result)
    elif i[0] == "P/A":
        result = P_A(i[1], i[2], i[3])[1]
        messagebox.showinfo("RESULT:",result)
    elif i[0] == "A/P":
        result = A_P(i[1], i[2], i[3])[1]
        messagebox.showinfo("RESULT:",result)
    elif i[0] == "A/F":
        result = A_F(i[1], i[2], i[3])[1]
        messagebox.showinfo("RESULT:",result)
    elif i[0] == "P/G":
        result = P_G(i[1], i[2], i[3])[1]
        messagebox.showinfo("RESULT:",result)
    elif i[0] == "A/G":
        result = A_G(i[1], i[2], i[3])[1]
        messagebox.showinfo("RESULT:",result)
    else:
        messagebox.showerror('Some thing went wrong')

Calculate_One_Time_Period = Button(Serval_Time_Periods_Inputs_Label_Frame, text="Calculate Present Data", command=Calc_Present_Data , bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, pady=10, padx=5)

Add_Serval_Time_Periods = Button(Serval_Time_Periods_Inputs_Label_Frame, text="+", command=Add , bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, pady=10, padx=5)

Calculate_Serval_Time_Periods = Button(Serval_Time_Periods_Inputs_Label_Frame, text="Calculate", command=ListCheck, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, pady=10, padx=5)

Clear_List = Button(Serval_Time_Periods_Inputs_Label_Frame, text="Clear List", command=ClearList, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, pady=10, padx=5)
# -------------------------------------------------------------------------------------------------------

# TargetFrame = ttk.Frame(frame1, width=900, style="Custom.TFrame", padding=5)
# TargetFrame.pack(side=TOP, fill="x", pady=10)

# TargetLabel = LabelFrame(TargetFrame, text="How many years does it take to get the value of F?",  fg="#fcba03", font="Verdana 15", bg=bgColor2, labelanchor='n')
# TargetLabel.pack(fill="both", expand="yes")

# Label(TargetLabel, text="F:", fg="#fcba03", font="Verdana 15", bg=bgColor2).pack(side=LEFT, pady=10, padx=10)
# TargetEntry = Entry(TargetLabel, textvariable=F_Target, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2)
# TargetEntry.pack(side=LEFT, pady=10, padx=10)

# def CalcTarget():
#     pass

# TargetBTN = Button(TargetLabel, text="Calculate", command=CalcTarget, bg=bgColor2, fg="#fcba03", width=8, height=1, font="Verdana 15", relief="raised").pack(side=LEFT, padx=10, pady=10)


# ---------- Present Worth Method Section (Frame 2) -----------------------------
    # ----------------- PWM Variables -------------------
PWA_Methods = StringVar()
Income_Cost = StringVar()
PWA_Methods_i_Entry = DoubleVar()
PWA_Methods_n_Entry = DoubleVar()
PWA_Methods_Value_Entry = DoubleVar()
IC_Value = DoubleVar()
    #  ---------------- PWM UI ------------------
PWM_Frame_1 = ttk.Frame(frame2, width=900, style="Custom.TFrame", padding=5)
PWM_Frame_1.pack(side=TOP, fill="x")
PWM_Frame_1_c_PF = Radiobutton(PWM_Frame_1, text="P/F", variable=PWA_Methods, value="P/F", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)
PWM_Frame_1_c_FP = Radiobutton(PWM_Frame_1, text="F/P", variable=PWA_Methods, value="F/P", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)
PWM_Frame_1_c_AF = Radiobutton(PWM_Frame_1, text="A/F", variable=PWA_Methods, value="A/F", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)
PWM_Frame_1_c_FA = Radiobutton(PWM_Frame_1, text="F/A", variable=PWA_Methods, value="F/A", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)
PWM_Frame_1_c_PA = Radiobutton(PWM_Frame_1, text="P/A", variable=PWA_Methods, value="P/A", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)
PWM_Frame_1_c_AP = Radiobutton(PWM_Frame_1, text="A/P", variable=PWA_Methods, value="A/P", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)
PWM_Frame_1_c_PG = Radiobutton(PWM_Frame_1, text="P/G", variable=PWA_Methods, value="P/G", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)
PWM_Frame_1_c_AG = Radiobutton(PWM_Frame_1, text="A/G", variable=PWA_Methods, value="A/G", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)

PWM_Frame_2 = ttk.Frame(frame2, width=900, style="Custom.TFrame")
PWM_Frame_2.pack(side=TOP, fill="x")

PWM_Frame_1_c7 = Radiobutton(PWM_Frame_2, text="Cost", variable=Income_Cost, value="cost", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)
PWM_Frame_1_c7 = Radiobutton(PWM_Frame_2, text="Income", variable=Income_Cost, value="income", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)

PWM_Frame_3 = ttk.Frame(frame2, width=900, style="Custom.TFrame")
PWM_Frame_3.pack(side=TOP, fill="x")

Label(PWM_Frame_3, text="i%:", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
PWM_Frame_3_i_input = Entry(PWM_Frame_3, textvariable=PWA_Methods_i_Entry, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)

PWM_Frame_4 = ttk.Frame(frame2, width=900, style="Custom.TFrame")
PWM_Frame_4.pack(side=TOP, fill="x")

Label(PWM_Frame_4, text="n:", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
PWM_Frame_4_n_input = Entry(PWM_Frame_4, textvariable=PWA_Methods_n_Entry, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)


PWM_Frame_5 = ttk.Frame(frame2, width=900, style="Custom.TFrame")
PWM_Frame_5.pack(side=TOP, fill="x")

Label(PWM_Frame_5, text="P|F|A:", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
PWM_Frame_5_value_input = Entry(PWM_Frame_5, textvariable=PWA_Methods_Value_Entry, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)

PWM_Frame_6 = ttk.Frame(frame2, width=900, style="Custom.TFrame")
PWM_Frame_6.pack(side=TOP, fill="x")

methodsDict = {
    "P/F": P_F,
    "P/A": P_A,
    "F/A": F_A,
    "F/P": F_P,
    "A/F": A_F,
    "A/P": A_P,
    "P/G": P_G,
    "A/G": A_G 
}

Cost_Income_List = []
def Add_cost_income_to_list():
    try:
        user_inputs = [PWA_Methods.get(), Income_Cost.get(), PWA_Methods_i_Entry.get(), PWA_Methods_n_Entry.get(), PWA_Methods_Value_Entry.get()]
        if user_inputs[0] != "" and user_inputs[1] != "" and user_inputs[2] != 0.0 and user_inputs[3] != 0.0 and user_inputs[4] != 0.0:
            Cost_Income_List.append(user_inputs)
            messagebox.showinfo("ADDED SUCCESSFUL", user_inputs)
            # print(Cost_Income_List)
            return Cost_Income_List
        else:
            messagebox.showerror('Input Error','Choose Method')
    except:
        messagebox.showerror('Error','Some thing went wrong')

def calc_cost_and_income():
    Cost_Income_Sum = 0
    for x in Cost_Income_List:
        m = x[0]
        res = 0
        res += methodsDict[m](x[2], x[3], x[4])[1]
        # print(methodsDict[m](x[2], x[3], x[4])[1])
        if x[1] == "cost":
            res = res * (-1)
        Cost_Income_Sum += res
    messagebox.showinfo("RESULT OF Cost and Incomes:", Cost_Income_Sum)
    return Cost_Income_Sum
    

def clearCostIncomeList():
    Cost_Income_List.clear()
    messagebox.showinfo("Info", "Reset Successful !")

add_cost_income_Btn = Button(PWM_Frame_6, text="+", command=Add_cost_income_to_list, bg=bgColor2, fg="#fcba03", width=8, height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=5, pady=5) 

calc_cost_and_income_Btn = Button(PWM_Frame_6, text="Calculate Cost and Income", command=calc_cost_and_income, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=5, pady=5) 
clear_cost_income_list = Button(PWM_Frame_6, text="RESET", command=clearCostIncomeList, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=5, pady=5) 
 
PWM_Frame_7 = ttk.Frame(frame2, width=900, style="Custom.TFrame")
PWM_Frame_7.pack(side=TOP, fill="x")

Label(PWM_Frame_7, text="Initial Cost(IC):", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
IC_Entry = Entry(PWM_Frame_7, textvariable=IC_Value, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)


def calc_NPW():
    try:
        Cost_Income_Sum = 0
        for x in Cost_Income_List:
            m = x[0]
            res = 0
            res += methodsDict[m](x[2], x[3], x[4])[1]
            if x[1] == "cost":
                res = res * (-1)
            Cost_Income_Sum += res
        npw_result = Cost_Income_Sum - IC_Value.get()
        messagebox.showinfo("RESULT OF NPW", npw_result)
    except:
        messagebox.showerror('Error','Some thing went wrong')

NPW_Btn = Button(PWM_Frame_7, text="Calculate NPW", command=calc_NPW, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=5, pady=5) 

# def print_method():
#     print(PWA_Methods.get())
# PWM_Frame_1_btn1 = Button(PWM_Frame_1, text="Text", command=print_method, bg=bgColor2, fg="#fcba03", width=8, height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=10, pady=10)

# ------------------------------------- Annual Worth Method Section (NAW) --------------------------------
#  ارزش یکنواخت سالیانه خالص =   درآمد یکنواخت یالیانه   -    هزینه یکنواخت سالیانه
# NAW = EUAB(Benefit) - EUAC(Cast)
# EUAC:
#  if(A/F):: P(A/P, i%, n) - SV(A/F, i%, n) + A
#  elif(P/F): (P - SV(P/F, i%, n))(A/P, i%, n) + A
#  else: (P-SV)(A/P, i%, n)+SV(i)+A
# ------------------------------ NWA Variables ------------------------------------------------
P_cost = DoubleVar() # Primary Cost variable
Salvage_value = DoubleVar() # Salvage Value variable
Useful_life_NAW_Method = DoubleVar() # Useful Life variable
yearly_cost = DoubleVar() # Yearly Cost variable
NAW_Method_Choose = StringVar() # NWA Method
NAW_i = DoubleVar() # NWA i% variable
EUAB_value = DoubleVar() # EUAB Value variable

# ------------------------------ NWA UI ---------------------------------

NWA_Frame_1 = ttk.Frame(frame3, width=900, style="Custom.TFrame", padding=5)
NWA_Frame_1.pack(side=TOP, fill="x")
Label(NWA_Frame_1, text="Which one?", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
NWA_method_AF = Radiobutton(NWA_Frame_1, text="A/F", variable=NAW_Method_Choose, value="A/F", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)
NWA_method_AF = Radiobutton(NWA_Frame_1, text="P/F", variable=NAW_Method_Choose, value="P/F", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)
NWA_method_AF = Radiobutton(NWA_Frame_1, text="None Of Them", variable=NAW_Method_Choose, value="none", fg="#fcba03", font="Verdana 12", bg=bgColor2, activebackground=bgColor, activeforeground="#fcba03").pack(side=LEFT, padx=5, pady=5)

NWA_Frame_2 = ttk.Frame(frame3, width=900, style="Custom.TFrame", padding=5)
NWA_Frame_2.pack(side=TOP, fill="x")
Label(NWA_Frame_2, text="P(Primary Cost):", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
primary_cost_NWA_Entry = Entry(NWA_Frame_2, textvariable=P_cost, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)

NWA_Frame_3 = ttk.Frame(frame3, width=900, style="Custom.TFrame", padding=5)
NWA_Frame_3.pack(side=TOP, fill="x")
Label(NWA_Frame_3, text="SV(Salvage Value):", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
salvage_value_NWA_Entry = Entry(NWA_Frame_3, textvariable=Salvage_value, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)

NWA_Frame_4 = ttk.Frame(frame3, width=900, style="Custom.TFrame", padding=5)
NWA_Frame_4.pack(side=TOP, fill="x")
Label(NWA_Frame_4, text="n(Useful Life):", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
useful_life_NWA_Entry = Entry(NWA_Frame_4, textvariable=Useful_life_NAW_Method, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)

NWA_Frame_5 = ttk.Frame(frame3, width=900, style="Custom.TFrame", padding=5)
NWA_Frame_5.pack(side=TOP, fill="x")
Label(NWA_Frame_5, text="A(Yearly Cost):", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
yearly_cost_NWA_Entry = Entry(NWA_Frame_5, textvariable=yearly_cost, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)

Cost_list = []
def add_yearly_cost():
    try:
        Cost_list.append(yearly_cost.get())
        messagebox.showinfo("Add Successful", f"You Add: {yearly_cost.get()}")
        return Cost_list
    except:
        messagebox.showerror('Error','Some thing went wrong')

def clear_yearly_cost_list():
    try:
        Cost_list.clear()
        messagebox.showinfo("Clear Successful", "List cleared !")
    except:
        messagebox.showerror('Error','Some thing went wrong')


def Show_yearly_cost_list():
    try:
        messagebox.showinfo("Add Successful", f"Your Costs: {Cost_list}")
    except:
        messagebox.showerror('Error','Some thing went wrong')
yearly_cost_NWA_Add_Btn = Button(NWA_Frame_5, text="Add Cost", command=add_yearly_cost, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=5, pady=5) 
yearly_cost_NWA_Clear_List_Btn = Button(NWA_Frame_5, text="Clear Cost List", command=clear_yearly_cost_list, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=5, pady=5) 
yearly_cost_NWA_Show_List_Btn = Button(NWA_Frame_5, text="Show Cost List", command=Show_yearly_cost_list, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=5, pady=5) 


NWA_Frame_6 = ttk.Frame(frame3, width=900, style="Custom.TFrame", padding=5)
NWA_Frame_6.pack(side=TOP, fill="x")
Label(NWA_Frame_6, text="i(i%):", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
yearly_cost_NWA_Entry = Entry(NWA_Frame_6, textvariable=NAW_i, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)

def calc_EUAC():
    try:
        EUAC_List = [NAW_Method_Choose.get(), P_cost.get(), Salvage_value.get(), Useful_life_NAW_Method.get(), NAW_i.get(), Cost_list]
        if EUAC_List[0] == "A/F":
            result = (EUAC_List[1] *  A_P(EUAC_List[4], EUAC_List[3])[0]) - (EUAC_List[2] * A_F(EUAC_List[4], EUAC_List[3])[0]) + sum(EUAC_List[5])
            messagebox.showinfo("RESULT OF EUAC", result)
        elif EUAC_List[0] == "P/F":
            result = (EUAC_List[1] - (EUAC_List[2] * P_F(EUAC_List[4], EUAC_List[3])[0])) * (A_P(EUAC_List[4], EUAC_List[3])[0]) + sum(EUAC_List[5])
            messagebox.showinfo("RESULT OF EUAC", result)
        elif EUAC_List[0] == "none":
            result = (EUAC_List[1] - EUAC_List[2]) * (A_P(EUAC_List[4], EUAC_List[3])[0]) + (EUAC_List[2] * EUAC_List[4]/100) + sum(EUAC_List[5])
            messagebox.showinfo("RESULT OF EUAC", result)
        else:
            messagebox.showerror('Input Error','Please Complete Inputs.')
    except:
        messagebox.showerror('Error','Some thing went wrong')

def Calc_NAW():
    try:
        NAW_List = [NAW_Method_Choose.get(), P_cost.get(), Salvage_value.get(), Useful_life_NAW_Method.get(), NAW_i.get(), yearly_cost.get(), EUAB_value.get()]
        if NAW_List[0] == "A/F":
            result = (NAW_List[1] *  A_P(NAW_List[4], NAW_List[3])[0]) - (NAW_List[2] * A_F(NAW_List[4], NAW_List[3])[0]) + NAW_List[5]
            messagebox.showinfo("RESULT OF NAW", NAW_List[6] - result)
        elif NAW_List[0] == "P/F":
            result = (NAW_List[1] - (NAW_List[2] * P_F(NAW_List[4],  NAW_List[3])[0])) * (A_P(NAW_List[4], NAW_List[3])[0]) + NAW_List[5]
            messagebox.showinfo("RESULT OF NAW", NAW_List[6] - result)
        elif NAW_List[0] == "none":
            result = (NAW_List[1] - NAW_List[2]) * (A_P(NAW_List[4], NAW_List[3])[0]) + (NAW_List[2] * NAW_List[4]/100) + NAW_List[5]
            messagebox.showinfo("RESULT OF NAW", NAW_List[6] - result)
        else:
            messagebox.showerror('Input Error','Please Enter All Inputs.')
    except:
        messagebox.showerror('Error','Some thing went wrong')




NWA_Frame_7 = ttk.Frame(frame3, width=900, style="Custom.TFrame", padding=5)
NWA_Frame_7.pack(side=TOP, fill="x")
Label(NWA_Frame_7, text="EUAB(Benefit):", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
EUAB_value_Entry = Entry(NWA_Frame_7, textvariable=EUAB_value, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)

NWA_Frame_8 = ttk.Frame(frame3, width=900, style="Custom.TFrame", padding=5)
NWA_Frame_8.pack(side=TOP, fill="x")
EUAC_Btn = Button(NWA_Frame_8, text="Calculate EUAC", command=calc_EUAC, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=5, pady=5) 
NAW_Btn = Button(NWA_Frame_8, text="Calculate NAW", command=Calc_NAW, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=5, pady=5) 


# ------------------------- Payback Period Method -----------------------------------
    # -------------------------------- Payback Period Variables --------------------------------
PBPV_i = DoubleVar()
PBPV_p = DoubleVar()
PBPV_n = IntVar()
PBPV_increase_income = DoubleVar()
PBPV_cf = DoubleVar()
PBPV_mapp = DoubleVar()
    # -------------------------------- Payback Period UI --------------------------------  
PBPV_Frame_1 = ttk.Frame(frame4, width=900, style="Custom.TFrame", padding=5)
PBPV_Frame_1.pack(side=TOP, fill="x")
Label(PBPV_Frame_1, text="P:", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
PBPV_p_Entry = Entry(PBPV_Frame_1, textvariable=PBPV_p, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)
Label(PBPV_Frame_1, text="MAPP:", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
PBPV_mapp_Entry = Entry(PBPV_Frame_1, textvariable=PBPV_mapp, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)


PBPV_Frame_2 = ttk.Frame(frame4, width=900, style="Custom.TFrame", padding=5)
PBPV_Frame_2.pack(side=TOP, fill="x")
Label(PBPV_Frame_2, text="How many year:", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
PBPV_n_Entry = Entry(PBPV_Frame_2, textvariable=PBPV_n, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)
Label(PBPV_Frame_2, text="i%:", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
PBPV_n_Entry = Entry(PBPV_Frame_2, textvariable=PBPV_i, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)


PBPV_Frame_3 = ttk.Frame(frame4, width=900, style="Custom.TFrame", padding=5)
PBPV_Frame_3.pack(side=TOP, fill="x")
Label(PBPV_Frame_3, text="First year income:", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
PBPV_n_Entry = Entry(PBPV_Frame_3, textvariable=PBPV_cf, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)
Label(PBPV_Frame_3, text="The amount increases each year:", fg="#fcba03", font="Verdana 12", bg=bgColor2).pack(side=LEFT, padx=5, pady=5)
PBPV_n_Entry = Entry(PBPV_Frame_3, textvariable=PBPV_increase_income, background=bgColor2, width=10, foreground="#fcba03", relief="sunken", font="Verdana 15", borderwidth=2).pack(side=LEFT, padx=5, pady=5)

def Calc_PBPV():
    Sum_Of_Years = 0
    year_1 = PBPV_cf.get() * P_F(PBPV_i.get(), 1)[0]
    Accumulation_to_recovery_of_initial_capital_first_year = -(PBPV_p.get()) + year_1
    Percentage_of_years_until_recovery = math.floor(PBPV_p.get() / abs(Accumulation_to_recovery_of_initial_capital_first_year))
    PBPV_List = [(0, -(PBPV_p.get()), -(PBPV_p.get()), -(PBPV_p.get()), 0), (1, PBPV_cf.get(), year_1, Accumulation_to_recovery_of_initial_capital_first_year, Percentage_of_years_until_recovery)]
    # print(PBPV_p.get() / abs(Accumulation_to_recovery_of_initial_capital_first_year))
    # print(PBPV_List)
    n = PBPV_n.get()
    for x in range(2, n+1):
        year = x
        FP_in_year = PBPV_List[-1][1] + PBPV_increase_income.get()
        FP_of_PV = P_F(PBPV_i.get(), x, FP_in_year)[1]
        Accumulation_to_recovery_of_initial_capital = PBPV_List[-1][-2] + FP_of_PV
        print(f"For Year: {x}")
        print("---------")
        print("Accumulation_to_recovery_of_initial_capital ", Accumulation_to_recovery_of_initial_capital)
        print("---------")
        if Accumulation_to_recovery_of_initial_capital > 0:
            Accumulation_to_recovery_of_initial_capital = 0
            print("Accumulation_to_recovery_of_initial_capital >= 0")
            print("---------")
        else:
            print("Accumulation_to_recovery_of_initial_capital < 0")
            print("---------")
        Percentage_of_years_until_recovery = abs(PBPV_List[-1][-2] / FP_of_PV)
        print("Percentage_of_years_until_recovery ",Percentage_of_years_until_recovery)
        print("---------")
        if Percentage_of_years_until_recovery > 1:
            Percentage_of_years_until_recovery = 1
            print("Percentage_of_years_until_recovery > 1")
            print("---------")
        else:
            print("Percentage_of_years_until_recovery < 1")
            print("---------")
        if 1 > PBPV_List[-1][-1] > 0:
            Percentage_of_years_until_recovery = 0
            print(PBPV_List[-1][-1], "> 0")
            print("---------")
        else:
            print(PBPV_List[-1][-1], "< 0")
            print("---------")
        PBPV_Sub_List = (year, FP_in_year, FP_of_PV, Accumulation_to_recovery_of_initial_capital, Percentage_of_years_until_recovery)
        print("PBPV_Sub_List ", PBPV_Sub_List)
        print("---------")
        PBPV_List.append(PBPV_Sub_List)
        print(PBPV_List)
        print("---------\n---------\n---------")
    for item in PBPV_List:
        Sum_Of_Years += item[-1]
    MAPP = PBPV_mapp.get()
    if MAPP > Sum_Of_Years:
        res = f"MAPP: {MAPP}\nResult Of Your Data: {Sum_Of_Years}\n {MAPP} > {Sum_Of_Years}\nProject Approval :)"
        messagebox.showinfo("Result", res)
    elif MAPP < Sum_Of_Years:
        res = f"MAPP: {MAPP}\nResult Of Your Data: {Sum_Of_Years}\n {MAPP} < {Sum_Of_Years}\nRejection Of The Project :("
        messagebox.showinfo("Result", res)

PBPV_Frame_4 = ttk.Frame(frame4, width=900, style="Custom.TFrame", padding=5)
PBPV_Frame_4.pack(side=TOP, fill="x")
PBPV_Btn = Button(PBPV_Frame_4, text="Calculate PBPV", command=Calc_PBPV, bg=bgColor2, fg="#fcba03", height=1, font="Verdana 12", relief="raised").pack(side=LEFT, padx=5, pady=5) 


root.mainloop()