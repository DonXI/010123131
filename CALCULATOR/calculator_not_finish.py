################################################################
# File: calculator PySimpleGui
# No: 6201012620082
################################################################
import PySimpleGUI as sg

button_num : dict = {'size' : (4,1), 'button_color' : ('black',"#F8F8F8"),
                     'font' : ('Franklin Gothic Book', 14)}

layout = [
    [sg.Text('0.0',size = (14,1), justification='right', font=('Franklin Gothic Book', 16), 
                background_color='black', text_color='red', key = "output"), sg.Button('C', **button_num)],
    [sg.Button('7',**button_num), sg.Button('8',**button_num), 
                sg.Button('9',**button_num), sg.Button('/',**button_num)],
    [sg.Button('4',**button_num), sg.Button('5',**button_num), 
                sg.Button('6',**button_num), sg.Button('*',**button_num)],
    [sg.Button('1',**button_num), sg.Button('2',**button_num), 
                sg.Button('3',**button_num), sg.Button('-',**button_num)],
    [sg.Button('0',**button_num), sg.Button('.',**button_num), 
                sg.Button('=',**button_num, bind_return_key=True), sg.Button('+',**button_num)]
]

window = sg.Window('CALCULATOR', layout)

while True:
    event, values = window.read()
    print(event)
    if event is None:
        break
