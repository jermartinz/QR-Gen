import qrcode
import io

qr = qrcode.QRCode()
def gen_ascii_qr(prompt):
    qr.add_data(prompt)
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())  

def gen_png_qr(prompt):
    qr.add_data(prompt)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(input("Enter the filename to save the QR code (e.g., qrcode.png): "))
    print("QR code saved as PNG image.")

while True:
    print("==== QR Code Generator ====")
    menu = input("Choose output format - (1) ASCII Art, (2) PNG Image, (3) Exit: ")
    if menu == '1':
        gen_ascii_qr(input("Enter the text or URL to encode in the QR code: "))
    elif menu == '2':
        gen_png_qr(input("Enter the text or URL to encode in the QR code: "))
    elif menu == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select 1 or 2.")
        continue
print("QR code generation complete.")