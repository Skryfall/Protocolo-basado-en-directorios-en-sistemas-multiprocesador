import PySimpleGUI as sg

sg.theme("Reds")

proc0Column = [ [sg.Text(text="Procesador 0", justification="center", font=("Any", 15))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Ejecutando: ", justification="left", font=("Any", 12)), sg.Text(text="WRITE 010;4A3B", justification="right", font=("Any", 12), key="instruccion0")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Contenido de la Caché L1", justification="center", font=("Any", 15))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="0", justification="right", font=("Any", 12))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="S", justification="right", font=("Any", 12), key="l1coherencia00")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l1direccion00")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l1dato00")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="1", justification="right", font=("Any", 12))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="S", justification="right", font=("Any", 12), key="l1coherencia01")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l1direccion01")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l1dato01")] ]

proc1Column = [ [sg.Text(text="Procesador 1", justification="center", font=("Any", 15))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Ejecutando: ", justification="left", font=("Any", 12)), sg.Text(text="WRITE 010;4A3B", justification="right", font=("Any", 12), key="instruccion1")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Contenido de la Caché L1", justification="center", font=("Any", 15))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="0", justification="right", font=("Any", 12))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="S", justification="right", font=("Any", 12), key="l1coherencia10")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l1direccion10")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l1dato10")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="1", justification="right", font=("Any", 12))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="S", justification="right", font=("Any", 12), key="l1coherencia11")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l1direccion11")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l1dato11")] ]

proc2Column = [ [sg.Text(text="Procesador 2", justification="center", font=("Any", 15))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Ejecutando: ", justification="left", font=("Any", 12)), sg.Text(text="WRITE 010;4A3B", justification="right", font=("Any", 12), key="instruccion2")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Contenido de la Caché L1", justification="center", font=("Any", 15))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="0", justification="right", font=("Any", 12))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="S", justification="right", font=("Any", 12), key="l1coherencia20")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l1direccion20")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l1dato20")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="1", justification="right", font=("Any", 12))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="S", justification="right", font=("Any", 12), key="l1coherencia21")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l1direccion21")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l1dato21")] ]

proc3Column = [ [sg.Text(text="Procesador 3", justification="center", font=("Any", 15))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Ejecutando: ", justification="left", font=("Any", 12)), sg.Text(text="WRITE 010;4A3B", justification="right", font=("Any", 12), key="instruccion3")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Contenido de la Caché L1", justification="center", font=("Any", 15))],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="0", justification="right", font=("Any", 12))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="S", justification="right", font=("Any", 12), key="l1coherencia30")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l1direccion30")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l1dato30")],
                [sg.Text(text="-----------------------------------------------------------------------------------", justification="center")],
                [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="1", justification="right", font=("Any", 12))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="S", justification="right", font=("Any", 12), key="l1coherencia31")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l1direccion31")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l1dato31")] ]

bloq0L2Column = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="0", justification="right", font=("Any", 12))],
                [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="DS", justification="right", font=("Any", 12), key="l2coherencia0")],
                [sg.Text(text="Procesador Dueño del Bloque:", justification="left", font=("Any", 12)), sg.Text(text="0", justification="right", font=("Any", 12), key="l2dueno0")],
                [sg.Text(text="Procesadores donde se Comparte:", justification="left", font=("Any", 12)), sg.Text(text="1, 2, 3", justification="right", font=("Any", 12), key="l2compartidos0")],
                [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l2direccion0")],
                [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l2dato0")] ]

bloq1L2Column = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="1", justification="right", font=("Any", 12))],
                  [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="DS", justification="right", font=("Any", 12), key="l2coherencia1")],
                  [sg.Text(text="Procesador Dueño del Bloque:", justification="left", font=("Any", 12)), sg.Text(text="0", justification="right", font=("Any", 12), key="l2dueno1")],
                  [sg.Text(text="Procesadores donde se Comparte:", justification="left", font=("Any", 12)), sg.Text(text="1, 2, 3", justification="right", font=("Any", 12), key="l2compartidos1")],
                  [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l2direccion1")],
                  [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l2dato1")] ]

bloq2L2Column = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="2", justification="right", font=("Any", 12))],
                  [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="DS", justification="right", font=("Any", 12), key="l2coherencia2")],
                  [sg.Text(text="Procesador Dueño del Bloque:", justification="left", font=("Any", 12)), sg.Text(text="0", justification="right", font=("Any", 12), key="l2dueno2")],
                  [sg.Text(text="Procesadores donde se Comparte:", justification="left", font=("Any", 12)), sg.Text(text="1, 2, 3", justification="right", font=("Any", 12), key="l2compartidos2")],
                  [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l2direccion2")],
                  [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l2dato2")] ]

bloq3L2Column = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="3", justification="right", font=("Any", 12))],
                  [sg.Text(text="Estado de Coherencia:", justification="left", font=("Any", 12)), sg.Text(text="DS", justification="right", font=("Any", 12), key="l2coherencia3")],
                  [sg.Text(text="Procesador Dueño del Bloque:", justification="left", font=("Any", 12)), sg.Text(text="0", justification="right", font=("Any", 12), key="l2dueno3")],
                  [sg.Text(text="Procesadores donde se Comparte:", justification="left", font=("Any", 12)), sg.Text(text="1, 2, 3", justification="right", font=("Any", 12), key="l2compartidos3")],
                  [sg.Text(text="Dirección de Memoria:", justification="left", font=("Any", 12)), sg.Text(text="111", justification="right", font=("Any", 12), key="l2direccion3")],
                  [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="AAAA", justification="right", font=("Any", 12), key="l2dato3")] ]

bloq0MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="0", justification="right", font=("Any", 12))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="0000", justification="right", font=("Any", 12), key="memdato0")] ]

bloq1MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="1", justification="right", font=("Any", 12))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="0000", justification="right", font=("Any", 12), key="memdato1")] ]

bloq2MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="2", justification="right", font=("Any", 12))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="0000", justification="right", font=("Any", 12), key="memdato2")] ]

bloq3MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="3", justification="right", font=("Any", 12))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="0000", justification="right", font=("Any", 12), key="memdato3")] ]

bloq4MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="4", justification="right", font=("Any", 12))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="0000", justification="right", font=("Any", 12), key="memdato4")] ]

bloq5MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="5", justification="right", font=("Any", 12))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="0000", justification="right", font=("Any", 12), key="memdato5")] ]

bloq6MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="6", justification="right", font=("Any", 12))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="0000", justification="right", font=("Any", 12), key="memdato6")] ]

bloq7MemColumn = [ [sg.Text(text="Bloque:", justification="left", font=("Any", 12)), sg.Text(text="7", justification="right", font=("Any", 12))],
                   [sg.Text(text="Dato:", justification="left", font=("Any", 12)), sg.Text(text="0000", justification="right", font=("Any", 12), key="memdato7")] ]

layout = [ [sg.Column(layout=proc0Column, element_justification="center", key="procesador0"), sg.Column(layout=proc1Column, element_justification="center"), sg.Column(layout=proc2Column, element_justification="center"), sg.Column(layout=proc3Column, element_justification="center")],
           [sg.Text(text="Contenido de la Caché L2", size=(110, 1), justification="center", font=("Any", 15))],
           [sg.Column(layout=bloq0L2Column, element_justification="center"), sg.Column(layout=bloq1L2Column, element_justification="center"), sg.Column(layout=bloq2L2Column, element_justification="center"), sg.Column(layout=bloq3L2Column, element_justification="center")],
           [sg.Text(text="Contenido de la Memoria", size=(73, 1), justification="center", font=("Any", 15)), sg.Text(text="Última Instrucción Generada", size=(35, 1), justification="center", font=("Any", 15))],
           [sg.Column(layout=bloq0MemColumn, element_justification="center"), sg.Column(layout=bloq1MemColumn, element_justification="center"), sg.Column(layout=bloq2MemColumn, element_justification="center"), sg.Column(layout=bloq3MemColumn, element_justification="center"), sg.Column(layout=bloq4MemColumn, element_justification="center"), sg.Column(layout=bloq5MemColumn, element_justification="center"), sg.Column(layout=bloq6MemColumn, element_justification="center"), sg.Column(layout=bloq7MemColumn, element_justification="center"), sg.Text(text="P0: READ 100", size=(45, 1), justification="center", font=("Any", 12), key="ultimaInstruccion")],
           [sg.Button(button_text="Ejecución Continua", font=("Any", 15), disabled=True, key="reanudar"), sg.Button(button_text="Pausa", font=("Any", 15), disabled=False, key="pausa"), sg.Button(button_text="Paso", font=("Any", 15), disabled=True, key="paso"), sg.InputText(disabled=True, key="nuevaInstruccion"), sg.Button(button_text="Aceptar", font=("Any", 15), disabled=True, key="aceptar"), sg.Text(text="Siguiente Instrucción", size=(51, 1), justification="center", font=("Any", 15))],
           [sg.Text(text="P0: READ 100", size=(124, 1), justification="right", font=("Any", 12), key="siguienteInstruccion")] ]

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