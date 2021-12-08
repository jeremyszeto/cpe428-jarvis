from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

SCREEN_WIDTH  =  2080
SCREEN_HEIGHT =  1800

def launchBrowser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://google.com")
    return driver

# based on gestures found here: 
# https://gibranbenitez.github.io/IPN_Hand/Classes

def one_finger_point(driver):
    # track mouse
    pass

def two_finger_point(driver):
    # scroll
    pass

def one_finger_click(driver):
    # click
    pass

def two_finger_click(driver):
    # right click
    pass

def throw_up(driver):
    # maximize window
    print("maximizing window...")
    driver.maximize_window()

def throw_down(driver):
    # minimize window
    print("minimizing window...")
    driver.minimize_window()

def throw_left(driver):
    # snap to left side of screen
    print("snapping left")
    width = driver.get_window_size().get("width")
    height = driver.get_window_size().get("height")
    driver.set_window_position(0, 0)
    driver.set_window_size(SCREEN_WIDTH/2, SCREEN_HEIGHT)

def throw_right(driver):
    # snap to right side of screen
    print("snapping right")
    width = driver.get_window_size().get("width")
    height = driver.get_window_size().get("height")
    driver.set_window_position(SCREEN_WIDTH/2, 0)
    driver.set_window_size(SCREEN_WIDTH/2, SCREEN_HEIGHT)

def open_twice(driver):
    # take screenshot
    pass

def one_finger_double_click(driver):
    pass

def two_finger_double_click(driver):
    pass

def zoom_in(driver):
    # zoom in
    print("zooming in...")
    driver.execute_script("document.body.style.MozTransform='scale(1.5)';")

def zoom_out(driver):
    # zoom out
    print("zooming out...")
    driver.execute_script("document.body.style.MozTransform='scale(0.5)';")

def main():
    s = Service('./geckodriver')
    # create driver
    driver = webdriver.Firefox(service=s)
    driver.implicitly_wait(10) # seconds
    # driver.set_context("chrome")
    driver.get("https://google.com")

    # possible actions:
    actions = {
        "one_finger_point": one_finger_point,
        "two_finger_point": two_finger_point,
        "one_finger_click": one_finger_click,
        "two_finger_click": two_finger_click,
        "throw_up"        : throw_up,
        "throw_down"      : throw_down,
        "throw_left"      : throw_left,
        "throw_right"     : throw_right,
        "open_twice"      : open_twice,
        "one_finger_double_click": one_finger_double_click,
        "two_finger_double_click": two_finger_double_click,
        "zoom_in"         : zoom_in,
        "zoom_out"        : zoom_out
    }
    # new tab

    # take input from neural net
    # while True:
        # get input
        # action = getInput()
        # print("The detected action is: {}".format(actions[action]))
    
    # switch tab right
    # switch tab left
    # new tab
    # scroll up/down
    # zoom in/out
    # minimize

    # throw_down(driver)
    # sleep(2)
    throw_up(driver)
    sleep(2)
    zoom_in(driver)
    sleep(2)
    zoom_out(driver)
    sleep(2)
    throw_left(driver)
    sleep(2)
    throw_right(driver)
    sleep(2)
    throw_down(driver)
    sleep(5)
    driver.quit()


if __name__ == "__main__":
    # driver = launchBrowser()
    # driver.minimize_window()
    # driver.maximize_window()
    # time.sleep(15)
    main()