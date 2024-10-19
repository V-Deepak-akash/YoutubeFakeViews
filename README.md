# YouTube Fake views bot in Brave with Tor

## Description

This project is a Python application that opens YouTube links in the Brave browser using Tor for privacy. It allows users to specify the number of tabs to open and automatically handles popups and cookie consent notices. The application also supports saving the last used YouTube link and the mouse coordinates for automated interactions.

## Features

- Open YouTube links in a new private Brave browser window with Tor enabled.
- Specify the number of tabs to open.
- Automatically handles bot verification popups and cookie consent.
- Saves the last used YouTube link and mouse coordinates for future use.
- User-friendly GUI built with Tkinter.

## Requirements

- Python 3.x
- `tkinter`
- `pyautogui`
- `plyer`
- `opencv-python`
- `pytesseract`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/V-Deepak-akash/YoutubeFakeViews.git
   cd youtube-link-opener
   ```
2.Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3.Install Tesseract-OCR: Tesseract-OCR is used for optical character recognition in the application. Follow these steps to install it:

Download the installer from the [Tesseract-OCR GitHub page](https://github.com/tesseract-ocr/tesseract). You will find installation instructions specific to your operating system.

Run the installer and follow the on-screen instructions to complete the installation.

After installing Tesseract, note the installation path (usually C:\Program Files\Tesseract-OCR\tesseract.exe on Windows).

Update the Tesseract path in the script: Open the script youtube_link_opener.py in a text editor. Find the line that sets the Tesseract command path:
   ```bash
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```
Ensure that the path matches the location where Tesseract was installed. If you installed it in a different directory, update the path accordingly.

4.Install Brave Browser: If you don’t have the Brave browser installed, the application can automatically install it for you. If you already have it installed, the application will use the existing installation

## Usage
Run the application: In your terminal or command prompt, navigate to the project directory and run:
   ```bash
   python youtube_link_opener.py
   ```
Enter the YouTube link: In the application window, type or paste the YouTube link you want to open.

Specify the number of tabs: Enter the desired number of tabs you want to open.

Open the link: Click the "Open in Brave" button to launch the links in the Brave browser.

Record Mouse Position :
This feature allows you to automate mouse clicks for opening a new private window and resetting the Tor connection in Brave. Here's how it works:

Click the "Record Mouse Position" button.
You'll receive a notification asking you to position your mouse over the "Customize and Control Brave" which looks like this ![image](https://github.com/user-attachments/assets/9aac0fa4-750c-4b8d-88c6-41c94fc50f2f)
 button in Brave.
Move your mouse to the button and wait for 5 seconds while the program records the coordinates.
After that, you'll get another notification to position your mouse over the "New Private Window with Tor" option in Brave's menu.
Again, move your mouse to this option and wait for 5 seconds.
Once both positions are recorded, the program will save the coordinates and use them to automate clicking these buttons when needed.

## Contributing
Contributions are welcome! If you would like to contribute, please feel free to submit a pull request or open an issue to discuss changes.
