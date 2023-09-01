import pyautogui
import subprocess
import time
import pygetwindow as gw
import win32gui
import win32con
import os 
import shutil 

#! Open console (cmd or powershell) in the D:\Webpass by doing cd D:\WebPass
#! Run pip install -r requirements.txt in the console before running the script
#! make sure you have the script placed in D:\ (in a USB or a partition named D:\, you can change this but I've made the script with D Drive in mind)
#! Make sure that you have the script in a folder called Webpass
#! Do not adjust the delays in the script as it might not work



source_path = r'D:\WebPass'
user_profile3 = os.path.expanduser("~")
destination_path = os.path.join(user_profile3, 'Desktop', 'WebPass')

# Step 1: Copy the folder from source to user's desktop
shutil.copytree(source_path, destination_path)



# Get the user profile path
user_profile2 = os.path.expanduser("~")

# Construct the file path to Desktop\WebPass\
file_path2 = os.path.join(user_profile2, 'Desktop', 'WebPass')

# Check if the file path exists
if os.path.exists(file_path2):

    # Run the launch_webbrowser.bat file
    subprocess.run(os.path.join(file_path2, 'launch_webbrowser.bat'), shell=True)


# Add a delay before the script starts (you can adjust this value as needed)
time.sleep(1)

def maximize_window_by_title(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

# Replace 'WebBrowserPassView' with the actual window title of the application
window_title = 'WebBrowserPassView'

# Launch the application 'WebBrowserPassView.exe' (if not already running) before running this script
# Your code to run the application or perform any other tasks

# Add a delay to allow the application to fully launch (you may need to adjust this value)
time.sleep(0)

# Maximize the window by the window title
maximize_window_by_title(window_title)

# Find the window with the title 'WebBrowserPassView' (exact title or a substring)
web_pass_view_window = gw.getWindowsWithTitle('WebBrowserPassView')[0]

# Activate the 'WebBrowserPassView' window
web_pass_view_window.activate()

# Perform a left click at (x=523, y=146)
pyautogui.moveTo(523, 146)
pyautogui.click()

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 's')

time.sleep(0)

user_profile = os.path.expanduser("~")

# Construct the file path to Desktop\WebPass\
file_path = os.path.join(user_profile, 'Desktop', 'WebPass')

# Copy the file path to the clipboard
pyautogui.write(file_path)

pyautogui.press('enter')

time.sleep(0)

# Move the mouse to (x=445, y=261) and then perform a left click to paste the directory
pyautogui.moveTo(445, 261)
pyautogui.click()

pyautogui.hotkey('ctrl', 'v')

pyautogui.press('enter')

time.sleep(0)

# Move the mouse to (x=198, y=419) and then perform a left click to write file name
pyautogui.moveTo(198, 419)
pyautogui.click()

pyautogui.write('passwords')

# Move the mouse to (x=504, y=484) and then perform a left click to save the file
pyautogui.moveTo(504, 484)
pyautogui.click()
subprocess.run(["taskkill", "/F", "/IM", "WebBrowserPassView.exe"])
shutil.move(destination_path, r'D:\WebPass_Copied')