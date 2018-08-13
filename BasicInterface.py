# some imports
import tkinter as tk
import SpeechInterface as SI

class GUI:
	"""
	very simple user interface class
	"""

	def __init__(self, master):
		"""
		creates an interface consisting of 
		two buttons - quit and record
		
		Args:
			master: of type Tk. Parent UI element
		"""
		
		self.master = master
		master.title("Simple User-Interface")

		self.close_button = tk.Button(master, text="QUIT", command=self.master.quit)
		self.close_button.pack()

		self.record_button = tk.Button(master, text="RECORD", command=self.run_recording)
		self.record_button.pack()
		
	def run_recording(self):
		"""
		calls the recording routine
		"""
		SI.record_voice()

# initialize command to none
with open("command_file.txt", "w") as command_file:	
	command_file.write('none')

# initialize UI
root = tk.Tk()
frame = GUI(root)

# run
root.mainloop()