from tkinter import *
mywindow = Tk()
mywindow.geometry("300x600")
mywindow.title("Registro de usuarios")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "Registro de usuarios", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()

usuarioL = Label(text = "Nombre de control: ", bg = "#FFEEDD")
usuarioL.place(x = 22, y = 70)
nombreL = Label(text = "Nombre: ", bg = "#FFEEDD")
nombreL.place(x = 22, y = 130)
apellidoPL = Label(text = "Apellido Paterno: ", bg = "#FFEEDD")
apellidoPL.place(x = 22, y = 190)
apellidoML = Label(text = "Apellido Materno: ", bg = "#FFEEDD")
apellidoML.place(x = 22, y = 250)
edadL = Label(text = "Edad: ", bg = "#FFEEDD")
edadL.place(x = 22, y = 310)
curpL = Label(text = "Curp: ", bg = "#FFEEDD")
curpL.place(x = 22, y = 370)
correoL = Label(text = "Correo: ", bg = "#FFEEDD")
correoL.place(x = 22, y = 430)
contraseñaL = Label(text = "Contraseña: ", bg = "#FFEEDD")
contraseñaL.place(x = 22, y = 480)
 
usuarioE = Entry(width = "40")
nombreE = Entry(width = "40",  show = "*")
apellidoPE = Entry( width = "40")
apellidoML = Entry(width = "40")
edadE = Entry(width = "40")
curpE = Entry(width = "40",  show = "*")
correoE = Entry( width = "40")
contraseñaE = Entry(width = "40")
 
usuarioE.place(x = 22, y = 100)
nombreE.place(x = 22, y = 160)
apellidoPE.place(x = 22, y = 220)
apellidoML.place(x = 22, y = 280)
edadE.place(x = 22, y = 340)
curpE.place(x = 22, y = 400)
correoE.place(x = 22, y = 455)
contraseñaE.place(x = 22, y = 510)
 
submit_btn = Button(mywindow,text = "Registrar", width = "30", height = "2", bg = "#00CD63")
submit_btn.place(x = 40, y = 540)

mywindow.mainloop()


