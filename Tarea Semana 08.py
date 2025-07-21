import tkinter as tk
from tkinter import ttk

# 🛠️ Clase que representa una reparación individual
class Reparacion:
    def __init__(self, dispositivo, problema, estado="Pendiente"):
        self.dispositivo = dispositivo  # Tipo de dispositivo (celular, laptop, etc.)
        self.problema = problema        # Descripción del problema
        self.estado = estado            # Estado de la reparación

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado  # Método para cambiar el estado

# 📋 Clase que gestiona múltiples reparaciones
class SistemaReparaciones:
    def __init__(self):
        self.lista_reparaciones = []  # Lista para almacenar objetos de tipo Reparacion

    def agregar_reparacion(self, reparacion):
        self.lista_reparaciones.append(reparacion)  # Agrega una nueva reparación

    def mostrar_reparaciones(self):
        # Devuelve una lista con los datos de todas las reparaciones
        return [(r.dispositivo, r.problema, r.estado) for r in self.lista_reparaciones]

# 🎛️ Clase principal que define el panel gráfico
class Dashboard(tk.Tk):
    def __init__(self, sistema):
        super().__init__()
        self.title("Panel de Reparaciones Electrónicas")
        self.geometry("600x400")
        self.sistema = sistema  # Instancia de SistemaReparaciones
        self.crear_interfaz()   # Llama al método para crear la interfaz visual

    def crear_interfaz(self):
        # Título del panel
        self.label_titulo = ttk.Label(self, text="Registro de Reparaciones", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        # 🔤 Entrada de datos
        self.frame_input = ttk.Frame(self)
        self.frame_input.pack(pady=5)

        # Campo para dispositivo
        ttk.Label(self.frame_input, text="Dispositivo:").grid(row=0, column=0)
        self.entry_dispositivo = ttk.Entry(self.frame_input)
        self.entry_dispositivo.grid(row=0, column=1)

        # Campo para problema
        ttk.Label(self.frame_input, text="Problema:").grid(row=1, column=0)
        self.entry_problema = ttk.Entry(self.frame_input)
        self.entry_problema.grid(row=1, column=1)

        # Botón para agregar reparación
        self.btn_agregar = ttk.Button(self.frame_input, text="Agregar", command=self.agregar_reparacion)
        self.btn_agregar.grid(row=2, column=0, columnspan=2, pady=5)

        # 🧾 Tabla para visualizar reparaciones
        self.tree = ttk.Treeview(self, columns=("Dispositivo", "Problema", "Estado"), show="headings")
        self.tree.heading("Dispositivo", text="Dispositivo")
        self.tree.heading("Problema", text="Problema")
        self.tree.heading("Estado", text="Estado")
        self.tree.pack(pady=10, fill="both", expand=True)

    def agregar_reparacion(self):
        # Lee los datos de las entradas
        dispositivo = self.entry_dispositivo.get()
        problema = self.entry_problema.get()
        # Crea una instancia de Reparacion y la agrega al sistema
        reparacion = Reparacion(dispositivo, problema)
        self.sistema.agregar_reparacion(reparacion)
        # Actualiza la tabla con la nueva reparación
        self.actualizar_tabla()

    def actualizar_tabla(self):
        # Limpia la tabla y la vuelve a llenar con las reparaciones actuales
        for row in self.tree.get_children():
            self.tree.delete(row)
        for dispositivo, problema, estado in self.sistema.mostrar_reparaciones():
            self.tree.insert("", "end", values=(dispositivo, problema, estado))

# 🔄 Punto de inicio del programa
if __name__ == "__main__":
    sistema = SistemaReparaciones()  # Crea el sistema
    app = Dashboard(sistema)         # Crea la interfaz gráfica
    app.mainloop()                   # Ejecuta el programa