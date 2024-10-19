# YouTube Link Opener in Brave with Tor

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
