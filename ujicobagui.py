from Tkinter import *
import ttk

judul_kolom = ( "Nama Lengkap", "Kota Asal", "Jurusan" )
data_mhs = [
    ('Vika Putri Ariyanti', 'Pekalongan', 'Teknik Informatika'),
    ('Aulia Salma Cahyarani', 'Depok', 'Teknik Informatika'),
    ('Zelin Ngilo', 'NTB', 'Sistem Informasi'),
    ('Haniyah', 'Depok', 'Sistem Informasi'),
    ('Fauzia Rahma Cahyarani', 'Depok', 'Teknik Informatika'),
    ('Novia Anggreani', 'Depok', 'Sistem Informasi'),
    ('Saidatul Arifah', 'Pekalongan', 'Teknik Informatika'),
    ('Laelatul Chasanah', 'Pekalongan', 'Ilmu Ekonomi Pembangunan'),
    ('Weningtyas Dwi Astuti', 'Pekalongan', 'Bahasa Inggris'),
    ('Sofiroh Febrianti', 'Pekalongan', 'Pendidikan Matematika'),
    ('Linda Kusuma Dewi', 'Pekalongan', 'Pendidikan Biologi'),
    ('Risma Fadhila', 'Pekalongan', 'Teknik Geodesi'),
    ('Lantip Adhi Hamdani', 'Pekalongan', 'Teknik Perkapalan'),
    ('Rexy Anggala Putra', 'Pekalongan', 'Matematika Murni'),
    ('Afzal  Arifiansyah', 'Jakarta', 'Teknik Informatika'),
    ('Yudha Romadhon', 'Bogor', 'Teknik Informatika'),
    ('Alvin Fadhila Yusuf', 'Depok', 'Teknik Informatika'),
    ('RR Dini Saptani Aprilia', 'Tanggerang', 'Teknik Informatika'),
    ('Farydatul Rohmana', 'Pati', 'Teknik Informatika'),
    ('Meithy Tri Andarini', 'Depok', 'Teknik Informatika')
    ]

class DemoTabelMHS:
    def __init__(self, induk, judul):
        self.induk = induk

        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.Tutup)
        self.induk.resizable(False, False)

        self.aturKomponen()
        self.isiTabel()

    def aturKomponen(self):
        mainFrame = Frame(self.induk)
        mainFrame.pack(fill=BOTH, expand=YES)

        fr_data = Frame(mainFrame, bd=10)
        fr_data.pack(fill=BOTH, expand=YES)

        self.trvTabel = ttk.Treeview(fr_data, columns=judul_kolom, show='headings')

        sbVer = Scrollbar(fr_data, orient='vertical', command=self.trvTabel.yview)
        sbHor = Scrollbar(fr_data, orient='horizontal', command=self.trvTabel.xview)

        sbVer.pack(side=RIGHT, fill=Y)
        sbHor.pack(side=BOTTOM, fill=X)
        self.trvTabel.pack(side=LEFT, fill=BOTH)

        lblStatus = Label(mainFrame, text='wwww.vikaputriariyanti.blogspot.co.id', bd=1, relief=SUNKEN)
        lblStatus.pack(side=BOTTOM, fill=X)

    def isiTabel(self):

        for kolom in judul_kolom:
            self.trvTabel.heading(kolom, text=kolom)

        for dat in data_mhs:
            self.trvTabel.insert('', 'end', values=dat)

    def Tutup(self, event=None):
        self.induk.destroy()

if __name__ == '__main__':
    root = Tk()

    app = DemoTabelMHS(root, ":: Demo Tabel Mahasiswa ::")

    root.mainloop()
