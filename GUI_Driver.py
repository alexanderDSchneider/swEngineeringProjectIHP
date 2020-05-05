# Author: Austin Thompson
# File: GUI_Driver.py
# Date: 4/23/2020

import tkinter as tk
from tkinter import ttk
from tkinter import *
from Algorithm import Algorithm
from login_script import *
import random
import tkinter



class GUI_Driver(tk.Tk):     #inherit from Tkinter
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        # create a dictionary
        # this will allow us to create different windows
        self.frames = {}
        
        for F in ( Login, Tutorial, StartScreen, Algorithm_Visualizer, CreateAccount):
            # screen on start
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(Login)
        
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
        
# this is a new page
#Alexander Schneider        
class Login(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
          
        #create login frame
        login_frame = tk.Frame(self, width=200, height=100)
        login_frame.pack()

        label = tk.Label(self, text = "Enter your user information", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        #username box        
        user_box = tk.Entry(login_frame)
        user_box.pack()
                   
        #password box
        pass_box = tk.Entry(login_frame)
        pass_box.pack()
            
        #on keypress call login function   
        login = tk.Button(self, text = "Login", command = lambda: on_login_press())
        login.pack()
                     
        createAccount = tk.Button(self, text = "Create Account", command = lambda: controller.show_frame(CreateAccount) )
        createAccount.pack()

        def on_login_press():
            #call function to login, returns one if correct
            #pass username and password to login funcion
            check = login_press(user_box.get(), pass_box.get())
            print(check)
            if(check == 1):
                #successfull login
                controller.show_frame(StartScreen)
            elif(check == 2):
                #login fail, no account by that name
                popupmsg("Login failed, no user by that name.")
                user_box.delete(0,"end")
                pass_box.delete(0,"end")
            else:
                #on fail clear boxes to try again
                popupmsg("Login failed incorrect password.")
                user_box.delete(0,"end")
                pass_box.delete(0,"end")

                
        def popupmsg(msg):
            popup = tk.Tk()
            popup.wm_title("!")
            label = ttk.Label(popup, text=msg)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
            B1.pack()
                


#Alexander Scheider
class CreateAccount(tk.Frame):               
            
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
          
        #create frame
        create_account_frame = tk.Frame(self, width=200, height=100)
        create_account_frame.pack()

        label = tk.Label(self, text = "Create your username and password", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        #username box        
        user_box = tk.Entry(create_account_frame)
        user_box.pack()
                  
        #password box
        pass_box = tk.Entry(create_account_frame)
        pass_box.pack()
            
        #on keypress    
        create = tk.Button(self, text = "Create", command = lambda: on_create_press())
        create.pack()

        def on_create_press():
            #call function to create account
            check = create_press(user_box.get(), pass_box.get())
            print(check)
            if(check == 1):
                #successfull 
                controller.show_frame(Login)
                popupmsg("Login information created.")
            else:
                #if fails clears box to try again
                popupmsg("Username already exists.")
                user_box.delete(0,"end")
                pass_box.delete(0,"end")


        def popupmsg(msg):
            popup = tk.Tk()
            popup.wm_title("!")
            label = ttk.Label(popup, text=msg)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
            B1.pack()       
                    
            


class StartScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Main Menu", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        startTutorial = tk.Button(self, text = "Start Tutorials", command = lambda: controller.show_frame(Tutorial))
        startTutorial.pack()
        
        algVis = tk.Button(self, text = "Visualize Algorithm", command = lambda: controller.show_frame(Algorithm_Visualizer))
        algVis.pack()
        
    
class Tutorial(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Select Tutorials", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        Beginner = tk.Button(self, text = "Beginner", command=lambda: controller.show_frame(StartScreen))
        Beginner.pack()
        
        Intermediate = tk.Button(self, text = "Intermediate", command=lambda: controller.show_frame(StartScreen))
        Intermediate.pack()
        
        Hard = tk.Button(self, text = "Hard", command=lambda: controller.show_frame(StartScreen))
        Hard.pack()
        
        Tutorial = tk.Button(self, text = "Tutorial 1", command=lambda: controller.show_frame(StartScreen))
        Tutorial.pack()
    
    
    
    
class Algorithm_Visualizer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Select Algorithm", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
       # self.columnconfigure(0, weight=1)
       # self.columnconfigure(1, weight=1)
        
        
        # Create a "UI" for the user to generate a new array, etc...
        algorithm_frame = tk.Frame(self, width=200, height=100)
        algorithm_frame.pack()
        
        
        # Create a label to select the algorithm type
        type_label = tk.Label(algorithm_frame, text = "Algorithm Type: ")
        type_label.pack(side=LEFT)
        # Dropdown menu to select type
        type_algorithm = ttk.Combobox(algorithm_frame, values=['Bubble Sort', 'Insertion Sort', 'Quick Sort'])
        type_algorithm.pack(side=LEFT)
        type_algorithm.current(0)
        
        # Enter the size of the array
        array_size = tk.Label(algorithm_frame, text = "Size (5-20): ")
        array_size.pack(padx = 15)
        entrysize = tk.Entry(algorithm_frame)
        entrysize.focus()
        entrysize.pack(pady=5)

        min_value = 20
        max_value = 200
        data = []
        chosen_algorithm = Algorithm(type_algorithm.get(), 10, min_value, max_value, data)
        
        # Slider to allow user to adjust playback speed
        speed = tk.Label(algorithm_frame, text = "Playback Speed")
        speed.pack()

        alg_speed = Scale(algorithm_frame, from_= 0.0, to = 3.0, length = 200, digits = 2, resolution = 0.1, orient = HORIZONTAL)
        alg_speed.place(relx=0.5, rely=.9, anchor=CENTER)
        
        canvas = Canvas(self, width=600, height=350, bg='snow2')
        create_array = tk.Button(self, text="Create New Array", command=lambda:Generate(chosen_algorithm, entrysize, canvas), bg='orange')
        create_array.place(relx=.43, rely=.20)
        
        start_visualizing = tk.Button(self, text="Animate", command = lambda:Animate(chosen_algorithm, canvas, alg_speed, type_algorithm), width = 13)
        start_visualizing.place(relx=.43, rely=.24)
        
        Home = tk.Button(self, text = "Home", command=lambda: controller.show_frame(StartScreen))
        Home.place(relx = .5, rely = .95, anchor = CENTER)
        

def Generate(algorithm, entrysize, canvas):
    if len(entrysize.get()) == 0:
        algorithm.size = 10
    else:
        algorithm.size = int(entrysize.get())
    
    # Simple logic to correct invalid inputs
    if algorithm.size > 20:
        algorithm.size = 20
    elif algorithm.size <= 0:
        algorithm.size = 10
        
    # Generate the random array
    algorithm.data = algorithm.generate_random_array()
    
    # call draw which displays the items in the array
    draw(algorithm, canvas, ['orange' for x in range(len(algorithm.data))])
    
def draw(algorithm, canvas, color_list):
    
    # Remove items in the canvas to draw on top of them
    canvas.delete("all")
    #create an output screen
    bar_height = 350
    width = 600
    offset = 20
    spacing = 10
    bar_width = width / (len(algorithm.data) + 1)
     
    # Unnecessary but makes differences between values easier to see
    normalized_data = [i / max(algorithm.data) for i in algorithm.data]
 
    # Iterate over list of normalized data
    for i, height in enumerate(normalized_data):
        
        # create_rectangle needs positions of two opposite
        # corners to draw a rectange so calculate based on canvas size
        x = i * (bar_width) + offset + spacing
        y = bar_height - height * 300
        x1 = (i + 1) * (bar_width) + offset
        y1 = bar_height
        
        # Draw the rectangles
        canvas.create_rectangle(x, y, x1, y1, fill = color_list[i])
        canvas.create_text(x, y, anchor=SW, text=str(algorithm.data[i]))
        
    # Update each time an item is moved so that the user can see when an item in the array is moved
    root.update()
    canvas.place(rely=.30, relx=.15)
     
def Animate(algorithm, canvas, alg_speed, type_algorithm):
    algorithm.name = type_algorithm.get()
    
    if algorithm.name == "Insertion Sort":
        algorithm.animate_insertion(canvas, draw, alg_speed)
        
    elif algorithm.name == "Bubble Sort":
        algorithm.animate_bubble(canvas, draw, alg_speed)
        
    elif algorithm.name == "Quick Sort":
        array = algorithm.data
        algorithm.animate_quick(canvas, draw, alg_speed, 0, len(array)-1)
    
    
    
    
LARGE_FONT = ("Times New Roman", 17)
root = GUI_Driver()
root.title("Introduction To Basic Programming Concepts")
root.geometry("900x700")
root.mainloop()

        
        
