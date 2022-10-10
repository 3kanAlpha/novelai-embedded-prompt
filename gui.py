import PySimpleGUI as sg
from rename import rename

layout = [
   [sg.Text("Target Directory: "), sg.InputText(), sg.FolderBrowse(key="input_dir")],
   [sg.Text("File Name Prefix: "), sg.InputText(key="name_prefix")],
   [sg.Column([[sg.Submit(button_text="Run")], [sg.Exit()]], justification="center")],
]

window = sg.Window("NovelAI Embedded Prompt", layout)

while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
    if event == "Run":
        rename(values["input_dir"], values["name_prefix"])
window.close()
# print(values)