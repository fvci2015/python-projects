import pyautogui
import time

class Clicker:
    def __init__(self, times):
        self.times = times
        self.click_count = 0

    def click(self):
        pyautogui.leftClick()
        self.click_count += 1

    def start_clicking(self):
        time.sleep(2)  # Initial delay
        while self.click_count < self.times:
            self.click()
        print("Stopped Clicking")
if __name__ == "__main__":
    times = 20  # Change this to the number of times you want it to click
    clicker = Clicker(times)
    clicker.start_clicking()
