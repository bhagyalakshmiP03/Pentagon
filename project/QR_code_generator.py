import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f"QR code saved as {file_name}")
    return img

data = input("Enter the data to be stored in QR code: ")
file_name = input("Enter the name of the file to save the QR code: ")  #
generate_qr_code(data, file_name)
# Output: QR code saved as qr_code.png or jpg or jpeg

