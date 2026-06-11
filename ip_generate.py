import random

def generateIP():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    d = random.randint(0, 255)
    print(f"""[+] Random IP: {a}.{b}.{c}.{d}
""")
    return