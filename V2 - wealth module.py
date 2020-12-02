import PySimpleGUI as sg

sg.theme('LightBrown3')


layout = [[sg.Text('Your Current Wealth', justification='center', size=(25, 1),
             font=("Times", 25), relief=sg.RELIEF_RIDGE)],
          [sg.Text()],
          [sg.Text('To calculate your current wealth fill in the value of your asssets and your monthly income.',
            size = (42,3), justification = 'center', font = ("Times", 14))],
          [sg.Text('Your total savings:', size = (30,1),font = ("Times", 14)),
           sg.Input(size = (10,1),font = ("Times", 14), key ='-SAVINGS-', enable_events = True, justification = 'right')],
          [sg.Text('Your shares:',size = (30,1),font = ("Times", 14)),
           sg.Input(size = (10,1),font = ("Times", 14), key = '-SHARES-', justification = 'right')],
          [sg.Text('Your precious metals:', size = (30,1),font = ("Times", 14)),
           sg.Input(size = (10,1),font = ("Times", 14), key = '-METALS-', justification = 'right')],
          [sg.Text('Any other investments:',size = (30,1),font = ("Times", 14)),
           sg.Input(size = (10,1),font = ("Times", 14), key = '-OTHER-', enable_events = True, justification = 'right')],
          [sg.Text(95 * '-')],
          [sg.Text('Your monthly income:', size=(30, 1), font=("Times", 14)),
          sg.Input(size=(10, 1), font=("Times", 14), key = ('-INCOME-'), justification = 'right')],
          [sg.Text()],
          [sg.Text('''Pressing the button below will calculate your total assets. The second number showes your real wealth. It measures how long will you be able to live in case you suddenly lost all your income. Will you have enough time to find another job? Or to educate yourself in some other profession?''',
            size=(45, 6), font=("Times", 14))],

          [sg.Text(size = (20,1)), sg.Button ('Result', size = (12,1),border_width=3,key = 'OK', use_ttk_buttons=True)],
          [sg.Text()],

          [sg.Frame('',layout=[
              [sg.Text('Assets total:', size=(30, 1), font=("Times", 16)),
               sg.Text(size=(10, 1), font=("Times", 16), text_color='Brown', key='-TOTAL-')],
              [sg.Text('Your wealth in months:', size=(30, 1), font=("Times", 16)),
           sg.Text (size=(10, 1), font=("Times", 16), text_color='Brown', key = '-WEALTH-')],
            ])]]

window = sg.Window('', layout, default_element_size=(40, 1), grab_anywhere=True,
                   auto_size_text = True, resizable = True)

while True:
    event, values = window.read()
    print(event,values)
    if event ==sg.WIN_CLOSED:
        break
    if event == 'OK':

        i1=values['-SAVINGS-']
        i2=values['-SHARES-']
        i3=values['-METALS-']
        i4=values['-OTHER-']
        resultT = float(i1)+float(i2)+float(i3)+float(i4)
        Total = round(resultT,2)
        inc = values['-INCOME-']
        w = float(Total) / float(inc)
        totalw = round(w, 1)

        window['-TOTAL-'].update(Total)




        window['-WEALTH-'].update(totalw)

window.close()


