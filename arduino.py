import time
import serial
import pandas as pd
from test import stop_Flag
import process_manager

'''
Print Sensor Readings Code:
now4 = datetime.now()
time_string4 = now4.strftime("%H:%M:%S:%f")
#print(f"-{self.name}4-{time_string4}T: {value_A4}")
'''

class Arduino:
    #Initializer
    #Establish Serial Connection
    def __init__(self, port, baudrate, name, dq, acquire, data):
        self.name = name
        self.dq = dq
        self.serial = serial.Serial(port, baudrate, timeout= 10, dsrdtr=True)
        print(f'Arduino Connected!')
        self.run = True
        self.acquire = acquire
        self.data = data

    def read(self, barrier):
        print(f'{self.name} preparing to run...')
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()
        time.sleep(2) #Allow time for Arduinos to prepare

        # check if arduino is a part of data acquisition
        if self.acquire:
            while self.run:
                try:
                    # write A4 to serial buffer so Serial.available() > 0 is true
                    self.serial.write(b'A4\n')  # Request reading from A4
                    value_A4 = float(self.serial.read_until(expected=b'\n').decode().strip().replace('\r.', ''))
                    self.dq.put([self.name+'4', value_A4]) # store value in queue
                    self.data[0].append(value_A4)
                    barrier.wait(timeout=5)

                    # write A5 to serial buffer so Serial.available() > 0 is true
                    self.serial.write(b'A5\n') #A5 Reading
                    value_A5 = float(self.serial.read_until(expected=b'\n').decode().strip().replace('\r.', ''))
                    self.dq.put([self.name+'5',value_A5]) # store value in queue
                    self.data[1].append(value_A5)
                    barrier.wait(timeout=5)

                    # write A5 to serial buffer so Serial.available() > 0 is true
                    self.serial.write(b'A6\n') #A6 Reading
                    value_A6 = float(self.serial.read_until(expected=b'\n').decode().strip().replace('\r.', ''))
                    self.dq.put([self.name+'6',value_A6]) # store value in queue
                    self.data[2].append(value_A6)
                    barrier.wait(timeout=5)

                    time.sleep(0.001)

                except Exception:
                    self.dq.put(["STOP", -1.0])

        else:
            self.serial.write(b'Start\n')

            while self.run:
                try:
                    value = self.serial.read_until(expected=b'\n').decode().strip().replace('\r.', '')
                    if value == 'End':
                        process_manager.terminate_processes()
                    else:
                        self.dq.put([self.name,float(value)])
                        self.data.append(float(value))

                except Exception:
                    self.dq.put(["STOP", -1.0])


    def stop(self):
        self.run = False
        df = pd.DataFrame()
        if not self.acquire:
            df[self.name] = list(self.data)
            self.serial.write(b'Finish\n')
        else:
            # Convert each Manager sublist to a regular list
            data_lists = [list(self.data[i]) for i in range(3)]
            # Find the minimum length among the lists
            min_length = min(len(lst) for lst in data_lists)
            # Truncate each list to the same length
            data_dict = {self.name + str(i): lst[:min_length] for i, lst in enumerate(data_lists)}
            df = pd.DataFrame(data_dict)
        df.to_csv(self.name + '_data.csv', index=False)
        print('Stop run')
        self.dq.put(["STOP", -1.0])
        stop_Flag.value += 1
        if self.serial.is_open:
            self.serial.close()
        print(f'Closed {self.name} Serial Connection')

