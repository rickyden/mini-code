import random
import tkinter as tk
from tkinter import ttk

#gui based
def main():

    def dice_roll():

        number_of_dice = int(Number_of_dice_Entry.get())

        if int(var.get()) == 0:
            dice_face = int(Custom_dice_Entry.get())
        else:
            dice_face = int(var.get())

        result = []
        for i in range(number_of_dice):
            result.append(random.randint(1, dice_face))
        
        for label in result_labels:
            label.destroy()

        result_labels.clear()

        for item in result:
            label = tk.Label(root, text=item, padx=10, pady=5, relief=tk.RAISED, bg="white", fg="black", font=set_font)
            label.grid(row=4, column=len(result_labels) + 3, padx=2, pady=2)
            result_labels.append(label)
            
    def enable_custom_input():
        print(var.get())
        if int(var.get()) == 0:
            Custom_dice_Entry.configure(state='normal')
        else:
            Custom_dice_Entry.configure(state='disable')

    set_font = ("Yu Gothic", 20)
    Custom_dice_Entry = 0

    root = tk.Tk()

    root.title("dice roller")
    root.geometry("800x500")

    var = tk.StringVar()

    text = tk.Label(root, text="dice roller",font=set_font)
    text.grid(row=0,column=1)
    Number_of_dice_label = tk.Label(root, text="Number of dice", font = set_font)
    Number_of_dice_label.grid(row=3, column=0,pady=2, padx=20)
    Number_of_dice_Entry = tk.Entry(root, text="",font=set_font, width=5)
    Number_of_dice_Entry.grid(row=4, column=0, pady=2)

    d3 = tk.Radiobutton(root, text="d3", font=set_font, variable=var, value = 3, command=enable_custom_input)
    d3.grid(row=1, column=1, sticky=tk.W)
    d4 = tk.Radiobutton(root, text="d4", font=set_font, variable=var, value = 4, command=enable_custom_input)
    d4.grid(row=2, column=1, sticky=tk.W)
    d6 = tk.Radiobutton(root, text="d6", font=set_font, variable=var, value = 6, command=enable_custom_input)
    d6.grid(row=3, column=1, sticky=tk.W)
    d10 = tk.Radiobutton(root, text="d10", font=set_font, variable=var, value = 10, command=enable_custom_input)
    d10.grid(row=4, column=1, sticky=tk.W)
    d20 = tk.Radiobutton(root, text="d20", font=set_font, variable=var, value = 20, command=enable_custom_input)
    d20.grid(row=5, column=1, sticky=tk.W)
    d100 = tk.Radiobutton(root, text="d100", font=set_font, variable=var, value = 100, command=enable_custom_input)
    d100.grid(row=6, column=1, sticky=tk.W)
    d_custom = tk.Radiobutton(root, text="Custom: d",font=set_font, variable=var, value = 0, command=enable_custom_input)
    d_custom.grid(row=7, column=1, sticky=tk.W)
    Custom_dice_Entry = tk.Entry(root, width= 10, font=set_font)
    Custom_dice_Entry.grid(row = 7, column = 2)
    Custom_dice_Entry.configure(state="disabled")

    result_labels = []

    result_text_label = tk.Label(root, text="Result:", font=set_font)
    result_text_label.grid(row=4, column=2, sticky=tk.W)

    button=tk.Button(root,text="roll",font=set_font,command=dice_roll)
    button.grid(row = 8,column=1, pady = 2)


    # def dice_roller():
    #     arg = Entry.get().split("d")
    #     times = int(arg[0])
    #     faces = int(arg[1])

    #     result = []
    #     for i in range(times):
    #         result.append(random.randint(1, faces))

    #     result_label.config(text=result)
    #     print("Entry value.:", arg)

    # pack()
    # text = tk.Label(root, text="dice roller",font=set_font)
    # text.pack()
    # Entry = tk.Entry(root, font=set_font)
    # Entry.pack()
    # result_label = tk.Label(root, text="", font=set_font)
    # result_label.pack()
    # button=tk.Button(root,text="roll",font=set_font,command=dice_roller)
    # button.pack(side = "bottom")

    root.mainloop()

# cmd based
# def mutliple_dice_roller(times, face):
#     result = []

#     for i in range(times):
#         result.append(random.randint(1, face))

#     return result

# def main():
#     result = None
#     while(result == None):
#         try:
#             arg = input("number of dice + dice face. e.g. 3d6\n").split("d")
#             result = mutliple_dice_roller(int(arg[0]), int(arg[1]))
#         except:
#             print("wrong input")
#     print(result)

if __name__ == "__main__":
    main()

