from  tkinter import ttk
from  tkinter import *

import sqlite3

class Paciente:

    db_name = 'camilla.db'

    def __init__(self, window):


        self.wind = window
        self.wind.title('Administración de información')

        frame = ttk.Notebook(self.wind)
        frame.pack()

        pes0 = ttk.Frame(self.wind)
        pes1 = ttk.Frame(self.wind)
        pes2 = ttk.Frame(self.wind)

        frame.add(pes0, text="Pacientes")
        frame.add(pes1, text="Antecedentes")
        frame.add(pes2, text="Mediciones")

        frame1 = LabelFrame(pes0, font=('arial', 18), text='Buscar pacientes')
        frame1.grid(row=0, column=0, pady=10, padx=10, sticky=N+W+E)
        Label(frame1, font=('arial', 12), text='# de documento').grid(row=1, column=0, pady=10, padx=10 )
        self.documento1 = Entry(frame1)
        self.documento1.grid(row=1, column=1, padx=10, pady=10)
        self.documento1.focus()
        ttk.Button(frame1, text="Buscar", command=self.cerrar).grid(row=1, column=2, padx=10, sticky=W+E)


        # acá se crea el Frame
        frame = LabelFrame(pes0, font=('arial', 18), text='Registro de nuevo paciente')
        frame.grid(row=1, column=0, pady=10)

        Label(frame, font=('arial', 12), text='Nombre').grid(row=1, column=0, pady=5, padx=5 )
        self.nombre = Entry(frame)
        self.nombre.grid(row=1, column=1)

        Label(frame, font=('arial', 12), text='Apellidos: ').grid(row=1, column=2, pady=5, padx=5 )
        self.apellidos = Entry(frame)
        self.apellidos.grid(row=1, column=3)

        Label(frame, font=('arial', 12), text='Nacimiento: ').grid(row=2, column=0, pady=5, padx=5 )
        self.nacimiento = Entry(frame)
        self.nacimiento.grid(row=2, column=1)

        Label(frame, font=('arial', 12), text='Sexo: ').grid(row=2, column=2, pady=5, padx=5 )
        self.sexo = ttk.Combobox(frame)
        self.sexo.grid(row=2, column=3)
        self.sexo["values"] = ["Femenino", "Masculino"]
        self.sexo.set("Femenino")

        Label(frame, font=('arial', 12), text='Documento: ').grid(row=3, column=0, pady=5, padx=5 )
        self.documento = Entry(frame)
        self.documento.grid(row=3, column=1)

        Label(frame, font=('arial', 12), text='Teléfono: ').grid(row=3, column=2, pady=5, padx=5 )
        self.telefono = Entry(frame)
        self.telefono.grid(row=3, column=3)

        Label(frame, font=('arial', 12), text='Email: ').grid(row=4, column=0, pady=5, padx=5 )
        self.email = Entry(frame)
        self.email.grid(row=4, column=1)

        ttk.Button(frame, text="Guardar", command=self.add_pacientes).grid(row=4, column=3, sticky=E)

        frame5 = LabelFrame(pes0, font=('arial', 18))
        frame5.grid(row=2, column=2, pady=10, padx=10, sticky=W+E)
        ttk.Button(frame5, text="Cerrar", command=self.cerrar).grid(row=5, column=3, sticky=W+E)


        frame2 = LabelFrame(pes1, font=('arial', 18), text='Antecedentes Personales')
        frame2.grid(row=0, column=1, pady=10, padx=10, sticky=N+W+E)
        Label(frame2, font=('arial', 12), text='Nombre').grid(row=1, column=0, pady=5, padx=5 )
        self.documento2 = Entry(frame2)
        self.documento2.grid(row=1, column=1)

        frame3 = LabelFrame(pes1, font=('arial', 18), text='Antecedentes Familiares')
        frame3.grid(row=1, column=1, pady=10, padx=10, sticky=N+W+E)
        Label(frame3, font=('arial', 12), text='Nombre').grid(row=1, column=0, pady=5, padx=5 )
        self.documento3 = Entry(frame3)
        self.documento3.grid(row=1, column=1)

        frame4 = LabelFrame(pes1, font=('arial', 18), text='Antecedentes Toxicológicos')
        frame4.grid(row=2, column=1, pady=10, padx=10, sticky=N+W+E)
        Label(frame4, font=('arial', 12), text='Nombre').grid(row=1, column=0, pady=5, padx=5 )
        self.documento4 = Entry(frame4)
        self.documento4.grid(row=1, column=1)

        frame6 = LabelFrame(pes2, font=('arial', 18), text='Mediciones')
        frame6.grid(row=0, column=2, pady=10, padx=10, sticky=N+W+E, rowspan=3)

        Label(frame6, font=('arial', 12), text='Presión Arterial').grid(row=1, column=0, pady=5, padx=5 )
        self.presionA = Entry(frame6)
        self.presionA.grid(row=1, column=1, pady=5, padx=5)

        Label(frame6, font=('arial', 12), text='Frecuencia Cardíaca').grid(row=2, column=0, pady=5, padx=5 )
        self.frecuenciac = Entry(frame6)
        self.frecuenciac.grid(row=2, column=1, pady=5, padx=5)

        Label(frame6, font=('arial', 12), text='% de oxígeno').grid(row=3, column=0, pady=5, padx=5 )
        self.oxigeno = Entry(frame6)
        self.oxigeno.grid(row=3, column=1, pady=5, padx=5)

        Label(frame6, font=('arial', 12), text='Estatura').grid(row=4, column=0, pady=5, padx=5)
        self.estatura = Entry(frame6)
        self.estatura.grid(row=4, column=1, pady=5, padx=5)

        Label(frame6, font=('arial', 12), text='Peso').grid(row=5, column=0, pady=5, padx=5)
        self.peso = Entry(frame6)
        self.peso.grid(row=5, column=1, pady=5, padx=5)

        Label(frame6, font=('arial', 12), text='IMC').grid(row=6, column=0, pady=5, padx=5)
        self.imc = Entry(frame6)
        self.imc.grid(row=6, column=1, pady=5, padx=5)
        ttk.Button(frame6, text="Tomar medición automática", command=self.cerrar).grid(row=7, column=1, padx=10, sticky=W+E)


    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            try:
                result = cursor.execute(query, parameters)
                conn.commit()
                return result
            except:
                return False

    def get_pacientes(self):
        query = 'select * from pacientes order by apellidos desc'
        db_rows = self.run_query(query)
        records = self.tree.get_children()

        # limpipar la tabla
        for element in records:
            self.tree.delete(element)

        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])

    def validation(self):
            return len(self.nombre.get()) != 0 and len(self.apellidos.get()) and len(self.documento.get()) and len(self.sexo.get()) and len(self.telefono.get()) and len(self.email.get()) and len(self.nacimiento.get())

    def add_pacientes(self):
        if self.validation():
            query = 'Insert into pacientes values(Null,?,?,?,?,?,?,?)'
            parameters = (self.apellidos.get(), self.nombre.get(), self.documento.get(), self.nacimiento.get(), self.telefono.get(), self.email.get(), self.sexo.get())
            self.run_query(query, parameters)
            self.get_pacientes()
            self.apellidos.delete(0, END)
            self.nombre.delete(0, END)
            self.documento.delete(0, END)
            self.telefono.delete(0, END)
            self.nacimiento.delete(0, END)
            self.email.delete(0, END)
        else:
            print("Todos los campos son obligatorios")

    def cerrar(self):
        window.destroy()


if __name__ == '__main__':
    window = Tk()
    window.resizable(False, False)
    application = Paciente(window)
    window.mainloop()
