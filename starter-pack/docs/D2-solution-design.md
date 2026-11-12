# D2 — System & Solution Design

**Project**: Digital Problem Framing Mini Project — Laundry Que
**Tim**: Arselly Tri Kurniasari, Atiqah Subandono, Davina Walasyah, Lailatul Fitriyah, Zaskia Azwa Mutmainah | **Tanggal**: [11/11/2026] | **Versi**: [v1.0]
**Template**: TPL-02

> **Petunjuk**: Hapus teks dalam `[...]` setelah diisi.
> Worksheet terkait: WS05, WS06, WS07

---

## 1. Daftar Kebutuhan (User Story)

| # | User Story | Prioritas |
|---|---|---|
| 1 | Sebagai Karyawan/kasir Laundry Que, saya ingin Setelah membayar, Google Sheet secara otomatis mengirimkan chat struk belanjaan dan link member secara bersamaan ke nomor WhatsApp pelanggan. sehingga Tidak perlu menyalin nomor dan mengirimkan struk secara manual satu persatu menggunakan pesan pribadi dengan aplikasi WhatsApp. | Tinggi |
| 2 | Sebagai Karyawan/kasir Laundry Que, saya ingin Mengirim Google Sheet untuk meminta pengisian ulang bahan baku (air, gas, sabun, pewangi, dll) kepada admin, sehingga Pengajuan restock teratur dan tidak lagi bergantung pada chat pribadi WhatsApp.| Sedang |
| 3 | Sebagai Karyawan/kasir Laundry Que, saya ingin Ketik tabung mesin cuci kosong Google Sheet akan mengirim notifikasi status tabung mesin cuci kepada pelanggan, apakah tabung sudah kosong atau belum secara otomatis, sehingga Memangkas waktu tunggu dan tidak membuat laundry penuh dengan antrian manusia ataupun antrian baju yang menumpuk. | Rendah |

## 2. Kriteria Penerimaan

| # | Kriteria Penerimaan (terukur & dapat diuji) |
|---|---|
| 1 | Sistem berhasil berhasil menghitung total pembayaran berdasarkan jenis layanan dan jumlah tabung yang dipilih pelanggan |
| 2 | Sistem berhasil menyimpan data transaksi ke Google Sheets dan mengirimkan nota otomatis ke WhatsAap pelannggan.|
| 3 | Sistem menampilkan pesan kesalahan jika nama, no telpon, jumlah tabung, jenis layanan, atau harga tidak valid. |

## 3. Success Metrics

| Metrik | Baseline (Sekarang) | Target | Cara Mengukur |
|---|---|---|---|
| Durasi pelayanan transaksi per pelanggan | 30 - 60 | 20 | Stopwatch sampel 3-5 |
| Durasi rekapitulasi harian pemilik | 20 menit / malam akhir shift | 10 menit / malam akhir shift | Wawancara & Uji Coba Langsung |
| Tingkat selisih pencatatan stok barang | 16 % selisih / 1-2 kali perbulan |0 % selisih / bulan | Stock opname bulanan|
|Frekuensi kesalahan hitung nota | 40 kali dalam jam sibuk | 0 kali | Audit sampel chat nota|

## 4. Desain Solusi

### 4.1 Konsep Solusi (ringkasan)
Membangun sistem pengiriman permintaan restock otomatis menggunakan Google Sheets untuk mengelola nama barang yang butuh di restock dan WhatsApp untuk mengirimkan data tetsebut  kepada admin sehingga proses pengajuan restock barang menjadi lebih cepat, praktis, dan mengurangi pekerjaan manual kasir.


### 4.2 Peta Komponen (IPO)

```
Input  ──▶  Proses  ──▶  Output
  │                           │
  └───── Data/Penyimpanan ────┘
```


- **Input**:Nama barang yang ingin di-restock. Jumlah stok yang tersedia. Jumlah barang yang dibutuhkan. Nama kasir. Tanggal permintaan.  Perkiraan biaya pembelian.
- **Proses**:Kasir memeriksa stok barang yang tersedia. Kasir mengajukan permintaan restock kepada admin. Sistem mencatat barang dan jumlah yang dibutuhkan. Admin memberikan uang untuk pembelian barang. Kasir membeli barang dan memperbarui jumlah stok 
- **Output**:Nama barang yang di-restock.  Jumlah barang yang dibeli. Total biaya pembelian. Nama kasir yang mengajukan. Status permintaan (Menunggu, Diproses, Selesai). 
- **Data/Penyimpanan**:Nama barang yang di-restock.  Jumlah barang yang dibeli. Total biaya pembelian. Nama kasir yang mengajukan. Status permintaan (Menunggu, Diproses, Selesai).



### 4.3 Flowchart & Pseudocode

_[Tempel flowchart di `assets/` dan tulis pseudocode di bawah]_

```
[PSEUDOCODE]
ALGORITMA Pengiriman_pesan_Restock_Barang_Otomatis
KAMUS DATA: 
Nama_barang,nama_karyawan:STRING
Jumlah_barang,tanggal:INTEGER

ALUR LOGIKA:
   MULAI

INPUT stok_barang 

IF stok_barang 5>= THEN
   OUTPUT “Catat tanggal dan stock barang”
ELSE
   INPUT nama_kasir,tanggal,nama_barang KE google_sheet

   KIRIM_PESAN “Permintaan restock” KE Admin VIA WhatsApp

   TERIMA_PESAN “Permintaan dari kasir” OLEH Admin
   SETUJUI_PERMINTAAN Oleh Admin
   SERAHKAN_UANG(Admin ke Kasir)

   BELI_BARANG_RESTOCK OLEH Kasir
ENDIF

SELESAI

   

  

## 5. Hasil Validasi Pemilik Usaha

- **Tanggal validasi**: [DD/MM/YYYY]
- **Feedback pemilik**: [...]
- **Perubahan setelah validasi**: [...]

---

**Status**: ⬜ Draf → ⬜ Review Tim → ⬜ Validasi Pemilik → ⬜ Final (GATE 1)