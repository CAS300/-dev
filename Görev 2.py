toplam=1 # Toplamı tutacak değişken, başlangıçta 1 olarak ayarlanır
sayi=int(input("Sayi: ")) # Kullanıcıdan bir tam sayı alınır
for i in range(1,sayi): # 1'den girilen sayıya kadar olan aralıktaki sayılarla döngü başlatılır
    toplam+=i+1 # Her adımda, toplam değişkenine (i + 1) değeri eklenir
print(toplam)