class Student:
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade

    def study(self):
        return f"{self.name} ({self.id}) esta estudiando."
    
    def hw(self, assignment):
       return f"{self.name} ({self.id}) hizo tarea: un {assignment}.\nSu calificación fue: {self.grade}."

    def go_class(self, subj):
        return f"{self.name} ({self.id}) ha entrado a clase de {subj}."
    
st1 = Student("Fer", 1, 9)
st2 = Student("Sandra", 2, 8)

print(st1.go_class("Inglés"))
print(st2.go_class("Álgebra"))
print(st1.study())
print(st2.study())
print("\n"+st1.hw("ensayo"))
