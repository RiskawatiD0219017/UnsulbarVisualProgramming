class handphone:
    def __init__(self, inputmerek, inputjumlah, inputharga):
        
        self.merek = inputmerek
        self.jumlah = inputjumlah
        self.harga = inputharga


hp1 = handphone("Iphone",10, 2000000)
hp2 = handphone("Samsung",15, 3000000)

print (hp1.harga)
