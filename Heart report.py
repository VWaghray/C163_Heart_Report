from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("600x600")
root.title("Heart report")

q1rb = StringVar(value="0")
q1 = Label(root, text="Do you have shortness of breath during routine activities?")
q1.pack()
q1r1 = Radiobutton(root, text="Yes", variable=q1rb, value = "yes")
q1r1.pack()
q1r2 = Radiobutton(root, text="No", variable=q1rb, value = "no")
q1r2.pack()

q2rb = StringVar(value="0")
q2 = Label(root, text="Do you have swelling in the feet/ankles/legs ar abdomen")
q2.pack()
q2r1 = Radiobutton(root, text="Yes", variable=q2rb, value = "yes")
q2r1.pack()
q2r2 = Radiobutton(root, text="No", variable=q2rb, value = "no")
q2r2.pack()

q3rb = StringVar(value="0")
q3 = Label(root, text="Do you have any of the symptoms - confusion, disorientation, or loss of memory?")
q3.pack()
q3r1 = Radiobutton(root, text="Yes", variable=q3rb, value = "yes")
q3r1.pack()
q3r2 = Radiobutton(root, text="No", variable=q3rb, value = "no")
q3r2.pack()

q4rb = StringVar(value="0")
q4 = Label(root, text="Do you experience shortness of breath while resting/lying down?")
q4.pack()
q4r1 = Radiobutton(root, text="Yes", variable=q4rb, value = "yes")
q4r1.pack()
q4r2 = Radiobutton(root, text="No", variable=q4rb, value = "no")
q4r2.pack()

q5rb = StringVar(value="0")
q5 = Label(root, text="Do you experience persistent weezing/coughing that produces white or pink blood tinged muscles?")
q5.pack()
q5r1 = Radiobutton(root, text="Yes", variable=q5rb, value = "yes")
q5r1.pack()
q5r2 = Radiobutton(root, text="No", variable=q5rb, value = "no")
q5r2.pack()

def heart():
    score =  0
    if q1rb.get()=="yes":
        score = score+20
        print(score)
    if q2rb.get()=="yes":
        score = score+20
        print(score)
    if q3rb.get()=="yes":
        score = score+20
        print(score)
    if q4rb.get()=="yes":
        score = score+20
        print(score)
    if q5rb.get()=="yes":
        score = score+20
        print(score)
        
    if score <= 20:
        messagebox.showinfo("Report", "You don't need to see a doctor 🙂")
    elif score > 20 and score <= 60:
        messagebox.showinfo("Report", "You might need to see a doctor 😐")
    else:
        messagebox.showinfo("Report", "I strongly advise you to see a doctor 😭")

btn = Button(root, text="Click Me", command = heart)
btn.pack()
root.mainloop()


