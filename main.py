# main.py
import aritmatika
import bangun_datar
import bangun_ruang

def main():
    # Menggunakan modul aritmatika
    print("Operasi Aritmatika:")
    print(f"10 + 5 = {aritmatika.tambah(10, 5)}")
    print(f"10 - 5 = {aritmatika.kurang(10, 5)}")
    print(f"10 * 5 = {aritmatika.kali(10, 5)}")
    print(f"10 / 5 = {aritmatika.bagi(10, 5)}")

    # Menggunakan modul bangun datar
    print("\nBangun Datar:")
    print(f"Luas Persegi (sisi 4) = {bangun_datar.luas_persegi(4)}")
    print(f"Keliling Persegi (sisi 4) = {bangun_datar.keliling_persegi(4)}")
    print(f"Luas Lingkaran (radius 5) = {bangun_datar.luas_lingkaran(5)}")
    print(f"Keliling Lingkaran (radius 5) = {bangun_datar.keliling_lingkaran(5)}")

    # Menggunakan modul bangun ruang
    print("\nBangun Ruang:")
    print(f"Volume Kubus (sisi 3) = {bangun_ruang.volume_kubus(3)}")
    print(f"Luas Permukaan Kubus (sisi 3) = {bangun_ruang.luas_permukaan_kubus(3)}")
    print(f"Volume Balok (panjang 3, lebar 4, tinggi 5) = {bangun_ruang.volume_balok(3, 4, 5)}")
    print(f"Luas Permukaan Balok (panjang 3, lebar 4, tinggi 5) = {bangun_ruang.luas_permukaan_balok(3, 4, 5)}")
    print(f"Volume Tabung (radius 3, tinggi 7) = {bangun_ruang.volume_tabung(3, 7)}")
    print(f"Luas Permukaan Tabung (radius 3, tinggi 7) = {bangun_ruang.luas_permukaan_tabung(3, 7)}")

if __name__ == "__main__":
    main()
