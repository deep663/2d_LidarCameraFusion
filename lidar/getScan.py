import sys
from rplidar import RPLidar
from datetime import datetime
import keyboard as kb


PORT_NAME = 'COM5'


def run():
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    
    scan_count = 0
    write = False
    scan = 0
    try:
        for measurment in lidar.iter_measures(max_buf_meas=None):
            if kb.is_pressed('s'):
                write = True
                path = f'data/scan{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt'
                outfile = open(path, 'w')
            if write and scan_count < 3:
                line = '\t'.join(str(v) for v in measurment)
                outfile.write(line + '\n')
                if measurment[0] == True:
                    scan_count += 1
            elif(scan_count >= 3):
                outfile.close()
                print("Scan {} finished!".format(scan))
                scan += 1
                scan_count = 0
                write = False
    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()

if __name__ == '__main__':
    run()