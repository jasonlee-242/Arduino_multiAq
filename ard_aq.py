#Libraries
from arduino import *
from plotter import *
import multiprocessing as mp
import sys
import glob

def openArduino(barrier, name, port, dqueue, baudrate = 115200):
    ard = Arduino(port, baudrate, name, dqueue)
    ard.read(barrier)
    return

def startPlotter(dqueue,colors):
    plotter = RealTimePlotter(dqueue,colors)
    plotter.start()
    return

def find_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/ttyUSB*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/ttyUSB*')
    else:
        raise Exception('Unsupported Platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass

    return result

if __name__ == "__main__":

    sensorColors = {
        'R4': (255,0,0),
        'R5': (132,5,5),
        'R6': (202,112,112),
        'G4': (0,255,0),
        'G5': (5,132,5),
        'G6': (112,202,112),
        'B4': (0,0,255),
        'B5': (5,5,132),
        'B6': (77,115,153)
    }

    sensor_barrier = mp.Barrier(3)
    dataQueue = mp.Queue()
    emptyQueue = mp.Queue()

    ports = find_ports()
    names = ["R", "B", "G"]

    # Instantiate 3 arduinos for data acquisition
    arduino_instances = [Arduino(ports[i], 115200, names[i], dataQueue, True) for i in range(3)]
    # Instantiate another arduino for cuff pressurization
    arduino_instances.append(Arduino(ports[3], 9600, "Cuff", emptyQueue, False))

    # ard_processes = [mp.Process(target=openArduino, args=(sensor_barrier,
    #                      names[i], ports[i], dataQueue)) for i in range(len(ports))]
    ard_processes = [mp.Process(target = arduino_instances[i].read, args=(sensor_barrier,)) for i in range(len(ports))]
    ard_processes.append(mp.Process(target = startPlotter, args=(dataQueue, sensorColors)))

    process_manager.set_instances(arduino_instances)

    for p in ard_processes:
        p.start()

    while stop_Flag.value != len(arduino_instances):
        continue

    for arduino in range(len(ard_processes)):
        ard_processes[arduino].terminate()
        print('Joining Arduino...')
        ard_processes[arduino].join()

    print("Acquisition Finished!")
