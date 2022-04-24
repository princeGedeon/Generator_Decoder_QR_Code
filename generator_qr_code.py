import qrcode
#INPUT
nom=input("Nom et Prenoms :").split()

profession=input("Profession :")
# Link for website
input_data = f"Nom : {nom[0]}\nPrénoms: {' '.join(nom[1:])}\nProfession : {profession}"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=3,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')