"""Referências:
        Calculadora: https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
        Playlist: https://www.youtube.com/playlist?list=PLqx8fDb-FZDFznZcXb_u_NyiQ7Nai674-
"""


"""from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()"""

"""from tkinter import *

class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

        self.fnameLabel = Label(master, text="First Name")
        self.fnameLabel.grid()

        self.fnameEntry = StringVar()
        self.fnameEntry = Entry(textvariable=self.fnameEntry)
        self.fnameEntry.grid()

        self.lnameLabel = Label(master, text="Last Name")
        self.lnameLabel.grid()

        self.lnameEntry = StringVar()
        self.lnameEntry = Entry(textvariable=self.lnameEntry)
        self.lnameEntry.grid()

        def buttonClick():
            print("You pressed Submit!")
            print(self.fnameEntry.get() + " " + self.lnameEntry.get() +",ou clicked the button!")

        self.submitButton = Button(master, text="Submit", command=buttonClick)
        self.submitButton.grid()

guiFrame = GUI()
guiFrame.mainloop()"""


from tkinter import *

class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

        #Definindo os CAMPOS na interface
        #Obtem o numero de entrada
        self.EntradaLabel = Label(master, text="Insira o número: ")
        self.EntradaLabel.grid(column=0, row=0)
        self.Entrada = StringVar()
        self.Entrada = Entry(textvariable=self.Entrada)
        self.Entrada.grid(column=0, row=1)
        
        #Apresenta o resultado na tela
        self.resultadoLabel = Label(master, text="Resultado")
        self.resultadoLabel.grid(column=0, row=2)
        self.Resultado = StringVar()
        self.Resultado = Entry(textvariable=self.Resultado)
        self.Resultado.grid(column=0, row=3)

        #Definindo o COMPORTAMENTO dos botões
        def buttonClick_Fatorial():
            print("You pressed Fatorial!")
            
            numero = int(self.Entrada.get())
            resultado_obtido = self.fatorial(numero)

            #Atualiza as informações do campo "Resultado"
            self.Resultado.delete(0,END) #Limpa o conteudo do campo
            self.Resultado.insert(0, str(resultado_obtido)) #Adiciona o novo conteúdo
        
        def buttonClick_Potencia():
            print("You pressed Potencia!")
            
            numero = int(self.Entrada.get())
            resultado_obtido = self.potencia(numero)

            #Atualiza as informações do campo "Resultado"
            self.Resultado.delete(0,END) #Limpa o conteudo do campo
            self.Resultado.insert(0, str(resultado_obtido)) #Adiciona o novo conteúdo
        
        #Definindo os botões na interface
        self.submitButton = Button(master, text="Fatorial", command=buttonClick_Fatorial)
        self.submitButton.grid(column=0, row=4)

        self.submitButton = Button(master, text="Potencia", command=buttonClick_Potencia)
        self.submitButton.grid(column=1, row=4)
    
    def fatorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.fatorial(n - 1)
    
    def potencia(self, n):
        return n ** 2

#Chamada principal
guiFrame = GUI()
guiFrame.mainloop()