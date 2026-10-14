"""
Digital Problem Framing Mini Project — Starter Code
===================================================
Program ini adalah template awal untuk prototipe CLI.
Ganti isi fungsi dan menu sesuai dengan masalah yang kalian temukan.

Petunjuk:
1. Jalankan: python src/main.py
2. Mulai dari menu paling sederhana, lalu tambah fitur bertahap
3. Selalu uji setiap fitur baru sebelum menambah yang lain
"""

import os
import csv
from datetime import datetime


# ============================================================
# KONFIGURASI
# ============================================================

NAMA_FILE_DATA = "data_penjualan.csv"  # File untuk menyimpan data
FIELDNAMES = ["tanggal", "item", "harga", "jumlah"]  # Kolom data


# ============================================================
# FUNGSI-FUNGSI UTAMA
# ============================================================

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def tampilkan_header(judul):
    """Menampilkan header yang rapi."""
    print("\n" + "=" * 50)
    print(f"  {judul}")
    print("=" * 50)


def tampilkan_menu():
    """Menampilkan menu utama."""
    tampilkan_header("MENU UTAMA")
    print("  1. Tambah Data Penjualan")
    print("  2. Lihat Semua Data")
    print("  3. Lihat Total Penjualan Hari Ini")
    print("  4. Cari Item")
    print("  0. Keluar")
    print("-" * 50)


def inisialisasi_file():
    """Membuat file CSV jika belum ada."""
    if not os.path.exists(NAMA_FILE_DATA):
        with open(NAMA_FILE_DATA, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
        print(f"[INFO] File {NAMA_FILE_DATA} berhasil dibuat.")


def baca_data():
    """Membaca semua data dari file CSV."""
    data = []
    if os.path.exists(NAMA_FILE_DATA):
        with open(NAMA_FILE_DATA, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    return data


def simpan_data(data_baru):
    """Menambahkan data baru ke file CSV."""
    with open(NAMA_FILE_DATA, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(data_baru)


# ============================================================
# MENU-MENU APLIKASI
# ============================================================

def tambah_data():
    """Menu untuk menambah data penjualan baru."""
    tampilkan_header("TAMBAH DATA PENJUALAN")

    item = input("Nama item: ").strip()
    if not item:
        print("[ERROR] Nama item tidak boleh kosong!")
        return

    try:
        harga = float(input("Harga per item (Rp): "))
        jumlah = int(input("Jumlah: "))
    except ValueError:
        print("[ERROR] Harga dan jumlah harus berupa angka!")
        return

    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data_baru = {
        "tanggal": tanggal,
        "item": item,
        "harga": str(harga),
        "jumlah": str(jumlah)
    }

    simpan_data(data_baru)
    print(f"\n[OK] Data '{item}' berhasil disimpan!")


def lihat_semua_data():
    """Menu untuk melihat semua data."""
    tampilkan_header("SEMUA DATA PENJUALAN")

    data = baca_data()

    if not data:
        print("[INFO] Belum ada data.")
        return

    print(f"{'No':<5} {'Tanggal':<20} {'Item':<20} {'Harga':<15} {'Jumlah':<8} {'Total':<15}")
    print("-" * 85)

    for i, row in enumerate(data, 1):
        harga = float(row['harga'])
        jumlah = int(row['jumlah'])
        total = harga * jumlah
        print(f"{i:<5} {row['tanggal']:<20} {row['item']:<20} Rp{harga:>10,.0f} {jumlah:>6} Rp{total:>10,.0f}")

    print("-" * 85)
    print(f"Total data: {len(data)} records")


def lihat_total_hari_ini():
    """Menu untuk melihat total penjualan hari ini."""
    tampilkan_header("TOTAL PENJUALAN HARI INI")

    data = baca_data()
    tanggal_hari_ini = datetime.now().strftime("%Y-%m-%d")

    total = 0
    count = 0

    for row in data:
        if row['tanggal'].startswith(tanggal_hari_ini):
            harga = float(row['harga'])
            jumlah = int(row['jumlah'])
            total += harga * jumlah
            count += 1

    print(f"Tanggal: {tanggal_hari_ini}")
    print(f"Jumlah transaksi: {count}")
    print(f"Total penjualan: Rp {total:,.0f}")

    if count == 0:
        print("[INFO] Belum ada penjualan hari ini.")


def cari_item():
    """Menu untuk mencari item."""
    tampilkan_header("CARI ITEM")

    keyword = input("Masukkan nama item yang dicari: ").strip().lower()

    if not keyword:
        print("[ERROR] Kata kunci tidak boleh kosong!")
        return

    data = baca_data()
    hasil = [row for row in data if keyword in row['item'].lower()]

    if not hasil:
        print(f"[INFO] Item '{keyword}' tidak ditemukan.")
        return

    print(f"\nHasil pencarian '{keyword}':")
    print(f"{'No':<5} {'Tanggal':<20} {'Item':<20} {'Harga':<15} {'Jumlah':<8}")
    print("-" * 70)

    for i, row in enumerate(hasil, 1):
        harga = float(row['harga'])
        print(f"{i:<5} {row['tanggal']:<20} {row['item']:<20} Rp{harga:>10,.0f} {row['jumlah']:>6}")

    print(f"\nDitemukan {len(hasil)} records.")


# ============================================================
# PROGRAM UTAMA
# ============================================================

def main():
    """Fungsi utama yang menjalankan program."""
    inisialisasi_file()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (0-4): ").strip()

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            lihat_semua_data()
        elif pilihan == "3":
            lihat_total_hari_ini()
        elif pilihan == "4":
            cari_item()
        elif pilihan == "0":
            print("\nTerima kasih! Sampai jumpa.")
            break
        else:
            print("[ERROR] Pilihan tidak valid!")

        input("\nTekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()
