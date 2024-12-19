
import serial,time
pic=serial.Serial("COM6",9600)


while(1):
    menu = input()
    if menu == ("a"):
        envio_pic="033"
        pic.write(envio_pic.encode())
        envio_pic = "P"
        pic.write(envio_pic.encode())
        time.sleep(1)
        envio_pic = "000"
        pic.write(envio_pic.encode())
        envio_pic = "M"
        pic.write(envio_pic.encode())

    if menu== ("s"):
        envio_pic="002"
        pic.write(envio_pic.encode())
        envio_pic = "M"
        pic.write(envio_pic.encode())
        time.sleep(1)
        envio_pic = "000"
        pic.write(envio_pic.encode())
        envio_pic = "P"
        pic.write(envio_pic.encode())

    if menu== ("d"):
        envio_pic="035"
        pic.write(envio_pic.encode())
        envio_pic = "G"
        pic.write(envio_pic.encode())
        time.sleep(1)
        envio_pic = "000"
        pic.write(envio_pic.encode())
        envio_pic = "G"
        pic.write(envio_pic.encode())