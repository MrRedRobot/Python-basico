class Personaje:
    nombre= "Default"
    fuerza= 0
    inteligencia= 0
    defensa = 0
    vida = 0

    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.__nombre=nombre
        self.__fuerza=fuerza
        self.__inteligencia=inteligencia
        self.__defensa=defensa
        self.__vida=vida

    def get_nombre(self):
        return self.__nombre

    def set_fuerza(self,fuerza):
        self.__fuerza=fuerza
        

class Guerrero(Personaje):
    
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida,espada):
        super().__init__(nombre,fuerza,inteligencia,defensa,vida)
        self.espada= espada

    def poder(self):
        print("Poder de guerrero...")

class Mago(Personaje):
    
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida,varita):
        super().__init__(nombre,fuerza,inteligencia,defensa,vida)
        self.varita= varita

    def poder(self):
        print("Poder de mago...")
        
        
miPersonaje = Personaje("RedMonkey",75,85,80,95)
monkey = Guerrero("Monkey",75,85,80,95)
print(miPersonaje.nombre)

