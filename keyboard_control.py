from djitellopy import tello
from time import sleep
import key_press_module

def get_keyboard_input():
    """
    Gets the user's keyboard input, and returns a list of values to be used to control the drone.

    drone (tello.Tello): Tello object representing the physical drone being used.

    Returns a list of values to be used as arguments to command the drone's direction/movement.
    """
    left_right, forward_back, up_down, yaw = 0, 0, 0, 0
    speed = 50

    if key_press_module.get_key("LEFT"):
        left_right = -speed
    elif key_press_module.get_key("RIGHT"):
        left_right = speed
    elif key_press_module.get_key("UP"):
        forward_back = speed
    elif key_press_module.get_key("DOWN"):
        forward_back = -speed
    elif key_press_module.get_key("w"):
        up_down = speed
    elif key_press_module.get_key("s"):
        up_down = -speed
    elif key_press_module.get_key("a"):
        yaw = speed
    elif key_press_module.get_key("d"):
        yaw = -speed
    elif key_press_module.get_key("e"):
        drone.takeoff()
    elif key_press_module.get_key("q"):
        drone.land()

    return [left_right, forward_back, up_down, yaw]


def main():
    global drone

    key_press_module.init()

    drone = tello.Tello()
    drone.connect()
    print(drone.get_battery())

    while True:
        left_right, forward_back, up_down, yaw = get_keyboard_input()
        drone.send_rc_control(left_right, forward_back, up_down, yaw)
        sleep(0.05)

if __name__ == '__main__':
    main()
