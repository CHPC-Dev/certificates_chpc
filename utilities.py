from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import datetime
import uuid

def generate_certificate(full_name):
   
    """
    name, date, and serial number are centered on the certificate 
    by first calculating the bounding box of the text using the selected font.
    The bounding box provides the width and height of the text, which allows 
    us to determine how much space the text will occupy on the certificate. 
    Once we have the text width and height, we can adjust the x and y positions of
    the text so that it is centered on the predefined 
    coordinates (coords_name, coords_date, coords_serial) for 
    each respective field. This ensures that regardless of the length
    of the name or the date, the text will always be centered correctly on the certificate.
    """
    
    img = Image.open("winter_school.png").convert("RGB")
    draw = ImageDraw.Draw(img)

    # Fonts
    font_name = ImageFont.truetype("Candarab.ttf", 50)
    font_date = ImageFont.truetype("Candarab.ttf", 50)
    font_serial = ImageFont.truetype("Candarab.ttf", 20)


    # Center coordinates
    coords_name = (890, 389)
    coords_date = (890, 622)
    coords_serial = (1639, 1220)

    # --- Name ---
    bbox_name = draw.textbbox((0, 0), full_name, font=font_name)
    text_width = bbox_name[2] - bbox_name[0]
    text_height = bbox_name[3] - bbox_name[1]
    x_name = coords_name[0] - text_width / 2
    y_name = coords_name[1] - text_height / 2
    draw.text((x_name, y_name), full_name, fill=(0, 0, 0), font=font_name)

    # --- Date ---
    period = "28 July to 8 August 2025"
    bbox_date = draw.textbbox((0, 0), period, font=font_date)
    text_width2 = bbox_date[2] - bbox_date[0]
    text_height2 = bbox_date[3] - bbox_date[1]
    x_date = coords_date[0] - text_width2 / 2
    y_date = coords_date[1] - text_height2 / 2
    draw.text((x_date, y_date), period, fill=(0, 0, 0), font=font_date)

   # --- Serial ---
    serial_number = f"CHPC-2026-{str(uuid.uuid4())[:8].upper()}"
    serial_text = f"{serial_number}"
    serial_color = (80, 1, 24)

    bbox_serial = draw.textbbox((0, 0), serial_text, font=font_serial)
    text_width3 = bbox_serial[2] - bbox_serial[0]
    text_height3 = bbox_serial[3] - bbox_serial[1]
    x_serial = coords_serial[0] - text_width3 / 2
    y_serial = coords_serial[1] - text_height3 / 2

    draw.text((x_serial, y_serial), serial_text, fill=serial_color, font=font_serial)

    # Save PDF to memory
    buffer = BytesIO()
    img.save(buffer, format="PDF", resolution=100.0)
    buffer.seek(0)

    return buffer.getvalue(), period, serial_number
