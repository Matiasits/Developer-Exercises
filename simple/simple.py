import random

def generador_dicc():    
    lista = []
    id = 1
    for i in range(0,10):
        edad = random.randint(1,100)
        lista.append({id:edad})
        id += 1
    return lista
    
def ordenar_lista(lista):
    
    for numPasada in range(len(lista)-1,0,-1):
        for i in range(numPasada):
            mayor = list(lista[i].values())
            siguiente = list(lista[i+1].values())
            if mayor < siguiente:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    masViejo = list(lista[0].keys())
    masJoven = list(lista[-1].keys())
    
    print(f"Id mas viejo: {masViejo[0]}\nId mas joven: {masJoven[0]}")
    return lista
    
print(ordenar_lista(generador_dicc()))