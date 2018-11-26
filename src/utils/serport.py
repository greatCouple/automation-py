# -- coding: utf-8 --
import serial

serport = serial.Serial(port='COM4', baudrate=115200, timeout=2)


class SerialPort:
    def switchAdb(self):
        serport.write(b'\r$EEPD\r')
        serport.write(b'\r$EEPU\r')
        serport.write(b'\r$EEPP\r')


if __name__ == "__main__":
    SerialPort().switchAdb()
