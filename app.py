import qrcode

data = "https://your-website-link.com"

qr = qrcode.make(data)

qr.save("my_qr.png")

print("QR Code Generated Successfully!")
