class Animal:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass
    
    def __str__(self):
        return f"{self.nombre} ({self.edad} años)."
    
class Mamifero(Animal):
    def __init__(self, nombre, edad, tipo_pelo):
        super().__init__(nombre, edad)
        self.tipo_pelo = tipo_pelo

class Perro(Mamifero):
    def hacer_sonido(self):
        return "Guau"
    
class Gato(Mamifero):
    def hacer_sonido(self):
        return "Miau"
    
class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu"
    
def main():
    perro = Perro("Firulais", 3, "Corto")
    gato = Gato("Bigotes", 2, "Largo")
    vaca = Vaca("Otis", 4)

    print(f"{perro.nombre} tiene pelo {perro.tipo_pelo}.")
    print(f"{gato.nombre} tiene pelo {gato.tipo_pelo}.")