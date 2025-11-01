import cv2
from pyzbar.pyzbar import decode

image_path = "C:\Users\Christian\OneDrive\Pictures\Screenshots\Screenshot-2025-11-01-205342.png"

# Load the image
image = cv2.imread(image_path)

# Decode QR codes in the image
qr_codes = decode(image)

if qr_codes:
    for qr in qr_codes:
        # Get QR code bounding box
        x, y, w, h = qr.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Get QR data and type
        qr_data = qr.data.decode("utf-8")
        qr_type = qr.type

        # Display text on image
        cv2.putText(image, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2)

        print(f"Detected QR Code: {qr_data}")
else:
    print("No QR Code found in the image.")

# Show the image with detected QR code
cv2.imshow("QR Code Scanner", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
