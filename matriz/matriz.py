import random

def matriz(filas=5,columnas=5):
    matriz=[]

    for fila in range(filas):
        matriz.append([])
        for columna in range(columnas):
            numero = random.randint(0,100)
            matriz[fila].append(numero)
    
    return matriz

def sonConsecutivos(lista):
    inicio = None
    final = None
    resultado = True
    #variable para determinar el siguiente de un num
    diferencia_al_siguiente = 1
    for i in range(1,len(lista)):
        if (lista[0] + diferencia_al_siguiente) != lista[i]:
              resultado = False
        diferencia_al_siguiente += 1
    return resultado

def desglozar(matriz):
    inicio = None
    final = None
    col = []
    pos = 0
    for fila in matriz:
        col.append(fila[pos])
        if sonConsecutivos(fila):
            inicio = f"Inicio horizontal {fila.index(fila[0])}"
            final = f"Final horizontal {fila.index(fila[-1])}"
        pos += 1
    if sonConsecutivos(col):
        inicio = f"Inicio Vertical {matriz[0].index(col[0])}"
        final = f"Final Vertical {matriz[-1].index(col[-1])}"
            
    return f"{inicio}, {final}"

print(desglozar(matriz()))
