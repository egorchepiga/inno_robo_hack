import socket
import time
host = '127.0.0.1'
port = 10099

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))
client.send(bytes('ROBOT:MOTORS:HeadR:POSSET:-30\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.Elbow:POSSET:-95\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.WristR:POSSET:-90\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.ElbowR:POSSET:-55\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:TorsoF:POSSET:55\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.ShoulderS:POSSET:-90\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.ShoulderS:POSSET:-90\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.ShoulderS:POSSET:-100\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.WristR:POSSET:-100\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:TorsoR:POSSET:15\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.WristF:POSSET:8\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.Finger.Thumb:POSSET:-90\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.Finger.Ring:POSSET:90\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.Finger.Little:POSSET:90\r\n\r\n','ASCII'))
time.sleep(5)
client.send(bytes('ROBOT:MOTORS:R.WristF:POSSET:10\r\n\r\n','ASCII'))
time.sleep(1)

#open
client.send(bytes('ROBOT:MOTORS:TorsoF:POSSET:-90\r\n\r\n','ASCII'))
time.sleep(1)
client.send(bytes('ROBOT:MOTORS:R.ShoulderS:POSSET:60\r\n\r\n','ASCII'))
client.send(bytes('ROBOT:MOTORS:R.Elbow:POSSET:900\r\n\r\n','ASCII'))
client.send(bytes('ROBOT:MOTORS:TorsoR:POSSET:-70\r\n\r\n','ASCII'))
client.send(bytes('ROBOT:MOTORS:R.Finger.Ring:POSSET:-90\r\n\r\n','ASCII'))
client.send(bytes('ROBOT:MOTORS:R.Finger.Little:POSSET:-90\r\n\r\n','ASCII'))

response = client.recv(1024)

print(response)

client.close()