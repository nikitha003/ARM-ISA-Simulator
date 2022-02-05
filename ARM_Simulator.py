#This program will simulate a ARM 32 bit processor in a GUI.
#This will help in learning and executing each ARM instruciton and see the results visually
#The user can visualise what is going on in registers and memory locations

from tkinter import *
from tkinter import ttk
ARM_window = Tk()
ARM_window.title("ARM Simulator")
ARM_canvas = Canvas(ARM_window, width = 2000, height = 1200, bg = "pink")
ARM_canvas.pack()
debug = 1


def combo_enter(event):
    global combo_info_label
    current_instruction = instr1_combo.get()
    if debug:
        print("The Combobox value is: " + current_instruction)
    if current_instruction == "":
        combo_info_label = Label(ARM_canvas, text = "Choose an instruction to know more", font = ("Arial", 15), bg = "black", fg = "white")
        combo_info_label.place(x = 600, y = 400)
    elif current_instruction == "ADD":
        combo_info_label = Label(ARM_canvas, text = "ADD  destReg, srcReg, op2 // destReg = srcReg + op2\n Example: ADD  R0, R1, R2 //R0 = R1 + R2", font = \
                ("Arial", 15), bg = "black", fg = "white")
        combo_info_label.place(x =600, y = 400)
    else:
        print("End")


def combo_leave(event):
    global combo_info_label
    combo_info_label.destroy()

instr_label = Label(ARM_canvas, text = "Choose an ARM instruction", font = ("Arial", 20), bg = "black", fg = "white")
instr_label.place(x = 10, y =10)

instr1_combo = ttk.Combobox(ARM_canvas, values = ["ADD", "MOV", "SUB", "LDR", "STR", "PUSH", "POP"], width = 5)
instr1_combo.place(x = 10, y =50)
instr1_combo.bind("<Enter>", combo_enter) 
instr1_combo.bind("<Leave>", combo_leave)

operand11_combo = ttk.Combobox(ARM_canvas, values = ["R0","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11","R12"], width = 3)
operand11_combo.place(x = 70, y= 50)

operand12_combo = ttk.Combobox(ARM_canvas, values = ["R0","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11","R12"], width = 3)
operand12_combo.place(x = 115, y= 50)

operand13_name = ""
operand13_entry = Entry(ARM_canvas, textvariable = operand13_name, fg = "white", bg = "black", font = ("Arial", 10), width = 5)
operand13_entry.place(x = 160, y = 50)

ARM_window.mainloop()
