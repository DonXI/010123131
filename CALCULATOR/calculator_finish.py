################################################################
# File: calculator PySimpleGui
# No: 6201012620082
################################################################
import PySimpleGUI as sg

button_num : dict = {'size' : (4,1), 'button_color' : ('black',"#F8F8F8"),
                     'font' : ('Franklin Gothic Book', 14)}
sg.theme('DarkTeal')
layout = [
    [sg.Text('',size = (15,1), justification='right', font = ('Franklin Gothic Book', 20), 
                background_color='black', text_color='red', key = "val")],
    [sg.Button("AC",**button_num), sg.Button('C',**button_num), 
                sg.Button("+/-",**button_num), sg.Button('/',**button_num)],
    [sg.Button('7',**button_num), sg.Button('8',**button_num), 
                sg.Button('9',**button_num), sg.Button('*',**button_num)],
    [sg.Button('4',**button_num), sg.Button('5',**button_num), 
                sg.Button('6',**button_num), sg.Button('-',**button_num)],
    [sg.Button('1',**button_num), sg.Button('2',**button_num), 
                sg.Button('3',**button_num), sg.Button('+',**button_num)],
    [sg.Button('%',**button_num), sg.Button('0',**button_num), 
                sg.Button('.',**button_num), sg.Button('=',**button_num)]
]

window = sg.Window('CALCULATOR', layout)

output = ' '

while True:
    event, values = window.read()
    print(event)
    if event is None:
        break
    if event == 'AC':
        output = ''
        window['val'].update(output)
    if event == 'C':
        try:
            output = output[:-1]
            window['val'].update(output)
        except:
            output = ''

    if event in ['0','1','2','3','4','5','6','7','8','9']:
        output += event
        window['val'].update(output)

    if event in ['+','-','*','/']:
        output += event
        window['val'].update(output)

    if event =='.':
        output += event
        window['val'].update(output)
    
    if event == '=':
        try:
            output = str(float(eval(output)))
            window['val'].update(output)
        except:
            pass

    if event == '%':
        output = str(float(output) / 100)
        window['val'].update(output)

    if event == '+/-':
        output = str(float(output) * (-1))
        window['val'].update(output)