import serial
import time
import click

@click.command()
@click.pass_context
@click.option('--comport', prompt="Enter the COM port in COM(portno) format",prompt_required=True, help='COM port of the device')
@click.option('--baudrate', default=9600, help='Baud Rate of the communication')
@click.option('--timestamp/--notimestamp', default=True, help='If the timestamp of printing is to be shown or not')
def readserial(ctx, comport, baudrate, timestamp):
    print(f'Connecting to {comport} at {baudrate} baudrate')
    print('Starting within 5 secs..')
    print()
    time.sleep(5)
    ser = serial.Serial(comport.strip().upper(), baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read
    while True:
        data = ser.readline().decode().strip()

        if data and timestamp:
            timestamp = time.strftime('%H:%M:%S')
            print(f'{timestamp} > {data}')
        elif data:
            print(data)        


if __name__ == '__main__':
    readserial() 
    # readserial('COM6', 9600, True)                          # COM port, Baudrate, Show timestamp