from zxing import BarCodeReader

image_path = "C:\Users\Christian\OneDrive\Pictures\Screenshots\Screenshot-2025-11-01-205344.png"

# Initialize ZXing reader
reader = BarCodeReader()

# Decode the image
result = reader.decode(image_path)

if result:
    print("Barcode Format:", result.format)  # Should show MAXICODE if detected
    print("Decoded Data:", result.parsed)
else:
    print("No MaxiCode detected in the image.")
