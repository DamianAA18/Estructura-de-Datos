"""" 
Hecho por Aguileta Argueta Mario Damian
22 / 09 / 2025
"""
class CifradoCesar:
    def __init__(self):
        self.numenc=0 #numero para encriptacion (abreviatura de numenc)
        self.abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.texto = ""
        self.textoEncriptado = ""
        self.textoDesencriptado = ""
    def menu(self):
        self.opc=int(input("""Ingrese una Opción: 
            1) Mensaje Encriptado a Desencriptar: 
            2) Mensaje Normal a Encripar: 
            <<>>"""))
        while self.opc>0:
            if self.opc==1:
                self.numenc=int(input("Ingrese el Metodo de Encriptación Usado: (1 al 25): "))
                self.texto = input("Ingrese el texto encriptado: ")
                self.desencriptar(self.texto)
                self.resultado()
                break
            elif self.opc==2:
                self.numenc=int(input("Ingrese un Metodo de Encriptación: (1 al 25): "))
                self.texto = input("Ingrese el texto a encriptar: ").lower()
                self.encriptar(self.texto)
                self.resultado()
                break
            else:
                print("Opcion NO valida")
                self.opc=int(input("""Ingrese una Opción: 
            1) Mensaje Encriptado a Desencriptar: 
            2) Mensaje Normal a Encripar: 
            <<>>"""))
    def encriptar(self,texto):
        self.textoEncriptado=""
        for letra in texto:
            if letra in self.abc:
                i=self.abc.index(letra)
                k=(i+self.numenc) %len(self.abc)
                self.textoEncriptado+=self.abc[k]
            else:
                self.textoEncriptado+=letra
    def desencriptar(self,texto):
        self.textoDesencriptado=""
        for letra in texto:
            if letra in self.abc:
                i=self.abc.index(letra)
                k=(i-self.numenc) %len(self.abc)
                self.textoEncriptado+=self.abc[k]
            else:
                self.textoEncriptado+=letra
    def resultado(self):
        if self.opc==1:
            print (f"""
                El Texto original es: {self.texto}
                El Mensaje Desencriptado es: {self.textoEncriptado}
                El numero de encriptacion usado fue: {self.numenc}
                """)
        elif self.opc==2:
            print (f"""
                El Texto original es: {self.texto}
                El Nuevo Texto Encriptado es: {self.textoEncriptado}
                El numero de encriptacion usado fue: {self.numenc}
                """)
obj=CifradoCesar()
obj.menu()
