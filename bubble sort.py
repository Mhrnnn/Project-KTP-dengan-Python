#bubblesort = dia ngurutinnya dengan ngebandingin data secara berpasangan, jadi dia tukerannya sama pasangannya doang, beda kayak insertion sort

#bubble sort while while while
def swap(L1,i,j): #fungsi ini untuk menukar pasangan
    L1[i],L1[j] = L1[j],L1[i]

def bubble1(L1): #fungsi ini untuk sortnya
    ubah = True
    pjg = len(L1) #banyaknya perulangan yg digunakan untuk mengecek data dari awal
    while pjg > 1 and ubah: 
        ubah = False
        j=1
        while j < pjg : #selama 1 lebih kecil dari si pjg maka :
            if L1[j] < L1[j-1]: #jika nilai list di indeks 1 < nilai list di indeks 0
                ubah = True
                swap(L1,j,j-1) #j sebagai 'i'nya (nilainya 1) dan j-1 = 0
            j+=1 #while harus ada ket ini supaya ngeloop, kalo for ga perlu
        print(L1)

        if not ubah: #jika ubah nilainya false maka ga ngelakuin looping lagi karna udah terurut
            print("hasil akhir = %s" %str(L1))
            pjg-=1

pjg = int(input("panjang list L yang diinginkan = "))
L = []

j = 1
while j < pjg+1 :
    data = int(input("masukan data yang ke %i untuk list L = " %j))
    L.append(data)
    j += 1
    
print("-----------------------------------------------------------")
print("sebelum bubble sort")
print(L)
print("setelah bubble sort")
bubble1(L)
                
#bubble sort while while for
def swap(L1,i,j): #fungsi ini untuk menukar pasangan
    L1[i],L1[j] = L1[j],L1[i]

def bubble1(L1): #fungsi ini untuk sortnya
    ubah = True
    pjg = len(L1) #banyaknya perulangan yg digunakan untuk mengecek data dari awal
    while pjg > 1 and ubah: 
        ubah = False
        j=1
        while j < pjg : #selama 1 lebih kecil dari si pjg maka :
            if L1[j] < L1[j-1]: #jika nilai list di indeks 1 < nilai list di indeks 0
                ubah = True
                swap(L1,j,j-1) #j sebagai 'i'nya (nilainya 1) dan j-1 = 0
            j+=1 #while harus ada ket ini supaya ngeloop, kalo for ga perlu
        print(L1)

        if not ubah: #jika ubah nilainya false maka ga ngelakuin looping lagi karna udah terurut
            print("hasil akhir = %s" %str(L1))
            pjg-=1

print("------------------------------------------------------------------------------")
pjg = int(input("panjang list L yang diinginkan = "))
L = []

for j in range (1,pjg+1) :
    data = int(input("masukan data yang ke %i untuk list L = " %j))
    L.append(data)
    
print("-----------------------------------------------------------")
print("sebelum bubble sort")
print(L)
print("setelah bubble sort")
bubble1(L)

