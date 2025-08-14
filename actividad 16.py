
class biblioteca:
    def __init__(self,codigo,titulo,autor,año ):
        self.codigo = codigo
        self.titulo = titulo
        self.autor= autor
        self.año = año


    def mostrar_info(self):
        return f"codigo: {self.codigo}-Titulo: {self.titulo} - autor: {self.autor} - año: {self.año} "


class Registro_libro:
    def __init__(self):
        self.libro = {}


    def registro_libro(self):
        try:
            codigo=input("ingrese codigo de libro")
            if codigo in self.libro:
                print("ya existe un libro con ese codigo")
                return
            titulo=input("ingrese titulo ")
            autor= input("ingrese autor de libro")
            año=int(input("ingrse año de libro ejp. 1993"))

            self.libro[codigo]=biblioteca(codigo,titulo,autor,año)
            print("libro agregado con exito. \n")

        except ValueError:
            print("dato incorrecto")


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


def menu():
    print("=======menu principal======")
    print("1. regitro de libros ")
    print("2. registro de estudiante")
    print("3. prestar libro")
    print("4. devolver libro ")
    print("5. eliminar libro")
    print("6. agregar libro ")
    print("7. eliminar estudiante ")
    print("8. agregar estudiante")
    print("9. salir")


registro = RegistroEstudiantes()
op=0

while op!=9:
    menu()
    try:
        op=int(input("ingrese una opcion a ejecutar"))
        match op:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                print("fin del progrma")
            case _:
                print("has ingresado una opcion invalida")
    except ValueError:
        print("has ingresado un dato invlido")


