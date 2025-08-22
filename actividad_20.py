class Empleado:
    def __init__(self, nombre, puesto, salario, codigo):
        self.nombre = nombre
        self.puesto = puesto
        self.__salario = float(salario)
        self.__codigo = codigo

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario < 0:
            raise ValueError("El salario debe ser mayor a 0")
        self.__salario = float(nuevo_salario)

    @property
    def id_empleado(self):
        return self.__codigo

    def mostrar_info(self):
        return f"Empleado: {self.nombre} - Código: {self.__codigo} - Puesto: {self.puesto} | Salario: Q{self.__salario:}"


class Departamento:
    def __init__(self, nombre_dpto, codigo_interno):
        self.nombre_dpto = nombre_dpto
        self.__codigo_interno = codigo_interno
        self.__empleados = []

    def agregar_empleado(self, empleado):
        if empleado is None:
            raise TypeError("Se debe proporcionar un objeto Empleado, no None")

        codigo_emp = empleado.id_empleado
        if codigo_emp is None:
            raise ValueError("El empleado no tiene código asignado")

        for e in self.__empleados:
            if e.id_empleado == codigo_emp:
                raise ValueError(f"Ya existe un empleado con código {codigo_emp} en el departamento")

        for e in self.__empleados:
            if e is empleado:
                raise ValueError("Este empleado ya fue agregado a este departamento (misma instancia)")

        self.__empleados.append(empleado)

    def eliminar_empleado(self, codigo):
        for i, e in enumerate(self.__empleados):
            if e.id_empleado == codigo:
                del self.__empleados[i]
                return True
        return False

    def listar_empleados(self):
        return list(self.__empleados)

    def buscar_empleado(self, codigo):
        for e in self.__empleados:
            if e.id_empleado == codigo:
                return e
        return None

    def calcular_nomina(self):
        total = 0
        for e in self.__empleados:
            total += e.salario
        return total

    def mostrar_info(self):
        return f"Departamento: {self.nombre_dpto} | Código interno: {self.__codigo_interno} | Empleados: {len(self.__empleados)}"


e1 = Empleado("Ana Machic", "Vendedor", 1200.0, "E001")
e2 = Empleado("Fernando Pérez", "Diseñador", 1500.0, "E002")
e3 = Empleado("Juan Tiu", "Diseñador", 1300, "E003")

ventas = Departamento("Ventas", "D-VEN")
diseniador = Departamento("Desarrollo", "D-DESIGN")

ventas.agregar_empleado(e1)
diseniador.agregar_empleado(e2)
diseniador.agregar_empleado(e3)

print(f"\n{e1.nombre}")
print(f"Salario: {e1.salario}")
print(f"Código: {e1.id_empleado}")
print(e1.mostrar_info())

print(f"\n{e2.nombre}")
print(f"Salario: {e2.salario}")
print(f"Código: {e2.id_empleado}")
print(e2.mostrar_info())

print(f"\n{e3.nombre}")
print(f"Salario: {e3.salario}")
print(f"Código: {e3.id_empleado}")
print(e3.mostrar_info())

print("\n-- Lista de empleados de Ventas --")
for emp in ventas.listar_empleados():
    print(emp.mostrar_info())

print("\n-- Lista de empleados de Desarrollo --")
for emp in diseniador.listar_empleados():
    print(emp.mostrar_info())

print("\nNomina")
print(f"Equipo de ventas Q{ventas.calcular_nomina()}")
print(f"Equipo de desarrollo Q{diseniador.calcular_nomina()}")

e2.salario = 2000.0
e1.salario = 1500.0
print("\nDespués de subir salario")
print(e1.mostrar_info())
print(e2.mostrar_info())