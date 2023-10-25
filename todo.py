#---------------- ATHTHANAYAKA MUDALIGE Mahen ------------------------------------

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import json

#functions 

def updateView():
    tasksShowed = []
    for taskONE in tasks:
        tasksShowed.append(str(taskONE["num"]) + " - " + taskONE["taskName"] + " - " + taskONE["done"]) 
    taskCombobox['values'] = tasksShowed
    taskCombobox.current(0)

def addTask():
    try:
        test = int(addTaskEntry.get())
        tkinter.messagebox.showwarning("WARNING", "il n'y a que des nombres !")
    except ValueError:
        task = {"taskName": addTaskEntry.get(), "done": "NOT DONE", "num": len(tasks)}
        tasks.append(task)
        updateView()
        tkinter.messagebox.showinfo("Tâche ajoutée", f"La tâche [{addTaskEntry.get()}] est ajoutée")

def suppTask():
    try:
        deletedIndex = int(taskUpdateDeleteEntry.get())
        if(deletedIndex > len(tasks) or deletedIndex < 0):
            tkinter.messagebox.showwarning("WARNING", "Le numéro n'est pas correct")
        else:
            tkinter.messagebox.showinfo("Tâche supprimée", f"La tâche [{tasks[deletedIndex]['taskName']}] est supprimée")
            tasks.pop(deletedIndex)
            updateView()
    except ValueError:
        tkinter.messagebox.showerror("ERROR", "Ce n'est pas un numéro")


def updateTask():
    try:
        updateIndex = int(taskUpdateDeleteEntry.get())
        if(updateIndex > len(tasks) or updateIndex < 0):
            tkinter.messagebox.showwarning("WARNING", "Le numéro n'est pas correct")
        else:
            tasks[updateIndex]["done"] = "DONE ✔" 
            updateView()
            tkinter.messagebox.showinfo("Tâche mis à jour", f"La tâche [{tasks[updateIndex]['taskName']}] est terminé !")

    except ValueError:
        tkinter.messagebox.showerror("ERROR", "Ce n'est pas un numéro")

def saveTask():
    with open("data.json", "w") as json_file:
        json.dump(tasks, json_file)
    tkinter.messagebox.showinfo("Tâches sauvegarde", "Les tâches sont maintenant sauvegardée !")

def loadTask():
    global tasks
    with open("data.json", "r") as json_file:
        tasks = json.load(json_file)
        updateView()
    tkinter.messagebox.showinfo("Tâches Chargé", "Les tâches sont maintenant chargée !")


#init fenetre
fenetre = tk.Tk()
fenetre.title("To Do Launcher")
fenetre.geometry("800x500")


#DESIGN
paddings = {'padx': 5, 'pady': 5}
font_T = ("Helvetica", 12)
width_E = 25
width_C = 40
width_B = 20
#list of task
tasks = []


#adding task
addTaskLabel = tk.Label(fenetre, text="Ajouter une tâche", font=font_T)
addTaskEntry = tk.Entry(fenetre,font=font_T, width=width_E)
addTaskButton = tk.Button(fenetre, text="Ajouter", command= addTask,font=font_T)
addTaskLabel.grid(row=0, column=0, **paddings)
addTaskEntry.grid(row=0, column=1, **paddings)
addTaskButton.grid(row=0, column=2, **paddings)



# delete / update task
taskUpdateDeleteLabel = tk.Label(fenetre, text="Mettre à jour / Supprimer une tâche ",font=font_T)
taskUpdateDeleteEntry = tk.Entry(fenetre,font=font_T, width=width_E)
deleteTaskButton = tk.Button(fenetre, text="supprimer", command= suppTask,font=font_T)
updateTaskButton = tk.Button(fenetre, text="terminer", command= updateTask,font=font_T)
taskUpdateDeleteLabel.grid(row=1, column=0, **paddings)
taskUpdateDeleteEntry.grid(row=1, column=1, **paddings)
deleteTaskButton.grid(row=1, column=2, **paddings)
updateTaskButton.grid(row=1, column=3, **paddings)


#comboBox (liste deroulante)
taskCombobox = ttk.Combobox(fenetre, values="No_TASK",font=font_T,width=width_C)
taskCombobox.current(0)
taskCombobox.grid(row=2, column=0, columnspan=3, **paddings)

saveButton = tk.Button(fenetre, text="Sauvegarder les tâches", command=saveTask,font=font_T)
saveButton.grid(row=3, column=0, **paddings)
loadButton = tk.Button(fenetre, text="Charger les tâches", command=loadTask,font=font_T)
loadButton.grid(row=3, column=2, **paddings)



fenetre.mainloop()