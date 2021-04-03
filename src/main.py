import PySimpleGUI as sg

sg.theme("Reds")

proc0Column = [ [sg.Text(text="Procesador 0", justification="center", font=("Any", 10))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Ejecutando: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="instruccion0")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Contenido de la Caché L1", justification="center", font=("Any", 10))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Set:", justification="left", font=("Any", 10)), sg.Text(text="0", justification="right", font=("Any", 10))],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="0", justification="right", font=("Any", 10))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherencia00")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1direccion00")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1dato00")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Set:", justification="left", font=("Any", 10)), sg.Text(text="1", justification="right", font=("Any", 10))],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="1", justification="right", font=("Any", 10))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherencia01")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1direccion01")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1dato01")] ]

proc1Column = [ [sg.Text(text="Procesador 1", justification="center", font=("Any", 10))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Ejecutando: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="instruccion1")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Contenido de la Caché L1", justification="center", font=("Any", 10))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Set:", justification="left", font=("Any", 10)), sg.Text(text="0", justification="right", font=("Any", 10))],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="0", justification="right", font=("Any", 10))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherencia10")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1direccion10")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1dato10")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Set:", justification="left", font=("Any", 10)), sg.Text(text="1", justification="right", font=("Any", 10))],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="1", justification="right", font=("Any", 10))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherencia11")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1direccion11")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1dato11")] ]

proc2Column = [ [sg.Text(text="Procesador 2", justification="center", font=("Any", 10))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Ejecutando: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="instruccion2")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Contenido de la Caché L1", justification="center", font=("Any", 10))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Set:", justification="left", font=("Any", 10)), sg.Text(text="0", justification="right", font=("Any", 10))],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="0", justification="right", font=("Any", 10))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherencia20")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1direccion20")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1dato20")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Set:", justification="left", font=("Any", 10)), sg.Text(text="1", justification="right", font=("Any", 10))],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="1", justification="right", font=("Any", 10))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherencia21")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1direccion21")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1dato21")] ]

proc3Column = [ [sg.Text(text="Procesador 3", justification="center", font=("Any", 10))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Ejecutando: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="instruccion3")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Contenido de la Caché L1", justification="center", font=("Any", 10))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Set:", justification="left", font=("Any", 10)), sg.Text(text="0", justification="right", font=("Any", 10))],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="0", justification="right", font=("Any", 10))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherencia30")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1direccion30")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1dato30")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Set:", justification="left", font=("Any", 10)), sg.Text(text="1", justification="right", font=("Any", 10))],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="1", justification="right", font=("Any", 10))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherencia31")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1direccion31")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1dato31")] ]

bloq0L2Column = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="0", justification="right", font=("Any", 10))],
                   [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="XX", justification="right", font=("Any", 10), key="l2coherencia00")],
                   [sg.Text(text="Procesador Dueño del Bloque:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l2dueno00")],
                   [sg.Text(text="Procesadores donde se Comparte:", justification="left", font=("Any", 10)), sg.Text(text="X, X, X", justification="right", font=("Any", 10), key="l2compartidos00")],
                   [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l2direccion00")],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l2dato00")] ]

bloq1L2Column = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="1", justification="right", font=("Any", 10))],
                   [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="XX", justification="right", font=("Any", 10), key="l2coherencia01")],
                   [sg.Text(text="Procesador Dueño del Bloque:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l2dueno01")],
                   [sg.Text(text="Procesadores donde se Comparte:", justification="left", font=("Any", 10)), sg.Text(text="X, X, X", justification="right", font=("Any", 10), key="l2compartidos01")],
                   [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l2direccion01")],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l2dato01")] ]

bloq2L2Column = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="2", justification="right", font=("Any", 10))],
                   [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="XX", justification="right", font=("Any", 10), key="l2coherencia10")],
                   [sg.Text(text="Procesador Dueño del Bloque:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l2dueno10")],
                   [sg.Text(text="Procesadores donde se Comparte:", justification="left", font=("Any", 10)), sg.Text(text="X, X, X", justification="right", font=("Any", 10), key="l2compartidos10")],
                   [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l2direccion10")],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l2dato10")] ]

bloq3L2Column = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="3", justification="right", font=("Any", 10))],
                   [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 10)), sg.Text(text="XX", justification="right", font=("Any", 10), key="l2coherencia11")],
                   [sg.Text(text="Procesador Dueño del Bloque:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l2dueno11")],
                   [sg.Text(text="Procesadores donde se Comparte:", justification="left", font=("Any", 10)), sg.Text(text="X, X, X", justification="right", font=("Any", 10), key="l2compartidos11")],
                   [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l2direccion11")],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l2dato11")] ]

bloq0MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="0", justification="right", font=("Any", 10))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memdato0")] ]

bloq1MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="1", justification="right", font=("Any", 10))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memdato1")] ]

bloq2MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="2", justification="right", font=("Any", 10))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memdato2")] ]

bloq3MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="3", justification="right", font=("Any", 10))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memdato3")] ]

bloq4MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="4", justification="right", font=("Any", 10))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memdato4")] ]

bloq5MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="5", justification="right", font=("Any", 10))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memdato5")] ]

bloq6MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="6", justification="right", font=("Any", 10))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memdato6")] ]

bloq7MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 10)), sg.Text(text="7", justification="right", font=("Any", 10))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memdato7")] ]

layout = [ [sg.Column(layout=proc0Column, element_justification="center", key="procesador0"), sg.Column(layout=proc1Column, element_justification="center"), sg.Column(layout=proc2Column, element_justification="center"), sg.Column(layout=proc3Column, element_justification="center")],
           [sg.Text(text="Contenido de la Caché L2", size=(149, 1), justification="center", font=("Any", 10))],
           [sg.Text(text="Set 0", size=(70, 1), justification="center", font=("Any", 10)), sg.Text(text="Set 1", size=(80, 1), justification="center", font=("Any", 10))],
           [sg.Column(layout=bloq0L2Column, element_justification="center"), sg.Column(layout=bloq1L2Column, element_justification="center"), sg.Column(layout=bloq2L2Column, element_justification="center"), sg.Column(layout=bloq3L2Column, element_justification="center")],
           [sg.Text(text="Contenido de la Memoria", size=(105, 1), justification="center", font=("Any", 10)), sg.Text(text="Última Instrucción Generada:", size=(40, 1), justification="center", font=("Any", 10)), sg.Text(text="XX: XXXXX XXX;XXXX", justification="center", font=("Any", 10), key="ultimaInstruccion")],
           [sg.Column(layout=bloq0MemColumn, element_justification="center"), sg.Column(layout=bloq1MemColumn, element_justification="center"), sg.Column(layout=bloq2MemColumn, element_justification="center"), sg.Column(layout=bloq3MemColumn, element_justification="center"), sg.Column(layout=bloq4MemColumn, element_justification="center"), sg.Column(layout=bloq5MemColumn, element_justification="center"), sg.Column(layout=bloq6MemColumn, element_justification="center"), sg.Column(layout=bloq7MemColumn, element_justification="center"), sg.Text(text="Siguiente Instrucción:", size=(40, 1), justification="center", font=("Any", 10)), sg.Text(text="XX: XXXXX XXX;XXXX", justification="center", font=("Any", 10), key="siguienteInstruccion")],
           [sg.Button(button_text="Ejecución Continua", font=("Any", 10), disabled=False, key="reanudar"), sg.Button(button_text="Pausa", font=("Any", 10), disabled=True, key="pausa"), sg.Button(button_text="Paso", font=("Any", 10), disabled=False, key="paso"), sg.InputText(disabled=False, key="nuevaInstruccion"), sg.Button(button_text="Aceptar", font=("Any", 10), disabled=False, key="aceptar")] ]

window = sg.Window(title="Protocolo Basado en Directorios en Sistemas Multiprocesador", layout=layout)

def main():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "pausa":
            window["reanudar"].update(disabled=False)
            window["pausa"].update(disabled=True)
            window["paso"].update(disabled=False)
            window["nuevaInstruccion"].update(disabled=False)
            window["aceptar"].update(disabled=False)
        if event == "reanudar":
            window["reanudar"].update(disabled=True)
            window["pausa"].update(disabled=False)
            window["paso"].update(disabled=True)
            window["nuevaInstruccion"].update(disabled=True)
            window["aceptar"].update(disabled=True)
        if event == "aceptar":
            window["siguienteInstruccion"].update(values["nuevaInstruccion"])

    window.close()

if __name__ == "__main__":
    main()