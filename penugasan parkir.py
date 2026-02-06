import tkinter as tk

BIAYA_PER_JAM = 2000

def hitung_biaya():
    try:
        masuk = int(entry_masuk.get())
        keluar = int(entry_keluar.get())
        lama = keluar - masuk
        if lama < 0:
            label_biaya.config(text="Jam tidak valid")
        else:
            total = lama * BIAYA_PER_JAM
            label_biaya.config(text=f"Biaya: Rp. {total}")
    except:
        label_biaya.config(text="Input salah")

root = tk.Tk()
root.title("Program Parkir")

tk.Label(root, text="Jam Masuk").pack()
entry_masuk = tk.Entry(root)
entry_masuk.pack()

tk.Label(root, text="Jam Keluar").pack()
entry_keluar = tk.Entry(root)
entry_keluar.pack()

tk.Button(root, text="Hitung Biaya", command=hitung_biaya).pack(pady=5)

label_biaya = tk.Label(root, text="Biaya: Rp. 0")
label_biaya.pack()

root.mainloop()