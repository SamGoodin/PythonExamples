import tkinter as tk
from tkinter.constants import NORMAL


class gui:
    
    def __init__(self):
        # initialize the window
        self.window = tk.Tk(className=' Window Title')
    
        # set the window size
        self.window.geometry("300x300")
        
        # set the window icon
        #self.window.iconbitmap("icon.ico")
        #self.window.iconphoto(False, tk.PhotoImage(file='hidden leaf.png'))
        self.window.tk.call('wm', 'iconphoto', self.window._w, tk.PhotoImage(file='hidden leaf.png'))
        
        # bind keypress check to the window
        self.window.bind("<Shift-Q>", self.handle_exit)
        
        # creates arbitrary list of widgets to keep track of
        self.widgets = []
        
        # creates text widget
        message = tk.Label(text="Hello, GUI")
        # adds widget to screen and sizes window to widget
        # message.pack()
        self.widgets.append(message)
        
        # creates button widget
        buttonA = tk.Button(
            text="Button Press",
            width=25,
            height=5,
            bg="red",
            fg="black",
            command=self.buttonPress)
        #buttonA.pack()
        self.widgets.append(buttonA)
        
        buttonB = tk.Button(
            text="Print input from text box",
            width=25,
            height=5,
            bg='blue',
            fg='black')
        # binds left mouse press (<Button-1>) to the button
        buttonB.bind("<Button-1>", self.handle_buttonpress)
        self.widgets.append(buttonB)
        
        # creates entry field widget
        self.entry = tk.Entry(
            master=self.window,
            fg="black",
            bg="white",
            width=500,
            state=NORMAL)
        self.entry.bind("<Key>", self.handle_keypress)
        self.widgets.append(self.entry)
        
        # adds all widgets to the screen
        for widget in self.widgets:
            widget.pack()
        
        # starts Tkinter event loop 
        # -must add widgets before executing
        self.window.mainloop()
        
    # buttonpress function using command arg
    def buttonPress(self):
        print("Button pressed")
        
    # buttonpress function using bind
    def handle_buttonpress(self, event):
        print("Button Press event detected: " + repr(event))
        print("Input in text box: " + self.entry.get())
    
    # keypress function
    def handle_keypress(self, event):
        print("Key Press event detected: " + event.keysym)
    
    # exit function
    def handle_exit(self, event):
        print("Exit Key Press event detected: Shift + " + event.keysym)
        # destroy to quit mainloop and exit
        # -quit() method exits without quitting mainloop
        print("Exiting window...")
        self.window.destroy()
        print("Exiting program...")

if __name__ == '__main__':
    import sys
    sys.exit(gui())