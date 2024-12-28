from djitellopy import tello
import time
import key_press_module
import cv2
import os


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
    elif key_press_module.get_key("z"):
        cv2.imwrite(f"resources/images/{time.time()}.jpg", img)
        time.sleep(0.3)

    return [left_right, forward_back, up_down, yaw]


def main():
    global img

    global drone
    os.makedirs("resources/images", exist_ok=True)
    key_press_module.init()

    drone = tello.Tello()
    drone.connect()
    print(drone.get_battery())

    drone.streamon()

    while True:
        left_right, forward_back, up_down, yaw = get_keyboard_input()
        drone.send_rc_control(left_right, forward_back, up_down, yaw)

        img = drone.get_frame_read().frame
        img = cv2.resize(img, (144, 144))
        cv2.imshow("Stream", img)
        cv2.waitKey(1) # 1ms delay


if __name__ == '__main__':
    main()
