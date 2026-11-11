# Dokumentasi Kode — Starter Code

## Overview

Program ini adalah **template awal** untuk prototipe CLI (Command Line Interface) yang dibuat sebagai bagian dari proyek Digital Problem Framing Mini Project.

## Cara Menjalankan

```bash
python src/main.py
```

## Struktur Kode

```
main.py
├── KONFIGURASI        ← Pengaturan file data
├── FUNGSI-FUNGSI UTAMA
│   ├── clear_screen()        ← Membersihkan layar
│   ├── tampilkan_header()    ← Menampilkan header
│   ├── tampilkan_menu()      ← Menampilkan menu utama
│   ├── inisialisasi_file()   ← Membuat file CSV jika belum ada
│   ├── baca_data()           ← Membaca data dari CSV
│   └── simpan_data()         ← Menyimpan data ke CSV
├── MENU-MENU APLIKASI
│   ├── tambah_data()         ← Input data penjualan baru
│   ├── lihat_semua_data()    ← Tampilkan semua data
│   ├── lihat_total_hari_ini()← Hitung total hari ini
│   └── cari_item()           ← Cari item berdasarkan nama
└── PROGRAM UTAMA
    └── main()                ← Loop utama program
```

## Library yang Digunakan

| Library | Fungsi | Whitelist |
|---|---|---|
| `os` | Clear screen | ✅ |
| `csv` | Baca/tulis file CSV | ✅ |
| `datetime` | Ambil tanggal/waktu | ✅ |

## Modifikasi

Untuk menyesuaikan dengan masalah yang kalian temukan:

1. **Ganti konfigurasi** di bagian KONFIGURASI (nama file, kolom data)
2. **Tambah menu** baru di fungsi `tampilkan_menu()`
3. **Tambah fungsi** baru untuk setiap menu
4. **Uji setiap perubahan** sebelum menambah yang baru

## File Data

Program menyimpan data di file `data_penjualan.csv` dengan format:

```csv
tanggal,item,harga,jumlah
2026-09-11 10:30:00,Nasi Goreng,15000,2
2026-09-11 10:35:00,Es Teh,5000,3
```

## Yang Perlu Diubah

- [ ] Ganti `NAMA_FILE_DATA` sesuai kebutuhan
- [ ] Ganti `FIELDNAMES` sesuai kolom data yang diperlukan
- [ ] Tambah menu dan fungsi sesuai masalah yang diselesaikan
- [ ] Sesuaikan output dengan kebutuhan pemilik usaha
