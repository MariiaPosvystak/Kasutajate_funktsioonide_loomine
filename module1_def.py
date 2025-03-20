#1
def arithmetic(arv1:float,arv2:float,tehe:str)->any:
    """Lihtne kalkulaator 
    + - liitmine
    - - lahutamine
    * - korrutamine 
    / - jagamine
    :param float arv1: Sisend kasutajalt, mingi ujukomaarv
    :param float arv2: Sisend kasutajalt, mingi ujukomaarv
    :param str tehe: aritmeetiline, tehe, mis valib kasutaja
    :rtype: var Määrata tüüp(float või str)
    """
    if tehe in ["+","-","*","/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="tundmatu te´he"
    return vastus

#2
def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab tõeväärtsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v

#3.1
def square(külg:float)->any:
    """Ruudu pindala ja ümbermõõt leidmine
    :param float külg: Ruudu külg
    :rtype: float tagastab ruudu pindala
    """
    S=külg**2
    P=külg*4
    d=(2)**(1/2)*külg
    return S,P,d

#3.2
def square(külg:float)->any:
    """Ruudu pindala ja ümbermõõt leidmine
    :param float külg: Ruudu külg
    :rtype: float tagastab ruudu pindala
    """
    S=külg**2
    P=külg*4
    d=(2)**(1/2)*külg
    s_list=[S,P,d]
    return s_list

#4.1
def season(kuu:int,season:str)->any:
    """Kuu number ja season leidmine
    :param int kuu: kuu number
    :param str season: 
    """

    if kuu==1 or 2 or 12:
        season="Talv"
    elif kuu==3 or 4 or 5:
        season="Kevad"
    elif kuu==6 or 7 or 8:
        season="Suvel"
    elif kuu==9 or 10 or 11:
        season="Sügis"
    else:
        print("Vale!")
    return season

#4.2
def seasonInput()->str:
    """
    """
    kuu=int(input("Sisesta kuu number: "))
    while True:
        if kuu in range (1,13):
            break
        else:
            kuu=int(input("Sisesta kuu number: "))
    return season(kuu)

#5
def bank(aeur:float, years:int)->float:
    """
    """
    for i in range(years):
        aeur=aeur * 1.10
    return aeur

#6.1 - Простые числа Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
def is_prime(arv:int)->bool:
    """ Primaarvud
    Tagastab True, kui see on lihtne ja False, kui 
    """
    if 0<=arv<1001:
        if arv in [0,1]:
            pass
        else:
            for i in range(2,arv):
                if arv%i==0:
                    return False
                else:
                    return True

#7 - Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.
def date(day:int, mounth:int, year:int)->bool:
    """
    """
    if year<1 or mounth<1 or day<1:
        return False
    kalender=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mounth%4==0:
        kalender[1]=29
    return day<=kalender[mounth-1]

#8
def XOR_uncipher(cipher_string, key)->any:
    cipher_bytes = cipher_string.encode()
    key_bytes = key.encode()
    decoded_bytes = []
    for i in range(len(cipher_bytes)):
        decoded_byte = cipher_bytes[i] ^ key_bytes[i % len(key_bytes)]
        decoded_bytes.append(decoded_byte)
    return bytes(decoded_bytes).decode(errors='ignore')

# Преобразуем зашифрованную строку в список байтов 
# Получаем байт ключа
# Создаем список для восстановленных символов
# Применяем операцию XOR для каждого байта зашифрованной строки с соответствующим байтом ключа
# Используем циклический ключ
# Преобразуем восстановленные байты обратно в строку и возвращаем ее