'''Measures sensor scanning speed'''
import rplidar
import time

PORT_NAME = 'COM5'

def run():
    '''Main function'''
    lidar = rplidar.RPLidar(PORT_NAME)
    old_t = None
    data = []
    try:
        print('Press Ctrl+C to stop')
        lidar.motor_speed = rplidar.MAX_MOTOR_PWM
        for _ in lidar.iter_scans(scan_type='express',min_len=100,max_buf_meas=False):
            now = time.time()
            if old_t is None:
                old_t = now
                continue
            delta = now - old_t
            print('%.2f Hz, %.2f RPM' % (1/delta, 60/delta))
            data.append(delta)
            old_t = now
    except KeyboardInterrupt:
        print('Stoping. Computing mean...')
        lidar.stop()
        # lidar.stop_motor()
        lidar.disconnect()
        delta = sum(data)/len(data)
        print('Mean: %.2f Hz, %.2f RPM' % (1/delta, 60/delta))

if __name__ == '__main__':
    run()