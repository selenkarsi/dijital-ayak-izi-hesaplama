
def puan_hesapla(sosyal_medya, gunluk_saat, paylasim_sayisi):
    puan = (sosyal_medya * 20) + (gunluk_saat * 5) + (paylasim_sayisi * 2)
    return puan


def risk_seviyesi(puan):
    if puan < 50:
        return "Düşük Risk"
    elif puan < 100:
        return "Orta Risk"
    else:
        return "Yüksek Risk"


def dosyaya_kaydet(kullanici_bilgisi):
    with open("dijital_ayak_izi.txt", "a") as dosya:
        dosya.write(str(kullanici_bilgisi))


print("Dijital ayak izi hesaplama sistemi")

kullanicilar = []
platformlar = ("Instagram", "TikTok", "Twitter", "Facebook")

while (True):

    try:
        ad = input("adiniz: ")

        print("kullandiiginiz platform sayisini giriniz\n")
        print("platformlar:", platformlar)

        sosyal_medya = int(input("kac tane sosyal medya platformu kullaniyorsunuz?: "))
        gunluk_saat = float(input("gunde kaç saat internette vakit geciriyorsunuz?: "))
        paylasim_sayisi = int(input("haftalik paylasim sayiniz: "))

        
        puan = puan_hesapla(sosyal_medya, gunluk_saat, paylasim_sayisi)

        seviye = risk_seviyesi(puan)

        kullanici = {
            "ad": ad,
            "platform sayisi": sosyal_medya,
            "gunluk saat": gunluk_saat,
            "paylasim sayisi": paylasim_sayisi,
            "puan": puan,
            "risk": seviye
        }
        kullanicilar.append(kullanici)

        dosyaya_kaydet(kullanici)

        print("sonuc: \n")
        print("dijital ayak İzi puani:", puan)
        print("risk seviyesi:", seviye)

    except ValueError:
        print("HATA: lutfen sayisal deger giriniz!")

    except Exception as hata:
        print("beklenmeyen hata olustu:", hata)

    cevap = input("yeni kullanici eklemek ister misiniz? (e/h): \n")

    if cevap.lower() != "e":
        break


print("tum kullanicilar\n")

for kisi in kullanicilar:
    print(kisi)

print("veriler 'dijital_ayak_izi.txt' dosyasina kaydedildi.\n")