import random
import time
import tkinter as tk

class SayiTahminOyunu:
    def __init__(self):
        self.sayi = self.sayiUret()
        self.tahminSayisi = 0
        self.root = tk.Tk()
        self.root.title("Sayı Tahmin Oyunu")
        self.root.geometry("300x150")
        self.root.resizable(False, False)
        
        self.label = tk.Label(self.root, text="Aklımda 0 ile 100 arasında bir sayı tuttum. Hadi bu sayıyı tahmin et!")
        self.label.pack(pady=5)
        self.label2 = tk.Label(self.root, text="Tahmininizi giriniz:")
        self.label2.pack(pady=5)
        self.entry = tk.Entry(self.root, width=20)
        self.entry.pack(pady=5)
        self.button = tk.Button(self.root, text="Tahmin Et", command=self.tahminEt)
        self.button.pack(pady=5)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def on_close(self):
        self.root.destroy()
        
    def sayiUret(self):
        return random.randint(0, 101)

    def tahminEt(self):
        try:
            girilen = int(self.entry.get())
            self.tahminSayisi += 1

            if self.sayi == girilen:
                sonuc = "Tebrikler, {} sayısını {}. tahmininizde buldunuz.\nYeni bir sayı tuttum. Hadi Tahmin Et!".format(self.sayi, self.tahminSayisi)
                self.sayi = self.sayiUret()
                self.tahminSayisi = 0
            elif girilen < 0 or girilen > 100:
                sonuc = "Girdiğiniz {} sayısı, 0 ile 100 arasında bir sayı değil!".format(girilen)
            elif self.sayi < girilen:
                sonuc = "Girdiğiniz {} sayısı aklımda tuttuğum sayıdan büyük!".format(girilen)               
            elif self.sayi > girilen:
                sonuc = "Girdiğiniz {} sayısı aklımda tuttuğum sayıdan küçük!".format(girilen) 

            self.label.configure(text=sonuc)
            self.entry.delete(0, tk.END)

        except ValueError:
            self.label.configure(text="Oyundan çıkış isteğiniz alındı.")
            self.root.after(2000, self.root.destroy)
        
    def baslat(self):
        self.root.mainloop()

if __name__ == "__main__":
    s = SayiTahminOyunu()
    s.baslat()
    print("Program Kapatılıyor. Bekleyiniz...")
    time.sleep(2)
