import datetime
import os
import smtplib
from email.message import EmailMessage
from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime

#LAYOUT

sg.SetOptions(background_color='white',
       text_element_background_color='white',
       text_color='#0e0e0e',
       input_elements_background_color='white',
       button_color=('white','#375a64'),
       font=('ARIAL BLACK',9),
       element_background_color='white',

)



layout = [

    [sg.Text('Nome')],
    [sg.Input(key='nome', size=(42,1))],

    [sg.Text('Email', size=(20,1))],
    [sg.Input(key='email', size=(42,1))],

    [sg.Text('Valor: R$'), sg.Spin(values=list(range(999999)), key='valor', initial_value=1000, size=(10,1))],

    [sg.Button('Enviar', key='enter', size=(10,1)), sg.Button('Cancelar', key='cancel', button_color='#ff4f5b', size=(10,1))],

    [sg.Output(size=(42,5))],

]

janela = sg.Window('Enviar Email', layout)


while True:

    eventos, valores = janela.read()

    if eventos == sg.WIN_CLOSED:
        break

    if eventos == 'cancel':
        break

    if eventos == 'enter':



        nome = valores['nome']
        email = valores['email']
        valor = valores['valor']



        os.system('cls')



        try:
            data_e_hora_atual = datetime.now()
            data_e_hora = data_e_hora_atual.strftime('%d/%m/%Y às %H:%M')
            corpo_email = f""""
                         <p>Olá, <b>{nome}</b></p>
                         <p>Seu Pagamento no valor de <b style="color: 'green'">R${valor}</b> foi enviado para sua conta</p>
                         <p><b>Por favor, verifique sua conta!</b></p>

                         <p>{data_e_hora}</p>
                         """

            msg = EmailMessage()
            msg['Subject'] = 'Informações'
            msg['From'] = 'cdlr.emailteste@gmail.com'
            msg['To'] = email
            password = 'pass'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)


            envio = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            envio.login('cdlr.emailteste@gmail.com', password=password)
            envio.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
            print('EMAIL ENVIADO')


        except:
            print(f'ERRO AO ENVIAR O EMAIL')
