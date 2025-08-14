class biblioteca:
    def __init__(self,titulo,autor,año,codigo ):
        self.titulo = titulo
        self.autor= autor
        self.año = año
        self.codigo=codigo

    def mostrar_info(self):
        return f"Titulo: {self.titulo} - autor: {self.autor} - año: {self.año} - codigo: {self.codigo}"


class Registro_libro:
    def __init__(self):
        self.libro = {}

class estudiante:
    def __init__(self,carnet,nombre,carrera ):
        self.carnet = carnet
        self.nombre= nombre
        self.carrere=carrera


    def mostrar_info(self):
        return f"carnet: {self.carnet} - nombre: {self.nombre} - carrera: {self.carrere} - codigo:"

class RegistroEstudiantes:
    def __init__(self):

        self.Estudiantes = {}

    def agregar(self):
        try:
            carnet = input("Ingresar carnet del estudiante: ")
            if carnet in self.Estudiantes:
                print("Ya existe un estudiante con ese carnet.\n")
                return

            nombre = input("Ingresar nombre del estudiante: ")
            edad = int(input("Ingresar edad del estudiante: "))

            self.Estudiantes[carnet] = estudiante(carnet, nombre, edad)
            print("Estudiante agregado.\n")
        except ValueError:
            print("Error: La edad debe ser un número entero.\n")

    def mostrar(self):
        if not self.Estudiantes:
            print("No hay estudiantes registrados.\n")
            return

        print("\nLista de estudiantes:")
        for i, estudiante in enumerate(self.Estudiantes.values(), start=1):
            print(f"{i}. {estudiante.mostrar_info()}")
        print()

    def eliminar(self):
        carnet_buscado = input("Ingresar el carnet del estudiante a eliminar: ")
        if carnet_buscado in self.Estudiantes:
            del self.Estudiantes[carnet_buscado]
            print("Estudiante eliminado.\n")
        else:
            print("Estudiante no encontrado.\n")



registro = RegistroEstudiantes()

def menu():
    print("=======menu principal======")
    print("1.  ")
    print("2. ")
    print("3. ")
    print("4. ")
