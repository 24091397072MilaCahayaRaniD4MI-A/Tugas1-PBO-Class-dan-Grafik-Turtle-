class DataPribadi:
    # Constructor (__init__)
    def __init__(self, nama, kelas, nim, jurusan, fakultas, kampus):
        self.nama = nama
        self.kelas = kelas
        self.nim = nim
        self.jurusan = jurusan
        self.fakultas = fakultas
        self.kampus = kampus

    # Method untuk menampilkan data pribadi
    def tampilkan_data(self):
        print("=== Data Pribadi Mahasiswa ===")
        print(f"Nama     : {self.nama}")
        print(f"Kelas    : {self.kelas}")
        print(f"NIM      : {self.nim}")
        print(f"Jurusan  : {self.jurusan}")
        print(f"Fakultas : {self.fakultas}")
        print(f"Kampus   : {self.kampus}")
        print(f"")

# Membuat object dari class DataPribadi
mahasiswa1 = DataPribadi(
    "Mila Cahaya Rani",
    "2024C",
    "24091397071",
    "Teknik Informatika",
    "Fakultas Teknik",
    "Universitas Airlangga"
)
mahasiswa2 = DataPribadi(
    "Nabila Maharani",
    "2024A",
    "24091397025",
    "Manajemen Bisnis",
    "Fakultas Ekonomi dan Bisiis",
    "Universitas Airlangga"
)
mahasiswa3 = DataPribadi(
    "Nuha Khasanah",
    "2024A",
    "24091397034",
    "Pendidikan Agama Islam",
    "Fakultas Keguruan dan Ilmu Pendidikan",
    "Universitas Airlangga"
)
mahasiswa4 = DataPribadi(
    "Zunika Kusuma",
    "2024C",
    "24091397078",
    "Akuntansi",
    "Fakultas Ekonomi dan Bisnis",
    "Universitas Airlangga"
)
mahasiswa5 = DataPribadi(
    "Elfina Prasetya",
    "2024B",
    "24091397052",
    "Hukum",
    "Fakultas Hukum",
    "Universitas Airlangga"
)

# Memanggil method untuk menampilkan data
mahasiswa1.tampilkan_data()
mahasiswa2.tampilkan_data()
mahasiswa3.tampilkan_data()
mahasiswa4.tampilkan_data()
mahasiswa5.tampilkan_data()
