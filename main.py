from tkinter import *
from Ventana import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer  #EL LIST TRAINER ES PARA HACER MI DICCIONARIO CON PALABRAS

chat = ChatBot("chatvr")
chat.storage.drop()
charla2 = open("charla.txt","r").readlines()
entrenador=ListTrainer(chat)
entrenador.train(charla2)

def main():
    root=Tk()
    root.title("KAB")
    root.iconbitmap("robot icon.ico")
    app=Ventana(root)
    app.mainloop()

if __name__=="__main__":
    main()