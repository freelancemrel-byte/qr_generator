import functions
def choice_manager(chioce:str):
    if chioce == "1":
        return functions.link_or_text_generator
    elif chioce == "2":
        return functions.contact_card_generator
    elif chioce =="3":
        return functions.wifi_qr_generator
    elif chioce == "4":
        return 
    else:
        return -1
