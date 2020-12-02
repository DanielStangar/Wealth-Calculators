import PySimpleGUI as sg

sg.theme ('LightBrown3')
layout = [[sg.Text('WEALTH CALCULATOR')],
          [sg.Text('Initial Amount', size=(20,1)),sg.InputText(key='-PRINCIPAL-',size=(20,1))],
          [sg.Text ('Annual Interest', size=(30,1)),sg.InputText(key='-INTEREST-', size=(10,1))],
          [sg.Text ('Monthly Instalments', size=(30,1)),sg.InputText(key='-INSTALMENT-', size=(10,1))],
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
        p=values['-PRINCIPAL-']
        i=values['-INTEREST-']
        t=values['-YEARS-']
        m=values['-INSTALMENT-']
        mi = float(0.01*float(i)/12)
        exp = 12*float(t)
        result1 = float(p)*(1+float(mi))**int(exp)
        result2 = int(m)*(((1+float(mi))**int(exp))-1 )/float(mi)
        resultT = result1+result2
        Total = round(resultT,2)

        window['-OUTPUT-'].update(Total)

window.close()
exit()

