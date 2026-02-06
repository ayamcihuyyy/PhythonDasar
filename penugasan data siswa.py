import tkinter as tk

def simpan():
    data = f"""
Nama Lengkap : {entry_nama.get()}
Tanggal Lahir : {entry_ttl.get()}
Asal Sekolah : {entry_asal.get()}
NISN : {entry_nisn.get()}
Nama Ayah : {entry_ayah.get()}
Nama Ibu : {entry_ibu.get()}
No HP : {entry_hp.get()}
Alamat : {text_alamat.get("1.0", tk.END)}
-------------------------
"""
    text_output.insert(tk.END, data)

def hapus():
    entry_nama.delete(0, tk.END)
    entry_ttl.delete(0, tk.END)
    entry_asal.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_hp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

root = tk.Tk()
root.title("Data Siswa Baru")

labels = [
    "Nama Lengkap", "Tanggal Lahir", "Asal Sekolah", "NISN",
    "Nama Ayah", "Nama Ibu", "Nomor Telepon / HP"
]

entries = []

for label in labels:
    tk.Label(root, text=label).pack()
    e = tk.Entry(root, width=40)
    e.pack()
    entries.append(e)

entry_nama, entry_ttl, entry_asal, entry_nisn, entry_ayah, entry_ibu, entry_hp = entries

tk.Label(root, text="Alamat").pack()
text_alamat = tk.Text(root, height=4, width=40)
text_alamat.pack()

tk.Button(root, text="Simpan", command=simpan).pack(pady=3)
tk.Button(root, text="Hapus", command=hapus).pack(pady=3)

text_output = tk.Text(root, height=10, width=50)
text_output.pack()

root.mainloop()