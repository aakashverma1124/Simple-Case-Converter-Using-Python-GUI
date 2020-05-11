from tkinter import *
from tkinter.messagebox import *

font = ("Verdana", 22, 'bold')

def buttonClick(event):
    b = event.widget
    text = b["text"]

    if(text == '='):
        try:
            expression = textField.get()
            answer = eval(expression)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            showerror('Error', e)
        return

    textField.insert(END, text)

def allClear():
    textField.delete(0, END)

def clear():
    expression = textField.get()
    expression = expression[0: len(expression) - 1]
    textField.delete(0, END)
    textField.insert(0, expression)

window = Tk()
window.title("Calculator")
window.geometry("450x600")

pic = PhotoImage(file="img/technology.png")
headingLabel = Label(window, image=pic)
headingLabel.pack(side=TOP, pady=20)

headingTitle = Label(window, text="My Calculator", font = font )
headingTitle.pack(side=TOP, pady=10)

textField = Entry(window, font= font, justify=CENTER)
textField.pack(side=TOP, pady=10, fill=X, padx=20)

frame = Frame(window)
frame.pack(side=TOP)

btnValue=1
for row in range(3):
    for col in range(3):
        button = Button(frame, text=btnValue, font=font, width=5, height=2)
        button.grid(row=row, column=col, pady=3, padx=3)
        btnValue += 1
        button.bind('<Button-1>', buttonClick)


dotButton = Button(frame, text=".", font=font, width=5, height=2)
dotButton.grid(row=3, column=0, pady=3, padx=3)
dotButton.bind('<Button-1>', buttonClick)

zeroButton = Button(frame, text="0", font=font, width=5, height=2)
zeroButton.grid(row=3, column=1, pady=3, padx=3)
zeroButton.bind('<Button-1>', buttonClick)

equalButton = Button(frame, text="=", font=font, width=5, height=2)
equalButton.grid(row=3, column=2, pady=3, padx=3)
equalButton.bind('<Button-1>', buttonClick)

plusButton = Button(frame, text="+", font=font, width=5, height=2)
plusButton.grid(row=0, column=3, pady=3, padx=3)
plusButton.bind('<Button-1>', buttonClick)

minusButton = Button(frame, text="-", font=font, width=5, height=2)
minusButton.grid(row=1, column=3, pady=3, padx=3)
minusButton.bind('<Button-1>', buttonClick)

multiplyButton = Button(frame, text="*", font=font, width=5, height=2)
multiplyButton.grid(row=2, column=3, pady=3, padx=3)
multiplyButton.bind('<Button-1>', buttonClick)

divisionButton = Button(frame, text="/", font=font, width=5, height=2)
divisionButton.grid(row=3, column=3, pady=3, padx=3)
divisionButton.bind('<Button-1>', buttonClick)

clearButton = Button(frame, text="C", font=font, width=11, height=2, command=clear)
clearButton.grid(row=4, column=0, columnspan=2, pady=3, padx=3)

allClearButton = Button(frame, text="AC", font=font, width=11, height=2, command=allClear)
allClearButton.grid(row=4, column=2, columnspan=2, pady=3, padx=3)

window.mainloop()
