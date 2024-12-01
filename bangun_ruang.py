# bangun_ruang.py
import math

def volume_kubus(sisi):
    return sisi ** 3

def luas_permukaan_kubus(sisi):
    return 6 * (sisi ** 2)

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def volume_tabung(radius, tinggi):
    return math.pi * (radius ** 2) * tinggi

def luas_permukaan_tabung(radius, tinggi):
    return 2 * math.pi * radius * (radius + tinggi)
