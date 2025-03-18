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

def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab tõeväärtsuses formaadis tulemus
    """

