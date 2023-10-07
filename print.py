from pytube import YouTube
from tkinter import *
from tkinter import messagebox as Messagebox

def accion():
    enlace=videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

def popup():
    Messagebox.showinfo("Sobre mi","Enlace a mi perfil....")  
     


root = Tk()
root.config(bd=15)
root.title("Descargador de youtube")

imagen = PhotoImage(file="youtube.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para Mas Informacion", menu=helpmenu)
menubar.add_command(label="Informacion del autor", command=popup)
menubar.add_command(label="salir", command=root.destroy)

instrucciones = Label(root, text="Programa para descargar video de youtube")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Descargar :)", command=accion)
boton.grid(row=2, column=1)

root.mainloop()