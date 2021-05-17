# nama file :paket.py
# mengimpor modul geometri2D
# yang berada di dalam paket matematika
import matematika.geometri2D

def main():
    """bujur sangkar"""
    sisi = 5
    luas = matematika.geometri2D.luasbujursangkar(5)
    print("BUJUR SANGKAR")
    print("panjang : ", sisi)
    print("luas: ", luas)

if __name__== "__main__":
    main()