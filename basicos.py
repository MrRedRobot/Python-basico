#Funciones basicas

lista = ["Hola","soy","la","lista","Hola"] 
tupla = ("Hola","tupla",True,False,1,0.1,"Hola")
         
def suma(num1,num2):
    return num1+num2

def accederLista():
    for indice in range(len(lista)):
        print("Indice: ",indice,"Elemento: ",lista[indice])
    
    lista.append(3)
    print("Lista al reves:",lista[-1])
    print("Sublista:",lista[0:3])
    print("Contar apariciones:",lista.count("Hola"))
    print("Obtener el indice de un elemento:",lista.index("lista"))
    print("Remover elemento:",lista.remove(4))
           
def manipularTupla():
    print(tupla.index(0.1))
    print(tupla.count("Hola"))
  
# Defining main function
def main():
    print("!!! HEY MAIN")
    accederLista()
    manipularTupla()

# Using the special variable 
# __name__
if __name__=="__main__":
    main()