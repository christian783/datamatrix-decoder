from pylibdmtx.pylibdmtx import decode
from PIL import Image

image = Image.open("C:\Users\Christian\OneDrive\Pictures\Screenshots\Screenshot-2025-11-01-205340.png")

# Decode Data Matrix
decoded_objects = decode(image)

# Print all decoded results
for obj in decoded_objects:
    print("Decoded Data:", obj.data.decode("utf-8"))
