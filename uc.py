from bir import A
from iki import B
import sys

class C(B, A):

    on = int
    bir = int

    def __init__(self):
        pass

    def korGir(self):
        print("")
        kor = int(input("sayi gir:")) # iki basamak sart ve !, ? dahil et
        if kor < 0 or kor > 89:
            print("Bu sayilar olmaz, yeniden dene")
            return self.korGir()
        else:
            self.korAc(kor)

    def korAc(self, num):
        self.on = num // 10
        self.bir = num % 10

    def korCheck(self):
        if [self.on, self.bir] in super().mayin:
            print("Boooom!")
            return False
        else:
            self.bolgeCheck()
            return True
        
    def bolgeCheck(self):
        if [self.on, self.bir] in super().mayinKomsu:
            super().mayinSayi(self.on, self.bir)
        else:
            super().alanAc(self.on, self.bir)

deger = True

if __name__ == "__main__":
    print("Mayin Oyununa hos geldin")
    obj = A()
    obj2 = B()
    obj3 = C()

    obj2.printMayin()

    while deger:
        obj3.korGir()
        deger = obj3.korCheck()
        obj.printBoard()