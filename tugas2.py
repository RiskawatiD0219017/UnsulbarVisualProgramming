class handphone:
    pass

hp1 = handphone()
hp2 = handphone ()
hp3 = handphone  ()

hp1.merek = 'Redmi'
hp1.jumlah = '5'

hp2.merek = 'Iphone'
hp2.jumlah = '10'

hp3.merek = 'Samsung'
hp3.jumlah = '20'

print(hp1.__dict__, hp2.__dict__, hp3.__dict__)
