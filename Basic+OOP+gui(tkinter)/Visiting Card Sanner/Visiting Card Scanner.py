import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# Function to open and display image
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((400, 400))  # Resize image to fit the window
        img_label.image = ImageTk.PhotoImage(image)
        img_label.config(image=img_label.image)
        global scanned_image
        scanned_image = image  # Store image for processing

# Function to process image and perform OCR
def process_image():
    if scanned_image:
        gray_image = scanned_image.convert("L")  # Convert to grayscale
        extracted_text = pytesseract.image_to_string(gray_image, lang='eng')  # Perform OCR
        show_extracted_text(extracted_text)

# Function to display extracted text in a new window
def show_extracted_text(text):
    info_window = tk.Toplevel(root)
    info_window.title("Extracted Text")
    text_widget = tk.Text(info_window)
    text_widget.insert(tk.END, text)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack()

# Main tkinter window
root = tk.Tk()
root.title("Visiting Card Scanner")

# Widgets
open_button = tk.Button(root, text="Open Image", command=open_image)
process_button = tk.Button(root, text="Process Image", command=process_image)
img_label = tk.Label(root)
img_label.pack()
open_button.pack()
process_button.pack()

# Global variable to store the scanned image
scanned_image = None

# Start the tkinter main loop
root.mainloop()
