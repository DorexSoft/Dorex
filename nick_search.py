import os
import platform
import colorama
from colorama import Fore
import requests

def nickname():
    nick = input('[+] Введите ник пользователя: ')

    instagram = f'https://www.instagram.com/{nick}'
    tiktok = f'https://www.tiktok.com/@{nick}'
    twitter = f'https://twitter.com/{nick}'
    facebook = f'https://www.facebook.com/{nick}'
    youtube = f'https://www.youtube.com/@{nick}'
    tme = f'https://t.me/{nick}'
    roblox = f'https://www.roblox.com/user.aspx?username={nick}'
    twitch = f'https://www.twitch.tv/{nick}'
    vk = f'https://vk.com/{nick}'
    kwork = f'https://kwork.ru/user/{nick}'
    steamcommunity = f'https://steamcommunity.com/id/{nick}'
    playerok = f'https://playerok.com/profile/{nick}'
    github = f'https://github.com/{nick}'
    ok = f'https://ok.ru/{nick}'
    pornhub = f'https://rt.pornhub.com/users/{nick}'
    soundcloud = f'https://soundcloud.com/{nick}'
    tumblr = f'https://www.tumblr.com/blog/view/{nick}'
    ask = f'https://ask.fm/{nick}'
    znanija = f'https://znanija.com/app/profile/{nick}'
    deviantart = f'https://www.deviantart.com/{nick}'
    flickr = f'https://www.flickr.com/{nick}'
    flinkedin = f'https://ru.linkedin.com/in/{nick}'
    myspace = f'https://myspace.com/{nick}'
    pinterest = f'https://www.pinterest.com/{nick}'
    reddit = f'https://www.reddit.com/user/{nick}'

    response = requests.get(vk)
    if response.status_code == 200:
        print(Fore.GREEN + vk)
    else:
        print(Fore.RED + vk)

    response = requests.get(ok)
    if response.status_code == 200:
        print(Fore.GREEN + ok)
    else:
        print(Fore.RED + ok)

    response = requests.get(kwork)
    if response.status_code == 200:
        print(Fore.GREEN + kwork)
    else:
        print(Fore.RED + kwork)

    response = requests.get(twitch)
    if response.status_code == 200:
        print(Fore.GREEN + twitch)
    else:
        print(Fore.RED + twitch)

    response = requests.get(steamcommunity)
    if response.status_code == 200:
        print(Fore.GREEN + steamcommunity)
    else:
        print(Fore.RED + steamcommunity)

    response = requests.get(playerok)
    if response.status_code == 200:
        print(Fore.GREEN + playerok)
    else:
        print(Fore.RED + playerok)

    response = requests.get(github)
    if response.status_code == 200:
        print(Fore.GREEN + github)
    else:
        print(Fore.RED + github)

    response = requests.get(pornhub)
    if response.status_code == 200:
        print(Fore.GREEN + pornhub)
    else:
        print(Fore.RED + pornhub)

    response = requests.get(pinterest)
    if response.status_code == 200:
        print(Fore.GREEN + pinterest)
    else:
        print(Fore.RED + pinterest)

    response = requests.get(reddit)
    if response.status_code == 200:
        print(Fore.GREEN + reddit)
    else:
        print(Fore.RED + reddit)

    return