from rplidar import RPLidar
import keyboard
import time

lidar = RPLidar('COM5', baudrate=115200, timeout=3)

# info = lidar.get_info()
# print(info)

# health = lidar.get_health()
# print(health)

lidar.start_motor()
# lidar.motor_speed = 800
print("Motor speed:",lidar.motor_speed)
# time.sleep(5)
# lidar.start()
# for scan in lidar.iter_scans(max_buf_meas=10000):
# for scan in lidar.iter_scans(scan_type='normal',min_len=100,max_buf_meas=False):
    # filtered_angles = []
    # print(scan,"\n")
    # print(len(scan))

    # for point in scan:
    #     try:
    #         angle = point[1]
    #         distance = point[2]  
    #     except IndexError:
    #         continue
    #     if angle > 325 and angle < 360 or angle >= 0 and angle <= 35:
    #         # filtered_angles = point
    #          print(angle,":",distance)
    # break

    # if len(filtered_angles) != 0:
    #     print(filtered_angles)
while True:
    lidar.start()
    if keyboard.is_pressed('esc'):
            print('Exiting...')
            break


lidar.stop()
lidar.stop_motor()
lidar.disconnect()