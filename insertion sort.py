#insertion sort = mengurutkan data dengan membandingkan dengan MENGURUTKAN DATA PERTAMA DG DATA KEDUA LALU MEMBANDINGKAN LAGI DATA KEDUA DENGAN DATA KETIGA (satu persatu) dst.


#L = [67,13,71,39,45]

#menggunakan program while
def insertionsort(L): #L itu nama listnya
    for i in range(1,len(L)): #i nya jalan dari 1 karena udah ditentuin 1, dan jalannya sampai 5 karna len(A) itu 5 
        Ka = L[i] #lengan kanan = mulai dari indeks ke-i yaitu ke-1 artinya ke 13
        Ki = i - 1 #0 (karna i = 1 dan 1-1=0)
        while Ki >=0 and L[Ki] > Ka: #ketika indeks kiri yaitu 0 >= 0 dan L[0] > L[1] (nilai list pada indeks 0 > dari nilai list indeks 1)  maka
            L[Ki + 1] = L[Ki] #L[1]=L[0], artinya L[1] diisi L[0] (untuk pertukaran)
            Ki -= 1 #Ki dikurangi 1
            L[Ki + 1] = Ka #L[1]=Ka (list di indeks 1 dituker jadi Ka)

panjanglist = int(input("panjang list L yang diinginkan = ")) #untuk program input custom
L = [] #buat simpen list yang kita input

j = 1
while j < panjanglist+1 : #pake panjanglist+1 supaya loopingnya sampe panjanglist
    data = int(input("masukan data yang ke %i untuk list L = " %j)) #%j untuk formatting i nya
    L.append(data)
    j += 1 #untuk while harus ada ket ini supaya bisa looping

print("sebelum di insertion sort = ")
print(L)
insertionsort(L)
print("setelah di insertion sort = ")
print(L)
#=====================================================================================================================================================================
#menggunakan program for
def insertionsort(L): #L itu nama listnya
    for i in range(1,len(L)): #i nya jalan dari 1 karena udah ditentuin 1, dan jalannya sampai 5 karna len(A) itu 5 
        Ka = L[i] #lengan kanan = mulai dari indeks ke-i yaitu ke-1 artinya ke 13
        Ki = i - 1 #0 (karna i = 1 dan 1-1=0)
        while Ki >=0 and L[Ki] > Ka: #ketika indeks kiri yaitu 0 >= 0 dan L[0] > L[1] (nilai list pada indeks 0 > dari nilai list indeks 1)  maka
            L[Ki + 1] = L[Ki] #L[1]=L[0], artinya L[1] diisi L[0] (untuk pertukaran)
            Ki-=1 #Ki dikurangi 1
            L[Ki + 1] = Ka #L[1]=Ka (list di indeks 1 dituker jadi Ka)

panjanglist = int(input("panjang list L yang diinginkan = ")) #untuk program input custom
L = [] #buat simpen list yang kita input

for  j in range(1,panjanglist+1) : #artinya for loop ini sampe panjanglist, karna di for itu misal ditulis sampe 4 maka dia hanya mengulang 4-1 yaitu 3
    data = int(input("masukan data yang ke %i untuk list L = " %j)) #%j untuk formatting i nya
    L.append(data)

print("sebelum di insertion sort = ")
print(L)
insertionsort(L)
print("setelah di insertion sort = ")
print(L)
