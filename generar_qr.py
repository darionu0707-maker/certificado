import qrcode

# REEMPLAZA esta URL por tu dirección real de GitHub Pages.
URL = "https://TUUSUARIO.github.io/certificado/"

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="#172554", back_color="white")
img.save("QR_certificado.png")

print("QR creado: QR_certificado.png")
print("URL:", URL)
