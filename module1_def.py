def arithmetic(arv1:float,arv2:float,tehe:str)->any:
    """Lihtne kalkulaator 
    + - liitmine
    - - lahutamine
    * - korrutamine 
    / - jagamine
    :param float arv1: Sisend kasutajalt, mingi ujukomaarv
    :param float arv2: Sisend kasutajalt, mingi ujukomaarv
    :param str tehe: aritmeetiline, tehe, mis valib kasutaja
    :rtype: var M��rata t��p(float v�i str)
    """
    if tehe in ["+","-","*","/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="tundmatu te�he"
    return vastus

def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab t�ev��rtsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v

def square(k�lg:float)->any:
    """Ruudu pindala ja �mberm��t leidmine
    :param float k�lg: Ruudu k�lg
    :rtype: float tagastab ruudu pindala
    """
    S=k�lg**2
    P=k�lg*4
    d=(2)**(1/2)*k�lg
    return S,P,d

def square(k�lg:float)->any:
    """Ruudu pindala ja �mberm��t leidmine
    :param float k�lg: Ruudu k�lg
    :rtype: float tagastab ruudu pindala
    """
    S=k�lg**2
    P=k�lg*4
    d=(2)**(1/2)*k�lg
    s_list=[S,P,d]
    return s_list