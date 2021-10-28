print("UJIAN TENGAH SEMESTER ")
print("Nama : Aulia Claudia Rahma")
print("NIM : 2008030")
print("Mata Kuliah : UTS Pemrograman Berorientasi Objek")
print("\n")
print("======================================================")
print("            APLIKASI PENCATATAN UANG DIGITAL          ")
print("======================================================")

saldo_umum=100000
saldo_tabungan=200000
pin=1234

def cek_saldo():
    print ('Saldo Umum Anda Saat ini adalah Rp. {}'.format(saldo_umum))
    print ('Saldo Tabungan Anda Saat ini adalah Rp. {}'.format(saldo_tabungan))

def tarik_tunai(jml_tarik_tunai):
    global saldo_umum,saldo_tabungan
    
    print ('Saldo Umum Anda saat ini Rp. {}'.format(saldo_umum))
    jumlah_saldo_umum=saldo_umum-jml_tarik_tunai
    print ('Sisa saldo Umum Anda saat ini Rp. {}'.format(jumlah_saldo_umum))

    print ("Saldo Tabungan Anda saat ini Rp. {}".format(saldo_tabungan))
    jumlah_saldo_tabungan=saldo_tabungan-jml_tarik_tunai
    print('Sisa saldo tabungan anda saat ini Rp. {}'.format(jumlah_saldo_tabungan))

def setor_tunai(jml_setor_tunai):
    global saldo_umum,saldo_tabungan
    
    print ('Saldo Umum Anda saat ini Rp. {}'.format(saldo_umum))
    jumlah_saldo_umum=saldo_umum+jml_setor_tunai
    print ('Saldo Umum Anda saat ini menjadi Rp. {}'.format(jumlah_saldo_umum))

    print ("Saldo Tabungan Anda saat ini Rp. {}".format(saldo_tabungan))
    jumlah_saldo_tabungan=saldo_tabungan+jml_setor_tunai
    print('Saldo tabungan anda saat ini menajdi Rp. {}'.format(jumlah_saldo_tabungan))


def transfer(jml_transfer):
    global saldo_umum,saldo_tabungan
    
    print ('Saldo Anda Rp {}'.format(saldo))
    saldo=saldo-jml_transfer
    print("Transfer Berhasil, Saldo Anda Sekarang Rp. {}".format(saldo))

def ubah_pin(pin_lama,pin_baru):
    global pin
    
    if not pin_lama == pin:
        print("Pin Anda salah, silakan coba lagi atau hubungi bank yang terdekat")
    
    else:
        pin == pin_baru
    print ('Pin ATM Berhasil diperbaharui')
    

pilihan = None
penyimpanan = None
pin_lama = None
pin_baru = None
jumlah_saldo_umum=None
jumlah_saldo_tabungan=None

while True:
    print(""""
   ===== SELAMAT DATANG DI BANK AULIA =====
    1. CEK SALDO
    2. TARIK TUNAK
    3. SETOR TUNAI
    4. TRANSFER
    5. UBAH PIN
   ========================================== """)
    
    pilihan = int(input("Silahkan masukkan opsi : "))
    if pilihan == 1:
        cek_saldo()
        
        
    elif pilihan == 2:
        print("1. Saldo Umum")
        print("2. Saldo Tabungan")
        penyimpanan=int(input("Pilih penyimpanan Saldo : "))
        if penyimpanan==1:
            jumlah_saldo_umum=int(input("Nominal yang akan ditarik : "))
            tarik_tunai(jumlah_saldo_umum)
            print("===================================================")
        
        if penyimpanan==2:
            jumlah_saldo_tabungan=int(input("Nominal yang akan ditarik : "))
            tarik_tunai(jumlah_saldo_tabungan)
            print("===================================================")

    elif pilihan == 3:
        print("1. Saldo Umum")
        print("2. Saldo Tabungan")
        penyimpanan=int(input("Pilih penyimpanan Saldo : "))
        if penyimpanan==1:
            jumlah_saldo_umum=int(input("Nominal yang akan disetor : "))
            setor_tunai(jumlah_saldo_umum)
            print("===================================================")
        
        if penyimpanan==2:
            setor_tunai(saldo_tabungan)
            jumlah_saldo_tabungan=int(input("Nominal yang akan disetor : "))
            setor_tunai(jumlah_saldo_tabungan)
            print("===================================================")
    elif pilihan == 4:
        kode_bank = str(input("Masukkan kode bank : "))
        no_rek = str(input("Masukkan nomor rekening : "))
        jumlah = int(input("Masukkan Jumlah Transfer : "))
        transfer(jumlah)

    elif pilihan == 5:
        pin_lama = int(input("Masukkan pin lama Anda : "))
        pin_baru = int(input("Masukkan pin baru Anda : "))
        ubah_pin(pin_lama,pin_baru)
        
    else:
        print ("Pilihan Salah!")