import PySimpleGUI as sg

sg.theme ('LightBrown3')
layout = [[sg.Text('WEALTH CALCULATOR')],
          [sg.Text('Initial Amount', size=(20,1)),sg.InputText(key='-PRINCIPAL-',size=(20,1))],
          [sg.Text ('Annual Interest', size=(30,1)),sg.InputText(key='-INTEREST-', size=(10,1))],
          [sg.Text ('Number of years', size=(30,1)), sg.InputText(key='-YEARS-', size=(10,1))],
          [sg.Text('TOTAL', size =(20,1)),sg.InputText(key='-OUTPUT-',size=(20,1))],
          [sg.Button('Compute Result')]]

window=sg.Window('WEALTH CALCULATOR', layout, element_justification='center')
#event loop
while True:
    event, values = window.read()
    print(event,values)
    if event ==sg.WIN_CLOSED:
        break
    if event =='Compute Result':
        a=values['-PRINCIPAL-']
        b=values['-INTEREST-']
        c=values['-YEARS-']
        result = float(a)*(1+0.01*float(b))**float(c)
        window['-OUTPUT-'].update(result)

window.close()
exit()

