import random  # Rastgele seçimler yapmak için random modülünü içe aktarır

# Taş, Kağıt, Makas oyununun ana fonksiyonu
def tas_kagit_makas_ONUR_BIRCAN():
    
    # Oyunun kurallarını ve genel bilgiyi gösteren bir fonksiyon
    def mesaj():
        print("""
    \n********************
    Taş, Kağıt, Makas Oyununa Hoş Geldiniz!
    
    Kurallar:
    - Taş, makası kırarak yener.
    - Kağıt, taşı sararak yener.
    - Makas, kağıdı keserek yener.
    - Eğer iki oyuncu aynı hareketi seçerse, oyun berabere biter.
    - İlk iki turu kazanan oyunu kazanır.
    - Oynamak istemiyorsanız 'exit' yazabilirsiniz.
    \n********************""")

    # Kullanıcıdan geçerli bir seçim yapmasını sağlayan fonksiyon
    def kullanici_secimi_al():

        # Sonsuz döngü, kullanıcı doğru seçim yapana kadar devam eder
        while True:

             # Kullanıcıdan giriş alır
            secim = input("Bir seçim girin (Taş, Kağıt, Makas): ").strip().lower()
            
            # Seçim geçerli ise
            if secim in secimler:
                return secim
            
            # Kullanıcı 'exit' yazarsa oyun sonlandırılır
            elif secim == 'exit':

                print("Oyun sonlandırılıyor.")
                return None
            
            # Geçersiz seçim yapıldığında kullanıcıyı uyarır
            else:
                print("Geçersiz seçenek, lütfen tekrar deneyin.")

    # Bilgisayarın rastgele bir seçim yapmasını sağlayan fonksiyon
    def bilgisayar_secimi_al():

        # Secimler listesinden rastgele bir seçim yapar
        return random.choice(secimler)

    # Kullanıcı ve bilgisayarın seçimlerini karşılaştırarak kazananı belirleyen fonksiyon
    def kazanan_belirle(kullanici_secimi, bilgisayar_secimi):
        
        # İki seçim de aynı ise
        if kullanici_secimi == bilgisayar_secimi:
            # Beraberlik döndürür
            return "beraberlik"
        
        elif (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or \
             (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
             (kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt"):
            
            # Kullanıcı kazanır
            return "kullanici"
        
        else:
            # Bilgisayar kazanır
            return "bilgisayar"

    # Bilgisayarın oyuna devam etmek isteyip istemediğini rastgele belirleyen fonksiyon
    def bilgisayar_oyuna_devam_etmek_istiyor_mu():

        # Bilgisayarın devam edip etmeyeceğini rastgele belirler
        return random.choice([True, False])

    # Oyunun ana döngüsünü yöneten fonksiyon
    def oyunu_oyna():

        # Kullanıcının kazandığı tur sayısı
        kullanici_kazanma_skoru = 0

        # Bilgisayarın kazandığı tur sayısı
        bilgisayar_kazanma_skoru = 0

        # İki taraf da iki tur kazanana kadar devam eder
        while kullanici_kazanma_skoru < 2 and bilgisayar_kazanma_skoru < 2:
            
            # Kullanıcının seçimini alır
            kullanici_secimi = kullanici_secimi_al()
            
            # Kullanıcı 'exit' yazdıysa
            if kullanici_secimi is None:
                
                # Oyunu sonlandırır
                return False
            
            # Bilgisayarın seçimini alır ve Bilgisayarın seçimini gösterir
            bilgisayar_secimi = bilgisayar_secimi_al()
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            # Sonucu belirler
            sonuc = kazanan_belirle(kullanici_secimi, bilgisayar_secimi)
            
            # Kullanıcı kazandıysa
            if sonuc == "kullanici":

                # Kullanıcının skorunu artırır ve Turu kazandığına dair mesajını gösterir
                kullanici_kazanma_skoru += 1
                print("Tur kazandınız!\n")
            
            # Bilgisayar kazandıysa
            elif sonuc == "bilgisayar":

                # Bilgisayarın skorunu artırır ve Turu kaybettiğine dair mesajını gösterir
                bilgisayar_kazanma_skoru += 1
                print("Tur kaybettiniz!\n")
            
            # Beraberlik durumu
            else:
                print("Tur berabere!\n")
            
            # Güncel skoru gösterir
            print(f"Skor - Siz: {kullanici_kazanma_skoru}, Bilgisayar: {bilgisayar_kazanma_skoru}")
        
        # Kullanıcı iki tur kazandıysa mesajı gösterir
        if kullanici_kazanma_skoru == 2:
            print("Tebrikler! Oyunu kazandınız.\n")

        else:  # Bilgisayar iki tur kazandıysa mesajı gösterir
            print("Bilgisayar oyunu kazandı.\n")

        return True  # Oyun döngüsünü devam ettirir

    # Seçimlerin listesi
    secimler = ["taş", "kağıt", "makas"]
    mesaj()  # Oyun kurallarını ve bilgileri gösterir
    
    # Oyun döngüsü
    while True:

        # Oyunu oynar
        oyun_devam_ediyor_mu = oyunu_oyna()

        # Oyun bitmişse
        if not oyun_devam_ediyor_mu:
            break  # Döngüyü sonlandırır
        
        # Kullanıcıdan yeni oyun isteğini alır
        devam_etme = input("Başka bir oyun oynamak ister misiniz? (Evet/Hayır): ").strip().lower()
        
        # Kullanıcı devam etmek istiyorsa
        if devam_etme == "evet":

            # Bilgisayar devam etmek istiyor mu?
            if bilgisayar_oyuna_devam_etmek_istiyor_mu():
                # Bilgisayarın devam etmek istediğini bildirir
                print("\nBilgisayar da oyuna devam etmek istiyor!")
            
            else:
                # Bilgisayarın devam etmek istemediğini bildirir
                print("\nBilgisayar oyuna devam etmek istemiyor.")
                print("Oyunu oynadığınız için teşekkür ederim, Allah'a emanet olun...\n")
                break  # Döngüyü sonlandırır

        else:
            # Kullanıcı başka oyun istemiyorsa teşekkür mesajı
            print("Oyunu oynadığınız için teşekkür ederim, Allah'a emanet olun...\n")
            break  # Döngüyü sonlandırır

# Fonksiyonu çalıştırır
tas_kagit_makas_ONUR_BIRCAN()