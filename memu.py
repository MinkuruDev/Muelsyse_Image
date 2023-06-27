import keyboard
from PIL import Image, ImageGrab
from datetime import datetime

def saveMumuImage(): 
    now = datetime.now()
    current_time = now.strftime("%Y_%m_%d %H_%M_%S")
    img = ImageGrab.grabclipboard()
    img.save(f"./Muelsyse/{current_time}.png")
    print("saved: ", current_time)

def main():
    keyboard.add_hotkey('F12', saveMumuImage)
    keyboard.wait()

if __name__ == "__main__":
    main()
