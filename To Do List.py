import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import threading

window = Tk() #initiating window
window.geometry("465x450") #resulotion 
window.title("To Do List") #title
window.resizable(False, False) #*fixed resulotion*
# icon = PhotoImage(file='To_Do_list.png') #initiating app icon
# window.iconphoto(True, icon) #displaying icon


directory = "ToDo-List"
parent_dir = "C:\\"
folder = os.path.join(parent_dir, directory) 
if not(os.path.exists(folder)):#create directory if not exist
    os.mkdir(folder) 
active_tasks = os.path.join(folder, 'active-tasks.txt')
finished_tasks = os.path.join(folder, 'finished-tasks.txt')
if not(os.path.isfile(active_tasks)):
    with open(active_tasks, 'w'):
        pass
if not(os.path.isfile(finished_tasks)):
    with open(finished_tasks, 'w'):
        pass

def reset_app():
    #Reset the app
    cfile = open(active_tasks,'w')
    cfile.write('')
    cfile.close()

    ffile = open(finished_tasks,'w')
    ffile.write('')
    ffile.close()
    listbox_tasks.delete(0, END)
    listbox_deleted_tasks.delete(0, END)
    writing_screen.delete(0, END)
    writing_screen.config(state='disabled', disabledbackground='lightgray')
def quit_app():
    #Exit app
    window.quit()
def open_screen():
    writing_screen.config(state='normal') #disabling entry
    #would be cool if we created an Easter Egg


def inserting_tab1():
    readfile = open(active_tasks,'r')
    tasks_list = readfile.readline()
    readfile.close()
    tasks_list = tasks_list.split(',')
    tasks_list = list(filter(None, tasks_list))
    tasks_list.reverse()
    listbox_tasks.delete(0, END)#clearing listbox
    for i in tasks_list:
        listbox_tasks.insert(0, i)#inserting_tab1 items in listbox
    tasks_list = []

def inserting_tab2():
    d_readfile = open(finished_tasks,'r')
    deleted_tasks_list = d_readfile.readline()
    d_readfile.close()
    deleted_tasks_list = deleted_tasks_list.split(',')
    deleted_tasks_list = list(filter(None, deleted_tasks_list))
    deleted_tasks_list.reverse()
    listbox_deleted_tasks.delete(0, END)
    for i in deleted_tasks_list:
        listbox_deleted_tasks.insert(0, i)
    deleted_tasks_list = []
    
def add_task():
    if writing_screen.get() == '' or writing_screen.get() == ',':
        return
    writing_file = open(active_tasks,'a')
    writing_file.write(writing_screen.get() + ',')
    writing_file.close()
    inserting_tab1()
    writing_screen.delete(0, END)
    writing_screen.config(state='disabled', disabledbackground='lightgray')
   

def delete_task():
    try:
        index = listbox_tasks.curselection()
        deleting_file = open(active_tasks,'r')
        tasks_list = deleting_file.readline()
        deleting_file.close()
        tasks_list = tasks_list.split(',')
        tasks_list = list(filter(None, tasks_list))
        writing_file = open(finished_tasks, 'a')
        writing_file.write(tasks_list[index[0]] + ',')
        writing_file.close()
        del tasks_list[index[0]]
        deleting_file = open(active_tasks,'w')
        for i in tasks_list:
            deleting_file.write(i + ',')
        deleting_file.close()
        inserting_tab1()
        inserting_tab2()
    except IndexError:
        messagebox.showwarning("Error 305", "You didn't select any task to delete يابقري")
        writing_screen.delete(0, END)
        writing_screen.config(state='disabled', disabledbackground='lightgray')

menubar = Menu(window)
window.config(menu=menubar)
option_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Option", menu=option_menu)
option_menu.add_command(label="Reset App", command=reset_app)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=quit_app)

notebook = ttk.Notebook(window) #initiating Tabs
tab1 = Frame(notebook) #frame to host widget
tab2 = Frame(notebook) #frame to host widget
notebook.add(tab1,text=('Tab 1')) #initiating Tab 1
notebook.add(tab2,text=('Tab 2')) #initiating Tab 2
notebook.pack() #displaying Tabs

Label(tab1, text=('~~To-Do List~~'), font=('Constantia', 19, 'bold')).pack(side=TOP)
Label(tab2, text=('Finished Tasks :'), font=('Constantia', 19, 'bold')).pack(side=TOP)

listbox_deleted_tasks = Listbox(tab2, width=35, height=18, bd=2, bg='lightgray',font=('Constantia', 15))
listbox_deleted_tasks.pack(padx=30, pady=10, side=TOP)
listbox_tasks = Listbox(tab1, width=35, height=13, bd=6, font=('Constantia', 15))
listbox_tasks.pack(padx=30, pady=10, side=TOP)

organizing_btns = Frame(tab1)
plus_btn = Button(organizing_btns,text="+",font=("Arial", 12), bg= '#14a803', command=open_screen)
writing_screen = Entry(organizing_btns, bd  =2, font=("Arial",15))
enter_btn = Button(organizing_btns,text="Enter",font=("Arial",12), command=add_task)
# del_btn = PhotoImage(file = "x.png")
# del_btn = del_btn.subsample(15,15)
del_task = Button(organizing_btns,text=" Finish", font=("Arial",12), compound='left', command=delete_task)
organizing_btns.pack(side=BOTTOM)
plus_btn.pack(padx=3, side=LEFT)
writing_screen.pack(ipadx=3, side=LEFT); writing_screen.config(state='disabled', disabledbackground="lightgray")
enter_btn.pack(padx=3, side=LEFT)
del_task.pack(padx=3, side=RIGHT)

inserting_tab1()
inserting_tab2()

window.mainloop()