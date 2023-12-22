import pyperclip

link = pyperclip.paste()
id = link[32:].split("/")[0]

pyperclip.copy(f"https://drive.google.com/uc?id={id}")
