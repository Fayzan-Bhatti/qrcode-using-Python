!pip install qrcode
import qrcode
from PIL import ImageSequence, Image

# Create a list of URLs or text data to encode
data_list = ["https://www.goole.com"]

# Create an empty list to store individual QR code frames
frames = []

# Generate QR code frames for each data item
for data in data_list:
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    frames.append(img)

# Save the frames as an animated GIF
frames[0].save('animated_qr_code.gif', save_all=True, append_images=frames[1:], optimize=False, duration=500, loop=0)

# Optionally, you can also display the animated QR code
animated_qr_code = Image.open('animated_qr_code.gif')
animated_qr_code.show()
