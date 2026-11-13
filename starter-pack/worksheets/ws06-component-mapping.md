# **WORKBOOK: LEMBAR KERJA MAHASISWA WS06**

## **Success Metrics (BPI/DMAIC) & Pemetaan Komponen SI Awal**

Mata Kuliah: **Konsep Sistem Informasi (KSI)**  
Kerangka Kerja: **Project-Based Learning (PBL) Level 1**  
Fase Learning Spine: **Fase 3 — Define (Minggu 4\)**  
Sub-CPMK / SFIA: **S-01.1 (Intermediate \- Problem Framing) & S-03.1 (Intermediate \- Pemetaan SI)** \| **SFIA BUSA L1, METR L2**  
Keterkaitan Deliverable: **Bahan Utama Deliverable D1 Final (TPL-01) & D2 Draf (TPL-02)**

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

### **2\. Landasan Konseptual: Metrik BPI & Pemetaan 5 Pilar SI**

* **Business Process Improvement (BPI)** mengukur keberhasilan perbaikan proses bisnis melalui dua dimensi utama (Rainer et al., 2014):  
  * **Efisiensi (*Efficiency*)**: Mengukur penghematan sumber daya (*doing things well*), seperti efisiensi waktu siklus transaksi atau reduksi biaya operasional.  
  * **Efektivitas (*Effectiveness*)**: Mengukur pencapaian kualitas/tujuan (*doing the right things*), seperti akurasi data stok, penurunan angka selisih kasir, dan kepuasan pelanggan.  
* **Model 5 Pilar SI O'Brien**: Solusi sistem informasi dipetakan ke dalam pilar *People, Hardware, Software, Data,* dan *Network* (Marakas & O'Brien, 2013).

---

### **3\. Workspace A: Matrik Metrik Keberhasilan Bisnis (DMAIC Six Sigma)**

| Dimensi Metrik | Parameter Kinerja | Kondisi Baseline (As-Is) | Target Solusi (To-Be) | Metode Pengukuran |
| :---- | :---- | :---- | :---- | :---- |
| **Efisiensi (Waktu)** | Durasi pelayanan transaksi per pelanggan | 60 detik | 45 detik | Stopwatch sampel 3-5 transaksi |
| **Efisiensi (Waktu)** | Durasi rekapitulasi harian pemilik | 20 menit / malam akhir shift | 10 menit / malam akhir shift | Wawancara & uji coba langsung |
| **Efektivitas (Akurasi)** | Tingkat selisih pencatatan stok barang | 16 % selisih / 1-2 kali perbulan | 0 % selisih / bulan | Stock opname bulanan |
| **Efektivitas (Kualitas)** | Frekuensi kesalahan hitung nota | 40 kali dalam jam sibuk | \<40 kali | Audit sampel chat nota |

---

### **4\. Workspace B: Pemetaan Arsitektur 5 Pilar SI Solusi Awal**

```
┌──────────────────────────────────────────────────────────────┐
│                      PETA 5 PILAR SISTEM INFORMASI                      │         
├──────────────────────────────────────────────────────────────┤
│ 1. PEOPLE RESOURCES (Pengguna & Spesialis)                              │
│    • Pengguna Akhir: Pelanggan                                          │
│    • Pengelola Data: Kasir Laundry                                      │
├──────────────────────────────────────────────────────────────┤
│ 2. HARDWARE RESOURCES (Perangkat Mesin & Media)                         │
│    • Perangkat Fisik Input: Handphone                                   │
│    • Perangkat Fisik Output: Handphone                                  │
├──────────────────────────────────────────────────────────────┤
│ 3. SOFTWARE RESOURCES (Aplikasi & Prosedur Operational)                 │
│    • Aplikasi Program: Google Sheet, Google App Script, WhatsApp API, Python.   
│    • Prosedur Pengguna: Masukkan data pelanggan ke Google Sheet lalu diproses oleh Google apps Script. Setelah itu WhatsApp API akan mengirimkan pesan nota secara otomatis ke nomor pelanggan.                                                                │
├──────────────────────────────────────────────────────────────┤
│ 4. DATA RESOURCES (Struktur Data & Basis Data)                          │
│    • Data Transaksi: Data transaksi tersimpan dalam aplikasi Spintrack  │
│    • Data Produk/Stok: Pendataan produk/stok bersifat manual            │
├──────────────────────────────────────────────────────────────┤
│ 5. NETWORK RESOURCES (Jaringan Communication & Media)                   │
│    • Konektivitas: Wifi                                                 │
└──────────────────────────────────────────────────────────────┘
```

---

### **5\. Workspace C: Lembar Persetujuan Formal Mitra (Sign-Off)**

Dengan ini, pemilik / manajer UMKM mitra menyatakan setuju atas rumusan kebutuhan fungsional, target metrik keberhasilan, dan batas cakupan sistem yang dirancang oleh tim mahasiswa.

* **Nama UMKM Mitra**: Laundry Que  
* **Nama Pemilik / Pengelola**: Nurma  
* **Tanggal Persetujuan**: 13 November 2026

**Tanda Tangan Persetujuan Mitra**:

---

*(Cap / Tanda Tangan Pemilik UMKM Mitra)*

---

### **6\. Verifikasi Integritas AI (TPL-07) & Pengesahan**

* **Penggunaan AI Co-pilot**:  
  Apakah tim menggunakan AI untuk membantu merumuskan metrik BPI / diagram 5 pilar SI? \[ \] Ya  \[ \] Tidak  
  *(Jika Ya, wajib melampirkan formulir **TPL-07: AI Usage Disclosure & Verification Note**)*.

**Tanda Tangan Tim & Pengesahan Dosen**:

* **Phase Lead 3**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (Tanggal: \_\_\_\_\_\_\_\_\_\_)  
* **Dosen Coach**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (Tanggal: \_\_\_\_\_\_\_\_\_\_)  \[ \] Approved