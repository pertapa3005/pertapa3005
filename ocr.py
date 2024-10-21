import cv2
from PIL import Image
import pytesseract

# Path to the Tesseract executable (sesuaikan dengan lokasi instalasi Tesseract)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Fungsi untuk melakukan OCR pada gambar yang diambil dari webcam
def perform_ocr(frame):
    # Convert the captured frame to an image
    image = Image.fromarray(frame)
    
    # Convert image to grayscale
    grayscale_image = image.convert('L')
    
    # Enhance contrast (optional)
    enhanced_image = ImageEnhance.Contrast(grayscale_image).enhance(2)
    
    # Perform OCR using Indonesian language
    text = pytesseract.image_to_string(enhanced_image, lang='ind')
    
    return text

# Inisialisasi webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Webcam - Tekan "s" untuk Scan KTP, "q" untuk Keluar', frame)

    # Tunggu input dari user
    key = cv2.waitKey(1) & 0xFF

    # Jika 's' ditekan, lakukan OCR
    if key == ord('s'):
        ocr_result = perform_ocr(frame)
        print("Hasil OCR:")
        print(ocr_result)

    # Jika 'q' ditekan, keluar dari loop
    elif key == ord('q'):
        break

# Saat selesai, release capture
cap.release()
cv2.destroyAllWindows()
