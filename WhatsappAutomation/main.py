import pywhatkit
import tkinter as tk
from tkinter import messagebox

def send_whatsapp_message():
    try:
        phone_number = phone_number_entry.get()
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
        message = message_entry.get()

        pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        messagebox.showinfo("Message Sent", "Your WhatsApp message has been Sent.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("WhatsApp Message Sender")

# Phone number entry
phone_number_label = tk.Label(root, text="Phone Number:")
phone_number_label.pack()
phone_number_entry = tk.Entry(root)
phone_number_entry.pack()

# Hour entry
hour_label = tk.Label(root, text="Hour (24h format):")
hour_label.pack()
hour_entry = tk.Entry(root)
hour_entry.pack()

# Minute entry
minute_label = tk.Label(root, text="Minute:")
minute_label.pack()
minute_entry = tk.Entry(root)
minute_entry.pack()

# Message entry
message_label = tk.Label(root, text="Message:")
message_label.pack()
message_entry = tk.Entry(root)
message_entry.pack()

# Send button
send_button = tk.Button(root, text="Send", command=send_whatsapp_message)
send_button.pack()

# Run the GUI main loop
root.mainloop()
