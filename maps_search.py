import webbrowser

def open_map(latitude, longiude):
    url = f"https://www.google.ru/maps/@{latitude},{longiude},15z"
    webbrowser.open(url)
    return