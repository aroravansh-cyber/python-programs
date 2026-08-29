import qrcode
from urllib.parse import urlparse

print("=" * 40)
print("       QR CODE GENERATOR")
print("=" * 40)

url = input("Enter URL: ").strip()

# URL validation
parsed = urlparse(url)

if not parsed.scheme:
    url = "https://" + url
    parsed = urlparse(url)

if not parsed.netloc:
    print("Invalid URL!")
    exit()

filename = input("Enter file name (default: qr_code.png): ").strip()

if not filename:
    filename = "qr_code.png"

if not filename.endswith(".png"):
    filename += ".png"

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white"
)

img.save(filename)

print("\nQR Code generated successfully!")
print(f"URL      : {url}")
print(f"Saved as : {filename}")
