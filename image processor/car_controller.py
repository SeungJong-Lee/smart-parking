import socket, threading, keyboard

class Manual_control:
    def __init__(self) -> None:
        self.arduino = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        MAC = '98:d3:31:f6:0b:4b'
        self.arduino.connect((MAC,1))
        threading.Thread(target=self.drive).start()
    
    def send(self, msg):
        while 1:
            self.arduino.send(f'{msg}'.encode())
            if self.arduino.recv(1).decode()=='O':
                    break
    
    def drive(self):
        print('Manual drive')
        while 1:
            if keyboard.is_pressed('w'):
                self.send('whb')
            elif keyboard.is_pressed('s'):
                self.send('shb')
            elif keyboard.is_pressed('a'):
                self.send('lzz')
            elif keyboard.is_pressed('d'):
                self.send('rzz')
            elif keyboard.is_pressed('q'):
                self.send('Q')
            elif keyboard.is_pressed('e'):
                self.send('W')
            else:
                self.send('Ppp')
                self.send('ppp')
#Manual_control()