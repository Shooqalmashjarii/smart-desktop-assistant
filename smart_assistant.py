import tkinter as tk
import webbrowser
import subprocess
import os
import requests 
from datetime import datetime
from PIL import ImageGrab 


#Intent Detection 
def detect_intent(user_input):
    user_input = user_input.lower()
    if "google" in user_input or "search" in user_input or "look up" in user_input:
        return "googleSearch"
    elif "youtube" in user_input or "play video" in user_input:
        return "youtubeSearch"
    elif "screenshot" in user_input or "take picture" in user_input or "capture screen" in user_input:
        return "screenShot"
    elif "word" in user_input or "write a document" in user_input:
        return "startWord"
    elif "powerpoint" in user_input or "make a presentation" in user_input:
        return "startPowerpoint"
    elif "increase volume" in user_input or "louder" in user_input or "turn on volume" in user_input or "unmute" in user_input:
        return "highVolume"
    elif "lower volume" in user_input or "quieter" in user_input or "mute" in user_input or "turn off vol" in user_input or "decrease volume" in user_input:
        return "lowVolume"
    elif "increase brightness" in user_input or "brighter" in user_input:
        return "higherBrightness"
    elif "lower brightness" in user_input or "dimmer" in user_input or "decrease brightness" in user_input:
        return "lowerBrightness"
    elif "download music" in user_input:
        return "downloadMusic"
    else:
        return "LLM"

# LLM integration
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
headers = {
    "Authorization": "YOUR_HUGGINGFACE_API_KEY"
}

def ask_llm(question):
    payload = {"inputs": question}
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {"error": "Could not decode response."}

# System Commands
def google_search(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)

def youtube_search(query):
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)

def take_screenshot():
    image = ImageGrab.grab()
    filename = datetime.now().strftime("screenshot_%Y%m%d_%H%M%S.png")
    image.save(filename)
    return f"Screenshot saved as {filename}"

def open_notepad():
    if os.name == "nt":
        subprocess.Popen(["notepad.exe"])
    else:
        return "Notepad supported only on Windows"

def open_word():
    subprocess.Popen(["start", "winword"], shell=True)

def open_powerpoint():
    subprocess.Popen(["start", "powerpnt"], shell=True)

def increase_volume():
    os.system("nircmd.exe changesysvolume 2000")

def lower_volume():
    os.system("nircmd.exe changesysvolume -2000")

# GUI 
def handle_command():
    user_input = entry.get()
    entry.delete(0, tk.END)
    intent = detect_intent(user_input)

    if intent == "googleSearch":
        google_search(user_input)
        output.config(text="Searching Google...")
    elif intent == "youtubeSearch":
        youtube_search(user_input)
        output.config(text="Opening YouTube...")
    elif intent == "screenShot":
        result = take_screenshot()
        output.config(text=result)
    elif intent == "startWord":
        open_word()
        output.config(text="Opening Microsoft Word...")
    elif intent == "startPowerpoint":
        open_powerpoint()
        output.config(text="Opening PowerPoint...")
    elif intent == "highVolume":
        increase_volume()
        output.config(text="Volume Increased")
    elif intent == "lowVolume":
        lower_volume()
        output.config(text="Volume Decreased")
    elif intent == "LLM":
        result = ask_llm(user_input)
        output.config(text=str(result))
    else:
        output.config(text="Unknown command")

# GUI Window 
root = tk.Tk()
root.title("Smart Desktop Assistant")
root.geometry("500x300")
root.configure(bg="#4683d3") 

entry = tk.Entry(root, font=("Arial", 14), width=40)
entry.pack(pady=20)

submit_btn = tk.Button(root, text="Ask", command=handle_command, font=("Arial", 12))
submit_btn.pack()

output = tk.Label(root, text="", wraplength=400, font=("Arial", 12), bg="#4683d3", fg="white")
output.pack(pady=20)

root.mainloop()
