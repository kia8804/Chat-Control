from tkinter import *
from customtkinter import *
from PIL import Image # image processing

bot_name = "Chat Control"

app = CTk()
app.geometry("400x980")
app.title("Chat Control")
set_appearance_mode("dark")
title_label = CTkLabel(app, text="Chat Control",font=CTkFont(family="Helvectica", size=25, weight='bold'))
title_label.pack(padx=10, pady=(20,20))

def send_message(event=None):
    msg1 = entry.get().strip()
    if msg1:
        textbox.configure(state="normal")
        textbox.insert("end", f"You: {msg1}\n")
        textbox.configure(state="disabled")
        textbox.see("end")
        entry.delete(0, "end")
        
        msg2 = "Hello! How may I assist you today?" # replace with chatbot output
        textbox.configure(state="normal")
        textbox.insert("end", f"CC: {msg2}\n")
        textbox.configure(state="disabled")
        textbox.see("end")

def screenshot():
    # Not done yet
    textbox.configure(state="normal")
    textbox.insert("end", f"You sent a screenshot.\n")
    textbox.insert("end", "CC: Analyzing....\n") # replace with chatbot output
    textbox.configure(state="disabled")
    textbox.see("end")

send_icon = Image.open("airplane.png")
btn = CTkButton(master=app, 
                text="", 
                hover_color="#4158D0", 
                image=CTkImage(dark_image=send_icon, light_image=send_icon),
                command=send_message)
btn.place(relx=0.67, rely=0.90, relheight=0.06, relwidth=0.22)

camera_icon = Image.open("camera.png")
screenshot_btn = CTkButton(master=app, 
                           text="", 
                           hover_color="#4158D0", 
                           image=CTkImage(dark_image=camera_icon, light_image=camera_icon),
                           command=screenshot)

screenshot_btn.place(relx=0.82, rely=0.90, relheight=0.06, relwidth=0.12,)


entry = CTkEntry(master=app,
                 placeholder_text="Need help?",
                 width=300,
                 text_color="#FFFFFF")
entry.place(relwidth=0.70, relheight=0.06, rely=0.90, relx=0.011)
entry.bind("<Return>", send_message)
entry.focus_set()

# textbox = CTkTextbox(master=app, scrollbar_button_color="#FFCC70", corner_radius=16)
textbox = CTkTextbox(master=app, scrollbar_button_color="#FFFFFF", corner_radius=16, state="disabled")
textbox.place(relheight=0.80, relwidth=1, rely=0.10)

app.mainloop()