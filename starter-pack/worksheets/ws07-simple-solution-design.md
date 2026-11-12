# WORKBOOK: LEMBAR KERJA MAHASISWA (WS07)
## Simple Solution Design — IPO, Flowchart & Pseudocode

### INFORMASI UTAMA
* **Mata Kuliah:** Konsep Sistem Informasi (KSI)
* **Kerangka Kerja:** Project-Based Learning (PBL) Level 1
* **Learning Moment:** Fase 4: Design (Minggu 5–6)
* **Sub-CPMK / SFIA:** S-03.1 (Intermediate) | SFIA ARCH L2, DESN L2
* **Keterkaitan Deliverable:** Sumber utama pembuatan Deliverable D2 (System & Solution Design - TPL-02)
* **Phase Lead:** Mahasiswa D (Phase Lead 4 — Design)

---

### RUANG KERJA TIM (WORKSPACE)

#### 1. IDENTIFIKASI KELOMPOK & SOLUSI
* **Nama Tim:** Lailatul Fitriyah
* **Nama UMKM Mitra:** Laundry Que
* **Judul Solusi SI:** Mengirimkan pesan otomatis pengajuan restock
* **Phase Lead 4 (Design):** Lailatul Fitriyah

---

#### 2. PEMETAAN ARSITEKTUR 4 LAPISAN SI (M05)
Petakan solusi Anda ke dalam 4 lapisan arsitektur terintegrasi:

| Lapisan Arsitektur | Komponen Solusi Tim | Keterangan & Batasan |
| :--- | :--- | :--- |
| **1. Process Layer** *(Alur Kerja To-Be)* | Kasir mengisi permintaan restock melalui tabel stock. | Restock barang, To-Be yang lebih efisien dibanding As-Is. |
| **2. Data Layer** *(Struktur Data Logis)* | 1. Tabel Stok Barang.<br>2. Tabel Permintaan Restock. | Entitas data: tabel restock. |
| **3. Application Layer** *(Modul Program)* | 1. Google Sheets sebagai aplikasi utama.<br>2. Form input nama barang.<br>3. Rumus otomatis untuk menghitung total pembayaran.<br>4. Form pencatatan restock. | Modul Utama: Login, pencatatan restock. |
| **4. Infrastructure Layer** *(Perangkat Fisik)* | 1. Smartphone yang telah disediakan oleh Laundry.<br>2. Koneksi Wi-Fi atau data seluler.<br>3. WhatsApp. | Hardware: Smartphone POS; Net: Wi-Fi/4G; OS: Windows/Android. |

---

#### 3. SPESIFIKASI IPO (INPUT - PROCESSING - OUTPUT - STORAGE - CONTROL)
* **Fitur Fungsional Utama:** Pemberitahuan otomatis restock barang

* **Input:**
  * Nama barang yang ingin di-restock
  * Jumlah stok yang tersedia
  * Jumlah barang yang dibutuhkan
  * Nama kasir
  * Tanggal permintaan
  * Perkiraan biaya pembelian

* **Processing:**
  1. Kasir memeriksa stok barang yang tersedia.
  2. Kasir mengajukan permintaan restock kepada admin.
  3. Sistem mencatat barang dan jumlah yang dibutuhkan.
  4. Admin memberikan uang untuk pembelian barang.
  5. Kasir membeli barang dan memperbarui jumlah stok.

* **Output:**
  * Nama barang yang di-restock
  * Jumlah barang yang dibeli
  * Total biaya pembelian
  * Nama kasir yang mengajukan
  * Status permintaan (Menunggu, Diproses, Selesai)

* **Storage:**
  * Menyimpan nama barang di Google Sheets, seperti: nama barang yang mau di-restock, jumlah barang yang akan dibeli, nama kasir yang mengajukan, tanggal permintaan, status permintaan.

* **Control (Error Handling):**
  * Memasukkan nama barang.
  * Memasukkan jumlah barang harus berupa angka lebih dari 0.
  * Memasukkan total biaya harus berupa angka.
  * Sistem memeriksa kelengkapan data sebelum permintaan dikirim.
  * Sistem memberikan pemberitahuan jika permintaan berhasil dicatat.

---

#### 4. DIAGRAM ALIR (FLOWCHART) LOGIKA PROGRAM
*Petunjuk: Gambarkan diagram alir terstruktur menggunakan simbol standar (Persegi Panjang = Proses, Belah Ketupat = Keputusan IF-ELSE, Jajar Genjang = Input/Output, Oval = Start/End).*

![Diagram Flowchart Restock Otomatis](image.png)

---

#### 5. PSEUDOCODE TERSTRUKTUR (INDEPENDEN TEKNOLOGI)
Tuliskan kode semu terstruktur (pseudocode) untuk modul logika utama solusi Anda:

```text
ALGORITMA Pengiriman_pesan_Restock_Barang_Otomatis

KAMUS DATA: 
   Nama_barang, nama_karyawan : STRING
   Jumlah_barang, tanggal     : INTEGER

ALUR LOGIKA:
   MULAI
   INPUT stok_barang 
   IF stok_barang >= 5 THEN
       OUTPUT “Catat tanggal dan stock barang”
   ELSE
       INPUT nama_kasir, tanggal, nama_barang KE google_sheet
       KIRIM_PESAN “Permintaan restock” KE Admin VIA WhatsApp
       TERIMA_PESAN “Permintaan dari kasir” OLEH Admin
       SETUJUI_PERMINTAAN Oleh Admin
       SERAHKAN_UANG(Admin ke Kasir)
       BELI_BARANG_RESTOCK OLEH Kasir
   ENDIF
   SELESAI
```

---

### CHECKLIST REFLEKSI & PENGESAHAN WS07

- [x] Arsitektur 4 lapisan SI telah terdefinisi konsisten.
- [x] Tabel IPO mencakup kriteria Storage dan Control (penanganan eror).
- [x] Flowchart menggambarkan logika percabangan (IF-ELSE) dan perulangan (Loops) tanpa infinite loop.
- [x] Pseudocode terstruktur dengan rapi dan independen terhadap bahasa pemrograman.
- [x] Form TPL-07 (AI Usage Disclosure & Verification Note) telah dilampirkan.

**Tanggal Pengesahan:** 11/11/2026  
**Tanda Tangan Phase Lead 4 (Design):** *(Disertakan gambar/tanda tangan)*  
**Tanda Tangan Dosen Pembimbing / Coach:** ____________________