sayılar=[] # Boş bir liste oluşturuluyor
for i in range(1,100):  # 1 ile 99 arasında (100 hariç) sayılarla döngü başlatılıyor
    if i%2==0:          # Eğer sayı 2 ile kalansız bölünüyorsa, yani çift sayı ise
        sayılar.append(i)  # Bu çift sayı listeye ekleniyor
print(sayılar)