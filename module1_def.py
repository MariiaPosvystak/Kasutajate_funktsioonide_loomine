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
    Tagastab True, kui see on lihtne´ja False, kui 
    """
    if 0<=arv<1001:
        if arv in [0,1]:
            pass
        else:
            for i in range(2,arv):
                if arv%i==0:
                    v=False
                else:
                    v=True
    return v
#7