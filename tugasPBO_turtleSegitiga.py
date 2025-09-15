import turtle

class MyTurtle:
    def __init__(self, color, shape):
        self.t = turtle.Turtle()  # object turtle
        self.t.color(color)
        self.t.shape(shape)

    def maju(self, jarak):
        # Method untuk menggerakkan turtle maju
        self.t.forward(jarak)    

    def putar_kiri(self, sudut):
        # Method untuk memutar turtle ke kiri
        self.t.left(sudut)
    def gambar(self, ukuran):
        # Method untuk menggambar segitiga
        for _ in range(3):
            self.maju(ukuran)
            self.putar_kiri(120)

    def selesai(self):
        # Method untuk menyelesaikan gambar
        turtle.done()

# Membuat objek turtle dengan warna dan bentuk
turtle1 = MyTurtle("black", "turtle")

# Menggambar segitiga dengan ukuran sisi 150
turtle1.gambar(150)

# Menyelesaikan gambar
turtle1.selesai()

