import PySimpleGUI as sg
from rename import rename

layout = [
   [sg.Text("Target Directory: "), sg.InputText(), sg.FolderBrowse(key="input_dir")],
   [sg.Text("File Name Prefix: "), sg.InputText(key="name_prefix")],
   [sg.Text("Start Number: "), sg.InputText(key="start_num")],
   [sg.Column([[sg.Submit(button_text="Run")], [sg.Exit()]], justification="center")],
]

window = sg.Window("NovelAI Embedded Prompt", layout)

while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
    if event == "Run":
        start_num_i = 0
        if len(values["start_num"]) > 0:
            start_num_i = int(values["start_num"])
        rename(values["input_dir"], values["name_prefix"], start_num_i)
window.close()
# print(values)