import os
import platform
import colorama
from colorama import Fore
import requests

def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def nickname():
    nick = input('Введите ник пользователя: ')

    instagram = 'https://www.instagram.com/'
    tiktok = 'https://www.tiktok.com/@'
    twitter = 'https://twitter.com/'
    facebook = 'https://www.facebook.com/'
    youtube = 'https://www.youtube.com/@'
    tme = 'https://t.me/'
    roblox = 'https://www.roblox.com/user.aspx?username='
    twitch = 'https://www.twitch.tv/'
    vk = 'https://vk.com/'
    kwork = 'https://kwork.ru/user/'
    steamcommunity = 'https://steamcommunity.com/id/'
    playerok = 'https://playerok.com/profile/'
    github = 'https://github.com/'
    ok = 'https://ok.ru/'
    pornhub = 'https://rt.pornhub.com/users/'
    soundcloud = 'https://soundcloud.com/'
    tumblr = 'https://www.tumblr.com/blog/view/'
    ask = 'https://ask.fm/'
    znanija = 'https://znanija.com/app/profile/'
    deviantart = 'https://www.deviantart.com/'
    flickr = 'https://www.flickr.com/'
    flinkedin = 'https://ru.linkedin.com/in/'
    myspace = 'https://myspace.com/'
    pinterest = 'https://www.pinterest.com/'
    reddit = 'https://www.reddit.com/user/'

    instagram = instagram + str(nick)
    tiktok = tiktok + str(nick)
    twitter = twitter + str(nick)
    facebook = facebook + str(nick)
    youtube = youtube + str(nick)
    tme = tme + str(nick)
    roblox = roblox + str(nick)
    twitch = twitch + str(nick)
    vk = vk + str(nick)
    kwork = kwork + str(nick)
    steamcommunity = steamcommunity + str(nick)
    playerok = playerok + str(nick)
    github = github + str(nick)
    ok = ok + str(nick)
    pornhub = pornhub + str(nick)
    soundcloud = soundcloud + str(nick)
    tumblr = tumblr + str(nick)
    ask = ask + str(nick)
    znanija = znanija + str(nick)
    deviantart = deviantart + str(nick)
    flickr = flickr + str(nick)
    flinkedin = flinkedin + str(nick)
    myspace = myspace + str(nick)
    pinterest = pinterest + str(nick)
    reddit = reddit + str(nick)

    clear_console()

    response = requests.get(vk)
    if response.status_code == 200:
        print(Fore.GREEN + vk)
    else:
        print(Fore.RED + vk)

    response = requests.get(tiktok)
    if response.status_code == 200:
        print(Fore.GREEN + tiktok)
    else:
        print(Fore.RED + tiktok)

    response = requests.get(youtube)
    if response.status_code == 200:
        print(Fore.GREEN + youtube)
    else:
        print(Fore.RED + youtube)

    response = requests.get(tme)
    if response.status_code == 200:
        print(Fore.GREEN + tme)
    else:
        print(Fore.RED + tme)

    response = requests.get(roblox)
    if response.status_code == 200:
        print(Fore.GREEN + roblox)
    else:
        print(Fore.RED + roblox)

    response = requests.get(twitch)
    if response.status_code == 200:
        print(Fore.GREEN + twitch)
    else:
        print(Fore.RED + twitch)

    response = requests.get(kwork)
    if response.status_code == 200:
        print(Fore.GREEN + kwork)
    else:
        print(Fore.RED + kwork)

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

    response = requests.get(ok)
    if response.status_code == 200:
        print(Fore.GREEN + ok)
    else:
        print(Fore.RED + ok)

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

    response = requests.get(myspace)
    if response.status_code == 200:
        print(Fore.GREEN + myspace)
    else:
        print(Fore.RED + myspace)

    response = requests.get(flickr)
    if response.status_code == 200:
        print(Fore.GREEN + flickr)
    else:
        print(Fore.RED + flickr)

    response = requests.get(tumblr)
    if response.status_code == 200:
        print(Fore.GREEN + tumblr)
    else:
        print(Fore.RED + tumblr)

    return