import settings
from choice_manager import choice_manager
def build_app():
    while True:
        print(f"\n ------------- {settings.APP_TITLE} -------------")
        for item in settings.APP_OPTIONS:
            print(f"{item[0]}. {item[1]}")
        choice = input("Chose: ")
        action = choice_manager(chioce=choice)
        if action is None:
            break
        if action == -1:
            print("Invailed choice...")
        else:
            action()