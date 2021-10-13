#terkecil = k
#terbesar = b
#nilai tengah = mid


A = [1,12,13,141,14,33,4,2,32,42,64,76,5,4,5,3,8,121,31,42424,45,88,7,76,9898,767,5,41,86,886,56,7,89,81,90,78,34,100,98,22,31,54,44,55,667]
k = 0
b = len(A)-1
temukan = False
A.sort()
print(A)
cari = int(input("masukan angka :"))

while k <= b and not temukan:
    mid = (k+b)//2 
    if cari == A[mid]:
        temukan = True
    elif cari > A[mid]:
        k = mid + 1
    else:
        b = mid - 1

if temukan == True:
    print("Nilai",cari,"ditemukan")
else:
    print("Nilai",cari,"tidak ditemukan")
    
    
