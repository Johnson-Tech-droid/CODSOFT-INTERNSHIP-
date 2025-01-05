import tkinter
from tkinter import *

root = Tk()
root.title("TO-DO-List")
root.geometry("400x600+400+100") 
root.resizable(False, False)

task_list = []

root.config(bg="#2c3e50") 
heading = Label(root, text="To-Do List", font=("Helvetica", 24, "bold"), fg="#ecf0f1", bg="#2c3e50")
heading.pack(fill=X, pady=10)

frame = Frame(root, width=400, height=50, bg="#34495e")
frame.place(x=0, y=50)

task = StringVar()
task_entry = Entry(frame, textvariable=task, width=20, font=("Helvetica", 14), bd=0, bg="#ecf0f1", fg="#2c3e50")
task_entry.place(x=10, y=10)

def add_task():
    task_text = task.get()
    if task_text != "":
        listbox.insert(END, task_text)
        task_list.append(task_text)
        task.set("")
    else:
        print("No task entered")

add_button = Button(frame, text="ADD", font=("Helvetica", 14, "bold"), width=6, bg="#1abc9c", fg="#ecf0f1", bd=0, command=add_task)
add_button.place(x=270, y=7)

frame1 = Frame(root, bd=3, width=380, height=320, bg="#2c3e50")
frame1.place(x=10, y=120)

listbox = Listbox(frame1, font=("Helvetica", 14), width=38, height=16, bg="#34495e", fg="#ecf0f1", cursor="hand2", selectbackground="#1abc9c")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task = selected_task_index[0]
        listbox.delete(selected_task)
        task_list.pop(selected_task)
    else:
        print("No task selected")

delete_button = Button(root, text="DELETE", font=("Helvetica", 14, "bold"), width=10, bg="#e74c3c", fg="#ecf0f1", command=delete_task)
delete_button.place(x=140, y=500)

root.mainloop()
