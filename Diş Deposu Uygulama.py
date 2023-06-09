from tkinter import *
from tkinter import messagebox
import mysql.connector
import hashlib
from mysql.connector import (connection)

#Mysql baslantisini yapmak icin
mydb = mysql.connector.connect(
    host='localhost',
    user = "root",
    passwd = "146360",
    database = "DisDeposu"
)

#Cursor ile calistirma imlec ile ilerleme yapmak icin ekliyoruz.
mycurs = mydb.cursor()


def openMain():


    def openInfo():
        inf = Toplevel()
        inf.title("Hakkında")
        inf.bind("<Escape>", lambda event: inf.destroy())
        Label(inf, text = "Disdeposu", font=("Times New Roman TUR", 14, "bold")).pack()
        Label(inf, text = "----------", font=("Times New Roman TUR", 14, "bold")).pack()
        Label(inf, text = "Diş Depomuz 2023 yılında hizmetinize başlamıştır").pack(anchor=W)
        Label(inf, text = "Bir Diş Hastanesinde Bulunması Gereken Her Ürün Vardır").pack(anchor=W)
        Label(inf, text = "Taksitli satışımız yoktur").pack(anchor=W)
        Label(inf, text = "Toplu alimlar icin : mkaanust@gmail.com").pack(anchor=W)

       
       #Giriş Yapmak İçin
    def openLogin():
        def openReg():
            kay = Tk()
            kay.title("Kayit Ol")
            kay.geometry("500x400+400+200")
            kay.resizable(True, True)
            kay.bind("<Escape>", lambda event: kay.destroy())
            Label(kay, text = "Kayit Ol", font=("Times New Roman TUR", 12, "bold")).grid(row=0, column=10)
            Label(kay, text = "-------------").grid(row=1, column=10)
            Label(kay, text = "").grid(row=2, column=2)
            Label(kay, text = "* olan alanlarin doldurulmasi zorunludur.").grid(row=3, column=10)
            Label(kay, text = "").grid(row=4, column=0)
            Label(kay, text = "").grid(row=5, column=1)
            Label(kay, text = "").grid(row=6, column=2)
            Label(kay, text = "").grid(row=7, column=3) 
            Label(kay, text = "").grid(row=4, column=4)
            Label(kay, text = "").grid(row=4, column=5)
            Label(kay, text = "*Hastane No*").grid(row=6, column=9)
            Label(kay, text = "Hastane Adı*").grid(row=7, column=9)
            Label(kay, text = "Hastane Numarası*").grid(row=9, column=9)
            Label(kay, text = "E-mail*").grid(row=10, column=9)
            Label(kay, text = "Parola*").grid(row=11, column=9)
            Label(kay, text = "Adres").grid(row=12, column=9)
            Hastane_No = Entry(kay)
            Hastane_No.grid(row=6, column=10)
            Hastane_adı = Entry(kay)
            Hastane_adı.grid(row=7, column=10)
            Hastane_numarası = Entry(kay)
            Hastane_numarası.grid(row=9, column=10)
            Email = Entry(kay)
            Email.grid(row=10, column=10)
            passwd = Entry(kay)
            passwd.grid(row=11, column=10)
            adres = Entry(kay)
            adres.grid(row=12, column=10)



            def kayit():

                if(len(str(passwd.get())) != 0):
                    h = hashlib.sha3_512()
                    h.update(str.encode(f"{str(passwd.get())}"))

                if(len(str(Hastane_No.get())) == 0 or len(str(Hastane_adı.get())) == 0 or  len(str(Email.get())) == 0 or len(str(adres.get())) == 0 or len(str(passwd.get())) == 0 or len(str(Hastane_numarası.get())) == 0):
                    messagebox.showwarning("Uyari", "Lutfen zorunlu alanlari bos birakmayiniz.")
                else:
                    if(not(str(Hastane_No.get()).isdigit())):
                        messagebox.showwarning("Uyari", "Hastane No yanlis girilmistir.\nLutfen tamami sayi oldugundan emin olun.")
                    elif(not(str(Hastane_numarası.get()).isdigit())):
                        messagebox.showwarning("Uyari", "Hastane Telefon numarasi yanlis girilmistir.\nLutfen tamami sayi oldugundan emin olun.")    
                    elif(str(Email.get()).find("@") == -1):
                        messagebox.showwarning("Uyari", "E-mail yanlis girilmistir.\nLutfen e-mail dogru oldugundan emin olun.")
                    else:
                        has = hashlib.sha3_512()
                        has.update(str.encode(f"{passwd.get()}"))
                        mycurs.execute("CALL setDishastaneleri(%s, %s, %s, %d, %s, %s,%s);", (str(Hastane_No.get()), str(Hastane_adı.get()), int(Hastane_numarası.get()), str(Email.get()), str(has.hexdigest()), str(adres.get())))
                        rspReg = messagebox.askokcancel("Kaydiniz basariyla tamamlanmistir.\nLutfen sisteme giris yapiniz.")
                        if rspReg == True :
                            kay.destroy()
                        elif rspReg == False :
                            kay.destroy()
                            logi.destroy()
        
            Button(kay, text="Kayit ol",relief = GROOVE,activebackground="blue", command=kayit).grid(row=14, column=11)

               #Satın alma işlemlerinin yapıldığı kısım
        def openBuy():
            def openSetting():
                ayar = Tk()
                ayar.title("Ayarlar")
                ayar.geometry("500x400+400+200")
                ayar.resizable(True, True)
                ayar.bind("<Escape>", lambda event: ayar.destroy())
                Label(ayar, text = "").grid(row=5, column=12)
                Label(ayar, text = "").grid(row=8, column=12)
                Label(ayar, text = "Sifre Guncelleme", font=("Times New Roman TUR", 12, "bold")).grid(row=10, column=10)
                Label(ayar, text = "----------", font=("Times New Roman TUR", 12, "bold")).grid(row=12, column=10)
                Label(ayar, text = "Eski Parola*").grid(row=14, column=9)
                Label(ayar, text = "Yeni Parola*").grid(row=15, column=9)
                esif = Entry(ayar,show="*")
                esif.grid(row=14, column=10)
                ysif = Entry(ayar,show="*")
                ysif.grid(row=15, column=10)
                def goster():
                    if(selea.get()== 1):
                        esif.config(show="")
                        ysif.config(show="")
                    else:
                        esif.config(show="*")
                        ysif.config(show="*")
                selea = IntVar(ayar) 
                shwa = Checkbutton(ayar, text="Sifreleri Goster", onvalue=1, offvalue=0, variable=selea, command=goster)
                shwa.grid(row=16, column=10)

             #Parola için güvenlik kontrol bloğu
                def gkontrol():
                    if(len(str(esif.get())) > 0 and len(str(ysif.get())) > 0):
                        if(str(esif.get()) == str(ysif.get())):
                            messagebox.showwarning("Uyari", "Ayni sifreleri girdiniz.")
                        else:
                            try:
                                mycurs.execute(f"CALL upPass('a@a.com', %s);", (str(ysif.get()),))
                                 
                            except mysql.connector.Error as e:
                                print ("Error code:", e.errno)
                                print ("SQLSTATE value:", e.sqlstate)
                                print ("Error message:", e.msg)      
                            messagebox.showinfo("Sifre Guncelleme", "Sifreniz basarili bir sekilde guncellenmistir.")
                            ayar.destroy()
                    elif(len(str(esif.get())) == 0 and len(str(ysif.get())) != 0 or len(str(esif.get())) != 0 and len(str(ysif.get())) == 0):
                        messagebox.showwarning("Uyari", "Lutfen zorunlu alanlari bos birakmayiniz.")

                Button(ayar, text="Guncelle",relief = GROOVE,activebackground="blue", command=gkontrol).grid(row=18, column=11)

                    
                #Siparişleri görüntülemek için
            def openOrder():
                order = Tk()
                order.title("Disdeposu")
                order.geometry("500x400+400+200")
                order.resizable(True, True)
                order.bind("<Escape>", lambda event: order.destroy())
                buy.destroy()
                Button(order, text="Ayarlar",relief = GROOVE,activebackground="blue", command=openSetting).pack(anchor=NE)
                Button(order, text="Cikis Yap",relief = GROOVE,activebackground="blue", command=order.destroy).pack(anchor=NE)
                sip = Text(order, height= 30 , width= 200)
                sip.pack(padx= 10, pady= 10, anchor=NW)
                Label(order, text = "Siparis Iptal*", font=("Times New Roman TUR", 12, "bold")).pack(anchor=SW)
                Label(order, text = "!Asagidaki alana iptal etmek istediginiz siparisin ID'sini giriniz.!").pack(anchor=SW)
                sipId = Entry(order)
                sipId.pack(anchor=SW)

                #Sipariş iptal için oluşturulan kod bloğu
                def siptal():
                    if (len(str(sipId.get())) == 0):
                        messagebox.showwarning("Uyari", "Lutfen siparis id alanini bos birakmayiniz.")
                    else:   
                        rspIp = messagebox.askokcancel("Siparis Iptal", f"{str(sipId.get())} nolu siparisiniz iptal etmek istediginizden emin misiniz.")
                        if rspIp == True :
                            mycurs.execute(f"CALL Siparisiptal({int(sipId.get())});")
                            messagebox.showinfo("Siparis Iptal", f"{str(sipId.get())} nolu siparisiniz iptal edilmistir.")
                        elif rspIp == False :
                            messagebox.showwarning("Siparis Iptal", "Siparisinizin iptal islemi iptal edilmistir.")
                        
                Button(order, text="Siparis Iptal Et",relief = GROOVE,activebackground="blue", command=siptal).pack(anchor=SW)
            
            #if kad == or passw ==
            try:
                mycurs.execute(f"CALL getPass(%s, %s);",(email.get(), passw.get()))
                result = mycurs.fetchall()
                if (result != "True"):
                    logi.destroy()
            except mysql.connector.Error as e:
                print ("Error code:", e.errno)
                print ("SQLSTATE value:", e.sqlstate)
                print ("Error message:", e.msg)



                buy = Tk()
            buy.title("Disdeposu")
            buy.geometry("500x400+400+200")
            buy.resizable(True, True)
            buy.bind("<Escape>", lambda event: buy.destroy())
            logi.destroy()
            Button(buy, text="Siparislerim",relief = GROOVE,activebackground="blue", command=openOrder).grid(row=0, column=10)
            Button(buy, text="Ayarlar",relief = GROOVE,activebackground="blue", command=openSetting).grid(row=0, column=11)
            Button(buy, text="Cikis Yap",relief = GROOVE,activebackground="blue", command=buy.destroy).grid(row=0, column=12)

            sVal1 = StringVar(buy)
            sVal2 = StringVar(buy)
            sVal3 = StringVar(buy)
            Label(buy, text = "Urunlerin Listesi", font=("Times New Roman TUR", 12, "bold")).grid(row=0, column=1)
           
            

            Label(buy, text = "Anguldurva").grid(row=3, column=1)
            Anguldurva = Spinbox(buy, from_=0, to=20, increment=1,textvariable=sVal1, justify=CENTER)
            Anguldurva.grid(row=3, column=5)
            Label(buy, text = "").grid(row=4, column=12)

            Label(buy, text = "Piyasemen").grid(row=20, column=1)
            Piyasemen = Spinbox(buy, from_=0, to=20, increment=1,textvariable=sVal2, justify=CENTER)
            Piyasemen.grid(row=20, column=5)
            Label(buy, text = "").grid(row=21, column=12)

            Label(buy, text = "RVG").grid(row=50, column=1)
            RVG = Spinbox(buy, from_=0, to=20, increment=1,textvariable=sVal3, justify=CENTER)
            RVG.grid(row=50, column=5)


 
            def al():
                
                urunad = ["Anguldurva", "Piyasemen", "RVG"]
                urunler=mycurs.execute("SELECT UrunFiyat FROM Urunler")
                urunfiyat = list()
                print(urunler)
                try: 
                    pass
                    

                        
                except mysql.connector.Error as e:
                    print ("Error code:", e.errno)
                    print ("SQLSTATE value:", e.sqlstate)
                    print ("Error message:", e.msg)
                tutar = ( int(Anguldurva.get()) * urunfiyat[0] ) + ( int(Piyasemen.get()) * urunfiyat[1] ) + ( int( RVG.get()) * urunfiyat[2] )
                rspBuy = messagebox.askyesno("Siparis Onay",f"""Siparisinizi onayliyor musunuz?
Anguldurva = {urunfiyat[0]} $ x {str(Anguldurva.get())}
Piyasemen = {urunfiyat[1]} $ x {str(Piyasemen.get())}
RVG = {urunfiyat[2]} $ x {str(RVG.get())}
+
----------------------------------------
Toplam Tutar =\t {tutar} $ """)
                if rspBuy == True :
                        messagebox.showinfo("Siparisiniz onaylanmistir.\n1 Hafta icersinde teslim edilecektir.")
                elif rspBuy == False :
                    sVal1.set("0")
                    sVal2.set("0")
                    sVal3.set("0")
            Label(buy, text = "").grid(row=90, column=12)
            Button(buy, text="Sipariş Ver ",relief = GROOVE,activebackground="blue", command=al).grid(row=100, column=12)
                    
                    
                    
                    
        logi = Tk()
        logi.title("Disdeposu")
        logi.geometry("500x400+400+200")
        logi.resizable(True, True)
        main.destroy()
        logi.bind("<Escape>", lambda event: logi.destroy())
        Label(logi, text = "", ).grid(row=0, column=0)
        Label(logi, text = "", ).grid(row=1, column=1)
        Label(logi, text = "", ).grid(row=2, column=2)
        Label(logi, text = "", ).grid(row=3, column=3)
        Label(logi, text = "", ).grid(row=4, column=0)
        Label(logi, text = "", ).grid(row=4, column=1)
        Label(logi, text = "", ).grid(row=4, column=2)
        Label(logi, text = "", ).grid(row=4, column=3) 
        Label(logi, text = "", ).grid(row=4, column=4)
        Label(logi, text = "", ).grid(row=4, column=5)
        Label(logi, text = "", ).grid(row=4, column=6)
        Label(logi, text = "", ).grid(row=4, column=7)
        Label(logi, text = "", ).grid(row=4, column=8)
        Label(logi, text = "E-mail").grid(row=4, column=9)
        Label(logi, text = "Parola").grid(row=5, column=9)
        email = Entry(logi)
        email.grid(row=4, column=10)
        passw = Entry(logi, show="*")
        passw.grid(row=5, column=10)
        def goster():
            if(sele.get()== 1):
                passw.config(show="")
            else:
                passw.config(show="*")
        sele = IntVar(logi) 
        shw = Checkbutton(logi, text="Sifreyi Goster", onvalue=1, offvalue=0, variable=sele, command=goster)
        shw.grid(row=7, column=10)
        
        Button(logi, text="Giris Yap",relief = GROOVE,activebackground="blue", command=openBuy).grid(row=8, column=11)
        Button(logi, text="Kayit ol",relief = GROOVE,activebackground="blue", command=openReg).grid(row=9, column=12)


    main = Tk()
    main.title("Disdeposu")
    main.geometry("500x400+400+200")
    main.resizable(True, True)
    main.bind("<Escape>", lambda event: main.destroy())

    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "Dis Deposuna Hoş Geldiniz").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Button(main, text="Giris Yapiniz",relief = GROOVE,activebackground="blue", command=openLogin).pack()
    Button(main, text="Hakkimizda",relief = GROOVE,activebackground="blue", command=openInfo).pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()


    main.mainloop()

openMain()
mydb.close()

