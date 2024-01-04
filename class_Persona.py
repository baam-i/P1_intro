"""persona
    estudiante
    empleado
"""

class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_data(self):
        return f"La persona es {self.name} y tiene {self.age} años."

class Empleado(Persona):
    def __init__(self, name, age, job):
        super().__init__(name, age)    
        self.job = job
    
    def print_data(self):
        return f"El empleado es {self.name}, trabaja en {self.job} y tiene {self.age} años."

class Estudiante(Persona):
    def __init__(self, name, age, career):
        super().__init__(name, age)
        self.career = career

    def print_data(self):
        def print_data(self):
            return f"El estudiante es {self.name}, estudia {self.career} y tiene {self.age} años."
        

#def main():
    