import tkinter as tk

w, h = 400,300 #set width and height for all windows

#set name and descriptions for each widget (aby som to nemusela hladat v kazdej definicii ale mohla to mat pokope a popripade prepisat) 
widget_info = [
    ["Radiobutton", "This is a Radiobutton. All the radiobuttons are linked together through a variable called 'v'. When you select one of the radiobuttons, the value of 'v' changes to the value assigned to that specific radiobutton. In this example, when you click on the canvas, it checks the value of 'v' and draws the corresponding shape (circle, square, or line) at the clicked position."],
    ["Checkbutton", "This is a Checkbox. You can set off and on values of the checkboxes and work with them further in functions."],
    ["Scale", "This is a Scale. You can set the values of the scale to a variable you can use later for coordinate changes or functions."],
    ["Spinbox", "This is a spinbox. You can set the minimum and maximum value and change what happens upon selecting each one with functions."],
    ["Listbox", "This is a Listbox. You can bind a listbox through buttons and functions, get the contents of the listbox and so on."],
    ["Combobox", ""],
]

def open_w1():
    global w, h
    
    #holds values for radiobuttons
    v = tk.IntVar()
    
    #opens new window
    widget1_win = tk.Toplevel(root)
    widget1_win.title(widget_info[0][0])
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

    #bottom frame
    instruction = tk.Label(instructions_frame, text="Select a shape:", font="Arial 10 bold")
    instruction.pack(side="left", padx=5, pady=5)

    radiobutton1 = tk.Radiobutton(instructions_frame, text='Circle', variable=v, value=1)
    radiobutton1.pack(side="right", padx=0, pady=5)
    radiobutton2 = tk.Radiobutton(instructions_frame, text='Square', variable=v, value=2)
    radiobutton2.pack(side="right", padx=0, pady=5)
    radiobutton3 = tk.Radiobutton(instructions_frame, text='Line', variable=v, value=3)
    radiobutton3.pack(side="right", padx=0, pady=5)

    #top frame
    description = tk.Label(description_frame, text = widget_info[0][1], wraplength=w)
    description.pack(side="bottom", pady=5, padx=5)

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
    widget2_win.title(widget_info[1][0])
    widget2_win.geometry(f"{w}x{h}")
    widget2_win.resizable(False, False)

    instructions_frame = tk.Frame(widget2_win)
    instructions_frame.pack(side="top", fill="x")

    description_frame = tk.Frame(widget2_win)
    description_frame.pack(side="bottom", fill="x", pady=5, expand=True)   

    canvas_frame = tk.Frame(widget2_win)
    canvas_frame.pack(expand=False, pady=5, fill="both")

    instructions = tk.Label(instructions_frame, text="Check the boxes to set the visibility of objects")
    instructions.pack(side="top")

    description = tk.Label(description_frame, text=widget_info[1][1], wraplength=w, pady = 10)
    description.pack(side="bottom")

    def draw():
        canvas2.delete('all')

        if object1.get() == True:
            canvas2.create_oval(30, 30, 40, 40, tag = "oval")
        
        if object2.get() == True:
            canvas2.create_rectangle(30, 50, 40, 60, tag="square")

    object1 = tk.BooleanVar()
    checkbutton1 = tk.Checkbutton(instructions_frame, text="circle", onvalue=True, offvalue=False, variable = object1, command=draw)
    object2 = tk.BooleanVar()
    checkbutton2 = tk.Checkbutton(instructions_frame, text="rectangle", onvalue=True, offvalue=False, variable= object2, command=draw)

    checkbutton1.pack(side="bottom")
    checkbutton2.pack(side="bottom")

    canvas2 = tk.Canvas(canvas_frame, width=w, height=h, bg="#EDC1FF")
    canvas2.pack()

def open_w3():
    global w, h, rx, ry
    
    rx, ry = 10, 10
    x, y = w//2-20, h//2-50

    widget3_win = tk.Toplevel(root)
    widget3_win.title(widget_info[2][0])
    widget3_win.geometry(f"{w}x{h}")
    widget3_win.resizable(False, False)

    instructions_frame = tk.Frame(widget3_win)
    instructions_frame.pack(side="top", fill="x")

    description_frame = tk.Frame(widget3_win)
    description_frame.pack(side="bottom", fill="x", pady=5, expand=True)   

    canvas_frame = tk.Frame(widget3_win)
    canvas_frame.pack(expand=False, pady=5, fill="both") 

    canvas3 = tk.Canvas(canvas_frame, width=w, height=h, bg="#EDC1FF")
    canvas3.pack(fill="both")

    canvas3.create_oval(x-rx, y-ry, x+rx, y+ry, width=2, outline="#c37aff", tag='oval')

    def changex(event):
        global rx
        rx = scalex.get()
        redraw()

    def changey(event):
        global ry
        ry = scaley.get()
        redraw()

    def redraw():
        canvas3.coords('oval',[x-rx, y-ry, x+rx, y+ry])

    instructions = tk.Label(instructions_frame, text="Move the scales to adjust the size of the circle")
    instructions.pack(side="top", expand=True)

    scalex = tk.Scale(canvas_frame, from_=10, to=w//2, orient="horizontal", length=w, command=changex)
    scaley = tk.Scale(canvas_frame, from_ =10, to= y, orient="vertical", command=changey)

    description = tk.Label(description_frame, wraplength=w, text=widget_info[2][1])
    description.pack(side="bottom", expand=True)

    scalex.place(x = 0, y = h - 115)
    scalex.set(rx)

    scaley.place(x = w - 40, y= 0, height=h-100)
    scaley.set(ry)

def open_w4():
    global w, h
    
    widget4_win = tk.Toplevel(root)
    widget4_win.title(widget_info[3][0])
    widget4_win.geometry(f"{w}x{h}")
    widget4_win.resizable(False, False)

    instructions_frame = tk.Frame(widget4_win)
    instructions_frame.pack(side="top", fill="x")

    description_frame = tk.Frame(widget4_win)
    description_frame.pack(side="bottom", fill="x", pady=5, expand=True)   

    canvas_frame = tk.Frame(widget4_win)
    canvas_frame.pack(expand=False, pady=5, fill="both") 

    canvas4 = tk.Canvas(canvas_frame, width=w, height=h, bg="white")
    canvas4.pack()

    colors = ['red', 'green', 'blue']

    def on_spinbox_change():
        value = int(spinbox.get())
        canvas4['bg'] = colors[value]

    description = tk.Label(description_frame, text=widget_info[3][1], wraplength=w)
    description.pack()

    spinbox = tk.Spinbox(instructions_frame, from_ = 0, to=2, width=10, command=on_spinbox_change)
    spinbox.pack()


def open_w5():
    global w, h
    
    #a list of colors in our lsit
    colors = ['red', 'green', 'blue', 'white', 'yellow', 'orange', 'pink']

    widget5_win = tk.Toplevel(root)
    widget5_win.title(widget_info[4][0])
    widget5_win.geometry(f"{w}x{h}")
    widget5_win.resizable(False, False)

    #copy pasted frames, every def uses the same ones...
    instructions_frame = tk.Frame(widget5_win)
    instructions_frame.pack(side="top", fill="x")

    description_frame = tk.Frame(widget5_win)
    description_frame.pack(side="bottom", fill="x", pady=5, expand=True)   

    canvas_frame = tk.Frame(widget5_win)
    canvas_frame.pack(expand=False, pady=5, fill="both") 

    canvas5 = tk.Canvas(canvas_frame, width=w, height=h, bg="#EDC1FF")
    canvas5.pack(fill="both")

    instructions = tk.Label(instructions_frame, text="Double click on a color to change it")
    instructions.pack(side="top", pady=5)

    #wraplength is used for cutting text into pieces so it can fit the parent frame
    description = tk.Label(description_frame, text=widget_info[4][1], wraplength=w)
    description.pack(fill="x", pady=5, padx=5)

    #create a listbox
    listbox = tk.Listbox(instructions_frame)
    listbox.pack(fill="both", pady=5, padx=5)

    for color in colors:
        listbox.insert('end', color)

    #linking the listbox with functions
    def recolor(event):
        selected = listbox.curselection()
        canvas5['bg'] = listbox.get(selected)

    listbox.bind('<Double-Button-1>', recolor)

def open_w6():
    global w, h
    
    widget6_win = tk.Toplevel(root)
    widget6_win.title(widget_info[5][0])

    canvas6 = tk.Canvas(widget6_win, width=w, height=h, bg="white")
    canvas6.pack()

#main window
root = tk.Tk()
root.title("Main Window")
root.geometry(f"{w}x{h}")
root.resizable(False, False)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

options_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Design", menu=options_menu)

#list of functions to get rid of manually copypasting info...
open_functions = [open_w1, open_w2, open_w3, open_w4, open_w5, open_w6]

for i in range(len(open_functions)):
    options_menu.add_command(label=widget_info[i][0], command = open_functions[i])

#main canvas in root
canvas_main = tk.Canvas(root, width=w, height=h, bg="#EDC1FF")
canvas_main.pack()

canvas_main.create_text(w//2, h//2, text="Please pick a widget you'd like to see", font="Arial 14 bold", fill="#c37aff")

root.mainloop()