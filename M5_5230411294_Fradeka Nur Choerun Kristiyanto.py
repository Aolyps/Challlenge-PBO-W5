class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre


class Jsong:
    def __init__(self):
        self.jsong = []
        self.jsong.sort()
    
    def add_jsong(self, judul, penyanyi, genre):
        jsong = next((jsong for jsong in self.jsong if jsong.judul == judul), None)
        if jsong is None:
            new_jsong = Music(judul, penyanyi, genre)
            self.jsong.append(new_jsong)
        else:
            print(f"Lagu dengan judul '{judul}' sudah ada.")

    def cari_jsong(self, penyanyi):
        result = [jsong for jsong in self.jsong if jsong.penyanyi == penyanyi]
        if result:
            for jsong in result:
                print(f"Judul: {jsong.judul}, Penyanyi: {jsong.penyanyi}, Genre: {jsong.genre}")
        else:
            print("Penyanyi tidak ditemukan.")

    def tampilkan_jsong(self):
        if not self.jsong:
            print("Tidak ada lagu yang tersimpan.")
        else:
            sorted_jsong = sorted(self.jsong, key=lambda x: x.judul)
            for j in sorted_jsong:
                print(f"Judul: {j.judul}, Penyanyi: {j.penyanyi}, Genre: {j.genre}")

    
    def remove_jsong(self, judul):
        song = next((jsong for jsong in self.jsong if jsong.judul == judul), None)
        if song:
            self.jsong.remove(song)
            print(f"Lagu '{judul}' berhasil dihapus.")
        else:
            print(f"Lagu dengan judul '{judul}' tidak ditemukan.")

jsong1 = Jsong()
jsong1.add_jsong("Bunny Girl", "AKASAKI", "J-Pop")
jsong1.add_jsong("Odoriko", "Vaundy", "J-Rock")
jsong1.add_jsong("Shinunoga E-Wa", "Fuji Kaze", "Pop")
jsong1.add_jsong("Tabun", "Yoasubi", "J-Pop")
jsong1.add_jsong("Kokoro no Tomo", "Mayumi Itsuwa", "Pop")

class Ksong:
    def __init__(self):
        self.ksong = []
        self.ksong.sort()
    
    def add_ksong(self, judul, penyanyi, genre):
        ksong = next((ksong for ksong in self.ksong if ksong.judul == judul), None)
        if ksong is None:
            new_ksong = Music(judul, penyanyi, genre)
            self.ksong.append(new_ksong)
        else:
            print(f"Lagu dengan judul '{judul}' sudah ada.")

    def cari_ksong(self, penyanyi):
        result = [ksong for ksong in self.ksong if ksong.penyanyi == penyanyi]
        if result:
            for ksong in result:
                print(f"Judul: {ksong.judul}, Penyanyi: {ksong.penyanyi}, Genre: {ksong.genre}")
        else:
            print("Penyanyi tidak ditemukan.")

    def tampilkan_ksong(self):
        if not self.ksong:
            print("Tidak ada lagu yang tersimpan.")
        else:
            sorted_ksong = sorted(self.ksong, key=lambda x: x.judul)
            for j in sorted_ksong:
                print(f"Judul: {j.judul}, Penyanyi: {j.penyanyi}, Genre: {j.genre}")

    
    def remove_ksong(self, judul):
        song = next((ksong for ksong in self.ksong if ksong.judul == judul), None)
        if song:
            self.ksong.remove(song)
            print(f"Lagu '{judul}' berhasil dihapus.")
        else:
            print(f"Lagu dengan judul '{judul}' tidak ditemukan.")

ksong1 = Ksong()
ksong1.add_ksong("UP", "KARINA AESPA", "Pop")
ksong1.add_ksong("Magnetic", "ILIT", "K-Pop")
ksong1.add_ksong("Armageddon", "AESPA", "K-Rock")
ksong1.add_ksong("QueenCard", "(G)I-dle", "K-Pop")
ksong1.add_ksong("Flower", "Kim Ji-soo", "Pop & Trap")

class Jawa:
    def __init__(self):
        self.jawa = [] 
        self.jawa.sort()
    
    def add_jawa(self, judul, penyanyi, genre):
        jawa = next((jawa for jawa in self.jawa if jawa.judul == judul), None)
        if jawa is None:
            new_jawa = Music(judul, penyanyi, genre)
            self.jawa.append(new_jawa)
        else:
            print(f"Lagu dengan judul '{judul}' sudah ada.")

    def tampilkan_jawa(self):
        if not self.jawa:
            print("Tidak ada lagu yang tersimpan.")
        else:
            sorted_jawa = sorted(self.jawa, key=lambda x: x.judul)
            for j in sorted_jawa:
                print(f"Judul: {j.judul}, Penyanyi: {j.penyanyi}, Genre: {j.genre}")

    def cari_jawa(self, penyanyi):
        result = [jawa for jawa in self.jawa if jawa.penyanyi == penyanyi]
        if result:
            for jawa in result:
                print(f"Judul: {jawa.judul}, Penyanyi: {jawa.penyanyi}, Genre: {jawa.genre}")
        else:
            print("Penyanyi tidak ditemukan.")

    def remove_jawa(self, judul):
        song = next((jawa for jawa in self.jawa if jawa.judul == judul), None)
        if song:
            self.jawa.remove(song)
            print(f"Lagu '{judul}' berhasil dihapus.")
        else:
            print(f"Lagu dengan judul '{judul}' tidak ditemukan.")
    
jawir = Jawa()
jawir.add_jawa("Kisinan 2", "Didik Budi", "Dangdut")
jawir.add_jawa("Lamunan", "Happy Asmara", "Dangdut")
jawir.add_jawa("Wirang", "Guyon Waton", "Dangdut")
jawir.add_jawa("LDR", "Denny Caknan", "Dangdut")
jawir.add_jawa("Sekti", "Denny Caknan", "Dangdut")

def main() :
    while True:
        print("\n============ Music Taste ============")
        print("1. Music Japan")
        print("2. Music Korean")
        print("3. Music Java")
        print("0. Out")

        menu = int(input("Masukkan pilihan anda: "))

        if menu == 1:
            while True:
                print("\n============ Sub Menu ============")
                print("Tampilan Lagu J-songs saat ini : ")
                jsong1.tampilkan_jsong()
                print("\n1. Tambah Music Japan")
                print("2. Cari Music Japan")
                print("3. Hapus Music ")
                print("0. Keluar")
                men = int(input("Masukkan pilihan anda: "))
                if men == 1:
                    judul = input("Masukkan Judul lagu : ")
                    penyanyi = input("Masukkan nama penyanyi : ")
                    genre = (input("Masukkan genre lagu : "))
                    jsong1.add_jsong(judul, penyanyi, genre)
                    print(f"Lagu {judul} berhasil ditambahkan.")
                elif men == 2:
                    penyanyi = input("Masukkan penyanyi yang dicari: ")
                    jsong1.cari_jsong(penyanyi)
                elif men == 3:
                    judul = input("Masukkan Judul lagu yang akan dihapus : ")
                    jsong1.remove_jsong(judul)
                else:
                    break
        
        elif menu == 2:
            while True:
                print("\n============ Sub Menu ============")
                print("Tampilan Lagu K-songs saat ini : ")
                ksong1.tampilkan_ksong()
                print("\n1. Tambah Music Korean")
                print("2. Cari Music Korean")
                print("3. Hapus Music ")
                print("0. Keluar")
                men = int(input("Masukkan pilihan anda: "))
                if men == 1:
                    judul = input("Masukkan Judul lagu : ")
                    penyanyi = input("Masukkan nama penyanyi : ")
                    genre = (input("Masukkan genre lagu : "))
                    ksong1.add_ksong(judul, penyanyi, genre)
                    print(f"Lagu {judul} berhasil ditambahkan.")
                elif men == 2:
                    penyanyi = input("Masukkan penyanyi yang dicari: ")
                    ksong1.cari_ksong(penyanyi)
                elif men == 3:
                    judul = input("Masukkan Judul lagu yang akan dihapus : ")
                    ksong1.remove_ksong(judul)
                else:
                    break

        elif menu == 3:
            while True:
                print("\n============ Sub Menu ============")
                print("Tampilan Lagu Java saat ini : ")
                jawir.tampilkan_jawa()
                print("\n1. Tambah Music Java")
                print("2. Cari Music Java")
                print("3. Hapus Music ")
                print("0. Keluar")
                men = int(input("Masukkan pilihan anda: "))
                if men == 1:
                    judul = input("Masukkan Judul lagu : ")
                    penyanyi = input("Masukkan nama penyanyi : ")
                    genre = (input("Masukkan genre lagu : "))
                    jawir.add_jawa(judul, penyanyi, genre)
                    print(f"Lagu {judul} berhasil ditambahkan.")
                elif men == 2:
                    penyanyi = input("Masukkan penyanyi yang dicari: ")
                    jawir.cari_jawa(penyanyi)
                elif men == 3:
                    judul = input("Masukkan Judul lagu yang akan dihapus : ")
                    jawir.remove_jawa(judul)
                else:
                    break
        elif menu == 0:
            print("Program akan keluar.")
            break
        else:
            print("Menu tidak valid.")

if __name__ == "__main__" :
    main()