import math
#Tomar de ejemplo la clase rectangulo
class Circulo:
    def __init__(self, radio): # toma un radio , centro
        if radio <= 0:
            print("No puede ingresar un radio menor o igual a 0\n")
        self.radio = radio

    def diametro_circulo(self)->float:
        return self.radio * 2
    
    def perimetro_circulo(self)->float:
        return math.pi * self.diametro_circulo() 
    
    def area_circulo(self)->float:
        return math.pi * (self.radio ** 2)
    
    def __str__(self) -> str:
        return f"El circulo tiene de radio: {self.radio}\nSu perimetro es: {self.perimetro_circulo()}\nSu area es: {self.area_circulo()}\n"
    
    def modificar_radio(self, nuevo_radio:float):
        self.radio = nuevo_radio
        
    def multiplicar_ciruclo(self, numero:int):
        if numero > 0:
            self.radio *= numero
        else:
            print("No puede multiplicar el radio por numeros igual o menores a 0\n")
            
c = Circulo(5.4)
print(c.__str__())

c.multiplicar_ciruclo(2)
print(c.__str__())

c.modificar_radio(10)
print(c.__str__())
