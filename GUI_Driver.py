import tkinter as tk
from tkinter import ttk
from tkinter import *
from Algorithm import Algorithm
import random


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
        
        for F in (Tutorial, StartScreen, Algorithm_Visualizer):
            # screen on start
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(StartScreen)
        
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
        
# this is a new page        
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
        entrysize.pack()

        min_value = 20
        max_value = 200
        data = []
        chosen_algorithm = Algorithm(type_algorithm.get(), 10, min_value, max_value, data)
        
        # Slider to allow user to adjust playback speed
        speed = tk.Label(algorithm_frame, text = "Playback Speed")
        speed.pack()

        alg_speed = Scale(algorithm_frame, from_= 0.0, to = 3.0, length = 200, digits = 2, resolution = 0.1, orient = HORIZONTAL)
        alg_speed.place(relx = 0.5, rely = .95, anchor = CENTER)
        
        canvas = Canvas(self, width=600, height=350, bg='snow2')
        create_array = tk.Button(self, text="Create New Array", command=lambda:Generate(chosen_algorithm, entrysize, canvas), bg='orange')
        create_array.pack()
        
        start_visualizing = tk.Button(self, text="Animate", command = lambda:Animate(chosen_algorithm, canvas, alg_speed, type_algorithm), width = 13)
        start_visualizing.pack()
        
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
    canvas.pack()
     
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

        
        