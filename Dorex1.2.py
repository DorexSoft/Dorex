import random
import time
import string
import requests     # Библиотека
import os
import platform
import colorama    # Библиотека
import phonenumbers    # Библиотека
from phonenumbers import carrier, geocoder
from colorama import init, Fore, Back, Style
import subprocess
import number_info
import email_search2

with open('License_Agreement.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(Fore.GREEN + line.strip())
a = input(Fore.GREEN +'Вы хотите открыть "DOREX"?  (1Yes, 2No) ')
def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
clear_console()
if a == '1':
    while True:
        print(Fore.GREEN +'''
                                ██████╗░░█████╗░██████╗░███████╗██╗░░██╗
                                ██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝
                                ██║░░██║██║░░██║██████╔╝█████╗░░░╚███╔╝░
                                ██║░░██║██║░░██║██╔══██╗██╔══╝░░░██╔██╗░
                                ██████╔╝╚█████╔╝██║░░██║███████╗██╔╝╚██╗
                                ╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝ ᵛ1.2
                             Телеграм канал проекта: https://t.me/DorexSoftware
———————————————————————————————————————————————————————————————————————————————————————————————————————————————
|    Инструменты                  |    Генераторы             |    Мануалы        |    Дополнительные модули  |
———————————————————————————————————————————————————————————————————————————————————————————————————————————————
| [1] Поиск по номеру телефона    | [9] Пароль                | [14] Osint        | [17] Osint tools          |
| [2] Шифровщик текста            | [10] Электронная почта    | [15] Анонимность  | [18] Eye of God 0.2       |
| [3] Мой IP                      | [11] Пасспорт             | [16] Поиск по IP  | [19] Doska                |
| [4] Место по координатам        | [12] Личность             |                   | [20] DataBase             |
| [5] Поиск по нику               | [13] Банковская карта     |                   | [21] Шаблоны для оформле- |
| [6] Сокращение ссылки           |                           |                   | ния                       |
| [7] Поиск по телеграм           |                           |                   |                           |
| [8] Поиск ко IP                 |                           |                   | [0] Выход                 |
———————————————————————————————————————————————————————————————————————————————————————————————————————————————
        ''')
        b = input('Выберите значение: ')
        if b == '1':
            b = None
            print('''
               ,,ggddY"""Ybbgg,,
          ,agd888b,_ "Y8, ___`""Ybga,
       ,gdP""88888888baa,.""8b    "888g,
     ,dP"     ]888888888P'  "Y     `888Yb,
   ,dP"      ,88888888P"  db,       "8P""Yb,    
  ,8"       ,888888888b, d8888a           "8,
 ,8'        d88888888888,88P"' a,          `8,
,8'         88888888888888PP"  ""           `8,
d'          I88888888888P"                   `b
8           `8"88P""Y8P'                      8
8            Y 8[  _ "                        8
8              "Y8d8b  "Y a                   8
8                 `""8d,   __                 8
Y,                    `"8bd888b,             ,P
`8,                     ,d8888888baaa       ,8' ##     ## ##     ##  ###     ###  #######  ######## #######
 `8,                    888888888888'      ,8'  ###    ## ##     ## ## ##   ## ## ##    ## ##       ##    ##
  `8a                   "8888888888I      a8'   ####   ## ##     ## ##  ## ##  ## ##    ## ##       ##    ##
   `Yba                  `Y8888888P'    adP'    ## ##  ## ##     ## ##   ###   ## #######  ######## #######
     "Yba                 `888888P'   adY"      ##  ## ## ##     ## ##         ## ##    ## ##       ## ##
       `"Yba,             d8888P" ,adP"'        ##   #### ##     ## ##         ## ##    ## ##       ##  ##
          `"Y8baa,      ,d888P,ad8P"'           ##    ###  #######  ##         ## #######  ######## ##   ##
               ``""YYba8888P""''
''')
            c = input('Введите номер телефона(Например: 79999999999): ')
            d = []
            d.append(c)
            d = list(c)
            print('')
            # Страны
            yk = ['3', '8', '0'] # Украина
            be = ['3', '7', '5'] # Белоруссия
            ar = ['3', '7', '4'] # Армения
            az = ['9', '9', '4'] # Азербайджан
            gr = ['9', '9', '5'] # Грузия
            ml = ['3', '7', '3'] # Молдова
            ki = ['9', '9', '6'] # Киргизия
            ta = ['9', '9', '2'] # Таджикистан
            tu = ['9', '9', '3'] # Туркменистан
            uz = ['9', '9', '8'] # Узбекистан
            fr = ['3', '3']      # Франция
            ge = ['4', '9']      # Германия
            sp = ['3', '4']      # Испания
            it = ['3', '9']      # Италия
            we = ['4', '4']      # Вликобритания
            ni = ['3', '1']      # Нидерланды
            hw = ['4', '6']      # Швеция
            po = ['4', '8']      # Польша
            ce = ['4', '2', '0'] # Чехия
            aw = ['4', '3']      # Австрия
            al = ['3','5','5']   # Албания
            an = ['3','7','6']   # Андорра
            be2 = ['3','2']      # Бельгия
            bo = ['3','8','7']   # Босния и Герцеговина
            bo2 = ['3','5','9']  # Болгария
            wa = ['3','9']       # Ватикан
            ve = ['3','6']       # Венгрия
            gr2 = ['3','0']      # Греция
            da = ['4','5']       # Дания
            ir = ['3','5','3']   # Ирландия
            is2 = ['3','5','4']  # Исландия
            ki2 = ['3','5','7']  # Кипр
            la = ['3','7','1']   # Латвия
            li = ['3','7','0']   # Литва
            lu = ['3','5','2']   # Люксембург
            ma = ['3','5','6']   # Мальта
            no = ['4','7']       # Норвегия
            po2 = ['3','5','1']  # Португалия
            ry = ['4','0']       # Румыния
            se = ['3','8','1']   # Сербия
            sl = ['4','2','1']   # Словакия
            sl2 = ['3','8','6']  # Словения
            tu2 = ['9','0']      # Турция
            fi = ['3','5','8']   # Финляндия
            ce2 = ['3','8','2']  # Черногория
            sh = ['4','1']       # Швейцария
            usa = ['1']          # США
            canada = ['1']       # Канада
            mexica = ['5','2']      # Мексика
            grenada = ['4','7','3']    # Гренада
            bag_ostrova = ['2','4','2']# Багамские острова
            yamayka = ['8','7','6']    # Ямайка
            argentina = ['5','4'] # Аргентина
            brasilia = ['5','5']  # Бразилия
            chili = ['5','6']     # Чили
            peru = ['5','1']      # Перу
            kolumbia = ['5','7']  # Колумбия
            paragwai = ['5','9','5'] # Парагвай
            urugwai = ['5','9','8']  # Уругвай
            wenesuela = ['5','8']    # Венесуэла
            akwador = ['5','9','3']  # Эквадор
            gayana = ['5','9','2']   # Гайана
            surinam = ['5','9','7']  # Суринам
            frnch_gviana = ['5','9','7'] # Французская Гвиана
            australia = ['6', '1']    # Австралия
            new_zelandya = ['6', '4'] # Новая Зеландия
            new_gweneya = ['6', '7', '5'] # Новая Гвинея
            fidjy = ['6', '7', '9'] # Фиджи
            samoa = ['6', '8', '5'] # Самоа
            tonga = ['6', '7', '6'] # Тонга
            micronezia = ['6', '9', '1'] # Микронезия
            nauru = ['6', '7', '4'] # Науру
            tuwalu = ['6', '8', '8'] # Тувалу
            banlgades = ['8', '8', '0']
            barbados = ['1', '2', '4', '6']
            bahren = ['9', '7', '3']
            butan = ['9', '7', '5']
            wetnam = ['8', '4']
            dania = ['2', '9', '9']
            india = ['9', '1']
            indonesia = ['6', '2']
            iordania = ['9', '6', '2']
            irak = ['9', '6', '4']
            iran = ['9', '8']
            kasahstan = ['7']
            kitai = ['8', '6']
            mianma = ['9', '5']
            kuwet = ['9', '6', '5']
            liwan = ['9', '6', '1']
            mongolia = ['9', '7', '6']
            nepal = ['9', '7', '7']
            oae = ['9', '7', '1']
            pakistan = ['9', '2']
            sau_ar = ['9', '6', '6']
            singapur = ['6', '5']
            tailand = ['6', '6']
            filipini = ['6', '3']
            sri_lanka = ['9', '4']
            uj_korea = ['8', '2']
            japan = ['8', '1']
            aljir = ['2', '1', '3']
            angola = ['2', '4', '4']
            benin = ['2', '2', '9']
            botsvana = ['2', '6', '7']
            burundi = ['2', '5', '7']
            watan = ['2', '2', '8']
            gabon = ['2','4','1']
            gana = ['2', '3', '3']
            gvinea = ['2', '2', '4']
            gvinea_bitsau = ['2', '4', '5']
            kongo = ['2', '4', '3']
            diego_suares = ['2', '6', '1']
            zambia = ['2', '6', '0']
            zimbabwe = ['2', '6', '3']
            kabo_werde = ['2', '3', '8']
            kamerun = ['2', '3', '7']
            kenia = ['2', '5', '4']
            kot_iwur = ['2', '2', '5']
            liberia = ['2', '3', '1']
            livia = ['2', '1', '8']
            mavritania = ['2', '2', '2']
            madagaskar = ['2', '6', '1']
            malavi = ['2', '6', '5']
            mali = ['2', '2', '3']
            maroko = ['2', '1', '2']
            namibia = ['2', '6', '4']
            niger = ['2', '2', '7']
            nigeria = ['2', '3', '4']
            res_kon = ['2', '4', '2']
            ruanda = ['2', '5', '0']
            uganda = ['2', '5', '6']
            tunis = ['2', '1', '6']
            cuar = ['2', '3', '6']
            had = ['2', '3', '5']
            uar = ['2', '7']

            rus = 'Россия'
            ukr = 'Украина'
            bel = 'Беларуссия'
            arm = 'Армения'
            aze = 'Азербайджан'
            gru = 'Грузия'
            mld = 'Молдова'
            kir = 'Киргизия'
            tad = 'Таджикистан'
            uzb = 'Узбекистан'
            tur = 'Туркменистан'
            frh = 'Франция'
            ger = 'Германия'
            isp = 'Испания'
            ita = 'Италия'
            wel = 'Британия'
            nid = 'Нидерланды'
            hwe = 'Швеция'
            pol = 'Польша'
            ceh = 'Чехия'
            aws = 'Австрия'
            alb = 'Албания'
            and2 = 'Андорра'
            bel2 = 'Бельгия'
            bos = 'Босния и Герцеговина'
            bol = 'Болгария'
            wat = 'Ватикан'
            wen = 'Венгрия'
            gre = 'Греция'
            dan = 'Дания'
            irl = 'Ирландия'
            isl = 'Исландия'
            kip = 'Кипр'
            lat = 'Латвия'
            lit = 'Литва'
            luk = 'Люксембург'
            mal = 'Мальта'
            nor = 'Норвегия'
            por = 'Португалия'
            rym = 'Румыния'
            ser = 'Сербия'
            slo = 'Словакия'
            sle = 'Словения'
            tur2 = 'Турция'
            fin = 'Финляндия'
            che = 'Черногория'
            shw = 'Швейцария'
            usa1 = 'США'
            can = 'Канада'
            mex = 'Мексика'
            gre1 = 'Гренада'
            bag = 'Багамские Острова'
            yam = 'Ямайка'
            arg = 'Аргентина'
            bra = 'Бразилия'
            chi = 'Чили'
            per = 'Перу'
            kol = 'Колумбия'
            par = 'Парагвай'
            uru = 'Уругвай'
            wen1 = 'Венесуэла'
            akw = 'Эквадор'
            gay = 'Гайана'
            sur = 'Суринам'
            frn_gv = 'Французская Гвиана'
            aus = 'Австралия'
            new_z = 'Новая Зеландия'
            new_g = 'Новая Гвинея'
            fid = 'Фиджи'
            sam = 'Самоа'
            ton = 'Тонга'
            mic = 'Микронезия'
            nau = 'Науру'
            tuw = 'Тувалу'
            ban = 'Бангладеш'
            bar = 'Барбадос'
            bah = 'Бахрейн'
            but = 'Бутан'
            wet = 'Вьетнам'
            dan1 = 'Дания'
            ind = 'Индия'
            ind1 = 'Индонезия'
            ior = 'Иордания'
            ira = 'Ирак'
            ira1 = 'Иран'
            kas = 'Казахстан'
            kit = 'Китай'
            mia = 'Мьянма'
            kuw = 'Кувейт'
            liw = 'Ливан'
            mon = 'Монголия'
            nep = 'Непал'
            oae1 = 'ОАЭ'
            pak = 'Пакистан'
            s_ar = 'Саудовская Аравия'
            sin = 'Сингапур'
            tai = 'Таиланд'
            fil = 'Филиппины'
            s_lan = 'Шри-Ланка'
            uj_kor = 'Южная Корея'
            jap = 'Япония'
            alj = 'Алжир'
            ang = 'Angola'
            ben = 'Бенин'
            bot = 'Ботсвана'
            bur = 'Бурунди'
            wat2 = 'Ватан'
            gab = 'Габон'
            gan = 'Гана'
            gvi = 'Гвинея'
            gvi1 = 'Гвинея-Бисау'
            kon = 'Демократическая Республика Конго'
            die = 'Диего-Суарес'
            zam = 'Замбия'
            zim = 'Зимбабве'
            kab = 'Кабо-Верде'
            kam = 'Камерун'
            ken = 'Кения'
            kot = 'Кот-д’Ивуар'
            lib = 'Либерия'
            liv = 'Ливия'
            mav = 'Мавритания'
            mad = 'Мадагаскар'
            mal3 = 'Малави'
            mal1 = 'Мали'
            mar = 'Марокко'
            nam = 'Намибия'
            nig = 'Нигер'
            nig1 = 'Нигерия'
            res = 'Республика Конго'
            rua = 'Руанда'
            uga = 'Уганда'
            tun = 'Тунис'
            cua = 'Центральноафриканская Республика'
            had3 = 'Чад'
            uar3 = 'Южноафриканская Республика'

            oceania1 = ['Новая Зеландия', 'Новая Гвинея', 'Фиджи', 'Самоа', 'Тонга', 'Микронезия', 'Науру', 'Тувалу']
            australia1 = ['Австралия']
            severamerika = ['США', 'Канада', 'Мексика', 'Гренада', 'Багамские острова', 'Ямайка']
            ujayaamerika = ['Аргентина', 'Бразилия', 'Чили', 'Парагвай', 'Перу', 'Колумбия', 'Уругвай', 'Венесуэла',
                            'Эквадор', 'Гайана', 'Суринам', 'Французская Гвиана']
            afrika = ['Алжир','Angola','Бенин','Ботсвана','Бурунди','Ватан','Габон','Гана','Гвинея','Гвинея-Бисау',
                      'Демократическая Республика Конго','Диего-Суарес','Замбия','Зимбабве','Кабо-Верде','Камерун',
                      'Кения','Кот-д’Ивуар','Либерия','Ливия','Мавритания','Мадагаскар','Малави','Мали','Марокко',
                      'Намибия','Нигер','Республика Конго','Руанда','Таджикистан','Уганда','Тунис',
                      'Центральноафриканская Республика','Чад','Южноафриканская Республика']
            europ = ['Россия', 'Украина', 'Беларусь', 'Грузия', 'Молдова', 'Франция', 'Германия', 'Испания', 'Австрия',
                     'Италия', 'Британия', 'Нидерланды', 'Швеция', 'Польша', 'Чехия', 'Албания', 'Андорра', 'Бельгия',
                     'Босния и Герцеговина', 'Болгария', 'Ватикан', 'Венгрия', 'Греция', 'Дания', 'Ирландия',
                     'Исландия', 'Кипр', 'Латвия', 'Литва', 'Люксембург', 'Мальта', 'Норвегия', 'Португалия', 'Румыния',
                     'Сербия', 'Словакия', 'Словения', 'Турция', 'Финляндия', 'Черногория', 'Швейцария']
            azia = ['Армения', 'Азербайджан', 'Киргизия', 'Таджикистан', 'Узбекистан', 'Туркменистан','Бангладеш',
                    'Барбадос','Бахрейн','Бутан','Вьетнам','Дания','Индия','Индонезия','Иордания','Ирак','Иран',
                    'Казахстан','Китай','Мьянма','Кувейт','Ливан','Монголия','Непал','ОАЭ','Пакистан',
                    'Саудовская Аравия','Сингапур','Таиланд','Филиппины','Шри-Ланка','Южная Корея','Япония',]

            # база данных имена
            name1 = ['Александр', 'Дмитрий', 'Максим', 'Сергей', 'Андрей', 'Алексей', 'Артём', 'Илья', 'Кирилл',
                     'Михаил', 'Никита', 'Матвей', 'Роман', 'Егор', 'Арсений', 'Иван', 'Денис', 'Евгений', 'Даниил',
                     'Тимофей', 'Владислав', 'Игорь', 'Владимир', 'Павел', 'Руслан', 'Марк', 'Константин', 'Тимур',
                     'Олег', 'Ярослав', 'Антон', 'Николай', 'Глеб', 'Данил', 'Савелий', 'Вадим', 'Степан', 'Юрий',
                     'Богдан', 'Артур', 'Семен', 'Макар', 'Лев', 'Виктор', 'Елисей', 'Виталий', 'Вячеслав', 'Захар',
                     'Мирон', 'Дамир', 'Георгий', 'Давид', 'Платон', 'Анатолий', 'Григорий', 'Демид', 'Данил',
                     'Станислав', 'Василий', 'Федор', 'Родион', 'Леонид', 'Одиссей', 'Валерий', 'Святослав',
                     'Борис', 'Эдуард', 'Марат', 'Герман', 'Петр']

            # Страна
            strane = 0
            if (d[0]) == '7':
                strane = rus
            elif d[:3] == yk:
                strane = ukr
            elif d[:3] == be:
                strane = bel
            elif d[:3] == ar:
                strane = arm
            elif d[:3] == az:
                strane = aze
            elif d[:3] == gr:
                strane = gru
            elif d[:3] == ml:
                strane = mld
            elif d[:3] == ki:
                strane = kir
            elif d[:3] == ta:
                strane = tad
            elif d[:3] == tu:
                strane = tur
            elif d[:3] == uz:
                strane = uzb
            elif d[:2] == fr:
                strane = frh
            elif d[:2] == ge:
                 strane = ger
            elif d[:2] == sp:
                strane = isp
            elif d[:2] == it:
                strane = ita
            elif d[:2] == we:
                strane = wel
            elif d[:2] == ni:
                strane = nid
            elif d[:2] == hw:
                strane = hwe
            elif d[:2] == po:
                strane = pol
            elif d[:3] == ce:
                strane = ceh
            elif d[:2] == aw:
                strane = aws
            elif d[:3] == al:
                strane = alb
            elif d[:3] == an:
                strane = and2
            elif d[:2] == be2:
                strane = bel2
            elif d[:3] == bo:
                strane = bos
            elif d[:3] == bo2:
                strane = bol
            elif d[:2] == wa:
                strane = wat
            elif d[:2] == ve:
                strane = wen
            elif d[:2] == gr2:
                strane = gre
            elif d[:2] == da:
                strane = dan
            elif d[:3] == ir:
                strane = irl
            elif d[:3] == is2:
                strane = isl
            elif d[:3] == ki2:
                strane = kip
            elif d[:3] == la:
                strane = lat
            elif d[:3] == li:
                strane = lit
            elif d[:3] == lu:
                strane = luk
            elif d[:3] == ma:
                strane = mal
            elif d[:2] == no:
                strane = nor
            elif d[:3] == po2:
                strane = por
            elif d[:2] == ry:
                strane = rym
            elif d[:3] == se:
                strane = ser
            elif d[:3] == sl:
                strane = slo
            elif d[:3] == sl2:
                strane = sle
            elif d[:2] == tu2:
                strane = tur2
            elif d[:3] == fi:
                strane = fin
            elif d[:3] == ce2:
                strane = che
            elif d[:2] == sh:
                strane = shw
            elif d[:1] == usa:
                strane = usa1
            elif d[:2] == mexica:
                strane = mex
            elif d[:3] == grenada:
                strane = gre1
            elif d[:3] == bag_ostrova:
                strane = bag
            elif d[:3] == yamayka:
                strane = yam
            elif d[:2] == argentina:
                strane = arg
            elif d[:2] == brasilia:
                strane = bra
            elif d[:2] == chili:
                strane = chi
            elif d[:2] == peru:
                strane = per
            elif d[:2] == kolumbia:
                strane = kol
            elif d[:3] == paragwai:
                strane = par
            elif d[:3] == urugwai:
                strane = uru
            elif d[:2] == wenesuela:
                strane = wen1
            elif d[:3] == akwador:
                strane = akw
            elif d[:3] == gayana:
                strane = gay
            elif d[:3] == surinam:
                strane = sur
            elif d[:3] == frnch_gviana:
                strane = frn_gv
            elif d[:2] == australia:
                strane = aus
            elif d[:2] == new_zelandya:
                strane = new_z
            elif d[:3] == new_gweneya:
                strane = new_g
            elif d[:3] == fidjy:
                strane = fid
            elif d[:3] == samoa:
                strane = sam
            elif d[:3] == tonga:
                strane = ton
            elif d[:3] == micronezia:
                strane = mic
            elif d[:3] == nauru:
                strane = nau
            elif d[:3] == tuwalu:
                strane = tuw
            elif d[:3] == banlgades:
                strane = ban
            elif d[:4] == barbados:
                strane = bar
            elif d[:3] == bahren:
                strane = bah
            elif d[:3] == butan:
                strane = but
            elif d[:2] == wetnam:
                strane = wet
            elif d[:3] == dania:
                strane = dan1
            elif d[:2] == india:
                strane = ind
            elif d[:2] == indonesia:
                strane = ind1
            elif d[:3] == iordania:
                strane = ior
            elif d[:3] == irak:
                strane = ira
            elif d[:2] == iran:
                strane = ira1
            elif d[:1] == kasahstan:
                strane = kas
            elif d[:2] == kitai:
                strane = kit
            elif d[:2] == mianma:
                strane = mia
            elif d[:3] == kuwet:
                strane = kuw
            elif d[:3] == liwan:
                strane = liw
            elif d[:3] == mongolia:
                strane = mon
            elif d[:3] == nepal:
                strane = nep
            elif d[:3] == oae:
                strane = oae1
            elif d[:2] == pakistan:
                strane = pak
            elif d[:3] == sau_ar:
                strane = s_ar
            elif d[:2] == singapur:
                strane = sin
            elif d[:2] == tailand:
                strane = tai
            elif d[:2] == filipini:
                strane = fil
            elif d[:2] == sri_lanka:
                strane = s_lan
            elif d[:2] == uj_korea:
                strane = uj_kor
            elif d[:2] == japan:
                strane = jap
            elif d[:3] == aljir:
                strane = alj
            elif d[:3] == angola:
                strane = ang
            elif d[:3] == benin:
                strane = ben
            elif d[:3] == botsvana:
                strane = bot
            elif d[:3] == burundi:
                strane = bur
            elif d[:3] == watan:
                strane = wat2
            elif d[:3] == gabon:
                strane = gab
            elif d[:3] == gana:
                strane = gan
            elif d[:3] == gvinea:
                strane = gvi
            elif d[:3] == gvinea_bitsau:
                strane = gvi1
            elif d[:3] == kongo:
                strane = kon
            elif d[:3] == diego_suares:
                strane = die
            elif d[:3] == zambia:
                strane = zam
            elif d[:3] == zimbabwe:
                strane = zim
            elif d[:3] == kabo_werde:
                strane = kab
            elif d[:3] == kamerun:
                strane = kam
            elif d[:3] == kenia:
                strane = ken
            elif d[:3] == kot_iwur:
                strane = kot
            elif d[:3] == liberia:
                strane = lib
            elif d[:3] == livia:
                strane = liv
            elif d[:3] == mavritania:
                strane = mav
            elif d[:3] == madagaskar:
                strane = mad
            elif d[:3] == malavi:
                strane = mal3
            elif d[:3] == mali:
                strane = mal1
            elif d[:3] == maroko:
                strane = mar
            elif d[:3] == namibia:
                strane = nam
            elif d[:3] == niger:
                strane = nig
            elif d[:3] == nigeria:
                strane = nig1
            elif d[:3] == res_kon:
                strane = res
            elif d[:3] == ruanda:
                strane = rua
            elif d[:3] == tunis:
                strane = tun
            elif d[:3] == cuar:
                strane = cua
            elif d[:3] == had:
                strane = had3
            elif d[:2] == uar:
                strane = uar3
            else:
                strane = 'не найдена'
            print('[+] Страна: ', strane)

            # Оператор
            phone_number = "+" + str(c)
            try:
                parsed_number = phonenumbers.parse(phone_number)

                if phonenumbers.is_valid_number(parsed_number):
                    operator = carrier.name_for_number(parsed_number, "ru")
                    if operator:
                        print(f'[+] Оператор: {operator}')
                else:
                    print('[+] Оператор не найден')
            except phonenumbers.NumberParseException as e:
                print(f'Ошибка парсинга номера: {e}')

                # Локация
            if strane in europ:
                print('[+] Локация: ', 'Европа')
            elif strane in azia:
                print('[+] Локация: Азия')
            elif strane in severamerika:
                print('[+] Локация: Северная Америка')
            elif strane in australia1:
                print('[+] Локация: ', 'Австралия')
            elif strane in ujayaamerika:
                print('[+] Локация: ', 'Южная Америка')
            elif strane in afrika:
                print('[+] Локация: ', 'Африка')
            elif strane in oceania1:
                print('[+] Локация: ', 'Океания')

                # Столица
            if strane == rus:
                print('[+] Столица: Москва')
            elif strane == ukr:
                print('[+] Столица: Киев')
            elif strane == bel:
                print('[+] Столица: Минск')
            elif strane == frh:
                print('[+] Столица: Париж')
            elif strane == ger:
                print('[+] Столица: Берлин')
            elif strane == wel:
                print('[+] Столица: Лондон')
            elif strane == arm:
                print('[+] Столица: Ереван')
            elif strane == aze:
                print('[+] Столица: Баку')
            elif strane == gru:
                print('[+] Столица: Тбилиси')
            elif strane == mld:
                print('[+] Столица: Кишинев')
            elif strane == kir:
                print('[+] Столица: Бишкек')
            elif strane == tad:
                print('[+] Столица: Душанбе')
            elif strane == uzb:
                print('[+] Столица: Ташкент')
            elif strane == tur:
                print('[+] Столица: Ашхабад')
            elif strane == isp:
                print('[+] Столица: Мадрид')
            elif strane == ita:
                print('[+] Столица: Рим')
            elif strane == nid:
                print('[+] Столица: Амстердам')
            elif strane == hwe:
                print('[+] Столица: Стокгольм')
            elif strane == pol:
                print('[+] Столица: Варшава')
            elif strane == ceh:
                print('[+] Столица: Прага')
            elif strane == aws:
                print('[+] Столица: Вена')
            elif strane == alb:
                print('[+] Столица: Тирана')
            elif strane == and2:
                print('[+] Столица: Андорра-ла-Велья')
            elif strane == bel2:
                print('[+] Столица: Брюссель')
            elif strane == bos:
                print('[+] Столица: Сараево')
            elif strane == bol:
                print('[+] Столица: София')
            elif strane == wat:
                print('[+] Столица: Ватикан')
            elif strane == wen:
                print('[+] Столица: Будапешт')
            elif strane == gre:
                print('[+] Столица: Афины')
            elif strane == dan:
                print('[+] Столица: Копенгаген')
            elif strane == irl:
                print('[+] Столица: Дублин')
            elif strane == isl:
                print('[+] Столица: Рейкьявик')
            elif strane == kip:
                print('[+] Столица: Никосия')
            elif strane == lat:
                print('[+] Столица: Рига')
            elif strane == lit:
                print('[+] Столица: Вильнюс')
            elif strane == luk:
                print('[+] Столица: Люксембург')
            elif strane == mal:
                print('[+] Столица: Валлетта')
            elif strane == nor:
                print('[+] Столица: Осло')
            elif strane == por:
                print('[+] Столица: Лиссабон')
            elif strane == rym:
                print('[+] Столица: Бухарест')
            elif strane == ser:
                print('[+] Столица: Белград')
            elif strane == slo:
                print('[+] Столица: Братислава')
            elif strane == sle:
                print('[+] Столица: Любляна')
            elif strane == tur2:
                print('[+] Столица: Анкара')
            elif strane == fin:
                print('[+] Столица: Хельсинки')
            elif strane == che:
                print('[+] Столица: Подгорица')
            elif strane == shw:
                print('[+] Столица: Берн')
            elif strane == usa1:
                print('[+] Столица: Вашингтон')
            elif strane == can:
                print('[+] Столица: Оттава')
            elif strane == mex:
                print('[+] Столица: Мехико')
            elif strane == gre1:
                print('[+] Столица: Сент-Джорджес')
            elif strane == bag:
                print('[+] Столица: Нассау')
            elif strane == yam:
                print('[+] Столица: Кингстон')
            elif strane == 'Аргентина':
                print('[+] Столица: Буэнос-Айрес')
            elif strane == 'Бразилия':
                print('[+] Столица: Бразилиа')
            elif strane == 'Чили':
                print('[+] Столица: Сантьяго')
            elif strane == 'Парагвай':
                print('[+] Столица: Асунсьон')
            elif strane == 'Перу':
                print('[+] Столица: Лима')
            elif strane == 'Колумбия':
                print('[+] Столица: Богота')
            elif strane == 'Уругвай':
                print('[+] Столица: Монтевидео')
            elif strane == 'Венесуэла':
                print('[+] Столица: Каракас')
            elif strane == 'Эквадор':
                print('[+] Столица: Кито')
            elif strane == 'Гайана':
                print('[+] Столица: Джорджтаун')
            elif strane == 'Суринам':
                print('[+] Столица: Парамарибо')
            elif strane == 'Французская Гвиана':
                print('[+] Столица: Кайенна')
            elif strane == 'Австралия':
                print('[+] Столица: Канберра')
            elif strane == 'Новая Зеландия':
                print('[+] Столица: Веллингтон')
            elif strane == 'Новая Гвинея':
                print('[+] Столица: Порт-Морсби')
            elif strane == 'Фиджи':
                print('[+] Столица: Сува')
            elif strane == 'Самоа':
                print('[+] Столица: Апиа')
            elif strane == 'Тонга':
                print('[+] Столица: Нукуалофа')
            elif strane == 'Микронезия':
                print('[+] Столица: Паликир')
            elif strane == 'Науру':
                print('[+] Столица: Йерон')
            elif strane == 'Тувалу':
                print('[+] Столица: Фунафути')
            elif strane == 'Бангладеш':
                print('[+] Столица: Дакка')
            elif strane == 'Барбадос':
                print('[+] Столица: Бриджтаун')
            elif strane == 'Бахрейн':
                print('[+] Столица: Манама')
            elif strane == 'Бутан':
                print('[+] Столица: Тхимпху')
            elif strane == 'Вьетнам':
                print('[+] Столица: Ханой')
            elif strane == 'Дания':
                print('[+] Столица: Нуук')
            elif strane == 'Индия':
                print('[+] Столица: Нью-Дели')
            elif strane == 'Индонезия':
                print('[+] Столица: Джакарта')
            elif strane == 'Иордания':
                print('[+] Столица: Амман')
            elif strane == 'Ирак':
                print('[+] Столица: Багдад')
            elif strane == 'Иран':
                print('[+] Столица: Тегеран')
            elif strane == 'Казахстан':
                print('[+] Столица: Нур-Султан')
            elif strane == 'Китай':
                print('[+] Столица: Пекин')
            elif strane == 'Мьянма':
                print('[+] Столица: Нейпьидо')
            elif strane == 'Кувейт':
                print('[+] Столица: Кувейт')
            elif strane == 'Ливан':
                print('[+] Столица: Бейрут')
            elif strane == 'Монголия':
                print('[+] Столица: Улан-Батор')
            elif strane == 'Непал':
                print('[+] Столица: Катманду')
            elif strane == 'ОАЭ':
                print('[+] Столица: Абу-Даби')
            elif strane == 'Пакистан':
                print('[+] Столица: Исламабад')
            elif strane == 'Саудовская Аравия':
                print('[+] Столица: Эр-Рияд')
            elif strane == 'Сингапур':
                print('[+] Столица: Сингапур')
            elif strane == 'Таиланд':
                print('[+] Столица: Бангкок')
            elif strane == 'Филиппины':
                print('[+] Столица: Манила')
            elif strane == 'Шри-Ланка':
                print('[+] Столица: Сри-Джаяварденепура-Котте')
            elif strane == 'Южная Корея':
                print('[+] Столица: Сеул')
            elif strane == 'Япония':
                print('[+] Столица: Токио')
            elif strane == 'Алжир':
                print('[+] Столица: Алжир')
            elif strane == 'Angola':
                print('[+] Столица: Луанда')
            elif strane == 'Бенин':
                print('[+] Столица: Порто-Ново')
            elif strane == 'Ботсвана':
                print('[+] Столица: Габороне')
            elif strane == 'Бурунди':
                print('[+] Столица: Гитега')
            elif strane == 'Ватан':
                print('[+] Столица: Ломе')
            elif strane == 'Габон':
                print('[+] Столица: Либревиль')
            elif strane == 'Гана':
                print('[+] Столица: Аккра')
            elif strane == 'Гвинея':
                print('[+] Столица: Конакри')
            elif strane == 'Гвинея-Бисау':
                print('[+] Столица: Бісау')
            elif strane == 'Демократическая Республика Конго':
                print('[+] Столица: Киншаса')
            elif strane == 'Диего-Суарес':
                print('[+] Столица: Антананариву')
            elif strane == 'Замбия':
                print('[+] Столица: Лусака')
            elif strane == 'Зимбабве':
                print('[+] Столица: Хараре')
            elif strane == 'Кабо-Верде':
                print('[+] Столица: Прая')
            elif strane == 'Камерун':
                print('[+] Столица: Яунде')
            elif strane == 'Кения':
                print('[+] Столица: Найроби')
            elif strane == 'Кот-д’Ивуар':
                print('[+] Столица: Ямусукро')
            elif strane == 'Либерия':
                print('[+] Столица: Монровия')
            elif strane == 'Ливия':
                print('[+] Столица: Триполи')
            elif strane == 'Мавритания':
                print('[+] Столица: Нуакшот')
            elif strane == 'Мадагаскар':
                print('[+] Столица: Антананариву')
            elif strane == 'Малави':
                print('[+] Столица: Лилонгве')
            elif strane == 'Мали':
                print('[+] Столица: Бамако')
            elif strane == 'Марокко':
                print('[+] Столица: Рабат')
            elif strane == 'Намибия':
                print('[+] Столица: Виндхук')
            elif strane == 'Нигер':
                print('[+] Столица: Ниамей')
            elif strane == 'Нигерия':
                print('[+] Столица: Абуджа')
            elif strane == 'Республика Конго':
                print('[+] Столица: Браззавиль')
            elif strane == 'Руанда':
                print('[+] Столица: Кигали')
            elif strane == 'Уганда':
                print('[+] Столица: Кампала')
            elif strane == 'Тунис':
                print('[+] Столица: Тунис')
            elif strane == 'Центральноафриканская Республика':
                print('[+] Столица: Банги')
            elif strane == 'Чад':
                print('[+] Столица: Нджаменна')
            elif strane == 'Южноафриканская Республика':
                print('[+] Столица: Претория')
            else:
                print('[+] Столица: Не найдена')

                # Валюта
            if strane == rus:
                print('[+] Валюта: (₽)рубли')
            elif strane == ukr:
                print('[+] Валюта: (₴)гривна')
            elif strane == bel:
                print('[+] Валюта: (Br)белорусский рубль')
            elif strane == arm:
                print('[+] Валюта: (֏)драм')
            elif strane == aze:
                print('[+] Валюта: (₼)манат')
            elif strane == gru:
                print('[+] Валюта: (ლ)лари')
            elif strane == mld:
                print('[+] Валюта: (MDL)молдавский лей')
            elif strane == kir:
                print('[+] Валюта: (сом)сом')
            elif strane == tad:
                print('[+] Валюта: (сомони)сомони')
            elif strane == uzb:
                print('[+] Валюта: (сум)сум')
            elif strane == tur:
                print('[+] Валюта: (TMT)туркменский манат')
            elif strane == frh:
                print('[+] Валюта: (€)евро')
            elif strane == ger:
                print('[+] Валюта: (€)евро')
            elif strane == isp:
                print('[+] Валюта: (€)евро')
            elif strane == ita:
                print('[+] Валюта: (€)евро')
            elif strane == wel:
                print('[+] Валюта: (£)фунт стерлингов')
            elif strane == nid:
                print('[+] Валюта: (€)евро')
            elif strane == hwe:
                print('[+] Валюта: (kr)шведская крона')
            elif strane == pol:
                print('[+] Валюта: (zł)злотый')
            elif strane == ceh:
                print('[+] Валюта: (Kč)чешская крона')
            elif strane == aws:
                print('[+] Валюта: (€)евро')
            elif strane == alb:
                print('[+] Валюта: (ALL)Албанский лек')
            elif strane == and2:
                print('[+] Валюта: (EUR)Евро')
            elif strane == bel2:
                print('[+] Валюта: (EUR)Евро')
            elif strane == bos:
                print('[+] Валюта: (BAM)Конвертируемая марка')
            elif strane == bol:
                print('[+] Валюта: (BGN)Болгарский лев')
            elif strane == wat:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == wen:
                print('[+] Валюта: (HUF)Венгерский форинт')
            elif strane == gre:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == dan:
                print('[+] Валюта: (DKK)Данская крона')
            elif strane == irl:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == isl:
                print('[+] Валюта: (ISK)Исландская крона')
            elif strane == kip:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == lat:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == lit:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == luk:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == mal:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == nor:
                print('[+] Валюта: (NOK)Норвежская крона')
            elif strane == por:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == rym:
                print('[+] Валюта: (RON)Румынский лей')
            elif strane == ser:
                print('[+] Валюта: (RSD)Сербский динар')
            elif strane == slo:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == sle:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == tur2:
                print('[+] Валюта: (TRY)Турецкая лира')
            elif strane == fin:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == che:
                print('[+] Валюта: (EUR)Евро ')
            elif strane == shw:
                print('[+] Валюта: (CHF)Швейцарский франк')
            elif strane == usa1:
                print('[+] Валюта: (USD)Доллар США')
            elif strane == can:
                print('[+] Валюта: (CAD)Канадский доллар')
            elif strane == mex:
                print('[+] Валюта: (MXN)Мексиканское песо')
            elif strane == gre1:
                print('[+] Валюта: (XCD)Восточно-карибский доллар')
            elif strane == bag:
                print('[+] Валюта: (BSD)Багамский доллар')
            elif strane == yam:
                print('[+] Валюта: (JMD)Ямайский доллар')
            elif strane == 'Аргентина':
                print('[+] Валюта: (ARS)Аргентинское песо')
            elif strane == 'Бразилия':
                print('[+] Валюта: (BRL)Бразильский реал')
            elif strane == 'Чили':
                print('[+] Валюта: (CLP)Чилийское песо')
            elif strane == 'Парагвай':
                print('[+] Валюта: (PYG)Парагвайский гуарани')
            elif strane == 'Перу':
                print('[+] Валюта: (PEN)Периуанский сол')
            elif strane == 'Колумбия':
                print('[+] Валюта: (COP)Колумбийское песо')
            elif strane == 'Уругвай':
                print('[+] Валюта: (UYU)Уругвайское песо')
            elif strane == 'Венесуэла':
                print('[+] Валюта: (VES)Венесуэльский боливар')
            elif strane == 'Эквадор':
                print('[+] Валюта: (USD)УСД')
            elif strane == 'Гайана':
                print('[+] Валюта: (GYD)Гаянский доллар')
            elif strane == 'Суринам':
                print('[+] Валюта: (SRD)Суринамский доллар')
            elif strane == 'Французская Гвиана':
                print('[+] Валюта: (EUR)Евро')
            elif strane == 'Австралия':
                print('[+] Валюта: (AUD)Австралийский доллар')
            elif strane == 'Новая Зеландия':
                print('[+] Валюта: (NZD)Новозеландский доллар')
            elif strane == 'Новая Гвинея':
                print('[+] Валюта: (PGK)Кина')
            elif strane == 'Фиджи':
                print('[+] Валюта: (FJD)Фиджийский доллар')
            elif strane == 'Самоа':
                print('[+] Валюта: (WST)Тала')
            elif strane == 'Тонга':
                print('[+] Валюта: (TOP)Тонгийский паанга')
            elif strane == 'Микронезия':
                print('[+] Валюта: (USD)Доллар США')
            elif strane == 'Науру':
                print('[+] Валюта: (AUD)Науруанский доллар')
            elif strane == 'Тувалу':
                print('[+] Валюта: (AUD)Австралийский доллар')
            elif strane == 'Бангладеш':
                print('[+] Валюта: Бангладешская така (BDT)')
            elif strane == 'Барбадос':
                print('[+] Валюта: Барбадосский доллар (BBD)')
            elif strane == 'Бахрейн':
                print('[+] Валюта: Бахрейнский динар (BHD)')
            elif strane == 'Бутан':
                print('[+] Валюта: Нгултрум (BTN)')
            elif strane == 'Вьетнам':
                print('[+] Валюта: Вьетнамский донг (VND)')
            elif strane == 'Дания':
                print('[+] Валюта: Гренландская крона (DKK)')
            elif strane == 'Индия':
                print('[+] Валюта: Индийская рупия (INR)')
            elif strane == 'Индонезия':
                print('[+] Валюта: Индонезийская рупия (IDR)')
            elif strane == 'Иордания':
                print('[+] Валюта: Иорданский динар (JOD)')
            elif strane == 'Ирак':
                print('[+] Валюта: Иракский динар (IQD)')
            elif strane == 'Иран':
                print('[+] Валюта: Иранский риал (IRR)')
            elif strane == 'Казахстан':
                print('[+] Валюта: Казахстанский тенге (KZT)')
            elif strane == 'Китай':
                print('[+] Валюта: Китайский юань (CNY)')
            elif strane == 'Мьянма':
                print('[+] Валюта: Мьянмский кьят (MMK)')
            elif strane == 'Кувейт':
                print('[+] Валюта: Кувейтский динар (KWD)')
            elif strane == 'Ливан':
                print('[+] Валюта: Ливанский фунт (LBP)')
            elif strane == 'Монголия':
                print('[+] Валюта: Монгол банкнот (MNT)')
            elif strane == 'Непал':
                print('[+] Валюта: Непальская рупия (NPR)')
            elif strane == 'ОАЭ':
                print('[+] Валюта: Дирхам ОАЭ (AED)')
            elif strane == 'Пакистан':
                print('[+] Валюта: Пакистанская рупия (PKR)')
            elif strane == 'Саудовская Аравия':
                print('[+] Валюта: Саудовский риял (SAR)')
            elif strane == 'Сингапур':
                print('[+] Валюта: Сингапурский доллар (SGD)')
            elif strane == 'Таиланд':
                print('[+] Валюта: Тайский бат (THB)')
            elif strane == 'Филиппины':
                print('[+] Валюта: Филиппинское песо (PHP)')
            elif strane == 'Шри-Ланка':
                print('[+] Валюта: Шри-ланкийская рупия (LKR)')
            elif strane == 'Южная Корея':
                print('[+] Валюта: Южнокорейский вон (KRW)')
            elif strane == 'Япония':
                print('[+] Валюта: Японская иена (JPY)')
            elif strane == 'Алжир':
                print('[+] Валюта: Алжирский динар (DZD)')
            elif strane == 'Angola':
                print('[+] Валюта: Ангольская кванза (AOA)')
            elif strane == 'Бенин':
                print('[+] Валюта: Франк КФА (XOF)')
            elif strane == 'Ботсвана':
                print('[+] Валюта: Пула (BWP)')
            elif strane == 'Бурунди':
                print('[+] Валюта: Бурундийский франк (BIF)')
            elif strane == 'Ватан':
                print('[+] Валюта: Франк КФА (XOF)')
            elif strane == 'Габон':
                print('[+] Валюта: Франк КФА (XAF)')
            elif strane == 'Гана':
                print('[+] Валюта: Ганский седи (GHS)')
            elif strane == 'Гвинея':
                print('[+] Валюта: Гвинейский франк (GNF)')
            elif strane == 'Гвинея-Бисау':
                print('[+] Валюта: Франк КФА (XOF)')
            elif strane == 'Демократическая Республика Конго':
                print('[+] Валюта: Конголезский франк (CDF)')
            elif strane == 'Диего-Суарес':
                print('[+] Валюта: Малагасийский ариари (MGA)')
            elif strane == 'Замбия':
                print('[+] Валюта: Замбийская квача (ZMW)')
            elif strane == 'Зимбабве':
                print('[+] Валюта: Зимбабвийский доллар (ZWL)')
            elif strane == 'Кабо-Верде':
                print('[+] Валюта: Кабо-верденский эскудо (CVE)')
            elif strane == 'Камерун':
                print('[+] Валюта: Франк КФА (XAF)')
            elif strane == 'Кения':
                print('[+] Валюта: Кенийский шиллинг (KES)')
            elif strane == 'Кот-д’Ивуар':
                print('[+] Валюта: Франк КФА (XOF)')
            elif strane == 'Либерия':
                print('[+] Валюта: Либерийский доллар (LRD)')
            elif strane == 'Ливия':
                print('[+] Валюта: Ливийский динар (LYD)')
            elif strane == 'Мавритания':
                print('[+] Валюта: Угийя (MRU)')
            elif strane == 'Мадагаскар':
                print('[+] Валюта: Малагасийский ариари (MGA)')
            elif strane == 'Малави':
                print('[+] Валюта: Малавийская квача (MWK)')
            elif strane == 'Мали':
                print('[+] Валюта: Франк КФА (XOF)')
            elif strane == 'Марокко':
                print('[+] Валюта: Марокканский дирхам (MAD)')
            elif strane == 'Намибия':
                print('[+] Валюта: Намибийский доллар (NAD)')
            elif strane == 'Нигер':
                print('[+] Валюта: Франк КФА (XOF)')
            elif strane == 'Нигерия':
                print('[+] Валюта: Нигерийская наира (NGN)')
            elif strane == 'Республика Конго':
                print('[+] Валюта: Франк КФА (XAF)')
            elif strane == 'Руанда':
                print('[+] Валюта: Руанди франк (RWF)')
            elif strane == 'Уганда':
                print('[+] Валюта: Угандийский шиллинг (UGX)')
            elif strane == 'Тунис':
                print('[+] Валюта: Тунисский динар (TND)')
            elif strane == 'Центральноафриканская Республика':
                print('[+] Валюта: Франк КФА (XAF)')
            elif strane == 'Чад':
                print('[+] Валюта: Франк КФА (XAF)')
            elif strane == 'Южноафриканская Республика':
                print('[+] Валюта: Южноафриканский ранд (ZAR)')
            else:
                print('Валюта: не найдена')
            print('')
            print('Проверьте эти ссылки: ')
            print('[+] Whatsap: '+'https://api.WhatsApp.com/send?phone='+str(c))
            print('[+] Viber :'+'https://viber://add?number='+str('+' + c))
            print('[+] Skype звонок: '+'https://skype:'+str('+' + c))
            print('[+] Telegram: '+'https://t.me/'+str('+' + c))
            print('[+] Звонок : '+'tel:'+str('+' + c))
            print('[+] Поиск в яндексе: '+'https://yandex.ru/yandsearch?text='+str('+' + c))
            print('[+] Поиск в гугл: '+'https://google.ru/search?q='+str('+' + c))
            print('')
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '9':
            def generate_password(length, uppercase=True, digits=True, punctuation=True):
                characters = string.ascii_lowercase
                if uppercase:
                    characters += string.ascii_uppercase
                if digits:
                    characters += string.digits
                if punctuation:
                    characters += string.punctuation

                password = ''.join(random.choice(characters) for i in range(length))
                return password

            length = int(input("Укажите длину пароля: "))
            include_uppercase = input("Включать заглавные буквы? (1/0): ").lower() == '1'
            include_digits = input("Включать цифры? (1/0): ").lower() == '1'
            include_punctuation = input("Включать специальные символы? (1/0): ").lower() == '1'

            generated_password = generate_password(length, include_uppercase, include_digits, include_punctuation)
            print("Сгенерированный пароль:", generated_password)

            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '10':
            emails = ['@gmail.com','@yahoo.com','@outlook.com','@mail.ru']
            def generate_random_string(num_letters, num_digits):
                letters = random.choices(string.ascii_letters, k=num_letters)
                digits = random.choices(string.digits, k=num_digits)
                random_string = letters + digits
                random.shuffle(random_string)
                return ''.join(random_string)

            num_strings = int(input("Введите количество почт: "))
            print("Сгенерированная(ые) почты:")
            for _ in range(num_strings):
                random_string = generate_random_string(random.randint(1, 10), random.randint(1, 10))
                print(random_string + random.choice(emails))

            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '2':
            import Cryptographer
            Cryptographer.Coder1()

            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '3':
            def get_external_ip():
                response = requests.get('https://api.ipify.org?format=json')
                ip = response.json()['ip']
                return ip


            external_ip = get_external_ip()
            print("Ваш внешний IP-адрес:", external_ip)

            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '14':
            clear_console()
            with open('manual_osint.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    print(line.strip())
            print('')

            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '15':
            clear_console()
            with open('manual_anonim.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    print(line.strip())
            print('')
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '11':
            sex = input('Какого пола будет владелец пасспота (1Мужской, 2Женский): ')
            if sex == 1 or sex == '1':
                name1 = ['Александр', 'Дмитрий', 'Максим', 'Сергей', 'Андрей', 'Алексей', 'Артём', 'Илья', 'Кирилл',
                         'Михаил', 'Никита', 'Матвей', 'Роман', 'Егор', 'Арсений', 'Иван', 'Денис', 'Евгений', 'Даниил',
                         'Тимофей', 'Владислав', 'Игорь', 'Владимир', 'Павел', 'Руслан', 'Марк', 'Константин', 'Тимур',
                         'Олег', 'Ярослав', 'Антон', 'Николай', 'Глеб', 'Данил', 'Савелий', 'Вадим', 'Степан', 'Юрий',
                         'Богдан', 'Артур', 'Семен', 'Макар', 'Лев', 'Виктор', 'Елисей', 'Виталий', 'Вячеслав', 'Захар',
                         'Мирон', 'Дамир', 'Георгий', 'Давид', 'Платон', 'Анатолий', 'Григорий', 'Демид', 'Данил',
                         'Станислав', 'Василий', 'Федор', 'Родион', 'Леонид', 'Одиссей', 'Валерий', 'Святослав',
                         'Борис', 'Эдуард', 'Марат', 'Герман', 'Петр']

                Surname1 = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов',
                            'Новиков', 'Федоров', 'Морозов', 'Волков', 'Алексеев', 'Лебедев', 'Семенов', 'Егоров',
                            'Павлов', 'Козлов', 'Степанов', 'Николаев', 'Орлов', 'Андреев', 'Макаров', 'Никитин',
                            'Захаров', 'Зайцев', 'Соловьев', 'Борисов', 'Яковлев', 'Григорьев', 'Романов', 'Воробьев',
                            'Сергеев', 'Кузьмин', 'Фролов', 'Александров', 'Дмитриев', 'Королев', 'Гусев', 'Киселев',
                            'Ильин', 'Максимов', 'Поляков', 'Сорокин', 'Виноградов', 'Ковалев', 'Белов', 'Медведев',
                            'Антонов', 'Тарасов', 'Жуков', 'Баранов', 'Филиппов', 'Комаров', 'Давыдов', 'Беляев',
                            'Герасимов', 'Богданов', 'Осипов', 'Сидоров', 'Матвеев', 'Титов', 'Марков', 'Миронов',
                            'Крылов', 'Куликов', 'Карпов', 'Власов', 'Мельников', 'Денисов']

                Middlename1 = ['Арсеньевич', 'Артёмович', 'Артемьевич', 'Артурович', 'Архипович', 'Давидович',
                               'Давыдович', 'Даниилович', 'Данилович', 'Демидович', 'Магомедович', 'Магометович',
                               'Макарович', 'Максимилианович', 'Максимович', 'Олегович', 'Осипович', 'Семёнович',
                               'Сергеевич', 'Сидорович']

                date1 = ['1994-09-14', '2003-04-21', '1996-06-25', '2008-11-02', '2001-05-11',
                        '1993-12-08', '2005-03-17', '1999-08-29', '2007-01-10', '1995-04-04',
                        '2000-10-15', '1997-07-19', '2006-02-26', '2009-09-07', '2002-06-30',
                        '1991-11-03', '1998-12-20', '2004-08-11', '1992-01-23', '2003-10-14',
                        '2006-03-05', '1995-09-28', '2008-12-18', '1993-05-22', '2001-04-06',
                        '1997-11-30', '1999-02-13', '2007-07-24', '2004-01-16', '1992-09-04',
                        '2005-10-08', '1996-03-21', '2002-11-12', '1994-06-03', '2000-07-28',
                        '1998-05-15', '2009-02-27', '1993-07-05', '2001-12-19', '1996-10-01',
                        '1995-08-12', '2007-06-09', '2002-03-23', '1999-12-02', '1997-04-08',
                        '2006-11-26', '2004-04-30', '2000-02-07', '1992-05-19', '1998-10-27']

                seria_j = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                           "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                           "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                           "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
                           "41", "42", "43", "44", "45", "46", "47", "48", "49", "50"]

                passport_offices1 = [
                    "Управление по вопросам миграции МВД России по Москве",
                    "Отделение паспортного стола в Санкт-Петербурге",
                    "Управление по вопросам миграции МВД России по Екатеринбургу",
                    "Отдел по вопросам миграции в Казани",
                    "Управление по вопросам миграции в Новосибирске",
                    "Отделение паспортного стола в Нижнем Новгороде",
                    "Управление по вопросам миграции в Ростове-на-Дону",
                    "Отдел по вопросам миграции в Челябинске",
                    "Управление по вопросам миграции в Самаре",
                    "Отделение паспортного стола в Уфе",
                    "Управление по вопросам миграции в Красноярске",
                    "Отдел по вопросам миграции в Волгограде",
                    "Управление по вопросам миграции в Воронеже",
                    "Отделение паспортного стола в Саратове",
                    "Управление по вопросам миграции в Омске",
                    "Отдел по вопросам миграции в Тольятти",
                    "Управление по вопросам миграции в Пермском крае",
                    "Отделение паспортного стола в Архангельске",
                    "Управление по вопросам миграции в Калининграде",
                    "Отдел по вопросам миграции в Ярославле"
                ]

                daterandom = random.choice(date1)
                dtr1 = []
                dtr1.append(daterandom)
                dtr1 = list(daterandom)

                print('[+] Фамилия: ', random.choice(Surname1))
                print('[+] Имя: ', random.choice(name1))
                print('[+] Отчество:', random.choice(Middlename1))
                print('[+] Дата рождения: ', daterandom)
                data_widachi = int(daterandom[:4]) + 14
                seria_j1 = str(data_widachi)[-2:]

                random_number = random.randint(101, 999999)
                formatted_number = str(random_number).zfill(6)
                print('[+] Серия: ', random.choice(seria_j), seria_j1)
                print('[+] Номер: ', formatted_number)
                print('[+] Дата выдачи: ', str(data_widachi) + str(daterandom[4:10]))
                print('[+] Выдан: ', random.choice(passport_offices1))

                b = input("Хотите запустить программу ещё раз? (1/0): ")


            elif sex == 2 or sex == '2':
                name2 = ['Анастасия', 'Анна', 'Мария', 'Елена', 'Дарья', 'Алина', 'Ирина', 'Екатерина', 'Арина',
                         'Полина', 'Ольга', 'Юлия', 'Татьяна', 'Наталья', 'Виктория', 'Елизавета', 'Ксения', 'Милана',
                         'Вероника', 'Алиса', 'Валерия', 'Александра', 'Ульяна', 'Кристина', 'София', 'Марина',
                         'Светлана', 'Варвара', 'Софья', 'Диана', 'Яна', 'Кира', 'Ангелина', 'Маргарита', 'Ева']

                Surname2 = ['Иванова', 'Смирнова', 'Кузнецова', 'Попова', 'Васильева', 'Петрова', 'Соколова',
                            'Михайлова', 'Новикова', 'Федорова', 'Морозова', 'Волкова', 'Алексеева', 'Лебедева',
                            'Семенова', 'Егорова', 'Павлова', 'Козлова', 'Степанова', 'Николаева', 'Орлова', 'Андреева',
                            'Макарова', 'Никитина', 'Захарова', 'Зайцева', 'Соловьева', 'Борисоваа', 'Яковлеваа',
                            'Григорьева', 'Романова', 'Воробьева', 'Сергеева', 'Кузьмина', 'Фролова', 'Александрова',
                            'Дмитриева', 'Королева', 'Гусева', 'Киселева', 'Ильина', 'Максимова', 'Полякова',
                            'Сорокина']

                Middlename2 = ['Андреевна', 'Андрониковна', 'Антоновна', 'Аркадьевна', 'Афанасьевна', 'Ивановна',
                               'Игнатьевна', 'Игоревна', 'Ильгизовна', 'Ильмировна', 'Павловна', 'Петровна',
                               'Платоновна', 'Прохоровна', 'Сахипзадовна', 'Семёновна', 'Сергеевна',
                               'Сидоровна', 'Сильвестровна', 'Фёдоровна', 'Филипповна']

                date2 = ['1994-09-14', '2003-04-21', '1996-06-25', '2008-11-02', '2001-05-11',
                         '1993-12-08', '2005-03-17', '1999-08-29', '2007-01-10', '1995-04-04',
                         '2000-10-15', '1997-07-19', '2006-02-26', '2009-09-07', '2002-06-30',
                         '1991-11-03', '1998-12-20', '2004-08-11', '1992-01-23', '2003-10-14',
                         '2006-03-05', '1995-09-28', '2008-12-18', '1993-05-22', '2001-04-06',
                         '1997-11-30', '1999-02-13', '2007-07-24', '2004-01-16', '1992-09-04',
                         '2005-10-08', '1996-03-21', '2002-11-12', '1994-06-03', '2000-07-28',
                         '1998-05-15', '2009-02-27', '1993-07-05', '2001-12-19', '1996-10-01',
                         '1995-08-12', '2007-06-09', '2002-03-23', '1999-12-02', '1997-04-08',
                         '2006-11-26', '2004-04-30', '2000-02-07', '1992-05-19', '1998-10-27']

                seria_j = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                         "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                         "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                         "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
                         "41", "42", "43", "44", "45", "46", "47", "48", "49", "50"]

                number_pas = []

                passport_offices2 = [
                    "Управление по вопросам миграции МВД России по Москве",
                    "Отделение паспортного стола в Санкт-Петербурге",
                    "Управление по вопросам миграции МВД России по Екатеринбургу",
                    "Отдел по вопросам миграции в Казани",
                    "Управление по вопросам миграции в Новосибирске",
                    "Отделение паспортного стола в Нижнем Новгороде",
                    "Управление по вопросам миграции в Ростове-на-Дону",
                    "Отдел по вопросам миграции в Челябинске",
                    "Управление по вопросам миграции в Самаре",
                    "Отделение паспортного стола в Уфе",
                    "Управление по вопросам миграции в Красноярске",
                    "Отдел по вопросам миграции в Волгограде",
                    "Управление по вопросам миграции в Воронеже",
                    "Отделение паспортного стола в Саратове",
                    "Управление по вопросам миграции в Омске",
                    "Отдел по вопросам миграции в Тольятти",
                    "Управление по вопросам миграции в Пермском крае",
                    "Отделение паспортного стола в Архангельске",
                    "Управление по вопросам миграции в Калининграде",
                    "Отдел по вопросам миграции в Ярославле"
                ]

                daterandom = random.choice(date2)
                dtr1 = []
                dtr1.append(daterandom)
                dtr1 = list(daterandom)

                print('[+] Фамилия: ', random.choice(Surname2))
                print('[+] Имя: ', random.choice(name2))
                print('[+] Отчество:', random.choice(Middlename2))
                print('[+] Дата рождения: ', daterandom)
                data_widachi = int(daterandom[:4]) + 14
                seria_j1 = str(data_widachi)[-2:]

                random_number = random.randint(101, 999999)
                formatted_number = str(random_number).zfill(6)
                print('[+] Серия: ', random.choice(seria_j),seria_j1)
                print('[+] Номер: ', formatted_number)
                print('[+] Дата выдачи: ', str(data_widachi) + str(daterandom[4:10]))
                print('[+] Выдан: ', random.choice(passport_offices2))

            else:
                print('Eror')

                b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '16':
            clear_console()
            with open('manual_search_on_IP.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    print(line.strip())
            print('')
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '17':
            import osint_tools
            osint_tools.osint_tools()
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '4':
            import maps_search
            latitude = input('Широта: ')
            longiude = input('Долгота: ')
            maps_search.open_map(latitude, longiude)
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '5':
            import nick_search
            nick_search.nickname()
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '12':
            import lichnost_generate
            lichnost_generate.generating()
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '6':
            import socr_url
            socr_url.shorten_url
            long_url = input("Введите длинную ссылку: ")
            short_url = socr_url.shorten_url(long_url)
            print("Укороченная ссылка:", short_url)
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '13':
            import card_generate
            card_generate.generate()
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '7':
            import telegram_search
            telegram_search.user()
            telegram_search.info()
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '8':
            import Valid_ip
            ip = input("[+] Введите IP-адрес: ")
            if Valid_ip.is_valid_ip(ip):
                print("[+] IP - valid")
                Valid_ip.get_ip_info(ip)
            else:
                print("[+] IP - not valid")
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '18':
            import main
            main.main()
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '19':
            subprocess.run("python Doska.py ", shell=True)
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '20':
            import DataBase
            DataBase.main()
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '21':
            import patterns
            patterns.v2()
            b = input("Хотите запустить программу ещё раз? (1/0): ")

        elif b == '0':
            print('End')
            break
        else:
            print('Eror')
            time.sleep(2)
        if b == "0":
            break
        else:
            clear_console()

elif a == '2':
    print('End')
else:
    print("Eror")
    time.sleep(2)