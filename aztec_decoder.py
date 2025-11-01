import cv2
from pyzbar.pyzbar import decode

image_path = "C:\Users\Christian\OneDrive\Pictures\Screenshots\Screenshot-2025-11-01-205343.png"

# Load the image
image = cv2.imread(image_path)

# Decode Aztec codes
codes = decode(image)

if codes:
    for code in codes:
        if code.type == "AZTEC":  # Make sure it's Aztec (optional filter)
            x, y, w, h = code.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            data = code.data.decode("utf-8")
            cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)

            print(f"Detected Aztec Code: {data}")
else:
    print("No Aztec Code found in the image.")

# Show the result
cv2.imshow("Aztec Code Scanner", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
