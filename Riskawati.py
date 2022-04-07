# class
class mahasiswa():

    __nilai = 0 # private

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim  # public

    def uts(self,input_nilai):
        self.__nilai += input_nilai

    def uas(self,input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,'Tidak Lulus')
        else:
            print(self.nama, 'Lulus')

# main programnya

riska = mahasiswa("Riska dinyatakan   :", 219008)
bilman = mahasiswa("Bilman dinyatakan :", 13317002)

riska.uts(10)
riska.uas(50)
riska.check_status()
bilman.uts(5)
bilman.uas(25)
bilman.__nilai = 60
bilman.check_status()
