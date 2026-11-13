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
* **Nama Tim:** Tim Bugenvil
* **Nama UMKM Mitra:** Laundry Que
* **Judul Solusi SI:** Pengiriman Nota Pelanggan Otomatis 
* **Phase Lead 4 (Design):** Lailatul Fitriyah

---

#### 2. PEMETAAN ARSITEKTUR 4 LAPISAN SI (M05)
Petakan solusi Anda ke dalam 4 lapisan arsitektur terintegrasi:

| Lapisan Arsitektur | Komponen Solusi Tim | Keterangan & Batasan |
| :--- | :--- | :--- |
| **1. Process Layer** *(Alur Kerja To-Be)* | 1.Kasir memasukkan data transaksi pelanggan ke Google Sheets. 2.Sistem menghitung total pembayaran secara otomatis. 3.Kasir membuat dan mengirim nota kepada pelanggan melalui WhatsApp| Alur transaksi kasir To-Be lebih efisien dibandingkan As-Is karena mengurangi pencatatan manual. |
| **2. Data Layer** *(Struktur Data Logis)* | 1. Tabel Data Pelanggan. 2. Tabel Transaksi. 3. Tabel Nota Pembayaran. | Entitas data disimpan dalam Google Sheets dan saling berkaitan sesuai kebutuhan operasional Laundry Que. |
| **3. Application Layer** *(Modul Program)* | 1. Google Sheets sebagai aplikasi utama. 2. Form input transaksi. 3. Rumus otomatis untuk menghitung total pembayaran. 4. Template nota pembayaran. | Modul utama: Input transaksi, hitung total/diskon, pembuatan nota |
| **4. Infrastructure Layer** *(Perangkat Fisik)* |1. Laptop atau komputer kasir. 2. Smartphone karyawan. 3. Koneksi internet Wi-Fi atau data seluler. 4. Google Chrome. 5. Sistem operasi Windows atau Android. | Hardware: Smartphone POS; Net: Wi-Fi/4G; OS: Windows/Android. |

---

#### 3. SPESIFIKASI IPO (INPUT - PROCESSING - OUTPUT - STORAGE - CONTROL)
* **Fitur Fungsional Utama:** Pemberitahuan otomatis restock barang

* **Input:**
  * Nama pelanggan
  * no.telpon pelanggan
  * jumlah tabung yang di pakai
  * jenis layanan: * cuci dan kering : Rp20000
                   * cuci : Rp10000
                   * keringkan : Rp10000
  * metode pembayaran : * Qris
                        * Cash
  
* **Processing:**
1.Kasir memasukkan nama dan nomor telepon pelanggan.
2.Sistem memeriksa data pelanggan di database.
3.Jika pelanggan baru, sistem memasukkan data pelanggan ke database.
4.Jika pelanggan lama, sistem menggunakan data yang sudah tersedia.
5.Kasir memilih jenis layanan laundry.
6.Sistem menentukan harga berdasarkan layanan yang dipilih.
7.Kasir memilih metode pembayaran (Cash atau QRIS).
8.Kasir mengonfirmasi apakah pembayaran sudah diterima.
9.Jika pembayaran sudah lunas, sistem membuat nota.
10.Sistem mengirimkan nota melalui WhatsApp pelanggan.

* **Output:**
  * Informasi nama pelanggan
  * Nomor telpon pelanggan
  * Jenis layanan yang di pilih
  * Metode pembayaran
  * Status pembayaran (lunas atau belum lunas)
  * Nota teransaksi yang dikirim otomatis melalui WhatsApp pelanggan.

* **Storage:**
  * Menyimpan data pelanggan , jenis layanan, dan pembayaran di Google Sheets.

* **Control (Error Handling):**
  * memastikan nama pelanggan den nomor telpon tidak kosong
  * membastikan nomor telpon di isi dengan format yang benar
  * memastikan jumlah tabung yang di gunakan lebih dari 0
  * memastikan jumlah layanan sudah dipilih
  * sistem menghitung ulang total pembayaran berdasarkan jumlah tabung dan harga layanan,

---

#### 4. DIAGRAM ALIR (FLOWCHART) LOGIKA PROGRAM
*Petunjuk: Gambarkan diagram alir terstruktur menggunakan simbol standar (Persegi Panjang = Proses, Belah Ketupat = Keputusan IF-ELSE, Jajar Genjang = Input/Output, Oval = Start/End).*

![Diagram Flowchart Restock Otomatis]([image](https://github.com/2600016002-alt/PBL-2026-LaundryQue/blob/569dd4e4137bef62661fee9705d41113eab2e136/starter-pack/assets/flowchart%20pengiriman%20nota%20laundry%20otomatis.png)

---

#### 5. PSEUDOCODE TERSTRUKTUR (INDEPENDEN TEKNOLOGI)
Tuliskan kode semu terstruktur (pseudocode) untuk modul logika utama solusi Anda:

text
```
ALGORITMA Pengiriman_Nota_Laundry_Que

KAMUS BAHASA
    nama            : STRING
    no_telepon      : STRING
    pelanggan       : STRING
    layanan         : STRING
    pembayaran      : STRING
    harga           : INTEGER
    status_lunas    : BOOLEAN

ALUR LOGIKA:
  MULAI
  INPUT nama, no_telepon

CEK DATABASE PELANGGAN

  IF pelanggan ditemukan THEN
    OUTPUT "Pelanggan lama"

  ELSE
    MASUKKAN nama, no_telepon
    MASUKKAN DATA KE DATABASE
    
ENDIF

  OUTPUT "Pilih jenis layanan"
  OUTPUT "1. Cuci kering Rp20.000"
  OUTPUT "2. Cuci Rp10.000"
  OUTPUT "3. Kering Rp10.000"

INPUT layanan

IF layanan = 1 THEN
    harga = 20000
ELIF layanan = 2 THEN
    harga = 10000
ELIF layanan = 3 THEN
    harga = 10000
ELSE
    OUTPUT "Pilihan layanan tidak tersedia"
ENDIF

OUTPUT "Pilih pembayaran"
OUTPUT "1. Cash"
OUTPUT "2. QRIS"

INPUT pembayaran

IF pembayaran = "Cash" THEN
    OUTPUT " KonfirmasiPembayaran Cash"
    
ELIF pembayaran = "QRIS" THEN
    OUTPUT "Konfirmasi pembayaran QRIS"
    status_lunas = TRUE
ENDIF

OUTPUT "Lunas"
BUAT NOTA
KIRIM NOTA KE WHATSAPP

SELESAI


---

### CHECKLIST REFLEKSI & PENGESAHAN WS07

- [x] Arsitektur 4 lapisan SI telah terdefinisi konsisten.
- [x] Tabel IPO mencakup kriteria Storage dan Control (penanganan eror).
- [x] Flowchart menggambarkan logika percabangan (IF-ELSE) dan perulangan (Loops) tanpa infinite loop.
- [x] Pseudocode terstruktur dengan rapi dan independen terhadap bahasa pemrograman.
- [x] Form TPL-07 (AI Usage Disclosure & Verification Note) telah dilampirkan.

**Tanggal Pengesahan:** 11/11/2026  
**Tanda Tangan Phase Lead 4 (Design):** *[image](https://github.com/2600016002-alt/PBL-2026-LaundryQue/blob/main/starter-pack/assets/ttd%20laila.png)*  
**Tanda Tangan Dosen Pembimbing / Coach:** ____________________
