import tkinter as tk

import SpeechInterface as SI

with open("command_file.txt", "w") as command_file:	
	command_file.write('none')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="COMMAND",
                   command=SI.record_voice)
slogan.pack(side=tk.LEFT)##

root.mainloop()