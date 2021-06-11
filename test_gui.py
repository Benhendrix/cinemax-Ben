import PySimpleGUI as gui

layout = [
    [gui.Text("WELKOM!", font="Helvetica 24")],
    [gui.Button("Sluiten", pad=((0, 0), (100, 10)), size=(70, None), font="Helvetica 14")]
]

window = gui.Window('Mijn eerste venster', layout, size=(300, 300), element_justification="c")

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Cancel' or event == "Sluiten"
    break
window.close()