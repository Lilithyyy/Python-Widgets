import tkinter as tk

w, h = 400,300 #set width and height for all windows

#set descriptions for each widget (aby som to nemusela hladat v kazdej definicii ale mohla to mat pokope a popripade prepisat)
labeldecriptions = [
    "This is the Radiobutton widget. All the radiobuttons are linked together through a variable called 'v'. When you select one of the radiobuttons, the value of 'v' changes to the value assigned to that specific radiobutton. In this example, when you click on the canvas, it checks the value of 'v' and draws the corresponding shape (circle, square, or line) at the clicked position.",
    "",
    "",
    "",
    "",
    "",
]

def open_w1():
    global w, h, labeldecriptions
    
    #holds values for radiobuttons
    v = tk.IntVar()
    
    #opens new window
    widget1_win = tk.Toplevel(root)
    widget1_win.title("Radiobutton")
    widget1_win.geometry(f"{w}x{h}")
    widget1_win.resizable(False, False)

    #frame for holding the widgets and canvas (3 pre lepsi vzhlad, hrala som sa s umiestnenim...)
    instructions_frame = tk.Frame(widget1_win)
    instructions_frame.pack(side="top", fill="x")

    description_frame = tk.Frame(widget1_win)
    description_frame.pack(side="bottom", fill="x", pady=5, expand=True)

    canvas_frame = tk.Frame(widget1_win)
    canvas_frame.pack(fill="both", pady=5, expand=False)

    #canvas
    canvas1 = tk.Canvas(canvas_frame, bg="#EDC1FF")
    canvas1.pack(fill="both")

    #vrchny frame
    instruction = tk.Label(instructions_frame, text="Select a shape:", font="Arial 10 bold")
    instruction.pack(side="left", padx=0, pady=5)

    radiobutton1 = tk.Radiobutton(instructions_frame, text='Circle', variable=v, value=1)
    radiobutton1.pack(side="right", padx=0, pady=5)
    radiobutton2 = tk.Radiobutton(instructions_frame, text='Square', variable=v, value=2)
    radiobutton2.pack(side="right", padx=0, pady=5)
    radiobutton3 = tk.Radiobutton(instructions_frame, text='Line', variable=v, value=3)
    radiobutton3.pack(side="right", padx=0, pady=5)

    #spodny frame
    description = tk.Label(description_frame, text = labeldecriptions[0], wraplength=w)
    description.pack(side="bottom", pady=5)

    #function for drawing shapes (viem, ze sme match este nerobili, ale chcela som to skusit)
    def on_click(click):
        type = v.get()
        match type:
            case 1:
                canvas1.create_oval(click.x-10, click.y-10, click.x+10, click.y+10)
            case 2:
                canvas1.create_rectangle(click.x-10, click.y-10, click.x+10, click.y+10)
            case 3:
                canvas1.create_line(click.x-10, click.y, click.x+10, click.y)
    
    canvas1.bind('<Button-1>', on_click)

def open_w2():
    global w, h
    
    widget2_win = tk.Toplevel(root)
    widget2_win.title("Widget 2")

    canvas2 = tk.Canvas(widget2_win, width=w, height=h, bg="white")
    canvas2.pack()

def open_w3():
    global w, h
    
    widget3_win = tk.Toplevel(root)
    widget3_win.title("Widget 3")

    canvas3 = tk.Canvas(widget3_win, width=w, height=h, bg="white")
    canvas3.pack()

def open_w4():
    global w, h
    
    widget4_win = tk.Toplevel(root)
    widget4_win.title("Widget 4")

    canvas4 = tk.Canvas(widget4_win, width=w, height=h, bg="white")
    canvas4.pack()

def open_w5():
    global w, h
    
    widget5_win = tk.Toplevel(root)
    widget5_win.title("Widget 5")

    canvas5 = tk.Canvas(widget5_win, width=w, height=h, bg="white")
    canvas5.pack()

def open_w6():
    global w, h
    
    widget6_win = tk.Toplevel(root)
    widget6_win.title("Widget 6")

    canvas6 = tk.Canvas(widget6_win, width=w, height=h, bg="white")
    canvas6.pack()

root = tk.Tk()
root.title("Main Window")
root.geometry(f"{w}x{h}")
root.resizable(False, False)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

options_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Design", menu=options_menu)

options_menu.add_command(label="Radiobutton", command = open_w1)
options_menu.add_command(label="Widget 2", command = open_w2)
options_menu.add_command(label="Widget 3", command = open_w3)
options_menu.add_command(label="Widget 4", command = open_w4)
options_menu.add_command(label="Widget 5", command = open_w5)
options_menu.add_command(label="Widget 6", command = open_w6)

#main canvas in root
canvas_main = tk.Canvas(root, width=w, height=h, bg="#EDC1FF")
canvas_main.pack()

canvas_main.create_text(w//2, h//2, text="Please pick a widget you'd like to see", font="Arial 14 bold", fill="#c37aff")

root.mainloop()