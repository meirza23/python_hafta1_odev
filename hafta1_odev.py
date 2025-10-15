# -----------------------------
# 1. SORU: Araba sınıfı yorumu
# -----------------------------
# Bu sınıf, bir araba nesnesi oluşturmak için kullanılır.
# Yapıcı metot (constructor) marka ve model değerlerini alır.
# 'bilgileri_yazdir' metodu ise bu bilgileri ekrana yazdırır.

class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgileri_yazdir(self):
        print(f"Marka: {self.marka}, Model: {self.model}")

# Kullanım
araba1 = Araba("Toyota", "Corolla")
araba1.bilgileri_yazdir()

# -----------------------------
# 2. SORU: Dikdortgen sınıfı
# -----------------------------
class Dikdortgen:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan_hesapla(self):
        return self.genislik * self.yukseklik

# Kullanım
dikdortgen1 = Dikdortgen(5, 10)
alan = dikdortgen1.alan_hesapla()
print(f"Dikdörtgenin alanı: {alan}")

# -----------------------------
# 3. SORU: Kare sınıfı
# -----------------------------
class Kare:
    def __init__(self, kenar_uzunlugu):
        self.kenar_uzunlugu = kenar_uzunlugu

    def kareyi_yazdir(self):
        for i in range(self.kenar_uzunlugu):
            print('* ' * self.kenar_uzunlugu)

# Kullanım
kare = Kare(5)
kare.kareyi_yazdir()

# -----------------------------
# 4. SORU: HesapMakinesi sınıfı
# -----------------------------
class HesapMakinesi:
    def topla(self, sayi1, sayi2, sayi3=None):
        if sayi3 is not None:
            return sayi1 + sayi2 + sayi3
        else:
            return sayi1 + sayi2

# Kullanım
hesap_makinesi = HesapMakinesi()
print("İki sayının toplamı:", hesap_makinesi.topla(10, 20))
print("Üç sayının toplamı:", hesap_makinesi.topla(10, 20, 30))

# -----------------------------
# 5. SORU: Merhaba sınıfı
# -----------------------------
class Merhaba:
    def merhaba_yazdir(self):
        print("Merhaba Dünya")

# Kullanım
merhaba = Merhaba()
merhaba.merhaba_yazdir()

# -----------------------------
# 6. SORU: Kalıtım örneği (İnsan - Hoca - Sekreter - Öğrenci)
# -----------------------------
class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def konus(self):
        print(f"{self.ad} diyor ki: Merhaba, ben bir insanım.")

# Hoca sınıfı
class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no

    def konus(self):
        print(f"{self.ad} diyor ki: Ben hocayım, derse başlayalım!")

    def ders_ver(self):
        print(f"{self.ad} (Sicil No: {self.sicil_no}) şu anda ders veriyor.")

# Sekreter sınıfı
class Sekreter(Insan):
    def __init__(self, ad, yas, ofis_no):
        super().__init__(ad, yas)
        self.ofis_no = ofis_no

    def konus(self):
        print(f"{self.ad} diyor ki: Evrakları hazırladım, hocam.")

    def toplantiyi_duzenle(self):
        print(f"{self.ad} toplantıyı düzenledi (Ofis No: {self.ofis_no}).")

# Öğrenci sınıfı
class Ogrenci(Insan):
    def __init__(self, ad, yas, ogrenci_no):
        super().__init__(ad, yas)
        self.ogrenci_no = ogrenci_no

    def konus(self):
        print(f"{self.ad} diyor ki: Hocam, ödevimi teslim ettim!")

    def ders_calis(self):
        print(f"{self.ad} (Öğrenci No: {self.ogrenci_no}) derse çalışıyor...")

# Kullanım örnekleri
hoca = Hoca("Sinan", 45, "H123")
hoca.konus()
hoca.ders_ver()

sekreter = Sekreter("Ayşe", 35, "B201")
sekreter.konus()
sekreter.toplantiyi_duzenle()

ogrenci = Ogrenci("Enes", 20, "O456")
ogrenci.konus()
ogrenci.ders_calis()