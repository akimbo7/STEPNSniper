import re
import requests
import pyautogui
from colorama import *; init()

def try_code(code):

    # CHANGE COORDS SO IT WORKS ON YOUR APP.

    for i in range(2):
        pyautogui.click(365,444) # CLICKS THE BOX TO ENTER CODE
        # CLICKS TWICE - ONCE TO CHECK THE CURSOR IS ACTUALLY ON THE APP - SECOND TO CLICK BOX

    #pyautogui.write(str(code))

    #pyautogui.click(445,490) # CLICKS THE START BUTTON TO TRY CODE

    print(f'[{Fore.YELLOW} SNIPE {Fore.RESET}] Sniped code: {Fore.YELLOW}{code}{Fore.RESET} - Check app to confirm.')

def get_messages():

    session = requests.Session()

    token = '' # YOUR DISCORD TOKEN

    headers = {'authorization': token}
    session.headers.update(headers)

    url = 'https://discord.com/api/v9/channels/960566842697592903/messages'

    code_list = []

    # DOES THIS ONCE TO GET ALL OLD CODES SO IT CAN CHECK WHEN A NEW CODE IS SENT

    response = session.get(url)
    data = response.json()

    for message in data:
        x = message['content']
        for word in x.split():
            if re.match(pattern="^\d{8}$", string=word):
                if word in code_list:
                    pass
                else:
                    code_list.append(word)
            else:
                pass

    print(f'[{Fore.BLUE} START {Fore.RESET}] Scraping...')

    while True:

        response = session.get(url)
        data = response.json()

        for message in data:
            x = message['content']
            for word in x.split():
                if re.match(pattern="^\d{8}$", string=word):
                    if word in code_list:
                        pass
                    else:
                        print(f'[{Fore.GREEN}NEW CODE{Fore.RESET}] {word}')
                        try_code(word)
                        code_list.append(word)
                else:
                    pass

if __name__ == '__main__':
    get_messages()
