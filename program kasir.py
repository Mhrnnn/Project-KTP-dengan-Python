pilihan="pesan"
while pilihan=="pesan":
    print("\n\t\t\tSELAMAT DATANG DI..................\n")
    print("\t\t\t\t\t\tKEDAI JARI JEMARI")
    print("\t\t\t\t\tTempat yang Pas untuk Mengerjakan Tugas\t")
    print("\nKODE \t\t\t\t\t\tMENU \t\t\t\tHARGA")
    print("a01 \t\t\t\tPaket Ayam Terbakar Rayuan Cinta \t\t30k")
    print("b02 \t\t\t\tPaket Indomie Anti Anxiety \t\t\t18k")
    print("c03 \t\t\t\tBakso Iga Pedas Sepedas Ucapanmu \t\t25k")
    print("d04 \t\t\t\tTeh Anti Galau \t\t\t\t\t 5k")
    print("e05 \t\t\t\tPaket Terserah 1 \t\t\t\t33k")
    print("f06 \t\t\t\tPaket Terserah 2 \t\t\t\t36k")
    print("g07 \t\t\t\tPaket Terserah 3 \t\t\t\t39k")
    print("h08 \t\t\t\tJus Rasa yang Pernah Ada \t\t\t13k")

    pesanan = input("\nMau Pesan Kode Makanan Apa? ")
    banyakpesanan = int(input("\nMau Pesan Berapa Banyak? "))

    if pesanan == "a01":
        listmenu="Paket Ayam Terbakar Rayuan Cinta"
        harga= 30000*banyakpesanan
        if banyakpesanan >=3:
            diskon=int(harga*0.1)
            totalharga=int(harga-diskon)
        else:
            diskon=0
            totalharga=int(harga)

    elif pesanan == "b02":
        listmenu="Paket Indomie Anti Anxiety"
        harga= 18000*banyakpesanan
        diskon=0
        totalharga=int(harga)

    elif pesanan == "c03":
        listmenu="Bakso Iga Pedas Sepedas Ucapanmu"
        harga= 25000*banyakpesanan
        diskon=0
        totalharga=int(harga)

    elif pesanan == "d04":
        listmenu="Teh Anti Galau"
        harga= 5000*banyakpesanan
        diskon=0
        totalharga=int(harga)

    elif pesanan == "e05":
        listmenu="Paket Terserah 1"
        harga= 33000*banyakpesanan
        if banyakpesanan >=3:
            diskon=int(harga*0.2)
            totalharga=int(harga-diskon)
        else:
            diskon=0
            totalharga=int(harga)

    elif pesanan == "f06":
        listmenu="Paket Terserah 2"
        harga= 36000*banyakpesanan
        if banyakpesanan >=3:
            diskon=int(harga*0.25)
            totalharga=int(harga-diskon)
        else:
            diskon=0
            totalharga=int(harga)

    elif pesanan == "g07":
        listmenu="Paket Terserah 3"
        harga= 39000*banyakpesanan
        if banyakpesanan >=3:
            diskon=int(harga*0.3)
            totalharga=int(harga-diskon)
        else:
            diskon=0
            totalharga=int(harga)

    elif pesanan == "h08":
        listmenu="Jus Rasa yang Pernah Ada"
        harga= 13000*banyakpesanan
        diskon=0
        totalharga=int(harga)

    else:
        listmenu="-"
        harga="-"
        diskon="-"
        totalharga="-"
        pilihan=input("Sayang Sekali Menu Tidak Tersedia, Coba Ulangi Lagi Ya...: ")

    print("--------------------------------------------------------------------")
    print("\t\t\tKedai Jari Jemari")
    print("--------------------------------------------------------------------")
    print("Menu Pesanan Anda   : ",listmenu)
    print("Jumlah Pesanan Anda : ",banyakpesanan)
    print("Harga  : ",harga)
    print("Diskon : ",diskon)
    print("--------------------------------------------------------------------")
    print("Jumlah Bayar : ",totalharga)
    print("--------------------------------------------------------------------")
    pilihan=input("Order Lagi Yuk ^_^\npesan/tidak = ",)
    if pilihan == "tidak":
        print("Terima kasih sudah berkunjung ke kedai kami ^_^")
