from local import *
import datetime
import pylab
import matplotlib.pyplot as plt
from numpy import pi

print(HELLO)


# Menu function -----------------------------------------------------
def menu():
    '''Lets user choose what program will do for him'''
    try:
        choice = int(input(MENU))
        return choice

    except ValueError:
        print(ERROR)


# -------------------------------------------------------------------

# Help functions ----------------------------------------------------
# Dictionaries and lists function -----------------------------------
def dictlist(fname):
    '''Creates a tuple'''
    f = open(fname, 'r')
    s = f.readlines()
    f.close()
    CURRENCY = {}
    KEY = []
    KEYS = []

    for j in s:
        j = j.replace('\t', ' ')
        j = j.replace('\n', '')
        j = j.replace(',', '.')
        t = j.split()
        CURRENCY[t[0]] = t[1]

    for i in s:
        key = i[0:10]
        KEY.append(datetime.datetime.date(
            datetime.datetime.strptime(key, '%d.%m.%Y')))
        KEYS.append(key)

    return (CURRENCY, KEY, KEYS)


# Example 1 ---------------------------------------------------------
def ex1(USD, USDkey, USDkeys):
    '''Draws graphics for USD exchange rate dynamics'''
    x = (USDkey)
    y1 = []

    for i in USDkeys:
        y1.append(float(USD[i]))

    y = (y1)
    plt.plot(x, y)
    plt.show()


# Example 2 ---------------------------------------------------------
def ex2(USD, USDkey, USDkeys, EUR, EURkey, EURkeys,
        CHF, CHFkey, CHFkeys, GBP, GBPkey, GBPkeys):
    '''Draws graphics for USD, EUR, CHF, GBP exchange rates dynamics'''
    xusd = (USDkey)
    y1usd = []

    for i in USDkeys:
        y1usd.append(float(USD[i]))

    yusd = (y1usd)

    plt.plot(xusd, yusd)
    xeur = (EURkey)
    y1eur = []

    for i in EURkeys:
        y1eur.append(float(EUR[i]))

    yeur = (y1eur)
    plt.plot(xeur, yeur)
    xchf = (CHFkey)
    y1chf = []

    for i in CHFkeys:
        y1chf.append(float(CHF[i]))

    ychf = (y1chf)
    plt.plot(xchf, ychf)
    xgbp = (GBPkey)
    y1gbp = []

    for i in GBPkeys:
        y1gbp.append(float(GBP[i]))

    ygbp = (y1gbp)
    plt.plot(xgbp, ygbp)
    plt.show()


# Example 3 ---------------------------------------------------------
def ex3(USD, USDkey, USDkeys, EUR, EURkey, EURkeys,
        CHF, CHFkey, CHFkeys, GBP, GBPkey, GBPkeys):
    '''Draws graphics for USD, EUR, CHF, GBP exchange rates dynamics'''
    xusd = (USDkey)
    y1usd = []

    for i in USDkeys:
        y1usd.append(float(USD[i]))

    yusd = (y1usd)
    plt.plot(xusd, yusd)
    xeur = (EURkey)
    y1eur = []

    for i in EURkeys:
        y1eur.append(float(EUR[i]))

    yeur = (y1eur)
    plt.plot(xeur, yeur)
    xchf = (CHFkey)
    y1chf = []

    for i in CHFkeys:
        y1chf.append(float(CHF[i]))

    ychf = (y1chf)
    plt.plot(xchf, ychf)
    xgbp = (GBPkey)
    y1gbp = []

    for i in GBPkeys:
        y1gbp.append(float(GBP[i]))

    ygbp = (y1gbp)
    plt.plot(xgbp, ygbp)
    plt.title('USD, EUR, CHF, GBP')
    plt.xlabel('Period')
    plt.ylabel('Cost')
    plt.grid(True)
    plt.show()


# Example 8 ---------------------------------------------------------
def ex8(USD, USDkey, USDkeys, EUR, EURkey, EURkeys,
        CHF, CHFkey, CHFkeys, GBP, GBPkey, GBPkeys):
    '''Draws graphics for USD, EUR, CHF, GBP exchange rates dynamics'''
    xusd = (USDkey)
    y1usd = []

    for i in USDkeys:
        y1usd.append(float(USD[i]))

    yusd = (y1usd)
    plt.plot(xusd, yusd)
    xeur = (EURkey)
    y1eur = []

    for i in EURkeys:
        y1eur.append(float(EUR[i]))

    yeur = (y1eur)
    plt.plot(xeur, yeur)
    xchf = (CHFkey)
    y1chf = []

    for i in CHFkeys:
        y1chf.append(float(CHF[i]))

    ychf = (y1chf)
    plt.plot(xchf, ychf)
    xgbp = (GBPkey)
    y1gbp = []

    for i in GBPkeys:
        y1gbp.append(float(GBP[i]))

    ygbp = (y1gbp)
    plt.plot(xgbp, ygbp)
    plt.legend(('USD', 'EUR', 'CHF', 'GBP'))
    plt.title('USD, EUR, CHF, GBP')
    plt.xlabel('Period')
    plt.ylabel('Cost')
    plt.grid(True)
    plt.show()


# Example 4 ---------------------------------------------------------
def ex4(USD, USDkey, USDkeys, EUR, EURkey, EURkeys,
        CHF, CHFkey, CHFkeys, GBP, GBPkey, GBPkeys):
    '''Draws graphics for USD, EUR, CHF, GBP exchange rates dynamics'''
    xusd = (USDkey)
    y1usd = []

    for i in USDkeys:
        y1usd.append(float(USD[i]))

    yusd = (y1usd)
    plt.subplot(2, 2, 1)
    plt.plot(xusd, yusd)
    plt.title('USD')
    plt.xlabel('Period')
    plt.ylabel('Cost')
    plt.grid(True)
    xeur = (EURkey)
    y1eur = []

    for i in EURkeys:
        y1eur.append(float(EUR[i]))

    yeur = (y1eur)
    plt.subplot(2, 2, 2)
    plt.plot(xeur, yeur)
    plt.title('EUR')
    plt.xlabel('Period')
    plt.ylabel('Cost')
    plt.grid(True)
    xchf = (CHFkey)
    y1chf = []

    for i in CHFkeys:
        y1chf.append(float(CHF[i]))

    ychf = (y1chf)
    plt.subplot(2, 2, 3)
    plt.plot(xchf, ychf)
    plt.title('CHF')
    plt.xlabel('Period')
    plt.ylabel('Cost')
    plt.grid(True)
    xgbp = (GBPkey)
    y1gbp = []

    for i in GBPkeys:
        y1gbp.append(float(GBP[i]))

    ygbp = (y1gbp)
    plt.subplot(2, 2, 4)
    plt.plot(xgbp, ygbp)
    plt.title('GBP')
    plt.xlabel('Period')
    plt.ylabel('Cost')
    plt.grid(True)
    plt.show()


# Example 5 ---------------------------------------------------------
def ex5(USD, USDkey, USDkeys, EUR, EURkey, EURkeys,
        CHF, CHFkey, CHFkeys, GBP, GBPkey, GBPkeys):
    '''Draws graphics for USD, EUR, CHF, GBP exchange rates dynamics'''
    spisokUSD1 = []
    spisokUSD2 = []
    spisokUSD3 = []
    spisokUSD4 = []
    spisokUSD5 = []
    spisokUSD6 = []
    spisokUSD7 = []
    spisokUSD8 = []
    spisokUSD9 = []
    spisokUSD10 = []
    spisokUSD11 = []
    spisokUSD12 = []
    sredUSD = []

    for i in range(16):
        spisokUSD1.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD1) / len(spisokUSD1))
    for i in range(18):
        spisokUSD2.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD2) / len(spisokUSD2))
    for i in range(22):
        spisokUSD3.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD3) / len(spisokUSD3))
    for i in range(21):
        spisokUSD4.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD4) / len(spisokUSD4))
    for i in range(19):
        spisokUSD5.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD5) / len(spisokUSD5))
    for i in range(21):
        spisokUSD6.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD6) / len(spisokUSD6))
    for i in range(21):
        spisokUSD7.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD7) / len(spisokUSD7))
    for i in range(23):
        spisokUSD8.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD8) / len(spisokUSD8))
    for i in range(22):
        spisokUSD9.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD9) / len(spisokUSD9))
    for i in range(21):
        spisokUSD10.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD10) / len(spisokUSD10))
    for i in range(21):
        spisokUSD11.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD11) / len(spisokUSD11))
    for i in range(22):
        spisokUSD12.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD12) / len(spisokUSD12))

    spisokEUR1 = []
    spisokEUR2 = []
    spisokEUR3 = []
    spisokEUR4 = []
    spisokEUR5 = []
    spisokEUR6 = []
    spisokEUR7 = []
    spisokEUR8 = []
    spisokEUR9 = []
    spisokEUR10 = []
    spisokEUR11 = []
    spisokEUR12 = []
    sredEUR = []

    for i in range(16):
        spisokEUR1.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR1) / len(spisokEUR1))
    for i in range(18):
        spisokEUR2.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR2) / len(spisokEUR2))
    for i in range(22):
        spisokEUR3.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR3) / len(spisokEUR3))
    for i in range(21):
        spisokEUR4.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR4) / len(spisokEUR4))
    for i in range(19):
        spisokEUR5.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR5) / len(spisokEUR5))
    for i in range(21):
        spisokEUR6.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR6) / len(spisokEUR6))
    for i in range(21):
        spisokEUR7.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR7) / len(spisokEUR7))
    for i in range(23):
        spisokEUR8.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR8) / len(spisokEUR8))
    for i in range(22):
        spisokEUR9.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR9) / len(spisokEUR9))
    for i in range(21):
        spisokEUR10.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR10) / len(spisokEUR10))
    for i in range(21):
        spisokEUR11.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR11) / len(spisokEUR11))
    for i in range(22):
        spisokEUR12.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR12) / len(spisokEUR12))

    spisokCHF1 = []
    spisokCHF2 = []
    spisokCHF3 = []
    spisokCHF4 = []
    spisokCHF5 = []
    spisokCHF6 = []
    spisokCHF7 = []
    spisokCHF8 = []
    spisokCHF9 = []
    spisokCHF10 = []
    spisokCHF11 = []
    spisokCHF12 = []
    sredCHF = []

    for i in range(16):
        spisokCHF1.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF1) / len(spisokCHF1))
    for i in range(18):
        spisokCHF2.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF2) / len(spisokCHF2))
    for i in range(22):
        spisokCHF3.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF3) / len(spisokCHF3))
    for i in range(21):
        spisokCHF4.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF4) / len(spisokCHF4))
    for i in range(19):
        spisokCHF5.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF5) / len(spisokCHF5))
    for i in range(21):
        spisokCHF6.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF6) / len(spisokCHF6))
    for i in range(21):
        spisokCHF7.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF7) / len(spisokCHF7))
    for i in range(23):
        spisokCHF8.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF8) / len(spisokCHF8))
    for i in range(22):
        spisokCHF9.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF9) / len(spisokCHF9))
    for i in range(21):
        spisokCHF10.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF10) / len(spisokCHF10))
    for i in range(21):
        spisokCHF11.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF11) / len(spisokCHF11))
    for i in range(22):
        spisokCHF12.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF12) / len(spisokCHF12))

    spisokGBP1 = []
    spisokGBP2 = []
    spisokGBP3 = []
    spisokGBP4 = []
    spisokGBP5 = []
    spisokGBP6 = []
    spisokGBP7 = []
    spisokGBP8 = []
    spisokGBP9 = []
    spisokGBP10 = []
    spisokGBP11 = []
    spisokGBP12 = []
    sredGBP = []

    for i in range(16):
        spisokGBP1.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP1) / len(spisokGBP1))
    for i in range(18):
        spisokGBP2.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP2) / len(spisokGBP2))
    for i in range(22):
        spisokGBP3.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP3) / len(spisokGBP3))
    for i in range(21):
        spisokGBP4.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP4) / len(spisokGBP4))
    for i in range(19):
        spisokGBP5.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP5) / len(spisokGBP5))
    for i in range(21):
        spisokGBP6.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP6) / len(spisokGBP6))
    for i in range(21):
        spisokGBP7.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP7) / len(spisokGBP7))
    for i in range(23):
        spisokGBP8.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP8) / len(spisokGBP8))
    for i in range(22):
        spisokGBP9.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP9) / len(spisokGBP9))
    for i in range(21):
        spisokGBP10.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP10) / len(spisokGBP10))
    for i in range(21):
        spisokGBP11.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP11) / len(spisokGBP11))
    for i in range(22):
        spisokGBP12.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP12) / len(spisokGBP12))

    xusd = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    USDy = []

    for i in sredUSD:
        USDy.append(i * pi)

    yusd = (USDy)
    plt.subplot(221, projection='polar')
    plt.title('USD')
    plt.plot(yusd, xusd)
    xeur = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    EURy = []

    for i in sredEUR:
        EURy.append(i * pi)

    yeur = (EURy)
    plt.subplot(222, projection='polar')
    plt.title('EUR')
    plt.plot(yeur, xeur)
    xchf = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    CHFy = []

    for i in sredCHF:
        CHFy.append(i * pi)

    ychf = (CHFy)
    plt.subplot(223, projection='polar')
    plt.title('CHF')
    plt.plot(ychf, xchf)
    xgbp = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    GBPy = []

    for i in sredGBP:
        GBPy.append(i * pi)

    ygbp = (GBPy)
    plt.subplot(224, projection='polar')
    plt.title('GBP')
    plt.plot(ygbp, xgbp)
    plt.show()


# Example 6 ---------------------------------------------------------
def ex6(USD, USDkey, USDkeys, EUR, EURkey, EURkeys,
        CHF, CHFkey, CHFkeys, GBP, GBPkey, GBPkeys):
    '''Draws graphics for USD, EUR, CHF, GBP exchange rates dynamics'''
    spisokUSD1 = []
    spisokUSD2 = []
    spisokUSD3 = []
    spisokUSD4 = []
    spisokUSD5 = []
    spisokUSD6 = []
    spisokUSD7 = []
    spisokUSD8 = []
    spisokUSD9 = []
    spisokUSD10 = []
    spisokUSD11 = []
    spisokUSD12 = []
    sredUSD = []

    for i in range(16):
        spisokUSD1.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD1) / len(spisokUSD1))
    for i in range(18):
        spisokUSD2.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD2) / len(spisokUSD2))
    for i in range(22):
        spisokUSD3.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD3) / len(spisokUSD3))
    for i in range(21):
        spisokUSD4.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD4) / len(spisokUSD4))
    for i in range(19):
        spisokUSD5.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD5) / len(spisokUSD5))
    for i in range(21):
        spisokUSD6.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD6) / len(spisokUSD6))
    for i in range(21):
        spisokUSD7.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD7) / len(spisokUSD7))
    for i in range(23):
        spisokUSD8.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD8) / len(spisokUSD8))
    for i in range(22):
        spisokUSD9.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD9) / len(spisokUSD9))
    for i in range(21):
        spisokUSD10.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD10) / len(spisokUSD10))
    for i in range(21):
        spisokUSD11.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD11) / len(spisokUSD11))
    for i in range(22):
        spisokUSD12.append(float(USD[USDkeys[i]]))
    sredUSD.append(sum(spisokUSD12) / len(spisokUSD12))

    spisokEUR1 = []
    spisokEUR2 = []
    spisokEUR3 = []
    spisokEUR4 = []
    spisokEUR5 = []
    spisokEUR6 = []
    spisokEUR7 = []
    spisokEUR8 = []
    spisokEUR9 = []
    spisokEUR10 = []
    spisokEUR11 = []
    spisokEUR12 = []
    sredEUR = []

    for i in range(16):
        spisokEUR1.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR1) / len(spisokEUR1))
    for i in range(18):
        spisokEUR2.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR2) / len(spisokEUR2))
    for i in range(22):
        spisokEUR3.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR3) / len(spisokEUR3))
    for i in range(21):
        spisokEUR4.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR4) / len(spisokEUR4))
    for i in range(19):
        spisokEUR5.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR5) / len(spisokEUR5))
    for i in range(21):
        spisokEUR6.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR6) / len(spisokEUR6))
    for i in range(21):
        spisokEUR7.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR7) / len(spisokEUR7))
    for i in range(23):
        spisokEUR8.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR8) / len(spisokEUR8))
    for i in range(22):
        spisokEUR9.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR9) / len(spisokEUR9))
    for i in range(21):
        spisokEUR10.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR10) / len(spisokEUR10))
    for i in range(21):
        spisokEUR11.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR11) / len(spisokEUR11))
    for i in range(22):
        spisokEUR12.append(float(EUR[EURkeys[i]]))
    sredEUR.append(sum(spisokEUR12) / len(spisokEUR12))

    spisokCHF1 = []
    spisokCHF2 = []
    spisokCHF3 = []
    spisokCHF4 = []
    spisokCHF5 = []
    spisokCHF6 = []
    spisokCHF7 = []
    spisokCHF8 = []
    spisokCHF9 = []
    spisokCHF10 = []
    spisokCHF11 = []
    spisokCHF12 = []
    sredCHF = []

    for i in range(16):
        spisokCHF1.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF1) / len(spisokCHF1))
    for i in range(18):
        spisokCHF2.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF2) / len(spisokCHF2))
    for i in range(22):
        spisokCHF3.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF3) / len(spisokCHF3))
    for i in range(21):
        spisokCHF4.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF4) / len(spisokCHF4))
    for i in range(19):
        spisokCHF5.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF5) / len(spisokCHF5))
    for i in range(21):
        spisokCHF6.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF6) / len(spisokCHF6))
    for i in range(21):
        spisokCHF7.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF7) / len(spisokCHF7))
    for i in range(23):
        spisokCHF8.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF8) / len(spisokCHF8))
    for i in range(22):
        spisokCHF9.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF9) / len(spisokCHF9))
    for i in range(21):
        spisokCHF10.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF10) / len(spisokCHF10))
    for i in range(21):
        spisokCHF11.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF11) / len(spisokCHF11))
    for i in range(22):
        spisokCHF12.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF12) / len(spisokCHF12))

    spisokGBP1 = []
    spisokGBP2 = []
    spisokGBP3 = []
    spisokGBP4 = []
    spisokGBP5 = []
    spisokGBP6 = []
    spisokGBP7 = []
    spisokGBP8 = []
    spisokGBP9 = []
    spisokGBP10 = []
    spisokGBP11 = []
    spisokGBP12 = []
    sredGBP = []

    for i in range(16):
        spisokGBP1.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP1) / len(spisokGBP1))
    for i in range(18):
        spisokGBP2.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP2) / len(spisokGBP2))
    for i in range(22):
        spisokGBP3.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP3) / len(spisokGBP3))
    for i in range(21):
        spisokGBP4.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP4) / len(spisokGBP4))
    for i in range(19):
        spisokGBP5.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP5) / len(spisokGBP5))
    for i in range(21):
        spisokGBP6.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP6) / len(spisokGBP6))
    for i in range(21):
        spisokGBP7.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP7) / len(spisokGBP7))
    for i in range(23):
        spisokGBP8.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP8) / len(spisokGBP8))
    for i in range(22):
        spisokGBP9.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP9) / len(spisokGBP9))
    for i in range(21):
        spisokGBP10.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP10) / len(spisokGBP10))
    for i in range(21):
        spisokGBP11.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP11) / len(spisokGBP11))
    for i in range(22):
        spisokGBP12.append(float(GBP[GBPkeys[i]]))
    sredGBP.append(sum(spisokGBP12) / len(spisokGBP12))

    r = 1
    xusd = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    yusd = (sredUSD)
    plt.subplot(221)
    plt.title('USD')
    plt.plot(r * xusd, r * yusd)

    xeur = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    yeur = (sredEUR)
    plt.subplot(222)
    plt.title('EUR')
    plt.plot(r * xeur, r * yeur)

    xchf = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    ychf = (sredCHF)
    plt.subplot(223)
    plt.title('CHF')
    plt.plot(r * xchf, r * ychf)

    xgbp = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    ygbp = (sredGBP)
    plt.subplot(224)
    plt.title('GBP')
    plt.plot(r * xgbp, r * ygbp)
    plt.show()


# Example 9 ---------------------------------------------------------
def ex9(USD, USDkey, USDkeys, EUR, EURkey, EURkeys,
        CHF, CHFkey, CHFkeys, GBP, GBPkey, GBPkeys):
    '''Draws graphics for USD, EUR, CHF, GBP exchange rates dynamics'''
    xusd = (USDkey)
    y1usd = []

    for i in USDkeys:
        y1usd.append(float(USD[i]))

    yusd = (y1usd)
    plt.plot(xusd, yusd, 'r--')
    xeur = (EURkey)
    y1eur = []

    for i in EURkeys:
        y1eur.append(float(EUR[i]))

    yeur = (y1eur)
    plt.plot(xeur, yeur, 'g^')
    xchf = (CHFkey)
    y1chf = []

    for i in CHFkeys:
        y1chf.append(float(CHF[i]))

    ychf = (y1chf)
    plt.plot(xchf, ychf, 'bs')
    xgbp = (GBPkey)
    y1gbp = []

    for i in GBPkeys:
        y1gbp.append(float(GBP[i]))

    ygbp = (y1gbp)
    plt.plot(xgbp, ygbp, 'y*')
    plt.grid(True)
    plt.show()


# Example 10 --------------------------------------------------------
def ex10(USD, USDkey, USDkeys):
    '''Draws graphics for USD exchange rates dynamics'''
    y1 = []
    x1 = []
    pylab.ion()
    pylab.draw()
    n = 0

    for i in USDkeys:
        x1.append(USDkey[n])
        y1.append(float(USD[i]))
        x = (x1)
        y = (y1)
        pylab.plot(x, y, 'b')
        pylab.draw()
        pylab.pause(0.01)
        pylab.title('USD')
        n += 1

    pylab.close()


# Example 11 --------------------------------------------------------
def ex11(CHF, CHFkey, CHFkeys):
    '''Draws graphics for USD, EUR, CHF, GBP exchange rates dynamics'''
    spisokCHF1 = []
    spisokCHF2 = []
    spisokCHF3 = []
    spisokCHF4 = []
    spisokCHF5 = []
    spisokCHF6 = []
    spisokCHF7 = []
    spisokCHF8 = []
    spisokCHF9 = []
    spisokCHF10 = []
    spisokCHF11 = []
    spisokCHF12 = []
    sredCHF = []

    for i in range(16):
        spisokCHF1.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF1) / len(spisokCHF1))
    for i in range(18):
        spisokCHF2.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF2) / len(spisokCHF2))
    for i in range(22):
        spisokCHF3.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF3) / len(spisokCHF3))
    for i in range(21):
        spisokCHF4.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF4) / len(spisokCHF4))
    for i in range(19):
        spisokCHF5.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF5) / len(spisokCHF5))
    for i in range(21):
        spisokCHF6.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF6) / len(spisokCHF6))
    for i in range(21):
        spisokCHF7.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF7) / len(spisokCHF7))
    for i in range(23):
        spisokCHF8.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF8) / len(spisokCHF8))
    for i in range(22):
        spisokCHF9.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF9) / len(spisokCHF9))
    for i in range(21):
        spisokCHF10.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF10) / len(spisokCHF10))
    for i in range(21):
        spisokCHF11.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF11) / len(spisokCHF11))
    for i in range(22):
        spisokCHF12.append(float(CHF[CHFkeys[i]]))
    sredCHF.append(sum(spisokCHF12) / len(spisokCHF12))

    xchf = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ychf = (sredCHF)
    plt.title('CHF')
    plt.bar(xchf, ychf)
    plt.show()


# Example 7 ---------------------------------------------------------
def ex7(USD, EUR):
    '''Creates a surface that has nth to do with IT-company'''
    from mpl_toolkits.mplot3d import axes3d
    import numpy as np

    ax = axes3d.Axes3D(plt.figure())
    X, Y = np.meshgrid(np.array([float(USD[key]) for key in USD]),
                       np.array([float(EUR[key]) for key in EUR]))
    Z = (Y - X) / Y
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    plt.title('Relative EUR/USD')
    plt.xlabel('USD')
    plt.ylabel('EUR')
    plt.show()


# Example 12 --------------------------------------------------------
def ex12():
    '''Draws graphics for USD, EUR exchange rates dynamics'''
    x = [1036.4, 1500, 154764.6]
    y = ['USD', 'EUR', 'OTHER']
    plt.pie(x, labels=y)
    plt.show()


# Example 13 --------------------------------------------------------
def ex13(USD, EUR):
    '''Creates a colored surface that has nth to do with IT-company'''
    from mpl_toolkits.mplot3d import axes3d
    from matplotlib.colors import LinearSegmentedColormap
    from matplotlib import cm
    import numpy as np

    ax = axes3d.Axes3D(pylab.figure())
    X, Y = np.meshgrid(np.array([float(USD[key]) for key in USD]),
                       np.array([float(EUR[key]) for key in EUR]))
    Z = (Y - X) / Y
    ax.plot_surface(X, Y, Z, rstride=10, cstride=10, cmap=cm.jet)
    pylab.title('Relative EUR/USD')
    pylab.xlabel('USD')
    pylab.ylabel('EUR')
    pylab.show()


# -------------------------------------------------------------------
# End of help functions ---------------------------------------------

# Main function -----------------------------------------------------
def main():
    '''Main function'''
    while True:
        choice = menu()

        if choice == 0:
            break

        elif choice == 1:
            ex1(fUSD[0], fUSD[1], fUSD[2])

        elif choice == 2:
            ex2(fUSD[0], fUSD[1], fUSD[2], fEUR[0], fEUR[1], fEUR[2],
                fCHF[0], fCHF[1], fCHF[2], fGBP[0], fGBP[1], fGBP[2])

        elif choice == 3:
            ex3(fUSD[0], fUSD[1], fUSD[2], fEUR[0], fEUR[1], fEUR[2],
                fCHF[0], fCHF[1], fCHF[2], fGBP[0], fGBP[1], fGBP[2])

        elif choice == 4:
            ex4(fUSD[0], fUSD[1], fUSD[2], fEUR[0], fEUR[1], fEUR[2],
                fCHF[0], fCHF[1], fCHF[2], fGBP[0], fGBP[1], fGBP[2])

        elif choice == 5:
            ex5(fUSD[0], fUSD[1], fUSD[2], fEUR[0], fEUR[1], fEUR[2],
                fCHF[0], fCHF[1], fCHF[2], fGBP[0], fGBP[1], fGBP[2])

        elif choice == 6:
            ex6(fUSD[0], fUSD[1], fUSD[2], fEUR[0], fEUR[1], fEUR[2],
                fCHF[0], fCHF[1], fCHF[2], fGBP[0], fGBP[1], fGBP[2])

        elif choice == 7:
            ex7(fUSD[0], fEUR[0])

        elif choice == 8:
            ex8(fUSD[0], fUSD[1], fUSD[2], fEUR[0], fEUR[1], fEUR[2],
                fCHF[0], fCHF[1], fCHF[2], fGBP[0], fGBP[1], fGBP[2])

        elif choice == 9:
            ex9(fUSD[0], fUSD[1], fUSD[2], fEUR[0], fEUR[1], fEUR[2],
                fCHF[0], fCHF[1], fCHF[2], fGBP[0], fGBP[1], fGBP[2])

        elif choice == 10:
            ex10(fUSD[0], fUSD[1], fUSD[2])

        elif choice == 11:
            ex11(fCHF[0], fCHF[1], fCHF[2])

        elif choice == 12:
            ex12()

        elif choice == 13:
            ex13(fUSD[0], fEUR[0])


# End of main function ----------------------------------------------

fUSD = dictlist('usd.txt')
fEUR = dictlist('eur.txt')
fGBP = dictlist('gbp.txt')
fCHF = dictlist('chf.txt')

if __name__ == '__main__':
    main()

# End of programm ---------------------------------------------------
