#matriks A
print('penginputan matriks A')
print('matriks A')
print('-------------------------------------------------------')
A = []
j = 0
u=int(input('\ninput jumlah baris yang diinginkan = '))
v=int(input('\nmasukkan jumlah kolom yang diinginkan = '))
for i in range (0,u):
    print('baris -',i+1)
    a = []
    while j < v :
        a.append(int(input('masukan data : ')))
        j = j + 1
    A.append(a)
    j = 0
    i = i + 1

print()
print('membentuk matriks A')
for a in A:
    print(a)
print()

#matriks B
print('penginputan matriks B')
print('matriks B')
print('-----------------------------------------------------')
B = []
q = 0
u=int(input('\ninput jumlah baris yang diinginkan = '))
v=int(input('\nmasukkan jumlah kolom yang diinginkan = '))
for i in range (0,u):
    print('baris ke -',i+1)
    b = []
    while q < v :
        b.append(int(input('data : ')))
        q = q + 1
    B.append(b)
    q = 0
    i = i + 1


print()
print('membentuk matriks B')
for b in B:
    print(b)
print()

print('--------------------------------------')
print('penjumlahan 2 matriks (A + B)')

for i in range(0,len(A)):
    row=[]
    for j in range(0,len(A[0])):
        total=0
        for k in range(0,len(A[0])):
            total = total + (A[i][k]*B[k][j])
        print(A[i][j] + B[i][j],end=' ')
    print()

print('--------------------------------------')
print('pengurangan 2 matriks (A - B)')
for i in range(0,len(A)):
    row=[]
    for j in range(0,len(A[0])):
        total=0
        for k in range(0,len(A[0])):
            total = total + (A[i][k]*B[k][j])
        print(A[i][j] - B[i][j],end=' ')
    print()

print('--------------------------------------')
print('perkalian 2 matriks (A x B)')

C=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(A)):
    
    for j in range(0,len(B)):
        
        for k in range(0,len(B)):
            C[i][j]=C[i][j] + (A[i][k]*B[k][j])
        print(C[i][j],end=' ')
    print()

