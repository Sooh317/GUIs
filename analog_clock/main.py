import tkinter as tk
import math
import time

class MyFrame(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.size = 200
        self.clock = tk.Canvas(self, width=self.size, height= self.size, background='white')
        self.clock.grid(row=0, column=0)

        self.font_size = int(self.size/15)
        for i in range(1, 12 + 1):
            x = self.size/2 + math.cos(math.radians(-i * 30 + 90))*(self.size/2)*0.85
            y = self.size/2 - math.sin(math.radians(-i * 30 + 90))*(self.size/2)*0.85
            self.clock.create_text(x, y, text=str(i), fill='black', font=('arial', 14))
        
        self.sec = time.localtime().tm_sec
        self.min = time.localtime().tm_min
        self.hour = time.localtime().tm_hour

    def display(self):

        x0, y0 = self.size/2, self.size/2
        
        self.sec = time.localtime().tm_sec
        angle = math.radians((self.sec/60)*360 - 90)
        x, y = self.create_clock_hands(angle, 0)
        self.clock.delete('SEC')
        self.clock.create_line(x0, y0, x, y, width=1, fill='red', tag='SEC')

        self.min = time.localtime().tm_min
        angle = math.radians((self.min/60)*360 - 90)
        x, y = self.create_clock_hands(angle, 1)
        self.clock.delete('MIN')
        self.clock.create_line(x0, y0, x, y, width=1, fill='blue', tag='MIN')

        self.hour = time.localtime().tm_hour
        angle = math.radians((self.hour%12)*30 + (self.min/60)*30 - 90)
        x, y = self.create_clock_hands(angle, 2)
        self.clock.delete('HOUR')
        self.clock.create_line(x0, y0, x, y, width=1, fill='green', tag='HOUR')

        self.after(100, self.display)
        

    def create_clock_hands(self, angle, id):
        if id == 0:
            x = self.size/2 + math.cos(angle)*(self.size/2)*0.7
            y = self.size/2 + math.sin(angle)*(self.size/2)*0.7
        elif id == 1:
            x = self.size/2 + math.cos(angle)*(self.size/2)*0.65
            y = self.size/2 + math.sin(angle)*(self.size/2)*0.65
        else:
            x = self.size/2 + math.cos(angle)*(self.size/2)*0.4
            y = self.size/2 + math.sin(angle)*(self.size/2)*0.4
        return x, y


root = tk.Tk()
f = MyFrame(root)
f.pack()
f.display()
root.mainloop()


