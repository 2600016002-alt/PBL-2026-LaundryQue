# **WS04: Problem Identification & Scope**

**Mata Kuliah**: Konsep Sistem Informasi (KSI)  
**Kerangka Kerja**: Project-Based Learning (PBL) Level 1  
**Fase Learning Spine**: **Fase 2 — Frame (Problem Discovery & Scope)**  
**Minggu / Alokasi Waktu**: Minggu 2 / 14 Jam Belajar  
**Sub-CPMK / SFIA**: S-01.1 (Introduce \- Problem Framing) \| SFIA BUSA L1 (*Business Analysis*), IRMG L1  
**Penanggung Jawab Fase**: **Phase Lead 2 (Frame — Mahasiswa B)**  
**Keterkaitan Deliverable**: Sumber Utama Penyusunan **Deliverable D1 (Problem Brief \- TPL-01)**

---

## **1\. Identifikasi Tim & Objek Proyek**

| Elemen Informasi | Rincian Identitas Kelompok & Mitra |
| :---- | :---- |
| **Nama Kelompok / Kelas** | Bugenvil / A |
| **Phase Lead 2 (Frame \- M2)** | Davina Walasyah / 2600016002 |
| **Nama UMKM Mitra Lapangan** | Laundry Que  |
| **Pemilik / Kontak Mitra** | Nurma / Karyawan  |

---

## **2\. Matriks Problem Framing & Analisis Akar Masalah (Root Cause Analysis)**

Gunakan temuan kuantitatif dari `WS03` untuk memisahkan antara **Gejala Permukaan (*Symptoms*)** dan **Akar Masalah Utama (*Root Cause*)** operasional bisnis mitra:

| No | Kategori Observasi | Gejala Permukaan (*Symptoms*) | Akar Masalah Operasional (*Root Cause*) | Bukti Kuantitatif (*Baseline Data*) |
| :---: | :---- | :---- | :---- | :---- |
| 1 | Proses Transaksi & Input Data Kasir  | Proses memasukkan pesanan terkadang membutuhkan waktu lebih lama karena aplikasi SpinTrack mengalami loading sekitar 1–2 menit. Selain itu, masih ada karyawan yang tidak meminta nomor telepon pelanggan saat melakukan pendataan.  | Penginputan pesanan masih bergantung pada aplikasi SpinTrack yang terkadang lambat saat diakses. Di sisi lain, cara karyawan dalam mengumpulkan data pelanggan juga belum dilakukan secara seragam.  | Loading SpinTrack sekitar 1-2 menit / pelanggan. SpinTrack ini mengalami loading tidak setiap saat jika karyawan memakai aplikasinya. Loading hanya beberapa kali. |
| 2 | Pengelolaan Stok Barang dan Pengiriman Nota  | Informasi mengenai stok barang yang habis masih disampaikan oleh kasir kepada admin melalui WhatsApp pribadi. Sementara itu, nota transaksi belum langsung diterima pelanggan dan harus diminta terlebih dahulu.  | Pencatatan stok belum menggunakan media khusus yang dapat diakses secara terpusat. Pengiriman nota juga masih dilakukan secara manual oleh karyawan, bukan secara otomatis setelah transaksi selesai.  |  |
| 3 | Rekapitulasi Keuangan  | Kasir masih perlu memeriksa kembali jumlah pemasukan dengan membandingkan data yang tercatat di SpinTrack dan uang yang diterima.  | Pengecekan pemasukan masih dilakukan dengan mencocokkan catatan pada aplikasi dan uang yang diterima oleh kasir secara manual.  | 20 menit / akhir shift |
| 4 | Pengelolaan Antrean Pelanggan  | Saat tabung mesin sudah tersedia, kasir perlu menelepon pelanggan satu per satu untuk memberitahukan bahwa sudah tiba giliran mereka untuk mencuci.  | Penyampaian informasi mengenai giliran mencuci masih mengandalkan panggilan telepon dari kasir karena belum tersedia fitur pemberitahuan antrean secara otomatis.  | 5-10 menit / pelanggan |

---

## **3\. Perumusan Problem Statement Kontekstual**

Berdasarkan analisis di atas, rumuskan **Problem Statement** utama dalam 1–2 paragraf terstruktur.  
*Petunjuk*: Hindari mendefinisikan masalah sebagai *"Mitra belum memiliki aplikasi Python/komputer"*. Definisikan dari hambatan bisnis nyata mitra\!

> **Rumusan Problem Statement Kelompok**:  
> Proses operasional Laundry Que masih memiliki beberapa kendala dalam beroperasional yaitu dalam proses transaksi, pengelolaan stok barang, pengiriman nota transaksi ke pelanggan, rekapitulasi keuangan di akhir shift, dan pengelolaan antrean pelanggan saat jam sibuk. Pada proses transaksi, aplikasi SpinTrack terkadang mengalami loading selama 1–2 menit dan penginputan data pelanggan belum dilakukan secara seragam oleh seluruh karyawan, ada yang mendata dengan benar dan ada yang tidak. Pengiriman nota masih dilakukan secara manual dari kasir ke nomor WhatsApp pelanggan, tidak otomatis seperti link member dari SpinTrack langsung ke nomor WhatsApp pelanggan dan pencatatan stok barang yang habis juga masih menggunakan pesan pribadi antara kasir dan admin. Pada proses rekapitulasi keuangan yang masih membutuhkan pencocokan antara data pemasukan di SpinTrack dengan uang yang diterima kasir. Ketika seluruh tabung mesin terisi, kasir juga harus menghubungi pelanggan satu per satu melalui telepon untuk memberitahukan gilirannya untuk mencuci, dengan waktu sekitar 5–10 menit yang dihabiskan karyawan hanya untuk menghubungi pelanggan yang tidak ada di area laundry que. Berbagai kendala tersebut menyebabkan pekerjaan karyawan menjadi kurang efisien dan berpotensi memperlambat pelayanan kepada pelanggan. Oleh karena itu, diperlukannya perbaikan pada proses pencatatan, pengelolaan informasi, dan pelayanan agar kegiatan operasional Laundry Que dapat berjalan lebih terorganisir dan efisien.  
> 

---

## **4\. Menetapkan Batasan Sistem (System Boundary / Scope Alignment)**

Untuk mencegah terjadinya pembengkakan fitur (*Scope Creep*) yang membahayakan penyelesaian proyek dalam 1 semester, tentukan secara tegas apa yang **Masuk Cakupan (*In-Scope*)** dan apa yang **Di Luar Cakupan (*Out-of-Scope*)**:

 ┌───────────────────────────────────────────┐  
 │                    SYSTEM BOUNDARY (BATASAN SISTEM)                    │  
 │                                                                        │  
 │   \[ IN-SCOPE: Fitur yang Akan Dibangun \]                               │  
 │   1\. Pencatatan transaksi kasir berbasis konsol (CLI).                 │  
 │   2\. Pengurangan stok otomatis setiap transaksi berhasil.              │  
 │   3\. Pencetakan ringkasan rekapitulasi harian untuk pemilik.           │  
 │                                                                        │  
 │─────────────────────────────────────────── │  
 │                                                                        │  
 │   \[ OUT-OF-SCOPE: Di Luar Cakupan Proyek \]                             │  
 │   1\. Integrasi gateway pembayaran e-wallet / QRIS otomatis.            │  
 │   2\. Fitur penggajian karyawan / manajemen HRD.                        │  
 │   3\. Pemesanan stok otomatis ke supplier luar.                         │   └────────────────────────────────────────────┘

### **Tabel Penegasan Cakupan Proyek (*Scope Alignment Table*)**

| No | Modul / Fitur Sistem | Status Cakupan (*In-Scope / Out-of-Scope*) | Alasan Pertimbangan Kelayakan (O'Brien) |
| :---: | :---- | :---: | :---- |
| **1** | Menu input pesanan yang berisi nama pelanggan, nomor telepon, jenis layanan, dan total pembayaran.  | **IN-SCOPE** | Memudahkan karyawan dalam memasukkan data pesanan agar proses transaksi menjadi lebih teratur.  |
| **2** | Pengiriman nota digital kepada pelanggan melalui WhatsApp.  | **IN-SCOPE** | Memudahkan pelanggan mendapatkan bukti pembayaran tanpa harus meminta nota terlebih dahulu kepada karyawan.  |
| **3** | Pencatatan stok perlengkapan laundry, seperti detergen, gas, dan air mineral.  | **IN-SCOPE** | Membantu karyawan mengetahui dan melaporkan perlengkapan yang sudah habis agar kebutuhan stok lebih mudah dipantau.  |
| **4** | Pencatatan pemasukan dan rekapitulasi keuangan berdasarkan shift karyawan.  | **IN-SCOPE** | Membantu kasir dalam memeriksa kesesuaian antara pemasukan yang tercatat di SpinTrack dengan uang yang diterima.  |
| **5** | Pengelolaan antrean dan pemberitahuan giliran pelanggan untuk menggunakan mesin cuci.  | **IN-SCOPE** | Membantu menghemat waktu kasir karena tidak perlu menghubungi pelanggan satu per satu ketika mesin sudah tersedia.  |
| **6** | Formulir pencatatan pesanan secara manual ketika terjadi pemadaman listrik.  | **IN-SCOPE** | Memungkinkan karyawan tetap mencatat data pelanggan dan pesanan meskipun aplikasi SpinTrack sedang tidak dapat digunakan.  |
| **7** | Penghubungan sistem secara langsung dengan aplikasi SpinTrack.  | **OUT-OF-SCOPE** | Memerlukan akses dan pengembangan langsung pada aplikasi SpinTrack yang berada di luar kemampuan proyek kelompok.  |
| **8** | Pengiriman pesan dan pembayaran yang terhubung secara otomatis dengan WhatsApp dan Livin' Merchant.  | **OUT-OF-SCOPE** | Membutuhkan proses integrasi dengan layanan pihak ketiga yang lebih kompleks.  |
| **9** | Pengaturan mesin cuci dan pengering melalui sistem secara otomatis.  | **OUT-OF-SCOPE** | Pengembangan proyek lebih difokuskan pada pencatatan administrasi dan pelayanan pelanggan, bukan pengaturan perangkat mesin.  |
| **10** | Penanganan pakaian pelanggan yang hilang, rusak, atau tertukar.  | **OUT-OF-SCOPE** | Permasalahan tersebut berkaitan dengan kebijakan dan tanggung jawab operasional laundry, bukan fitur utama yang akan dirancang kelompok.  |

---

## **5\. Target Metrik Keberhasilan Solusi (To-Be Targets)**

Tentukan target kuantitatif perbaikan yang ingin dicapai melalui solusi sistem informasi To-Be:

| Indikator Kinerja | Kondisi As-Is (Baseline) | Target To-Be (Expected) | Estimasi Persentase Peningkatan |
| :---- | :---: | :---: | :---: |
| **Waktu Pelayanan Transaksi Kasir** | 30-60 detik / pelanggan | **\< 30 detik / pelanggan** | Peningkatan efisiensi **33,33%**  |
| **Durasi Rekapitulasi Harian** | 20 menit / akhir shift | **\< 20 menit / malam** | Penghematan waktu **50%**  |
| **Akurasi Pencatatan Stok** | Selisih 1-2 kali / bulan | **Akurasi \> 98%** | Penurunan tingkat kesalahan selisih stok |

---

## **6\. Refleksi & Lembar Pengesahan Phase Lead**

### **A. Pertanyaan Refleksi Tim**

1. *Bagaimana tim memastikan bahwa batasan proyek yang ditetapkan realistis untuk diselesaikan dalam 16 minggu?*  
   * **Jawab**: Tim harus mampu memisahkan antara in-scope dan out-of-scope supaya projek yang tim jalankan dapat berjalan dengan lancar dan sesuai target yang sudah ditentukan.  
2. *Apakah pemilik usaha mitra telah menyetujui batasan sistem yang diusulkan oleh kelompok?*  
   * **Jawab**: Ya, sudah. Tim lebih dulu menjelaskan batasan sistem, privasi narasumber, serta privasi perusahaan sebelum tim menjelaskan rancangan kegiatan yang akan dijalankan kedepannya.

### **B. Tanda Tangan Pengesahan Phase Lead 2**

`Disusun oleh Phase Lead 2 (Frame): [ Davina Walasyah — 2600016002 ]`  
`Tanggal Penyusunan: [ 25/10/2026 ]`

`Tanda Tangan Phase Lead 2: ____________________`

`Diverifikasi oleh Dosen Pengampu / Coach:`  
`Tanggal: [ Tanggal ] | Status Checkpoint: [ APPROVED / REVISION NEEDED ]`  
`Catatan Dosen: __________________________________________________`
