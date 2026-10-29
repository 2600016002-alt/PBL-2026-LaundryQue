# WORKSHEET BOOK: WS02 — Need-to-Know List & Driving Question

* **Mata Kuliah:** Konsep Sistem Informasi (KSI)  
* **Kerangka Kerja:** Project-Based Learning (PBL) Level 1  
* **Learning Moment:** Discover (Minggu 1)  

---

## ℹ️ Informasi Worksheet

* **Worksheet Number:** WS02
* **Title:** Need-to-Know List & Driving Question
* **Learning Moment:** Discover
* **Purpose:** Menyusun daftar pertanyaan investigasi awal (*Need-to-Know List*) berdasarkan *Driving Question* proyek untuk memandu pencarian informasi awal dan observasi lapangan.
* **Related Learning Outcome:** CPMK-01; Sub-CPMK S-01.1 (I); SFIA BUSA L1, IRMG L1.
* **Related Deliverable:** Deliverable D1 (Problem Brief awal — TPL-01).
* **Related Module:** Modul M01 (Fondasi SI, Proses Bisnis & Value of Information).
* **Estimated Duration:** 1 Sesi (100 Menit), Minggu 1.
* **Ringkasan:** Pertanyaan *Need-to-Know* memandu investigasi lapangan kelompok. Selalu pastikan sumber informasi dan cara memperoleh data mematuhi protokol etika dan privasi data mitra.

---

## 🎯 Aktivitas Pembelajaran (Activity)

1. **Membedah Driving Question:** Membaca dan memahami kembali *Driving Question* utama proyek PBL Level 1 pada Project Wall studio.
2. **Konsolidasi Pengetahuan Awal:** Berdiskusi mengenai apa yang sudah diketahui (*What We Know*) tentang unit usaha mitra terpilih.
3. **Formulasi Need-to-Know List v1:** Merumuskan pertanyaan-pertanyaan kritis (*What We Need to Know*) yang harus dijawab melalui observasi dan wawancara di Minggu 2.
4. **Perencanaan Akses Etis:** Menentukan sumber informasi dan tata cara pengumpulan data yang menghormati etika dan privasi mitra.
5. **Identifikasi Konsep Kunci:** Mencatat istilah/konsep penting sistem informasi yang perlu dikuasai untuk dipajang di Project Wall.

---

## 🛠️ Ruang Kerja Tim (Workspace)

### 1. Driving Question Utama Proyek & Cara Memahami Masalah Nyata pada Laundry Que

#### Identified Issues:
1. **Pengiriman Nota Pesanan:** Nota pesanan masih dikirim secara manual melalui pesan pribadi WhatsApp dan tidak semua pelanggan dikirimkan atau menerima nota pesanan dari karyawan.
2. **Kendala Aplikasi SpinTrack:** Saat memasuki menu *“order”* terjadi *loading* yang cukup lama (sekitar 1–2 menit).
3. **Kendala Operasional Saat Mati Listrik:** Aplikasi SpinTrack tidak bisa menggunakan Wi-Fi dan hanya bisa digantikan menggunakan data seluler milik karyawan.
4. **Risiko Rekapitulasi Saat Pergantian Shift:** Pencatatan perlengkapan yang habis (air, gas, sabun cuci, dll.) masih manual menggunakan *chat* pribadi WhatsApp (staf kasir melaporkan barang *re-stock* kepada admin), serta staf kasir harus mengantisipasi apabila terjadi selisih antara data pemasukan yang ada pada SpinTrack dengan dana pemasukan fisik.
5. **Masalah Efisiensi Waktu bagi Kasir Selama Pengelolaan Antrean:** Pada saat jam ramai/sibuk, jumlah pelanggan sangat tinggi sehingga semua tabung mesin cuci penuh. Pelanggan yang ingin menitipkan pakaian kotor untuk dicuci setelah tabung kosong harus memberikan nomor WhatsApp mereka kepada kasir. Kasir akan menghubungi pelanggan ketika tabung telah kosong dan giliran mereka tiba. Menghubungi pelanggan satu per satu melalui telepon membutuhkan waktu sekitar 5–10 menit. Terkadang hal ini menyita waktu kasir saat melakukan tugas lain seperti melayani pelanggan yang datang dan tugas operasional lainnya.

---

#### Merumuskan Kebutuhan Awal yang Terukur:
1. **Pengiriman Nota Pesanan yang Terorganisir:** Memerlukan sistem pengiriman nota yang lebih terorganisir setelah pelanggan membayar tagihan, supaya tidak ada *miscommunication* antara pelanggan dan kasir.
2. **Peningkatan Performa Aplikasi SpinTrack:** Peningkatan kinerja/performa aplikasi SpinTrack supaya tidak ada hambatan saat membuka aplikasi yang mengharuskan pelanggan menunggu lebih lama di area kasir.
3. **Kebutuhan Operasional Saat Terjadi Pemadaman Listrik:** Memerlukan buku catatan manual jika sedang mati listrik, supaya data pelanggan tetap ada. Jika listrik sudah menyala, data pelanggan bisa dipindahkan ke aplikasi SpinTrack.
4. **Pengelolaan Rekapitulasi dan Pencatatan yang Terorganisir:** Karyawan membutuhkan pencatatan perlengkapan (detergen, gas, air mineral, dll.) dan rekapitulasi harian yang lebih terorganisir agar tidak mengalami selisih antara data pada SpinTrack dan dana pemasukan.
5. **Pengelolaan Antrean Pelanggan yang Lebih Efisien:** Memerlukan sistem pemberitahuan otomatis untuk mempersingkat waktu kasir dalam menghubungi pelanggan satu per satu.

---

#### Membangun Prototipe Sederhana yang Benar-Benar Membantu:

| Masalah | Rancangan Prototipe Sederhana | Isi Fitur / Detail | Tujuan |
| :--- | :--- | :--- | :--- |
| **Pengiriman Nota** | Fitur nota digital yang bisa dikirim melalui WhatsApp | Nama pelanggan, nomor telepon, jenis layanan, total pembayaran, dan tombol pengiriman nota otomatis ke WhatsApp pelanggan. | Pelanggan dapat menerima nota setelah transaksi dilakukan tanpa harus meminta nota terlebih dahulu kepada kasir. |
| **Performa SpinTrack** | Tampilan menu order yang lebih sederhana dan mudah diakses | Menu order, data pelanggan, jenis layanan, total yang harus dibayarkan, dan riwayat order. | Membantu mempersingkat waktu karyawan menginput data pelanggan serta mempersingkat waktu tunggu pelanggan. |
| **Pemadaman Listrik** | Formulir pencatatan pesanan manual untuk digunakan sementara | Nama pelanggan, nomor WhatsApp pelanggan, jenis layanan laundry, total biaya, nama karyawan penerima, status pemindahan data ke SpinTrack (sudah/belum). | Mencegah kesalahan input data saat SpinTrack tidak bisa digunakan akibat mati listrik (sebagai *backup* dari SpinTrack). |
| **Rekapitulasi Harian** | Tabel pencatatan stok perlengkapan dan pemasukan harian | **1. Tabel Rekapitulasi Harian:** Pemasukan dana SpinTrack, uang kasir, selisih.<br>**2. Tabel Perlengkapan:** Nama barang (detergen, gas, air mineral), kondisi stok, keterangan restock. | Memudahkan pemantauan barang, menghindari selisih data pemasukan, dan mempermudah admin memantau *restock*. |
| **Pengelolaan Antrean** | Sistem antrean dengan fitur pemberitahuan kepada pelanggan | Nama pelanggan, nomor WhatsApp, daftar antrean, status antrean, nomor tabung terisi, tombol notifikasi giliran. | Mempermudah kasir menghubungi pelanggan berikutnya sehingga pekerjaan operasional lain dapat dikerjakan lebih cepat. |

---

#### Visualisasi Prototipe
1. **Pengiriman Nota:** [image](https://github.com/2600016002-alt/PBL-2026-LaundryQue/blob/main/starter-pack/assets/Nota.png)
2. **Performa SpinTrack:** [image](https://github.com/2600016002-alt/PBL-2026-LaundryQue/blob/14cb63f1f9aad4021a43e1673856a1eccaf7b282/starter-pack/assets/Gemini_Generated_Image_s9rggfs9rggfs9rg.jpg)
3. **Rekapitulasi Harian:** [image](https://github.com/2600016002-alt/PBL-2026-LaundryQue/blob/main/starter-pack/assets/Rekapitulasi%20Harian.jpg)
4. **Pengelolaan Antrean:** [image](https://github.com/2600016002-alt/PBL-2026-LaundryQue/blob/main/starter-pack/assets/Flow%20Antrean.jpg)
5. **Formulir:** [image](https://github.com/2600016002-alt/PBL-2026-LaundryQue/blob/main/starter-pack/assets/Formulir.jpg)

---

### 2. Apa yang Sudah Kami Ketahui (What We Know)

* **Profil Singkat Mitra:**  
  Laundry Que berlokasi di depan Kafe Basabasi sekitar Universitas Ahmad Dahlan 4. Laundry ini berbasis *self-service*. Karyawan menyediakan tabung mesin cuci, tabung pengering, keranjang baju, *free Wi-Fi*, *free* air mineral, parkiran, ruang tunggu, tempat melipat pakaian bersih, tempat tas laundry pelanggan, dan toilet. Detergen/pewangi dapat dibeli di tempat atau membawa sendiri.

* **Operasional As-Is Awal:**
  1. Pelanggan tiba di halaman parkir Laundry Que.
  2. Pelanggan menuju meja kasir.
  3. Karyawan menanyakan data pelanggan (nama, nomor telepon, jenis layanan: Cuci Rp 10.000, Kering Rp 10.000).
  4. Karyawan menginput data ke aplikasi SpinTrack. (SpinTrack terkadang mengalami *loading* 1–2 menit pada menu utama).
  5. Muncul total pembayaran pada halaman SpinTrack.
  6. Karyawan memberikan informasi total pembayaran kepada pelanggan.
  7. Pelanggan membayar tagihan (cash/QRIS). Uang tunai masuk laci kasir dan diinput ke SpinTrack; QRIS masuk ke Livin' Merchant dan SpinTrack.
  8. Pelanggan mendapatkan pesan WhatsApp otomatis dari SpinTrack berisi *link member*.
  9. Pelanggan tidak mendapatkan nota transaksi jika tidak memintanya.
  10. Jika diminta, nota dikirimkan manual via pesan pribadi WhatsApp oleh karyawan.
  11. Karena berbasis *self-service*, pakaian tidak dibantu dicuci dan tidak ditimbang (1 tabung memuat 8–9 kg per pelanggan).
  12. Setelah transaksi, pelanggan menuju area mesin cuci.
  13. Pelanggan membuka pintu tabung mesin cuci.
  14. Pakaian dimasukkan satu per satu.
  15. Pintu tabung ditutup.
  16. Durasi cuci diatur karyawan via SpinTrack (sekitar 20–25 menit).
  17. Pakaian selesai dicuci dipindahkan ke tabung pengering (di atas mesin cuci).
  18. Pengering berputar otomatis selama 40 menit.
  19. Tabung pengering berhenti, pelanggan mengeluarkan pakaian ke keranjang untuk dilipat atau langsung dimasukkan ke tas pribadi.
  20. Pelanggan dapat meninggalkan Laundry Que setelah pakaian selesai dilipat dan dikemas.
  21. Jika antrean panjang dan 8 tabung terisi penuh, pelanggan dapat menunggu di ruang tunggu atau menitipkan pakaian (risiko kehilangan/tertukar bukan tanggung jawab karyawan). Karyawan akan menghubungi pelanggan via telepon (durasi 5–10 menit per pelanggan). Jika tidak menjawab, giliran diberikan ke pelanggan berikutnya.

* **Dugaan Masalah Awal:**
  1. **Pengiriman Nota Pesanan:** Nota dikirim secara manual, belum otomatis via WhatsApp.
  2. **Performa Aplikasi SpinTrack:** *Loading* aplikasi mencapai 1–2 menit sehingga menghambat transaksi.
  3. **Pencatatan Saat Pemadaman Listrik:** Belum ada sistem pencatatan otomatis/manual sebagai *backup*.
  4. **Rekapitulasi & Stok Perlengkapan:** *Restock* barang dan pencatatan keuangan kurang terorganisir.
  5. **Pengelolaan Antrean Pelanggan:** Menyita waktu kasir 5–10 menit per pelanggan saat menghubungi giliran antrean.

---

### 3. Daftar Pertanyaan Investigasi Awal (Need-to-Know List v1 — Minimal 6 Pertanyaan)

| No | Kategori | Pertanyaan Investigasi (Need-to-Know) | Sumber Informasi | Cara Mendapatkan secara Etis |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Profil Organisasi** | 1. Jenis layanan apa saja yang tersedia (kiloan, satuan, ekspres, atau antar-jemput)?<br>2. Bagaimana staf membagi tugas harian mereka? | Pemilik / Staf Kasir | Wawancara langsung berizin saat jam tenang mitra. |
| **2** | **Proses Bisnis** | 1. Bagaimana proses penandaan pakaian luntur/rusak dan pengecekan kondisi awal pakaian saat diterima?<br>2. Berapa lama durasi pengerjaan rata-rata untuk satu pelanggan? | Observasi Lapangan | Mengamati dan mencatat durasi transaksi dengan izin lisan. |
| **3** | **Data & Pencatatan** | Bagaimana cara UMKM merekap pembayaran, seperti uang tunai, QRIS, atau piutang/kasbon pelanggan? | Kasir / Buku Nota | Melihat contoh dokumen transaksi tanpa mencatat data pribadi sensitif. |
| **4** | **Masalah & Constraints** | 1. Apa hambatan operasional yang paling sering terjadi?<br>2. Apakah pernah terjadi pakaian tertukar/hilang, keterlambatan estimasi pesanan, kehilangan nota manual, atau gangguan listrik/air? | Pemilik Usaha | Wawancara terarah menggunakan instrumen WS03. |
| **5** | **Infrastruktur Fisik** | Bagaimana kualitas sinyal internet serta perangkat keras yang dimiliki (jumlah mesin cuci/pengering, tablet/smartphone, printer thermal)? | Lokasi Usaha | Observasi fisik keberadaan smartphone/tablet/Wi-Fi/4G. |
| **6** | **Target Solusi** | Apakah pemilik usaha ingin mahasiswa Sistem Informasi membantu melacak pendapatan, mencetak label barcode, mengirim notifikasi WhatsApp otomatis, atau hal teknis lainnya? | Pemilik Usaha | Wawancara diskusi ekspektasi dan batas kelayakan teknis. |

---

### 4. Kata dan Konsep Kunci yang Perlu Dikuasai (Glossary for Project Wall)

1. **Sistem Informasi (IS):** Kombinasi *People*, *Hardware*, *Software*, *Data*, dan *Network* untuk mengolah data menjadi informasi bermakna.
2. **Kondisi As-Is vs To-Be:** Pemetaan proses bisnis saat ini (*As-Is*) dibandingkan alur proses bisnis masa depan setelah perbaikan (*To-Be*).
3. **Bottleneck Operasional:** Titik kemacetan dalam alur proses bisnis yang menyebabkan perlambatan atau penurunan efisiensi.
4. **Value of Information:** Nilai tambah informasi yang akurat, tepat waktu, dan relevan untuk mendukung keputusan bisnis.
5. **Informed User:** Peran profesional yang memahami kapabilitas teknologi informasi untuk meningkatkan produktivitas organisasi.

---

## 💭 Refleksi Individu (Reflection)

<<<<<<< HEAD
**Q: Pertanyaan Need-to-Know mana yang menurut tim paling sulit dijawab dan mengapa?**
> **JAWABAN**
    
    1. 2600016018_Zaskia Azwa M: Pertanyaan kategori Target Solusi, karena kami belum bertemu pemilik usaha sehingga belum mengetahui solusi apa yang dibutuhkan bisnis usahanya, dari sisi karyawan pun masih bingung karena mereka merasa tidak memiliki hambatan dalam pekerjaan mereka.
    
    2. 2600016026_Atiqah Subandono: Pertanyaan kategori Data & Pencatatan, karena kami harus bisa membedakan mana pertanyaan maupun topik yang mengarah ke ranah pribadi, kami harus sangat berhati-hati agar tidak menghancurkan rasa percaya yang sudah dibangun.

    3. 2600016002_Davina Walasyah: "Jika dibangunkan alat bantu sistem informasi sederhana, kemampuan utama apa yang paling Bapak/Ibu harapkan?" karena takut pihak laundry menaruh harapan besar terhadap projek kami.

    4. 2600016043_Arselly Tri Kurniasari: Pertanyaan target solusi karena takut pemilik usahanya tidak bisa untuk diajak diskusi karna pemilik usahanya sibuk

    5. 2600016001_Lailatul Fitriyah: Pertanyaan bagian infrastruktur fisik karna menurut kami secara infrastruktur laundry que ini sudah memiliki sistem yang lumayan baik. 

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

5. 2600016001_Lailatul Fitriyah: Batasan laporan keuangan dan laporan shift karyawan karna ini data pribadi.
=======
* **Pertanyaan Need-to-Know mana yang menurut tim paling sulit dijawab dan mengapa?**  
  1. 2600016018 Zaskia Azwa Mutmainah: Pertanyaan kategori Target Solusi, karena kami belum bertemu pemilik usaha sehingga belum mengetahui solusi apa yang dibutuhkan bisnis usahanya, dari sisi karyawan pun masih bingung karena mereka merasa tidak memiliki hambatan dalam pekerjaan mereka. 
  2. 2600016002 Davina Walasyah: “Berapa lama waktu yang bisa kamu janjikan kepada saya untuk projek ini?”. Alasannya  karena walaupun kami  sudah memberikan batasan sistem seringkali mitra masih meragukan tim.
  3. 2600016043 Arselly Tri Kurniasari: Pertanyaan target solusi karena takut pemilik usahanya tidak bisa untuk diajak diskusi karna pemilik usahanya sibuk. 
  4. 2600016026 Atiqah Subandono:  Pertanyaan kategori Data & Pencatatan, karena kami harus bisa membedakan mana pertanyaan maupun topik yang mengarah ke ranah pribadi, kami harus sangat berhati-hati agar tidak menghancurkan rasa percaya yang sudah dibangun.
  5. 2600016001_Lailatul Fitriyah: Pertanyaan bagian infrastruktur fisik karna menurut kami secara infrastruktur laundry que ini sudah memiliki sistem yang lumayan baik. 



* **Informasi atau data apa yang TIDAK boleh kami akses / tanyakan kepada mitra demi menjaga etika dan privasi?**  
1. 2600016018 Zaskia Azwa Mutmainah: Kata sandi akun bank/riwayat transaksi Laundry Que.
2. 2600016002 Davina Walasyah: Data pribadi pelanggan/karyawan.
3. 2600016043 Arselly Tri Kurniasari: Laporan keuangan internal.
4. 2600016001 Lailatul Fitriyah: Laporan keuangan.
5. 2600016026 Atiqah Subandono: Keuntungan dan kerugian Laundry Que.
>>>>>>> ef889f19f07f6f5b8eac6bd5f53cfe58129ba8a8

---

## ✅ Checklist Kelulusan WS02

- [ ] *Need-to-Know List v1* tersusun dengan minimal 6 pertanyaan operasional yang valid.
- [ ] Setiap pertanyaan dilengkapi identifikasi sumber informasi dan cara perolehan yang etis.
- [ ] Kata/konsep kunci SI teridentifikasi untuk dipasang pada *Project Wall* studio.
- [ ] Berkas dikirim / diserahkan kepada dosen koordinator sebagai bukti *Check-in Checkpoint (b)*.

---

**Phase Lead Fase 1 (Discover):** Zaskia Azwa M  
**Tanggal Penyelesaian:** 16/10/2026  
**Status Checkpoint Dosen:** `[ ] Approved` / `[ ] Needs Revision`  
