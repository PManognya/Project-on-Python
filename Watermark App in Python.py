#Watermark App in Python
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

selected_image_path = ""

def upload_image():
    global selected_image_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if file_path:
        selected_image_path = file_path
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img_preview = ImageTk.PhotoImage(img)
        image_label.config(image=img_preview)
        image_label.image = img_preview  # keep reference so it doesn't get garbage collected

def add_watermark():
    if not selected_image_path:
        messagebox.showwarning("No image", "Please upload an image first.")
        return

    watermark_text = watermark_entry.get()
    if not watermark_text:
        messagebox.showwarning("No text", "Please enter watermark text.")
        return

    image = Image.open(selected_image_path).convert("RGBA")
    txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    try:
        font = ImageFont.truetype("arial.ttf", size=int(image.width / 15))
    except:
        font = ImageFont.load_default()

    # Position watermark in bottom-right corner
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = image.width - text_width - 20
    y = image.height - text_height - 20

    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 180))

    watermarked = Image.alpha_composite(image, txt_layer).convert("RGB")

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
    )
    if save_path:
        watermarked.save(save_path)
        messagebox.showinfo("Success", f"Watermarked image saved to:\n{save_path}")

# --- GUI Setup ---
window = Tk()
window.title("Watermark App")
window.config(padx=30, pady=30)

upload_btn = Button(window, text="Upload Image", command=upload_image)
upload_btn.pack(pady=10)

image_label = Label(window)
image_label.pack(pady=10)

watermark_entry = Entry(window, width=30)
watermark_entry.insert(0, "Enter watermark text")
watermark_entry.pack(pady=10)

add_watermark_btn = Button(window, text="Add Watermark & Save", command=add_watermark)
add_watermark_btn.pack(pady=10)

window.mainloop()