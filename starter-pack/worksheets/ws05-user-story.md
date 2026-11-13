# **WORKBOOK: LEMBAR KERJA MAHASISWA WS05**

## **Formulasi Kebutuhan Fungsional: User Story & Acceptance Criteria**

Mata Kuliah: **Konsep Sistem Informasi (KSI)**  
Kerangka Kerja: **Project-Based Learning (PBL) Level 1**  
Fase Learning Spine: **Fase 3 — Define (Minggu 3\)**  
Sub-CPMK / SFIA: **S-01.1 (Intermediate \- Problem Framing) & S-03.1 (Intermediate \- Pemetaan SI)** \| **SFIA BUSA L1, REQM L2**  
Keterkaitan Deliverable: **Bahan Utama Deliverable D2 (System & Solution Design \- TPL-02)**

---

### **1\. Identifikasi Kelompok & Rotasi Kepemimpinan**

* **Nama Kelompok**: Bugenvil  
* **Objek UMKM Mitra**: Laundry Que  
* **Phase Lead 3 (Define)**: Atiqah Subandono 2600016026 (Mahasiswa C)  
* **Anggota Tim**:  
1. Lailatul Fitriyah 2600016001  
2. Davina Walasyah 2600016002  
3. Zaskia Azwa Mutmainah 2600016018  
4. Arselly Tri Kurniasari 2600016043

---

### **2\. Landasan Konseptual: Analisis Sistem "What" vs "How"**

Dalam tahap *Systems Analysis*, fokus utama tim adalah menentukan **APA (*What*)** yang dibutuhkan pengguna bisnis untuk memecahkan masalahnya, **BUKAN BAGAIMANA (*How*)** sistem dibangun secara teknis (Marakas & O'Brien, 2013).

* **User Story** merepresentasikan kebutuhan fungsional dari sudut pandang pengguna bisnis dengan pola:  
  Sebagai Karyawan Laundry Que, Saya ingin Google Sheet yang mengirimkan notifikasi, chat, serta laporan otomatis, Sehingga dapat memangkas waktu dan lebih efisien"}\$\$  
* **Acceptance Criteria (Given-When-Then)** mendefinisikan batas kondisi kapan sebuah fitur dinyatakan selesai dan memenuhi syarat penerimaan pengguna (Rainer et al., 2021).

---

### **3\. Workspace A: Formulasi User Story Fungsional**

Petakan minimal **3 User Story Utama** yang langsung menjawab akar masalah pada D1 / WS04:

#### **User Story 1 (Fitur Nota Kasir / Input)**

* **Sebagai (*As a*)**:  
  Pelanggan Laundry Que  
* **Saya ingin (*I want to*)**:  
  Setelah membayar, WhatsApp API secara otomatis mengirimkan chat struk belanjaan ke nomor WhatsApp pelanggan.  
* **Sehingga (*So that*)**:  
  Tidak perlu meminta struk terlebih dahulu kepada karyawan, setelah transaksi berhasil nota otomatis terkirim.

#### **User Story 2 (Fitur Manajemen Stok / Data)**

* **Sebagai (*As a*)**:  
  Karyawan/kasir Laundry Que  
* **Saya ingin (*I want to*)**:  
  Mengirim Google Sheet untuk meminta pengisian ulang bahan baku (air, gas, sabun, pewangi, dll) kepada admin.  
* **Sehingga (*So that*)**:  
  Pengajuan restock teratur dan tidak lagi bergantung pada chat pribadi WhatsApp.

#### **User Story 3 (Fitur Pelaporan / Informasi)**

* **Sebagai (*As a*)**:  
  Karyawan/kasir Laundry Que  
* **Saya ingin (*I want to*)**:  
  Ketik tabung mesin cuci kosong WhatsApp API akan mengirim notifikasi status tabung mesin cuci kepada pelanggan, apakah tabung sudah kosong atau belum secara otomatis.  
* **Sehingga (*So that*)**:  
  Memangkas waktu tunggu dan tidak membuat laundry penuh dengan antrian manusia ataupun antrian baju yang menumpuk.

---

### **4\. Workspace B: Acceptance Criteria Berbasis Skenario (Given-When-Then)**

Susun kriteria penerimaan terstruktur untuk **User Story 1** (mencakup Skenario Sukses dan Skenario Penanganan Error):

#### **Skenario 1A: Transaksi Penjualan Berhasil (Happy Path)**

* **Diberikan (*Given*)**:  
  Pelanggan datang membawa baju lalu kasir memasukkan data pelanggan ke Google Sheet lalu diproses oleh Google Apps Script. Setelah itu WhatsApp API akan mengirimkan pesan nota secara otomatis ke nomor pelanggan.  
* **Ketika (*When*)**:  
  Setelah pembayaran masuk dan transaksi berhasil disimpan.  
* **Maka (*Then*)**:  
  WhatsApp API mengirim notifikasi pesan otomatis ke nomor WhatsApp pelanggan berisi nota pembayaran.

#### **Skenario 1B: Nomor WhatsApp Tidak Valid / Salah Input (Exception Path)**

* **Diberikan (*Given*)**:  
  Kasir mengkonfirmasi transaksi pembayaran pelanggan, namun nomor WhatsApp yang dimasukkan salah atau tidak terdaftar di WhatsApp.  
* **Ketika (*When*)**:  
  Transaksi berhasil disimpan dan sistem mencoba mengirimkan notifikasi.  
* **Maka (*Then*)**:  
  Sistem menampilkan peringatan *"Gagal mengirim pesan: Nomor WhatsApp tidak valid"* dan menyediakan tombol untuk memperbarui nomor pelanggan.

#### **Skenario 2A: Laporan Restock Berhasil (Happy Path)**

* **Diberikan (*Given*)**:  
  Kasir yang berjaga pada shift terakhir (shift 3\) berkeliling memeriksa barang apa saja yang habis dan mengirim permintaan restock dalam sistem.  
* **Ketika (*When*)**:  
  Pengajuan masuk ke dalam sistem memberikan data kepada admin apa saja yang perlu di restock.  
* **Maka (*Then*)**:  
  Admin menerima notifikasi laporan pengajuan restock pada sistem.

#### **Skenario 2B: Formulir Restock Kosong / Belum Memilih Barang (Exception Path)**

* **Diberikan (*Given*)**:  
  Kasir shift 3 membuka menu pengajuan restock di dalam sistem.  
* **Ketika (*When*)**:  
  Kasir menekan tombol "Kirim Pengajuan" tanpa memilih bahan baku yang habis.  
* **Maka (*Then*)**:  
  Sistem menolak pengajuan dan menampilkan pesan error *"Pilih minimal satu bahan baku dan isi jumlah yang diperlukan sebelum mengirim"*

#### **Skenario 3A: Google Sheet Berhasil Mengirimkan Notifikasi (Happy Path)**

* **Diberikan (*Given*)**:  
  Karyawan/kasir mengetahui bahwa salah satu tabung mesin cuci telah selesai digunakan dan sudah kosong.  
* **Ketika (*When*)**:  
  Karyawan/kasir mengetik perintah “tabung mesin cuci kosong” melalui Google Sheet.  
* **Maka (*Then*)**:  
  WhatsApp API secara otomatis mengirimkan notifikasi pada WhatsApp pelanggan bahwa mesin cuci sudah dapat digunakan. Pelanggan dapat langsung menggunakan mesin tanpa harus menunggu atau bertanya kepada karyawan.

#### **Skenario 3B: Koneksi Internet Terputus Saat Memuat Menu (Exception Path)**

* **Diberikan (*Given*)**:  
  Kasir ingin memperbarui status tabung mesin cuci yang telah selesai digunakan, tetapi terjadi gangguan sistem atau format perintah tidak dikenali.  
* **Ketika (*When*)**:  
  Kasir mengetik perintah "tabung mesin cuci kosong" melalui Google Sheet, tetapi Google Sheet gagal memproses perintah tersebut.  
* **Maka (*Then*)**:  
  Sistem menampilkan pop-up *"Koneksi terputus. Mencoba menghubungkan kembali..."*.

---

### **5\. Workspace C: Catatan Validasi Kebutuhan dengan Mitra (Field Confirmation)**

* **Tanggal Validasi**: 13 November 2026  
* **Narahubung Mitra**: \+62 881-3723-646 (Staf Kasir)  
* **Hasil Konfirmasi User Story**:  
  \[ \] Seluruh User Story disetujui mitra  
  \[ \] Terdapat penyesuaian/revisi kebutuhan (Tuliskan revisi jika ada):

  ---

---

### **6\. Verifikasi Integritas AI (TPL-07) & Pengesahan**

* **Penggunaan AI Co-pilot**:  
  Apakah tim menggunakan AI untuk membantu merumuskan skenario *Given-When-Then*? \[✔ \] Ya  \[ \] Tidak  
  *(Jika Ya, wajib melampirkan formulir **TPL-07: AI Usage Disclosure & Verification Note**)*.

**Tanda Tangan Tim & Pengesahan Dosen**:

* **Phase Lead 3**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (Tanggal: \_\_\_\_\_\_\_\_\_\_)  
* **Dosen Coach**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (Tanggal: \_\_\_\_\_\_\_\_\_\_)  \[ \] Approved