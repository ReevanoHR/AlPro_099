class Employee:

    def __init__(
        self,
        nama_depan,
        nama_belakang,
        gaji
    ):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.gaji = gaji

    def give_raise(
        self,
        kenaikan=5000
    ):
        self.gaji += kenaikan