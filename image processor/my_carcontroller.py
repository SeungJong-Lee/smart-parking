import socket, keyboard

arduino = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
MAC = '98:d3:31:f6:0b:4b'
arduino.connect((MAC,1))

while True:
    if keyboard.is_pressed('w'):
        msg='wqa'
    elif keyboard.is_pressed('s'):
        msg='sqa'
    elif keyboard.is_pressed('a'):
        msg='rqz'
    elif keyboard.is_pressed('d'):
        msg='lqz'
    elif keyboard.is_pressed('p'):
        msg='ppp'
    elif keyboard.is_pressed('P'):
        msg='Ppp'
    elif keyboard.is_pressed('q'):
        msg='Q'
    elif keyboard.is_pressed('e'):
        msg='W'
    else:
        msg = 'ppp'
        while 1:
            arduino.send(f'{msg}'.encode())
            if arduino.recv(1).decode()=='O':
                break
        msg = 'Ppp'
    while True:
        arduino.send(f'{msg}'.encode())
        if arduino.recv(1).decode()=='O':
            break



            