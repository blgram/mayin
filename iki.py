import random 
from bir import A

class B(A):

    mayin = []
    mayinKomsu = []
    bosluk = []
    sayi = 0 # mayin adeti
    sira = int
    sutun = int
    
    def __init__(self):
        self.mayinEkle()
        self.mayinKm()
        self.bosAlan()

    def mayinEkle(self):
        self.sira = random.randrange(0, 9)
        self.sutun = random.randrange(0, 9)

        while self.sayi < 10:
            if [self.sira, self.sutun] not in self.mayin:
                self.mayin.append([self.sira, self.sutun])
                self.sayi += 1
                return self.mayinEkle()
            else:
                return self.mayinEkle()

    def mayinKm(self):
        for eleman in self.mayin:
            self.function2(eleman)

    def function2(self, lst):
        a = lst[0] - 1
        b = lst[1] - 1

        for i in range(3):
            for j in range(3):
                self.function3(i+a, j+b)

    def function3(self, num1, num2): #mayinKomsu []
        if num1 == -1 or num1 == 9 or num2 == -1 or num2 == 9:
            pass
        elif [num1, num2] in self.mayin or [num1, num2] in self.mayinKomsu:
            pass
        else:
            self.mayinKomsu.append([num1, num2])

    def bosAlan(self): # bosluk []
        for i in range(super().height):
            for j in range(super().width):
                if [i, j] not in self.mayin and [i, j] not in self.mayinKomsu:
                    self.bosluk.append([i, j])
    
    def mayinSayi(self, arg1, arg2): #bunu Ubuntuda test et.
        sayimiz = 0

        a = arg1 - 1
        b = arg2 - 1

        for i in range(3):
            for j in range(3):
                if i+a > 8 or j+b > 8 or i+a < 0 or i+a < 0:
                    pass
                else:
                    if [i+a, j+b] in self.mayin:
                        sayimiz += 1

        super().sayiKoy(arg1, arg2, sayimiz)

    def alanAc(self, arg1, arg2):

        self.bosluk.remove([arg1, arg2])
        super().xKoy(arg1, arg2)
        self.yukari(arg1, arg2)
        self.asagi(arg1, arg2)
        self.sol(arg1, arg2)
        self.sag(arg1,arg2)

        self.sayiVer()
    

    def yukari(self, arg1, arg2):

        if [arg1-1, arg2] in self.bosluk:
            self.alanAc(arg1-1, arg2)

    def asagi(self, arg1, arg2):
        
        if [arg1+1, arg2] in self.bosluk:
            self.alanAc(arg1+1,arg2)

    def sol(self, arg1, arg2):

        if [arg1, arg2-1] in self.bosluk:
            self.alanAc(arg1, arg2-1)

    def sag(self, arg1, arg2):

        if [arg1, arg2+1] in self.bosluk:
            self.alanAc(arg1, arg2+1)

    def sayiVer(self):
        for i in range(super().height):
            for j in range(super().width):
                if super().board[i][j] == 'x':
                    self.etraf(i, j)

    def etraf(self, num1, num2):
        a = num1 - 1
        b = num2 - 1

        for i in range(3):
            for j in range(3):
                if i+a > 8 or j+b > 8 or i+a < 0 or i+a < 0:
                    pass
                else:
                    if [i+a, j+b] in self.mayinKomsu:
                        self.mayinKomsu.remove([i+a, j+b])
                        self.mayinSayi(i+a, j+b)
                

    def printMayinKomsu(self):
        print("Komsu:", self.mayinKomsu)

    def printMayin(self):
        print("Mayin:", self.mayin)

    def printBosluk(self):
        print("bosluk:", self.bosluk)
