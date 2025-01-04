from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("To-Do-List ")
window.geometry("325x275")
window.configure(bg="white")
import random


tasks = []

#Functions for buttons
def update_task_list():
    clear_show_tasks()
    for task in tasks:
        show_tasks.insert("end", task)

def clear_show_tasks():
    show_tasks.delete(0, "end")
    global tasks

def add_task():
    task = user_import.get()
    if task !="":
        tasks.append(task)
        update_task_list()
    else:
        label_display["text"]="Please enter a task below."

    user_import.delete(0, "end")


def clear_all_tasks():
    confirm = messagebox.askyesno("Confirm", "Do you want to delete all?")
    if confirm == True:
            global tasks
            tasks.clear()
            update_task_list()


def delete():
    task = show_tasks.get("active")

    if task in tasks:
        tasks.remove(task)
        update_task_list()


def sort_asc():
    tasks.sort()
    update_task_list()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_task_list()

def random_task():
    task = random.choice(tasks)
    label_display["text"]=task
    update_task_list()


def exit_program():
    quit()



label_title =Label(window, text ="Welcome to To-Do-List", bg ="white")
label_title.grid(row=0,column=0)

label_display= Label(window, text="", bg="white" )
label_display.grid(row=0,column=1)

user_import =Entry(window, width=17, )
user_import.grid(row=1,column=1)

add_task_button = Button(window, text ="Add Task", bg ="white", command=add_task)
add_task_button.grid(row=1,column=0)

clear_all_button = Button(window, text = "Clear All Tasks ", bg ="white", command=clear_all_tasks)
clear_all_button.grid(row=2,column=0)

delete_button = Button(window, text ="Delete", bg ="white", command=delete)
delete_button.grid(row=3,column=0)

sort_asc_button = Button(window, text ="Sort Tasks in ASC ", bg ="white", command=sort_asc)
sort_asc_button.grid(row=4,column=0)

sort_desc_button = Button(window, text ="Sort Tasks in DESC ", bg ="white", command=sort_desc)
sort_desc_button.grid(row=5,column=0)

random_task_button = Button(window, text ="Choose random task", bg ="white", command=random_task)
random_task_button.grid(row=6,column=0)

exit_button = Button(window, text = "Exit", bg = "white", command= exit_program)
exit_button.grid(row=7,column=0)



show_tasks =Listbox(window)
show_tasks.grid(row=2,column=1, rowspan=7)









window.mainloop()