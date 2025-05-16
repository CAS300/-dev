sayi_1=int(input("ilk sayıyı giriniz: "))
sayi_2=int(input("ikinci sayıyı giriniz: "))
toplam=(sayi_1+sayi_2)
çıkarma=(sayi_1-sayi_2)
çarpma=(sayi_1*sayi_2)
bölme=(sayi_1/sayi_2)
mod=(sayi_1%sayi_2)
üs=(sayi_1**sayi_2)
print(f"Toplama işlemi: {toplam} \nÇıkarma işlemi: {çıkarma} \nÇarpma işlemi: {çarpma} \nBölme işlemi {bölme} \nMod işlemi {mod} \nÜsalma işlemi {üs}" )

#----------------------------------------------------------------

toplam=1
sayi=int(input("Sayi: "))
for i in range(1,sayi):
    toplam+=i+1
print(toplam)

#----------------------------------------------------------------

sayılar=[]
for i in range(1,100):
    if i%2==0:
        sayılar.append(i)
print(sayılar)

#----------------------------------------------------------------

a=input("kelime: ")
a=list(a)
a=a[::-1]
print(a)
