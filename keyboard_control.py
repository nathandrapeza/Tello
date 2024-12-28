from djitellopy import tello
from time import sleep
import KeyPressModule

KeyPressModule.init()

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

def get_keyboard_input():
    left_right, forward_back, up_down, yaw = 0, 0, 0, 0
    speed = 50

    if KeyPressModule.get_key("LEFT"):
        left_right = -speed
    elif KeyPressModule.get_key("RIGHT"):
        left_right = speed
    elif KeyPressModule.get_key("UP"):
        forward_back = speed
    elif KeyPressModule.get_key("DOWN"):
        forward_back = -speed
    elif KeyPressModule.get_key("w"):
        up_down = speed
    elif KeyPressModule.get_key("s"):
        up_down = -speed
    elif KeyPressModule.get_key("a"):
        yaw = speed
    elif KeyPressModule.get_key("d"):
        yaw = -speed
    elif KeyPressModule.get_key("e"):
        drone.takeoff()
    elif KeyPressModule.get_key("q"):
        drone.land()

    return [left_right, forward_back, up_down, yaw]


def main():
    while True:
        left_right, forward_back, up_down, yaw = get_keyboard_input()
        drone.send_rc_control(left_right, forward_back, up_down, yaw)
        sleep(0.05)


if __name__ == '__main__':
    main()
