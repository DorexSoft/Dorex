import platform
import os

main = '''
▒█▀▀▀█ ▒█▀▀▀█ ▀█▀ ▒█▄░▒█ ▀▀█▀▀ 　 ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀▀█ ▒█░░░ 
▒█░░▒█ ░▀▀▀▄▄ ▒█░ ▒█▒█▒█ ░▒█░░ 　 ░▒█░░ ▒█░░▒█ ▒█░░▒█ ▒█░░░ 
▒█▄▄▄█ ▒█▄▄▄█ ▄█▄ ▒█░░▀█ ░▒█░░ 　 ░▒█░░ ▒█▄▄▄█ ▒█▄▄▄█ ▒█▄▄█'''

tools = '''

     [1] Nickname           [6] Search engines
      [2] Number             [7] Photo
       [3] IP                 [8] Maps   
        [4] Mail               [9] cameras
         [5] The media          [0] exit
'''

fuc_1 = '''
1) Посик по ник-нейму: 
 - snoop: https://github.com/snooppr/snoop?ysclid=m6z83ohano568528079
 - sherlock: https://github.com/sherlock-project/sherlock?ysclid=m6z84gwrfu338523868
'''
fuc_2 = '''
2) Поиск по номеру телефона: 
 - noblack-mail: https://github.com/DataSC3/noblack-mail?ysclid=m6z85rbvvv967258675
 - cldeanon: https://github.com/donotdisturbpleasee/CLDeanon?ysclid=m6z86xvh21467852800
 - phoneInfoga: https://github.com/FOGSEC/PhoneInfoga?ysclid=m6z882l6le434078515
 - phoneCheck: https://github.com/AlexZiroYT/PhoneCheck?ysclid=m6z88w9110594239433

 - https://t.me/QuickOpenSource_bot/
 - https://usersbox.org/
'''
fuc_3 = '''
3) Поиск по IP: 
 - noblack-mail: https://github.com/DataSC3/noblack-mail?ysclid=m6z85rbvvv967258675

 - 2ip: https://2ip.ru/ 
'''
fuc_4 = '''
4) Почта: 
 - https://github.com/martinvigo/email2phonenumber
 - https://github.com/megadose/holehe
'''
fuc_5 = '''
5) СМИ: 
 - РИА: https://ria.ru/
 - РКБ: https://rostov.rbc.ru/
'''
fuc_6 = '''
6) Поисковики: 
 - https://intelx.io/
 - https://searx.tiekoetter.com/
 - https://www.smartresultsnow.net/
'''
fuc_7 = '''
7) Фото: 
 - https://huggingface.co/spaces/ydshieh/Kosmos-2
 - https://www.huntintel.io/
'''
fuc_8 = '''
8) Карта: 
 - https://www.scribblemaps.com/
 - https://demo.f4map.com/
'''
fuc_9 = '''
9) Просмотр онлайн видео камер: 
 - https://www.serdi.ru/map/
 - http://camera.avk-wellcom.ru/
 - http://cam-world.ru/
 - https://www.geocam.ru/
 - https://world-cam.ru/
 - https://webcam-live.ru/
'''
def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

num_too = ''
def osint_tools():
    clear_console()
    print(main, tools)
    num_too = int(input('Enter function: '))
    if num_too == 1:
        print(fuc_1)
    elif num_too == 2:
        print(fuc_2)
    elif num_too == 3:
        print(fuc_3)
    elif num_too == 4:
        print(fuc_4)
    elif num_too == 5:
        print(fuc_5)
    elif num_too == 6:
        print(fuc_6)
    elif num_too == 7:
        print(fuc_7)
    elif num_too == 8:
        print(fuc_8)
    elif num_too == 9:
        print(fuc_9)
    else:
        "Eror!"
    return