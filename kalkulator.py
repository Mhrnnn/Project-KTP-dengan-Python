    
def Penjumlahan(a,b):
    Penjumlahan = float(a) + float(b)
    return Penjumlahan
    
def Pengurangan(a,b):
    Pengurangan = float(a) - float(b)
    return Pengurangan

def Perkalian(a,b):
    Perkalian = float(a) * float(b)
    return Perkalian

def Pembagian(a,b):
    Pembagian = float(a) / float(b)
    return Pembagian

pilihan="hitung"
while pilihan=="hitung":
    print("\n\t\tSelamat Datang di Program Kalkulator Sederhana \^_^/\n")
    a = float(input("masukan bilangan pertama : "))
    b = float(input("masukan bilangan kedua : "))
    print("\nMenu Kalkulator")
    print("\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\n5.Batal")
    print("\nSilahkan Pilih Menu Kalkulator yang Anda Inginkan.....")
    c = input("\nMenu Pilihan Anda : ")
    if c == "1":
        print("\nhasil : ",Penjumlahan(a,b))
    elif c == "2":
        print("\nhasil : ",Pengurangan(a,b))
    elif c == "3":
        print("\nhasil : ",Perkalian(a,b))
    elif c == "4":
        print("\nhasil : ",Pembagian(a,b))
    elif c == "5":
        print("terima kasih sudah menggunakan program ini....")
        break
    else:
        print("\noperasi error karena kesalahan input")

    pilihan=input("Apakah Anda Ingin Menghitung Lagi?\n(hitung/tidak) = ",)
    if pilihan == "tidak":
        print("Terima Kasih Sudah Menggunakan Program Ini ^_^\nSampai Jumpa Lagi........")
        break
