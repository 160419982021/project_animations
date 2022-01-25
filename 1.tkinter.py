import tkinter as tk

window = tk.Tk() #object that is root window
window.title('Tkinter Hello World')

text = tk.Label(text = "What's your name?", foreground = 'white', background = 'blue', width = 30, height = 3)
#text2 = tk.Label(text = 'Welcome to the Interface from Python')
#text3 = tk.Label(text = 'First try which you can see')

text.pack()
#text2.pack()
#text3.pack()

entry = tk.Entry(width = 30)
entry.pack()

def save_and_print():
    name = entry.get() #denis, type 'string'
    entry.delete(0, tk.END)
    print (name)

button = tk.Button(text = 'Submit', width = 30, height = 5, command = save_and_print)
button.pack(padx = 5, pady = 5)

window.blind('<Return>', command = save_and_print)
#window.blind('<Return>', lambda event:save_and_print()) #if func need parameters

print(text.configure().keys())
window.mainloop() #start event loop, method on top of 'window'
