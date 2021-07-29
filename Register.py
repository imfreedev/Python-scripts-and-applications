import os
import sys
import tkinter as tk


def filecreator():
    scene_dir()
    path = os.getcwd() + f"\{scene.get()}"
    reg = open(os.path.join(path, f"{scene.get()}-{inqua.get()} Take {take.get()}"), 'wb')
    aud = open(os.path.join(path, f"{scene.get()}-{inqua.get()} Audio {audio.get()}"), 'wb')


def scene_dir():
    path = os.getcwd() + f"\{scene.get()}"
    if not os.path.exists(path):
        os.mkdir(path)


def exitbutton():
    sys.exit()


def __maincore__():
    i = input("PRESS ENTER TO START")
    while i == "":
        #scene = input("Scena>")
        #inqua = input("Inquadratura>")
        #take = input("Take>")
        #audio = input("Audio>")
        i = input("PRESS ENTER TO CONFIRM")
        filecreator(scene,inqua,take,audio)

##### GUI #####

root = tk.Tk()
root.geometry("300x400")
root.title("Register")
root.grid_columnconfigure(0, weight=1)
root.resizable(False, False)

name_= tk.Label(root, text="Register", font=("Fixedsys", 32))
name_.grid(row=0, sticky="WE", padx=10, pady=10)

dir_label= tk.Label(root, text="Scena", font=("Calibri", 10))
dir_label.grid(row=1, sticky="WE", padx=10)

scene = tk.Entry(root)
#scene.insert(1, "Scena")
scene.grid(row=2, padx=10, sticky ="WE", pady=10)

file1_label= tk.Label(root, text="Inquadratura", font=("Calibri", 10))
file1_label.grid(row=3, sticky="WE", padx=10)

inqua = tk.Entry(root)
#inqua.insert(1, "Inquadratura")
inqua.grid(row=4, padx=10, sticky ="WE", pady=10)

file1_label= tk.Label(root, text="Take", font=("Calibri", 10))
file1_label.grid(row=5, sticky="WE", padx=10)

take = tk.Entry(root)
#take.insert(1, "Take")
take.grid(row=6, padx=10, sticky ="WE", pady=10)

file2_label= tk.Label(root, text="Audio", font=("Calibri", 10))
file2_label.grid(row=7, sticky="WE", padx=10)

audio = tk.Entry(root)
#audio.insert(1, "Audio")
audio.grid(row=8, padx=10, sticky ="WE", pady=10)

start_button = tk.Button(text="GENERATE", font=("Fixedsys"), command=filecreator)
start_button.grid(row=10, sticky="W", padx=10, pady=20)

rights_label= tk.Label(root, text="Created by Lorenzo Piarulli", font=("Calibri", 7))
rights_label.grid(row=11, sticky="NSE", padx=20, )
#filecreator(scene,inqua,take,audio)

if __name__ == "__main__":
    root.mainloop()

