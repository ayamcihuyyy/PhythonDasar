import tkinter as tk

def hitung_total():
    try:
        harga = int(entry_harga.get())
        qty = int(entry_qty.get())
        total = harga * qty
        label_total.config(text=f"Total: Rp. {total}")
    except:
        label_total.config(text="Input tidak valid")

root = tk.Tk()
root.title("Program Kasir")

tk.Label(root, text="Harga").pack()
entry_harga = tk.Entry(root)
entry_harga.pack()

tk.Label(root, text="Kuantitas").pack()
entry_qty = tk.Entry(root)
entry_qty.pack()

tk.Button(root, text="Hitung Total", command=hitung_total).pack(pady=5)

label_total = tk.Label(root, text="Total: Rp. 0")
label_total.pack()

root.mainloop()