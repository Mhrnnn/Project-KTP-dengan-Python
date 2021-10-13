list_KTP=[]
class KTP:
    def __init__(self, NIK, Nama, Tempat_lahir, Tanggal_Lahir_dd, Tanggal_Lahir_mm, Tanggal_Lahir_yyyy, Provinsi, Kota, Kecamatan, Kelurahan, RT, RW, Alamat, Jenis_Kelamin, Golongan_Darah, Agama, Status_Perkawinan, Pekerjaan, Kewarganegaraan):
        self.NIK                = NIK
        self.Nama               = Nama
        self.Tempat_lahir       = Tempat_lahir
        self.Tanggal_Lahir_dd   = Tanggal_Lahir_dd
        self.Tanggal_Lahir_mm   = Tanggal_Lahir_mm
        self.Tanggal_Lahir_yyyy = Tanggal_Lahir_yyyy
        self.Provinsi           = Provinsi
        self.Kota               = Kota
        self.Alamat             = Alamat
        self.RT                 = RT
        self.RW                 = RW
        self.Kelurahan          = Kelurahan
        self.Kecamatan          = Kecamatan
        self.Jenis_Kelamin      = Jenis_Kelamin
        self.Golongan_Darah     = Golongan_Darah
        self.Agama              = Agama
        self.Status_Perkawinan  = Status_Perkawinan
        self.Perkejaan          = Pekerjaan
        self.Kewarganegaraan    = Kewarganegaraan
        
    def cetak(self):
        print(f"NIK                 : {str(self.NIK)}",
              f"\nNama              : {str(self.Nama)}",
              f"\nTempat/Tgl lahir  : {str(self.Tempat_lahir)} {str(self.Tanggal_Lahir_dd)}-{str(self.Tanggal_Lahir_mm)}-{str(self.Tanggal_Lahir_yyyy)}",
              f"\nProvinsi          : {str(self.Provinsi)}",
              f"\nKota              : {str(self.Kota)}",
              f"\nAlamat            : {str(self.Alamat)}",
              f"\n      RT/RW       : {str(self.RT)}/{str(self.RW)}",
              f"\n      Kel/Desa    : {str(self.Kelurahan)}",
              f"\n      Kecamatan   : {str(self.Kecamatan)}",
              f"\nJenis_Kelamin     : {str(self.Jenis_Kelamin)}",
              f"\nGolongan_Darah    : {str(self.Golongan_Darah)}",
              f"\nAgama             : {str(self.Agama)}",
              f"\nStatus_Perkawinan : {str(self.Status_Perkawinan)}",
              f"\nPekerjaan         : {str(self.Perkejaan)}",
              f"\nKewarganegaraan   : {str(self.Kewarganegaraan)}",
              f"\nBerlaku Hingga    : Seumur Hidup",
              f"\n")
        
opsi="iya"
while (opsi=="iya"):
    print("\n\t\t\tProgram Data E-KTP")
    print("[1] Input Data E-KTP")
    print("[2] Lihat Data E-KTP") 
    print("[3] Hapus Data E-KTP")
    print("[4] Batal")
    print("\nSilahkan Pilih Menu")
    pilihan=int(input("\nMenu Pilihan Anda               : "))
    if(pilihan==1):
        a=int(input("\nNIK                               : "))
        digit=len(str(abs(a)))
        while(digit != 16):
            print("NIK Salah, Silahkan Coba Lagi")
            a=int(input("NIK : "))
            digit=len(str(abs(a)))
        b=str(input("Nama Lengkap                        : "))
        c=str(input("Tempat Lahir                        : "))
        d=int(input("Tanggal Lahir (hh)                  : "))
        e=int(input("Tanggal lahir (bb)                  : "))
        f=int(input("Tanggal lahir (tttt)                : "))
        g=str(input("Provinsi                            : "))
        h=str(input("Kota                                : "))
        i=str(input("Alamat                              : "))
        j=int(input("RT                                  : "))
        k=int(input("RW                                  : "))
        l=str(input("Kel/Desa                            : "))
        m=str(input("Kecamatan                           : "))
        n=str(input("Jenis Kelamin (L/P)                 : "))
        while(n!="L" and n!="P"):
            print("Jenis Kelamin Salah, Silahkan Masukan Ulang")
            n=str(input("Jenis Kelamin (L/P)       : "))
        o=str(input("Golongan Darah (A/B/AB/O)           : "))
        while(o!="A" and o!="B" and o!="AB" and o!="O"):
            print("Golongan Darah Salah, Silahkan Masukan Ulang")
            o=str(input("Golongan Darah (A/B/AB/O)           : "))
        p=str(input("Agama                               : "))
        q=str(input("Status Perkawinan                   : "))
        r=str(input("Pekerjaan                           : "))
        s=str(input("Kewarganegaraan                     : "))
        inputKTP = KTP(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s)
        print("")
        perulangan = str(input("\nApakah data yang diinputkan sudah benar ?\nTulis benar untuk melanjutkan dan salah untuk mengulang inputan : ",))
        if (perulangan=="benar"):
            list_KTP.append(inputKTP)
            print("")
            
        else:
            continue
        
    elif (pilihan==2):
        cetak_ktp=int(input("\nmohon inputkan urutan pengisian input data\n(pilih angka 1 jika anda baru pertama kali melakukan pengisian) : "))
        print("\n.................mohon tunggu sebentar.............")
        list_KTP[cetak_ktp - 1].cetak()

    elif(pilihan==3):
        hapus_ktp=int(input("\nmohon inputkan angka urutan penghapusan data\n(pilih angka 1 jika anda baru pertama kali melakukan penghapusan) : "))
        print("\nmohon tunggu sebentar.............")
        list_KTP[cetak_ktp - 1] = None
        print("\nKartu anda berhasil dihapus")
        
    elif(pilihan==4):
        print("\nprogram berhasil dibatalkan....")
        break
    else:
        print("\nterjadi kesalahan inputan")

    opsi=input("\nApakah anda ingin mengulang kembali program data E-KTP lagi?\n(iya/tidak) = ",)
    if opsi=="tidak":
        print("\nTerima kasih sudah mengunjungi program ini")
        
