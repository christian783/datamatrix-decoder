import cv2
from pyzbar.pyzbar import decode

image_path = "C:\Users\Christian\OneDrive\Pictures\Screenshots\Screenshot-2025-11-01-205341.png"

# Read the image
image = cv2.imread(image_path)

# Decode barcodes/QR codes in the image
barcodes = decode(image)

for barcode in barcodes:
    # Extract bounding box and draw rectangle
    x, y, w, h = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Get data and type
    barcode_data = barcode.data.decode('utf-8')
    barcode_type = barcode.type

    # Display the decoded text
    text = f"{barcode_data} ({barcode_type})"
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 0), 2)

    print(f"Detected: {barcode_data}  | Type: {barcode_type}")

# Show result
cv2.imshow("Image Barcode Scanner", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
