 #
 #
 #   @author
 #
 #   Aakash Verma
 #   http://aboutaakash.in
 #
 #
 #


# importing tkinter library

from tkinter import *

# utility font

font = ("Verdana", 14)
bigFont = ('Verdana', 20, 'bold')

window = Tk()
window.title("Case Convertor")
window.geometry('450x500')
window.configure(bg='navyblue')


def lowerToUpper():
    expression = textArea1.get("1.0","end-1c")
    expression = expression.upper()
    textArea2.delete("1.0","end-1c")
    textArea2.insert('1.0', expression)


def upperToLower():
    expression = textArea1.get("1.0","end-1c")
    expression = expression.lower()
    textArea2.delete("1.0", "end-1c")
    textArea2.insert('1.0', expression)


heading1 = Label(window, text="Enter your text:", font = bigFont, bg='navyblue', foreground='aliceblue')
heading1.pack(side=TOP, pady=10)

textArea1 = Text(window, font = font, height = 5, bg='aliceblue', foreground='black')
textArea1.pack(side=TOP, padx = 10, pady = 20)

heading2 = Label(window, text="Your converted text:", font = bigFont, bg='navyblue', foreground='aliceblue')
heading2.pack(side=TOP, pady=5)

textArea2 = Text(window, font = font, height = 5, bg='aliceblue', foreground='black')
textArea2.pack(side=TOP, padx = 10, pady = 20)


frame = Frame(window)
frame.pack(side=TOP)

button1 = Button(frame, text="UCase to LCase", font=bigFont, width=13, height=2, foreground='navyblue', command=upperToLower)
button1.grid(row=0, column=0, padx=3, pady=3)

button2 = Button(frame, text="LCase to UCase", font=bigFont, width=13, height=2, foreground='navyblue', command=lowerToUpper)
button2.grid(row=0, column=1, padx=3, pady=3)


window.mainloop()
