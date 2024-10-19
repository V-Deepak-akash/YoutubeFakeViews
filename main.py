import subprocess
import os
import urllib.request
import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
import threading
import time
import pyautogui
from plyer import notification
import cv2
import pytesseract
import numpy as np

# Tesseract-OCR path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# File to store the YouTube link and coordinates
LINK_FILE = "last_youtube_link.txt"
COORDS_FILE = "mouse_coords.txt"

def get_brave_path():
    """Check common locations for Brave Browser installation on Windows."""
    possible_paths = [
        r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

def install_brave():
    """Install Brave Browser by downloading the installer and running it."""
    brave_installer_url = "https://laptop-updates.brave.com/latest/winx64"
    installer_path = os.path.join(os.getenv('TEMP'), 'BraveInstaller.exe')

    update_status("Downloading Brave installer...")
    try:
        urllib.request.urlretrieve(brave_installer_url, installer_path)
        update_status("Download complete.")
    except Exception as e:
        update_status(f"Error downloading Brave installer: {e}")
        return

    update_status("Installing Brave Browser...")
    try:
        subprocess.run([installer_path, "/silent", "/install"], check=True)
        update_status("Brave Browser installation complete.")
    except subprocess.CalledProcessError:
        update_status("Silent installation failed. Trying manual installation...")
        try:
            subprocess.run([installer_path], check=True)
            update_status("Brave Browser installed successfully.")
        except subprocess.CalledProcessError as e:
            update_status(f"Manual installation failed: {e}. Please install Brave manually.")

def open_youtube_in_private_tor(brave_path, url):
    """Open a given URL in a new Brave private window with Tor enabled."""
    try:
        subprocess.run([brave_path, "--incognito", "--tor", url])
    except Exception as e:
        update_status(f"Error opening Brave Browser: {e}")

def open_tab_with_new_tor(brave_path, url):
    """Open a new Brave private window with Tor."""
    try:
        subprocess.Popen([brave_path, "--incognito", "--tor", url])
        time.sleep(20)  # Wait for the window to load
    except Exception as e:
        update_status(f"Error interacting with Brave Browser: {e}")

def validate_youtube_url(url):
    """Validate if the entered URL is a YouTube link."""
    youtube_regex = re.compile(r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$')
    return youtube_regex.match(url)

def update_status(message):
    """Update the status messages in the GUI."""
    status_text.config(state='normal')
    status_text.insert(tk.END, message + "\n")
    status_text.see(tk.END)
    status_text.config(state='disabled')
    root.update()

def show_notification(message):
    """Show a system notification using plyer."""
    notification.notify(
        title="YouTube Link Opener",
        message=message,
        app_name="YouTube Link Opener",
        timeout=5
    )

def save_youtube_link(url):
    """Save the YouTube link to a text file."""
    with open(LINK_FILE, "w") as file:
        file.write(url)
    update_status(f"Link saved: {url}")

def load_last_youtube_link():
    """Load the last YouTube link from the text file."""
    if os.path.exists(LINK_FILE):
        with open(LINK_FILE, "r") as file:
            return file.read().strip()
    return ""

def save_mouse_coords(coords):
    """Save the mouse coordinates to a text file."""
    with open(COORDS_FILE, "w") as file:
        file.write(f"{coords['new_private_window'][0]},{coords['new_private_window'][1]}\n")
        file.write(f"{coords['new_tor_connection'][0]},{coords['new_tor_connection'][1]}\n")
    update_status("Mouse coordinates saved.")

def load_mouse_coords():
    """Load the mouse coordinates from the text file."""
    if os.path.exists(COORDS_FILE):
        with open(COORDS_FILE, "r") as file:
            lines = file.readlines()
            new_private_window_coords = tuple(map(int, lines[0].strip().split(',')))
            new_tor_connection_coords = tuple(map(int, lines[1].strip().split(',')))
            return {
                'new_private_window': new_private_window_coords,
                'new_tor_connection': new_tor_connection_coords
            }
    return None

def record_mouse_position():
    """Record the mouse position for the specified actions."""
    show_notification("Position the mouse for the new private window button...")
    time.sleep(5)
    new_private_window_coords = pyautogui.position()
    update_status(f"Recorded position for new private window: {new_private_window_coords}")

    show_notification("Move mouse to the new Tor connection option...")
    time.sleep(5)
    new_tor_connection_coords = pyautogui.position()
    update_status(f"Recorded position for new Tor connection: {new_tor_connection_coords}")

    coords = {
        'new_private_window': new_private_window_coords,
        'new_tor_connection': new_tor_connection_coords
    }
    save_mouse_coords(coords)

def start_browser():
    """Handle the start button click event."""
    url = url_entry.get()
    num_tabs = int(num_tabs_entry.get())

    if validate_youtube_url(url):
        save_youtube_link(url)
        brave_path = get_brave_path()
        if brave_path:
            update_status("Brave Browser is installed. Opening the link...")
            threading.Thread(target=open_multiple_tabs, args=(brave_path, url, num_tabs)).start()
        else:
            update_status("Brave Browser is not installed. Installing now...")
            install_brave()
            brave_path = get_brave_path()
            if brave_path:
                update_status("Brave Browser installed successfully. Opening the link...")
                threading.Thread(target=open_multiple_tabs, args=(brave_path, url, num_tabs)).start()
            else:
                show_notification("Error: Failed to install Brave Browser.")
    else:
        show_notification("Invalid URL: Please enter a valid YouTube URL.")

def open_multiple_tabs(brave_path, url, num_tabs):
    """Open multiple tabs in Brave, resetting the Tor connection from the second tab onward."""
    for i in range(num_tabs):
        open_tab_with_new_tor(brave_path, url)
        time.sleep(5)  # Delay for the tab to load
        
        if i > 0:  # Reset Tor connection for subsequent tabs
            update_status("Resetting Tor connection for the next tab...")
            create_new_tor_connection()
    
    # After opening all tabs, check for popups using OCR
    for j in range(num_tabs):
        handle_browser_popups(j + 1)

def handle_browser_popups(tab_number):
    """Detect and handle browser popups using OCR."""
    for _ in range(tab_number):
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(6)

    update_status(f"Waiting for tab {tab_number} to load...")
    time.sleep(10)

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)[:, :, ::-1]
    
    # Save the screenshot for debugging
    cv2.imwrite(f"screenshot_debug_tab_{tab_number}.png", screenshot)
    update_status(f"Screenshot saved for tab {tab_number}")

    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_screenshot, lang='eng')
    update_status(f"Detected text in tab {tab_number}: {text}")

    if "sign in" in text.lower() and "bot" in text.lower():
        update_status("Detected bot verification. Creating new Tor connection.")
        create_new_tor_connection()
    elif "cookies" in text.lower() and ("accept" in text.lower() or "reject" in text.lower()):
        update_status("Detected cookie consent. Rejecting cookies.")
        scroll_and_reject_cookies()

    time.sleep(5)

def create_new_tor_connection():
    """Click on the 'New Tor Connection' option using stored mouse coordinates."""
    coords = load_mouse_coords()
    if coords:
        pyautogui.click(coords['new_private_window'])
        time.sleep(2)
        pyautogui.click(coords['new_tor_connection'])
        time.sleep(2)

def scroll_and_reject_cookies():
    """Scroll the page and click on the 'Reject Cookies' button."""
    time.sleep(2)
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width // 2, screen_height // 2)
    pyautogui.scroll(-500)
    time.sleep(2)

    reject_button_coords = (661, 633)  # Adjust as necessary
    pyautogui.click(reject_button_coords)
    time.sleep(2)

# Set up the GUI
root = tk.Tk()
root.title("YouTube Link Opener in Brave with Tor")
root.geometry("500x500")
root.configure(bg='#f0f0f0')

font_style = ("Helvetica", 12)
header_font_style = ("Helvetica", 14, "bold")

header_label = tk.Label(root, text="YouTube Link Opener", font=header_font_style, bg='#f0f0f0')
header_label.pack(pady=10)

url_label = tk.Label(root, text="Enter YouTube Link:", font=font_style, bg='#f0f0f0')
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50, font=font_style)
url_entry.pack(pady=5)

num_tabs_label = tk.Label(root, text="Number of Tabs to Open:", font=font_style, bg='#f0f0f0')
num_tabs_label.pack(pady=5)
num_tabs_entry = tk.Entry(root, width=10, font=font_style)
num_tabs_entry.insert(0, "2")  # Default value
num_tabs_entry.pack(pady=5)

start_button = tk.Button(root, text="Open in Brave", command=start_browser, font=font_style, bg='#0078D7', fg='white', padx=20, pady=5)
start_button.pack(pady=15)

record_button = tk.Button(root, text="Record Mouse Position", command=record_mouse_position, font=font_style, bg='#0078D7', fg='white', padx=20, pady=5)
record_button.pack(pady=15)

status_label = tk.Label(root, text="Status:", font=font_style, bg='#f0f0f0')
status_label.pack(pady=10)
status_text = scrolledtext.ScrolledText(root, width=60, height=10, state='disabled', wrap=tk.WORD)
status_text.pack(pady=5)

root.mainloop()
