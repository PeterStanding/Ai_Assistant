import qrcode, PIL

def generateQR(loc,fName):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    dir = "QR_CODES/"
    fmt = ".jpeg"

    qr.add_data(loc)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    final = dir + fName + fmt
    img.save(final)

    print("QR Code has been generated and Saved as:", fName)
