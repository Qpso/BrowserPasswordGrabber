# Simple Web Browser Password Grabber

This is a simple script that can be used to grab passwords from web browsers. Please note that this script is intended for educational purposes only and should not be used for malicious activities.

## Getting Started

Follow these steps to set up and run the password grabber:

1. **Download and Extract Files**
   - Download the files as a zip archive.
   - Extract the contents to a partition or a USB drive with drive letter `D:\`.
   - Create a folder called `WebPass` in the `D:\` drive.

2. **Download WebBrowserPassViewer**
   - Download the program [WebBrowserPassViewer](https://www.nirsoft.net/utils/web_browser_password.html).
   - Put `WebBrowserPassView.exe` and `WebBrowserPassView.cfg` in the `WebPass` folder you created in step 1.

3. **Install Dependencies**
   - Open a terminal (cmd or PowerShell).
   - Navigate to the `WebPass` folder by typing `cd D:\WebPass`.
   - Run the following command to install the required dependencies:
     ```shell
     pip install -r requirements.txt
     ```

4. **Run the Script**
   - After installing the dependencies, you can run the script.
   - The script will grab passwords using PyAutoGUI, simulating mouse and keyboard actions.
   - The stolen passwords will be saved in a folder called `WebPass_Copied`.
   - You can find the passwords at `D:\WebPass_Copied\passwords.txt`.

Alternatively, you can run the provided executable after completing the above steps instead of running the script, This is my first attempt at a script like this, and I'm not oblivious to the many inefficient techniques I've used. So, if you have any suggestions or have found any bugs, please let me know.

**Note:** Please use this script responsibly and only on systems you have permission to access. Unauthorized use of this script may violate privacy and legal regulations. Also this script has a hard time running with Windows 11 sometimes.


## Disclaimer

This script is for educational purposes only. The author is not responsible for any misuse or damage caused by its use.
