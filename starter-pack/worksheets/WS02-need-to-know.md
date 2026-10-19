# WORKSHEET BOOK: WS02 — Need-to-Know List & Driving Question

**Mata Kuliah:** Konsep Sistem Informasi (KSI)  
**Kerangka Kerja:** Project-Based Learning (PBL) Level 1  
**Learning Moment:** Discover (Minggu 1)  

---

## 📄 Informasi Worksheet

- **Worksheet Number:** WS02
- **Title:** Need-to-Know List & Driving Question
- **Learning Moment:** Discover
- **Purpose:** Menyusun daftar pertanyaan investigasi awal (Need-to-Know List) berdasarkan Driving Question proyek untuk memandu pencarian informasi awal dan observasi lapangan.
- **Related Learning Outcome:** CPMK-01; Sub-CPMK S-01.1 (I); SFIA BUSA L1, IRMG L1.
- **Related Deliverable:** Deliverable D1 (Problem Brief awal — TPL-01).
- **Related Module:** Modul M01 (Fondasi SI, Proses Bisnis & Value of Information).
- **Estimated Duration:** 1 Sesi (100 Menit), Minggu 1.
- **Ringkas:** Pertanyaan Need-to-Know memandu investigasi lapangan kelompok. Selalu pastikan sumber informasi dan cara memperoleh data mematuhi protokol etika dan privasi data mitra.

---

## 🛠️ Aktivitas Pembelajaran (Activity)

1. **Membedah Driving Question:** Membaca dan memahami kembali Driving Question utama proyek PBL Level 1 pada Project Wall studio.
2. **Konsolidasi Pengetahuan Awal:** Berdiskusi mengenai apa yang sudah diketahui (What We Know) tentang unit usaha mitra terpilih.
3. **Formulasi Need-to-Know List v1:** Merumuskan pertanyaan-pertanyaan kritis (What We Need to Know) yang harus dijawab melalui observasi dan wawancara di Minggu 2.
4. **Perencanaan Akses Etis:** Menentukan sumber informasi dan tata cara pengumpulan data yang menghormati etika dan privasi mitra.
5. **Identifikasi Konsep Kunci:** Mencatat istilah/konsep penting sistem informasi yang perlu dikuasai untuk dipajang di Project Wall.

---

## 🖥️ Ruang Kerja Tim (Workspace)

### 1. Driving Question Utama Proyek

**Cara Memahami Masalah Nyata pada Laundry Que:**
- **Pencatatan data pelanggan:** Struk masih dikirim secara manual melalui pesan pribadi Whatsapp, pencatatan data pelanggan seperti nama dan nomor telepon tidak sama antara karyawan satu dengan karyawan lainnya (karyawan A mencatat data pelanggan pada SpinTrack, karyawan B tidak mencatat data pelanggan).
- **Kendala aplikasi SpinTrack:** Saat memasuki menu “order” terjadi loading yang cukup lama sekitar 1-2 menit.
- **Kendala operasional saat mati listrik:** Aplikasi SpinTrack tidak bisa menggunakan Wi-Fi dan hanya bisa digantikan menggunakan data seluler, saat mati listrik mesin cuci tidak bisa beroperasional. Hal ini memaksakan Laundry Que untuk menutup orderan hingga listrik kembali menyala.
- **Risiko rekapitulasi saat pergantian shift:** Pencatatan perlengkapan yang habis (air, gas, sabun cuci, dll) masih manual menggunakan chat pribadi WhatApp (staff kasir melaporkan barang re-stock kepada admin), serta staff kasir harus mengantisipasi apabila terjadinya selisih antara data pemasukan yang ada pada SpinTrack dengan dana pemasukkan.

**Merumuskan Kebutuhan Awal yang Terukur:**
- Memangkas waktu tunggu (loading) pada menu order supaya proses pembayaran jauh lebih cepat.
- Pengubahan cara pengiriman struk order dari manual menggunakan chat pribadi WhatsApp menjadi sistem otomatisasi pengiriman struk digital.
- Menyediakan alur penginputan data pelanggan yang nyata, jelas, dan bersifat wajib bagi seluruh karyawan untuk mencegah ketidaksesuaian rekap tunai/saldo (tombok).
- Memperjelas alur penggunaan link member digunakan untuk apa, serta menyediakan modul yang efektif dan efisien guna merestock suatu barang.

**Membangun Prototipe Sederhana yang Benar-Benar Membantu:**
- Tampilan kasir yang ringan (lightweight) khusus untuk pencatatan nama pelanggan dan jenis layanan supaya lebih cepat dan memangkas waktu loading yang lama.
- Adakan fitur “chat otomatis” pada aplikasi SpinTrack untuk mengirimkan struk belanjaan yang langsung terkirim otomatis ke nomor WhatsApp pelanggan.
- Layar rekap harian yang mencocokkan saldo dengan uang tunai masuk secara real-time untuk mengurangi kesalahan perhitungan dan memiliki tombol pemicu trigger untuk meminta admin untuk restock bahan baku.

### 2. Apa yang Sudah Kami Ketahui (What We Know)
- **Profil Singkat Mitra:** Laundry Que depan kafe Basa-Basi, laundry berbasis *self service* menyediakan mesin cuci dan pengering baju.
- **Operasional As-Is Awal:** Laundry masih menggunakan pencatatan manual.
- **Dugaan Masalah Awal:** Pencatatan dan penghitungan rekapitulasi masih menggunakan kertas secara manual.

### 3. Daftar Pertanyaan Investigasi Awal (Need-to-Know List v1 — Minimal 6 Pertanyaan)

| # | Kategori | Pertanyaan Investigasi (Need-to-Know) | Sumber Informasi | Cara Mendapatkan secara Etis |
|---|---|---|---|---|
| 1 | Profil Organisasi | 1. Jenis layanan apa yang tersedia (kiloan, satuan, ekspres, atau antar-jemput)?<br>2. Bagaimana staf membagi tugas harian mereka? | Pemilik / Staf Kasir | Wawancara langsung berizin saat jam tenang mitra. |
| 2 | Proses Bisnis | 1. Bagaimana proses penandaan pakaian yang luntur atau rusak dan pengecekan kondisi awal pakaian pelanggan saat diterima?<br>2. Berapa lama durasi pengerjaan untuk satu pelanggan? | Observasi Lapangan | Mengamati dan mencatat durasi transaksi dengan izin lisan. |
| 3 | Data & Pencatatan | Bagaimana cara UMKM ini merekap pembayaran, seperti uang tunai, QRIS, atau piutang/kasbon pelanggan? | Kasir / Buku Nota | Melihat contoh dokumen transaksi tanpa mencatat data pribadi sensitif. |
| 4 | Masalah & Constraints |Apa hambatan operasional yang paling sering terjadi? Misalnya, pakaian tertukar atau hilang, keterlambatan estimasi pesanan, kehilangan nota manual, atau mati listrik atau air? | Pemilik Usaha | Wawancara terarah menggunakan instrumen WS03. |
| 5 | Infrastruktur Fisik | Bagaimana kualitas sinyal internet, serta perangkat keras apa yang dimiliki, seperti jumlah mesin cuci/pengering, tablet/smartphone, dan printer thermal untuk mencetak resi? | Lokasi Usaha | Observasi fisik keberadaan smartphone/tablet/Wi-Fi/4G. |
| 6 | Target Solusi | Apakah pemilik usaha ingin mahasiswa sistem informasi untuk membantu melacak pendapatan, mencetak label barcode, mengirimkan notifikasi otomatis melalui WhatsApp, atau hal lainnya yang masih berkaitan dengan teknologi? | Pemilik Usaha | Wawancara diskusi ekspektasi dan batas kelayakan teknis. |

---

## 🔑 4. Kata dan Konsep Kunci yang Perlu Dikuasai (Glossary for Project Wall)
1. **Sistem Informasi (IS):** Kombinasi People, Hardware, Software, Data, dan Network untuk mengolah data menjadi informasi bermakna.
2. **Kondisi As-Is vs To-Be:** Pemetaan proses bisnis saat ini (As-Is) dibandingkan alur proses bisnis masa depan setelah perbaikan (To-Be).
3. **Bottleneck Operasional:** Titik kemacetan dalam alur proses bisnis yang menyebabkan perlambatan atau penurunan efisiensi.
4. **Value of Information:** Nilai tambah informasi yang akurat, tepat waktu, dan relevan untuk mendukung keputusan bisnis.
5. **Informed User:** Peran profesional yang memahami kapabilitas teknologi informasi untuk meningkatkan produktivitas organisasi.

---

## 🧠 Refleksi Individu (Reflection)

**Q: Pertanyaan Need-to-Know mana yang menurut tim paling sulit dijawab dan mengapa?**
> **JAWABAN**
    
    1. 2600016018_Zaskia Azwa M:

    Pertanyaan kategori Target Solusi, karena kami belum bertemu pemilik usaha sehingga belum mengetahui solusi apa yang dibutuhkan bisnis usahanya, dari sisi karyawan pun masih bingung karena mereka merasa tidak memiliki hambatan dalam pekerjaan mereka.
    
    2. 2600016026_Atiqah Subandono:

    Pertanyaan kategori Data & Pencatatan, karena kami harus bisa membedakan mana pertanyaan maupun topik yang mengarah ke ranah pribadi, kami harus sangat berhati-hati agar tidak menghancurkan rasa percaya yang sudah dibangun.

    3. 2600016002_Davina Walasyah:

    "Jika dibangunkan alat bantu sistem informasi sederhana, kemampuan utama apa yang paling Bapak/Ibu harapkan?" karena takut pihak laundry menaruh harapan besar terhadap projek kami.

    4. 2600016043_Arselly Tri Kurniasari

    Pertanyaan target solusi karena takut pemilik usahanya tidak bisa untuk diajak diskusi karna pemilik usahanya sibuk





    . 2600016001_Lailatul Fitriyah:

        Pertanyaan bagian infrastruktur fisik karna menurut kami secara infrastruktur laundry que ini sudah memiliki sistem yang lumayan baik. 

**Q: Informasi atau data apa yang TIDAK boleh kami akses / tanyakan kepada mitra demi menjaga etika dan privasi?**
>**JAWABAN**

1. 2600016018_Zaskia Azwa Mutmainah:

Informasi yang tidak boleh kami ketahui adalah kata sandi akun bank, data pribadi pelanggan dan keuntungan usaha karena itu menyangkut informasi sensitif.

2. 2600016026_Atiqah Subandono:

Informasi atau data yang tidak boleh kami akses atau kami tanyakan kepada mitra demi menjaga etika dan privasi adalah hal yang berbau dan condong ke ranah pribadi seperti nomor rekening, ktp, data pelanggan, dsb.

3. 2600016002_Davina Walasyah:

Login ke akun kasir, karena itu perlu data pribadi karyawan yang menjaga pada shift tersebut dan tidak boleh kami ketahui.

4. 2600016043_Arselly Tri Kurniasari

Laporan keuangan internal, yang sangat rahasia dan mungkin tidak relevan untuk investigasi proses bisnis.

---

## ✅ Checklist Kelulusan WS02

- [x] Need-to-Know List v1 tersusun dengan minimal 6 pertanyaan operasional yang valid.
- [x] Setiap pertanyaan dilengkapi identifikasi sumber informasi dan cara perolehan yang etis.
- [x] Kata/konsep kunci SI teridentifikasi untuk dipasang pada Project Wall studio.
- [x] Berkas dikirim / diserahkan kepada dosen koordinator sebagai bukti Check-in Checkpoint (b).

---

**Phase Lead Fase 1 (Discover):** Zaskia Azwa M  
**Tanggal Penyelesaian:** 16/10/2026  
**Status Checkpoint Dosen:** [ ] Approved / [ ] Needs Revision  
**Catatan Dosen:** [...]
