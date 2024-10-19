## YouTube Fake Views Bot in Brave with Tor
## Description
This Python application allows you to open YouTube links in the Brave browser with Tor for enhanced privacy. It automates several tasks, including opening multiple tabs, handling popups, and rejecting cookie consent requests. It also saves your last used YouTube link and mouse coordinates for easy reuse.

## Features
- Open YouTube links in Brave’s private window with Tor.
- Specify the number of tabs to open.
- Automatically detects and handles bot verification and cookie consent popups.
- Saves your last used YouTube link and mouse coordinates for future use.
- Simple and user-friendly graphical interface (GUI) built with Tkinter.

##Requirements
- Python 3.x
- tkinter
- pyautogui
- plyer
- opencv-python
- pytesseract

##Installation
1. Clone the Repository
```
git clone https://github.com/V-Deepak-akash/YoutubeFakeViews.git
```
2. Navigate to the project directory:
```
cd youtube-link-opener
```
3. Install the Required Python Packages
```
pip install -r requirements.txt
```
4. Install Tesseract-OCR
Tesseract-OCR is used for text recognition. You need to install it:

Download the installer from the [Tesseract-OCR GitHub page](https://github.com/tesseract-ocr/tesseract).
Run the installer and follow the on-screen instructions.
Note the installation path (e.g., C:\Program Files\Tesseract-OCR\tesseract.exe on Windows).
Update the Tesseract path in the script:

```
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
Make sure the path matches where you installed Tesseract. If it’s different, update the path accordingly.

5. Install Brave Browser
The application will check if Brave is installed. If not, it can download and install Brave automatically.

## Usage
Run the Application:

In your terminal or command prompt, navigate to the project directory and run:
```
python youtube_link_opener.py
```
Enter the YouTube Link:

In the application window, type or paste the YouTube link you want to open.

Specify Number of Tabs:

Enter how many tabs you want to open.

Open the Link:

Click the "Open in Brave" button, and the links will open in the Brave browser.

Record Mouse Position for Automating Actions
This feature lets you record mouse coordinates to automate actions like opening a new private window and resetting the Tor connection in Brave.

Here’s how:

Click "Record Mouse Position" in the app.
You'll get a notification to position your mouse over the menu button (the three lines at the top right of Brave).
Move your mouse there and wait for 5 seconds to record the position.
Then, you’ll be prompted to move your mouse over the New Private Window with Tor option from the menu.
Again, wait 5 seconds to record this position.
The program saves these coordinates and uses them to automate mouse clicks in Brave.
Contributing
Contributions are welcome! If you have ideas or improvements, feel free to submit a pull request or open an issue to discuss changes


### Instructions to Customize:

1. **Replace `<username>`**: Ensure you replace `<username>` in the clone command with your actual GitHub username.
2. **Update License**: If you have a specific license for your project, mention it in the License section, or create a `LICENSE` file in your repository.
3. **Add any additional information**: You can customize the sections further based on any other specific details related to your project.

This template provides a clear overview of your project, how to install and use it, and encourages contributions. If you need further modifications or details, let me know!
