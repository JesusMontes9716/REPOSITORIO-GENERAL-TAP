#App para convertir pies a metros usando Tkinter
#JESUS MONTES
#23/02/2023

from tkinter import* # importar paquetes con todos los elementos
from tkinter import ttk # importar paquetes con ttk

class Conversor: 
    def __init__(self, raiz): # tipo constructor de la clase 
        raiz.title("PIES A METROS")

        self.pies = StringVar()
        self.metros = StringVar()

        #Padding(izquierda, arriba, derecha, abajo)
        mainFrame = ttk.Frame(raiz, padding="3 3 12 12")
        mainFrame.grid(column = 0, row = 0 )

        piesEntry = ttk.Entry(mainFrame,width=7, textvariable= self.pies)
        piesEntry.grid(column=1,row=0)

        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0)
        ttk.Label(mainFrame, text="Son equivalentes a").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)

        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2, row=2)
        
        piesEntry.focus()
        #Hacer operacion precionando Enter 
        raiz.bind("<Return>", self.calcular)

    def calcular(self, *args):

        print("Boton Precionado")
        piesUsuario = self.pies.get() #Siempre devuelve una cadena
        print("Pies ingresados: ", piesUsuario)
        try:
           piesFlotante = float(piesUsuario) #Conversion de cadena a flotante 
           metros = piesFlotante * 0.3048
           print("Metros: ", metros)
           self.metros.set(metros)
        except ValueError:
            print("NO ES UN DATO VALIDO")
            self.pies.set("")


if __name__=="__main__":
    print("Este es el archivo Principal.")
    print("Nada mas se mostrara esto si es el Pricipal")

