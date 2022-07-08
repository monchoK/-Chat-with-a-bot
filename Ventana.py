from tkinter import *
from main import chat, entrenador, ListTrainer
from tkinter import messagebox as mb
class Ventana(Frame):
    def __init__(self,master=None):
        super().__init__(master,width=800,height=500)
        self.master=master
        self.pack()
        self.crear_widgets()

    def agregar(self):
        self.pregunta1 =self.entradapregunta.get()
        self.respuesta1=self.entradarespuesta.get()
        f =open("charla.txt","a")
        f.write("\n")
        f.write(self.pregunta1)
        f.write("\n")
        f.write(self.respuesta1)
        f.close()
        while True:
            self.guardar=open("charla.txt","r").readlines()
            entrenador=ListTrainer(chat)
            entrenador.train(self.guardar)
            break
        
        self.entradapregunta.delete(0,END)
        self.entradarespuesta.delete(0,END)
        mb.showinfo("FELICIDADES","SE REGISTRO TU PREGUNTA Y RESPUESTA ")
        mb.configurate(bg="pink")



    def chatear(self):
        self.nuevacharla = self.entradachat.get()
        self.listachat.insert(END,"TU: ",self.nuevacharla)
        while True:
            self.peticion = self.nuevacharla
            self.respuesta= chat.get_response(self.peticion)
            self.listachat.insert(END,"BOT: ", self.respuesta)
            break
        self.entradachat.delete(0,END)
    def crear_widgets(self):
        #CREAMOS FRAME DE AGREGAR PREGUNTAS
        frame1=Frame(self,bg="#BBFD75",relief="groove",bd=7)
        frame1.place(x=0,y=0,width=200,height=500)
        
        self.titulo =Label(frame1,text="AYUDA AL BOT A CONVERSAR! ",font=("CAMBRIA",10),bg="#BBFD75",anchor="center")
        self.titulo.place(x=0,y=0,width=180,height=40)

        self.texto1=Label(frame1,text="AGREGA UNA ORACIÓN ! ",font=("CAMBRIA",12),bg="#BBFD75",anchor="center")
        self.texto1.place(x=0,y=60,width=180,height=40)
        self.emoji1 =Label(frame1,text="☟☟☟ (≧◉◡◉≦) ☟☟☟",font=("cambria",12),bg="#BBFD75",anchor="center")
        self.emoji1.place(x=0,y=120,width=180,height=40)

        self.entradapregunta=Entry(frame1,relief="ridge",bd=7,bg="#CEFB9F")
        self.entradapregunta.place(x=10,y=180,width=160,height=40)

        self.texto2 =Label(frame1,text="AGREGA SU RESPUESTA! ",font=("CAMBRIA",12),bg="#BBFD75",anchor="center")
        self.texto2.place(x=0,y=240,width=180,height=40)
        self.emoji1 =Label(frame1,text="☟☟☟ (っ＾▿＾) ☟☟☟",font=("cambria",12),bg="#BBFD75",anchor="center")
        self.emoji1.place(x=0,y=300,width=180,height=40)

        self.entradarespuesta=Entry(frame1,relief="ridge",bd=7,bg="#CEFB9F")
        self.entradarespuesta.place(x=10, y=360,width=160,height=40)

        self.botonagregar=Button(frame1,text="AGREGAR",relief="raised",activebackground="#49BD49",bg="#CEFB9F",bd=7,command=self.agregar)
        self.botonagregar.place(x=10,y=420,width=160,height=40)

        #CREAMOS FRAME DE CHATBOT
        frame2 =Frame(self)
        frame2.place(x=199,y=0,width=600,height=500)

        #IMAGEN DE FONDO
        self.imagen=PhotoImage(file="fondopastel.gif")
        self.lblfondo=Label(frame2,image=self.imagen,relief="groove",bd=7,bg="#F6A5F9")
        self.lblfondo.place(x=0,y=0,width=599,height=499)
        
        self.entradachat=Entry(frame2,relief="ridge",bd=7,bg="#F9CAFB")
        self.entradachat.place(x=40,y=40,width=450,height=40)
        self.botonentradachat =Button(frame2,relief="raised",activebackground="#EE81B1",bg="#F9CAFB",bd=7,text="CHARLAR",command=self.chatear)
        self.botonentradachat.place(x=510,y=40,width=70,height=40)

        self.listachat =Listbox(frame2,relief="ridge",bd=7,bg="#F9CAFB")
        self.listachat.place(x=40,y=100,width=520,height=360)


