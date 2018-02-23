from Tkinter import *

class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)                 
		self.master = master
		self.init_window()
        
    #Creation of init_window
	def init_window(self):
		# changing the title of our master widget      
		self.master.title("3D Transformation")

		# allowing the widget to take the full space of the root window
		self.pack(fill=BOTH, expand=1)

		self.canvas = Canvas(self, width=768, height=561)
		self.canvas.pack(fill="both", expand="yes")
		self.rect = self.canvas.create_rectangle(50, 25, 150, 75, fill="blue")

		self.guiPanel = LabelFrame(self)
		self.guiPanel.pack(fill="both", expand="yes")

		self.cubePanel = LabelFrame(self.guiPanel, text="Cube Controls")
		self.cubePanel.pack(fill="both", expand="yes", side=LEFT)

		self.vertex = Button(self.cubePanel, text="Vertex").place(relx=0.0, rely=0.5, anchor=W)
		self.edge = Button(self.cubePanel, text="Edge").place(relx=0.3, rely=0.5, anchor=CENTER)
		self.face = Button(self.cubePanel, text="Face").place(relx=0.5, rely=0.5, anchor=CENTER)
		self.zSlider = Scale(self.cubePanel, from_=-50, to=50, orient=HORIZONTAL, showvalue=False).place(relx=1.0, rely=0.5, anchor=E)

		self.camPanel = LabelFrame(self.guiPanel, text="Camera Controls")
		self.camPanel.pack(fill="both", expand="yes", side=RIGHT)

		self.top = Button(self.camPanel, text="Top").place(relx=0.0, rely=0.5, anchor=W)
		self.front = Button(self.camPanel, text="Front").place(relx=0.5, rely=0.5, anchor=CENTER)
		self.camSlider = Scale(self.camPanel, from_=0, to=100, orient=HORIZONTAL, showvalue=False).place(relx=1.0, rely=0.5, anchor=E)
# 		placing the button on my window

root = Tk()

#size of the window
root.geometry("896x693")

app = Window(root)

root.mainloop()