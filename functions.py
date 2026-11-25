import qrcode
def link_or_text_generator():
    text = input("Enter link or Text: ")
    file = input("File name: ")
    img = qrcode.make(text)
    img.save(file+".png")
    print(f"Saved: {file}.png")

def contact_card_generator():
    first = input("First name: ")
    last = input("Last name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    fullname = f"{first} {last}"
    card = ["Begin:Vcard","VERSION:3.0"]
    card.append(f"N:{last};{first}")
    card.append(f"N {fullname}")
    card.append(f"TEL {phone}")
    card.append(f"EMAIL {email}")
    card.append(f"END:Vcard")
    vcard = "\n".join(card)
    img = qrcode.make(vcard)
    img.save("contact_qr.png")
    print("Saved: contact_qr.png")

def wifi_qr_generator():
    ssid = input("Wifi name: ")
    password = input("Password: ")
    wifi = f"WIFI:T:WPA;S:{ssid}"
    wifi = f"{wifi};P:{password};;"
    img = qrcode.make(wifi)
    img.save("wifi_qr_code.png")
    print("Saved: wifi_qr_code.png")
