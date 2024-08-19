import random

def tas_kagit_makas_ADINIZ_SOYADINIZ():
    # Kullanıcının adını sorma
    kullanici_adi = input("Lütfen adınızı girin: ")

    # Oyunun kurallarını açıklayan karşılama mesajı
    print(f"Merhaba {kullanici_adi}! Taş, Kağıt, Makas oyununa hoş geldiniz.")
    print("Oyun kuralları: Taş makası yener, Makas kağıdı yener, Kağıt taşı yener.")
    print("İlk iki turu kazanan oyunu kazanır. Oynamak istemediğinizde 'çıkış' yazabilirsiniz.")

    while True:
        # Seçenekler ve sayaçlar
        secenekler = ["taş", "kağıt", "makas"]
        tur_sayisi = 0
        oyuncu_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0

        while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            oyuncu_secimi = input(f"{kullanici_adi}, Taş, Kağıt, Makas seçiminiz (çıkış için 'çıkış' yazın): ").lower()

            if oyuncu_secimi == "çıkış":
                print("Oyun sona eriyor. Görüşmek üzere!")
                return

            if oyuncu_secimi not in secenekler:
                print("Geçersiz seçim! Lütfen taş, kağıt veya makas seçin.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu kazandınız!")
                oyuncu_galibiyetleri += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_galibiyetleri += 1

            tur_sayisi += 1
            print(f"Tur sayısı: {tur_sayisi}, {oyuncu_galibiyetleri}-{bilgisayar_galibiyetleri} (Siz-Bilgisayar)")

        if oyuncu_galibiyetleri == 2:
            print(f"Tebrikler {kullanici_adi}! Oyunu kazandınız!")
        else:
            print(f"Maalesef {kullanici_adi}, oyunu bilgisayar kazandı.")

        # Devam etmek isteyip istemediğini sorma
        devam_et = input(f"{kullanici_adi}, başka bir oyun oynamak ister misiniz? (Evet/Hayır): ").lower()
        if devam_et == "hayır":
            print("Oyun sona erdi. Teşekkürler!")
            break

# Oyunu başlatmak için fonksiyonu çalıştırın
tas_kagit_makas_ADINIZ_SOYADINIZ()