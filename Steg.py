import cv2
import os

# Load the image
img = cv2.imread("fightclubimg.jpg")
if img is None:
    print("Error: Image not found. Make sure 'fightclubimg.jpg' exists in the current directory.")
    exit()

# Input secret message and passcode
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create dictionaries for character-to-value and value-to-character mapping
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Embed the message into the image
m = 0
n = 0
z = 0

for i in range(len(msg)):
    if n >= img.shape[0] or m >= img.shape[1]:  # Check if message fits in the image
        print("Error: Message is too long to fit in the image.")
        exit()
    img[n, m, z] = d[msg[i]]  # Embed the message
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through RGB channels

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
print("Message embedded successfully. Encrypted image saved as 'encryptedImage.jpg'.")

# Open the encrypted image (platform-independent)
if os.name == "nt":  # Windows
    os.system("start encryptedImage.jpg")
else:  # macOS or Linux
    os.system("open encryptedImage.jpg" if os.name == "posix" else "xdg-open encryptedImage.jpg")

# Decryption
message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for decryption: ")
if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]  # Extract the message
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("Incorrect passcode. YOU ARE NOT AUTHORIZED.")




