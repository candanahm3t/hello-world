print("""*****************************************
Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
 ****************************************""")

boy= float(input("Lütfen Boyunuzu Metre Cinsinden Girin:"))
kilo=float(input("Lütfen Kilonuzu Girin:"))
sonuc = kilo/(boy*boy)

if sonuc<18.5:
    print("Zayıfsınız")

elif sonuc>=18.5 and sonuc<25:
    print("Normal Kilodasınız")

elif sonuc>=25 and sonuc<30:
    print("Fazla Kilolarınız bulunmakta")

elif sonuc>30:
    print("Obezsiniz")