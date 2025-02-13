import qrcode
from PIL import Image

def generate_qr(data, file_name="qrcode.png"):
    # Crear el objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Crear la imagen del código QR
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f"Código QR generado: {file_name}")

if __name__ == "__main__":
    # Datos para el código QR (puede ser una URL, texto, etc.)
    data = input("Introduce el texto o URL para el código QR: ")
    file_name = input("Introduce el nombre del archivo (ejemplo: qrcode.png): ") or "qrcode.png"
    generate_qr(data, file_name)
