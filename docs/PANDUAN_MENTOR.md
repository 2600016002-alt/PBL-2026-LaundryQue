Tags: #type/guidebook #domain/pbl #pbl/level-1 #audience/mentor
# Buku Petunjuk Mentor — Project-Based Learning (PjBL) Level 1
Version : Draft v1.0 | Last Updated : 2026-09-20
Related Files:
- [[output/pbl/level_1/pbl_guidebook_for_instructor|pbl_guidebook_for_instructor]]
- [[output/pbl/level_1/pbl_guidebook_for_student_revisi_3|pbl_guidebook_for_student_revisi_3]]
- [[output/pbl/level_1/moodle/course_pbl_level_1_moodle_blueprint|course_pbl_level_1_moodle_blueprint]]
- [[output/pbl/level_1/worksheet_book|worksheet_book]]
- [[output/pbl/level_1/template_pack|template_pack]]
- [[output/pbl/level_1/assessment_rubrics|assessment_rubrics]]
- [[output/pbl/level_1/silabus/dasar_pemrograman|silabus_dasar_pemrograman]]
Shared References:
- [[output/pbl/shared/ai_policy|ai_policy]]
- [[output/pbl/shared/assessment_framework|assessment_framework]]

**Digital Problem Framing Mini Project** | Program Studi Sistem Informasi | Semester 1 (Foundation Entry) | TA 2026/2027

> **Peran mentor**: asisten dosen (pembina/tutor praktikum) yang mendampingi tim mahasiswa, terutama pada **praktikum Dasar Pemrograman** dan **onboarding alat (tools)**. Mentor memberi umpan balik, memfasilitasi praktikum, dan memberi **input penilaian sementara** kepada dosen — tidak menetapkan nilai akhir. Rasio: **1 mentor : 2 tim mahasiswa**.

---

## Daftar Isi
1. [Peran & Etika Mentor](#bagian-1-peran--etika-mentor)
2. [Alat & Lingkungan Kerja](#bagian-2-alat--lingkungan-kerja)
3. [Petunjuk Teknis per Pekan](#bagian-3-petunjuk-teknis-per-pekan)
4. [Penilaian, Pelaporan & Integritas](#bagian-4-penilaian-pelaporan--integritas)
5. [Troubleshooting Cepat](#bagian-5-troubleshooting-cepat)

---

# Bagian 1: Peran & Etika Mentor

## 1.1 Tanggung Jawab
| Area | Detail |
|---|---|
| Onboarding tools | Minggu 1: pandu akses e-learning, repositori GitHub, clone starter pack, menjalankan Python pertama kali |
| Praktikum mingguan | Fasilitasi sesi praktikum; dampingi tiap tim; bantu saat buntu dengan bertanya, bukan memberi jawaban jadi |
| Cek pekerjaan | Periksa kode, log uji, dan walkthrough mahasiswa; beri umpan balik spesifik |
| Input penilaian | Nilai tugas praktikum dengan rubrik dosen; serahkan skor + catatan bukti ke dosen Dasar Pemrograman |
| Penjaga integritas | Deteksi output AI mentah, free-rider, dan verification note yang janggal; laporkan ke dosen |

## 1.2 Batasan yang WAJIB dihormati
- **Jangan menuliskan kode untuk mahasiswa.** Boleh: memberi *hint*, menunjukkan langkah debug, mendemonstrasikan contoh berbeda.
- **Jangan membocorkan jawaban antar-tim.**
- **Jangan memutuskan nilai akhir** — skor mentor adalah masukan; dosen yang menetapkan.
- **Dilarang meminta/menerima imbalan** apa pun dari mahasiswa.

## 1.3 Prinsip Coaching
- Tanya sebelum menjawab: "Di baris mana menurutmu program mulai salah?" (*rubber duck debugging*).
- Satu pertanyaan = satu petunjuk, bukan satu solusi.
- Arahkan umpan balik ke **aspek rubrik** (tipe data, kontrol alur, fungsi, kualitas kode, pengujian, penjelasan walkthrough).

---

# Bagian 2: Alat & Lingkungan Kerja

## 2.1 Daftar Alat (disiapkan sebelum semester)
| Alat | Kebutuhan | Catatan |
|---|---|---|
| Python | 3.10+ | Centang **Add to PATH** saat instalasi |
| Git | Terbaru | `git config --global user.name` & `user.email` |
| GitHub | Akun mahasiswa/org | Repositori kerja per tim |
| Editor | VS Code (opsional) | Pasang ekstensi Python |
| E-learning (Moodle) | Course PBL Level 1 | Peran **Grader** pada aktivitas `| mentor` |
| Starter pack | `starter-pack/` (release) | Disediakan di e-learning/GitHub |

## 2.2 Aktivitas yang Diampu Mentor (16)
| Pekan | Aktivitas | Rubrik |
|---|---|---|
| 1 | Lat-M1 Program Pertama (IPO) | Rubrik Praktikum S-03.5 |
| 2 | Lat-M2 Tipe Data & Konversi | Rubrik Praktikum S-03.5 |
| 3 | Lat-M3 Percabangan IF-ELSE | Rubrik Praktikum S-03.5 |
| 4 | Lat-M4 Perulangan FOR & WHILE | Rubrik Praktikum S-03.5 |
| 5 | WS07-DP Pseudocode & Fungsi | Rubrik Desain S-03.1 |
| 6 | WPseud Perbaikan Pseudocode | Rubrik Desain S-03.1 |
| 7 | WS07-final Desain Final | Rubrik Desain S-03.1 |
| 8 | Gate1-DP Oral/Code Defense | Rubrik Defense S-03.1, S-03.5 |
| 9 | WS09 Rencana Build | Rubrik Rencana S-03.5 |
| 10 | CKPT-DP Checkpoint Fitur 1–2 | Rubrik Praktikum S-03.5 |
| 11 | WS10 Walkthrough · WS11 Sprint Log | Rubrik Walkthrough S-03.1, Praktikum S-03.5 |
| 12 | WS12 Validasi Pengguna | Rubrik Walkthrough S-03.1 |
| 13 | Gate2-DP D3 Final + Walkthrough | Rubrik D3 S-03.5 |
| 14 | Final-DP Finalisasi Kode & Demo | Rubrik D3 S-03.5 |
| 15 | DemoPrep-DP Skenario Demo | Rubrik Demo S-03.5 |
| 16 | Postmortem-DP Refleksi Akhir | Rubrik Refleksi S-03.5 |

## 2.3 Alur Git Dasar (diajarkan Pekan 1, dipakai terus)
```bash
git clone <url-repo-tim>
git add <file>
git commit -m "feat: menambah fitur input"
git push origin main
```
Pesan commit: `feat:` (fitur baru) · `fix:` (perbaikan) · `docs:` (dokumentasi).

## 2.4 Struktur Repo (wajib dilestarikan)
```
repo-tim/
├── docs/
│   ├── D1-problem-brief.md
│   ├── D2-solution-design.md
│   ├── D3-prototipe.md
│   ├── D4-portfolio.md
│   ├── screenshots/        # bukti eksekusi
│   └── evidence/           # E1-E7 (lampiran D4)
├── src/
│   ├── main.py
│   ├── README.md
│   └── test_log.md
├── worksheets/             # WS01-WS16
└── assets/
```

---

# Bagian 3: Petunjuk Teknis per Pekan

## Pekan 1 — Discover · ONBOARDING TOOLS (GitHub & E-Learning) + Lat-M1
**Aktivitas mentor**: `Lat-M1 | Latihan: Program Pertama (Input-Proses-Output)` — Rubrik Praktikum S-03.5.
**Tujuan**: setiap mahasiswa dapat mengakses e-learning, mengelola repo Git, dan menjalankan program Python pertama.

**SOP — A. Akses E-Learning**
1. Pastikan mahasiswa login Moodle dan masuk course **PBL Level 1**.
2. Unduh **PANDUAN_MAHASISWA** & **starter pack** dari resource course.
3. Cek akses forum umum + tempat submisi tugas **Lat-M1**.

**SOP — B. GitHub**
4. Buat akun GitHub (username profesional, mis. `nama_nim`) atau klaim undangan repositori tim.
5. Instal Git; set identitas:
   `git config --global user.name "Nama"` · `git config --global user.email "email@kampus"`
6. `git clone <url>` repositori starter (per tim); periksa struktur folder (lihat 2.4).
7. Dorong **commit pertama** tim: modifikasi kecil → add → commit → push.
8. Validasi: repo tim tampil di GitHub dan berisi `src/main.py` yang sudah ter-push.

**SOP — C. Python & Latihan Pertama**
9. Instal Python 3.10+ (centang *Add to PATH*); verifikasi `python --version`.
10. `python src/main.py` → harus muncul menu aplikasi CSV sederhana.
11. Buat program **Lat-M1** (sapa → baca → tampilkan ulang nama; beri komentar bagian *input / proses / output*).
12. Jalankan, ambil **screenshot**, unggah `.py` + screenshot di Moodle.

**Checklist mentor** (per mahasiswa): login e-learning ✓ · clone repo ✓ · commit pertama ter-push ✓ · `python src/main.py` jalan ✓ · Lat-M1 terunggah ✓.
**Pertanyaan coaching**: "Bagian mana yang disebut input? proses? output?" · "Apa isi `data_penjualan.csv` setelah program dijalankan?"
**Eskalasi**: kendala instalasi/PATH/akun → catat di log mentor & laporkan ke dosen sebelum pekan berikutnya.

## Pekan 2 — Frame · Tipe Data & Konversi
**Aktivitas mentor**: `Lat-M2 | Latihan: Tipe Data & Konversi` — Rubrik Praktikum S-03.5.
- **Sebelum**: cek repositori tim; pastikan kode Pekan 1 sudah di-push.
- **Selama**: pandu latihan konversi `int`/`float`/`str`; tekankan *type mismatch* (menjumlahkan string angka). Dampingi tiap tim; minta mahasiswa menjelaskan output sebelum mengeksekusi.
- **Setelah**: nilai `.py` + screenshot; cek komentar input/proses/output; beri umpan balik singkat; tandai yang masih gagal konversi.
- **Jebakan**: `input()` selalu mengembalikan string → mahasiswa lupa casting → *TypeError*. Bantu menyadari, jangan perbaiki langsung.

## Pekan 3 — Define · Percabangan IF-ELSE
**Aktivitas mentor**: `Lat-M3 | Latihan: Percabangan (IF-ELSE)` — Rubrik Praktikum S-03.5.
- **Sebelum**: sediakan 2-3 soal keputusan sederhana berkait proyek (mis. validasi stok, cek harga).
- **Selama**: minta mahasiswa menulis *flowchart mini* dulu, baru kode; tekankan indentasi & kondisi majemuk (`and`/`or`).
- **Setelah**: nilai logika percabangan (bukan sekadar jalan); uji dengan input di luar contoh (edge case).
- **Coaching**: "Kalau ada harga 0, masuk cabang mana? Kenapa?"

## Pekan 4 — Define · Perulangan FOR & WHILE
**Aktivitas mentor**: `Lat-M4 | Latihan: Perulangan (FOR & WHILE)` — Rubrik Praktikum S-03.5.
- **Sebelum**: siapkan contoh pengulangan menu utama (pola `while True` + menu) yang dipakai starter pack.
- **Selama**: tekankan perbedaan FOR (jumlah iterasi jelas) vs WHILE (berhenti berdasarkan kondisi); awas **infinite loop** (selalu sediakan cara keluar/`break`).
- **Setelah**: nil; cek apakah program bisa mengulang menu & keluar dengan benar. Catat mahasiswa yang belum paham kondisi berhenti → jadi perhatian di Pekan 5.

## Pekan 5 — Design · Pseudocode & Fungsi
**Aktivitas mentor**: `WS07-DP | Pseudocode & Dekomposisi Fungsi` — Rubrik Desain S-03.1.
- **Sebelum**: ingatkan mahasiswa membawa *outline* D1 (masalah + pemilik usaha) dan flowchart WS07.
- **Selama**: tuntun pemecahan alur solusi menjadi **fungsi-fungsi kecil** (satu fungsi satu tanggung jawab, meniru pola `tampilkan_menu()`, `baca_data()`, `simpan_data()` pada starter). Cek konsistensi pseudocode ↔ flowchart.
- **Setelah**: nilai struktur dekomposisi & kejelasan pseudocode. Verifikasi mahasiswa bisa **menjelaskan** ulang alurnya (bekal GATE 1).
- **Catatan**: mulai **Daftar Konsolidasi (log mentor)**: nama mahasiswa yang lemah menjelaskan → prioritas bimbingan.

## Pekan 6 — Design · Perbaikan Pseudocode
**Aktivitas mentor**: `WPseud | Revisi Pseudocode berdasarkan Umpan Balik` — Rubrik Desain S-03.1.
- **Sebelum**: siapkan daftar masukan umum kelas (mis. fungsi terlalu besar, nama fungsi tidak deskriptif).
- **Selama**: dampingi revisi per tim; pastikan umpan balik Pekan 5 benar-benar dimasukkan, bukan sekadar menyalin ulang.
- **Setelah**: bandingkan versi 1 vs revisi; nil kualitas perbaikan (proses revisi dinilai, bukan hasil semata). Catat tim yang revisinya hanya kosmetik.

## Pekan 7 — Design · Desain Final
**Aktivitas mentor**: `WS07-final | Finalisasi Desain (Flowchart + Pseudocode + Fungsi)` — Rubrik Desain S-03.1.
- **Sebelum**: cross-check dengan dosen Konsep Sistem Informasi mengenai keselarasan D2 (komponen SI) → poin yang sama di WS07.
- **Selama**: lakukan *desk check*: jalankan mental pseudocode dengan satu skenario; cari celah logika.
- **Setelah**: nilai desain final; tandai **siap GATE 1** vs **remedial < 55**. Kirim rekap ke dosen sebelum Pekan 8.

## Pekan 8 — GATE 1 · Oral/Code Defense (Milestone)
**Aktivitas mentor**: `Gate1-DP | Oral/Code Defense Desain Solusi` — Rubrik Defense S-03.1, S-03.5.
- **Sebelum**: assist dosen menyusun jadwal pertahanan; siapkan daftar pertanyaan per level (pemahaman dasar → analisis).
- **Selama**: tiap mahasiswa menjelaskan flowchart & pseudocode (percabangan, perulangan, keputusan stok) + verifikasi manual. Mentor mengamati, menandai bukti penjelasan, dan mencatat siapa yang tidak mampu menjelaskan (**gagal checkpoint individu, remedial < 55**).
- **Setelah**: serahkan lembar observasi ke dosen. **Jangan beri nilai akhir** — beri rekomendasi.
- **Catatan**: waktunya bersamaan dengan forum Observasi Presentasi GATE 1 (Komunikasi Pro.) — koordinasikan agar tidak bentrok.

## Pekan 9 — Build · Rencana Pengembangan Prototipe
**Aktivitas mentor**: `WS09 | Rencana Build Prototipe` — Rubrik Rencana S-03.5.
- **Sebelum**: siapkan template pemecahan D3 → 3-5 fitur + pemilik tiap fitur + cara uji + target selesai.
- **Selama**: pastikan tiap fitur punya **PIC** dan cara uji sederhana. Koordinasikan jadwal checkpoint mingguan bersama dosen; tekankan bahwa sprint log (WS11) akan jadi bukti kontribusi individu (anti-free-rider).
- **Setelah**: nilai kelayakan rencana (fitur terukur, tidak muluk). Catat pembagian beban antar anggota → awasi di Pekan 10–11.

## Pekan 10 — Build · Pengkodean & Uji Fitur 1–2
**Aktivitas mentor**: `CKPT-DP | Checkpoint Mingguan: Fitur 1-2 Selesai & Diuji` — Rubrik Praktikum S-03.5.
- **Sebelum**: cek log uji awal (kasus, input, output diharapkan, output aktual, status).
- **Selama**: lakukan **walkthrough singkat** per tim: jalankan kode, tanya per-wilayah logika. Verifikasi tiap anggota memahami bagian kode yang diklaimnya.
- **Setelah**: nilai fitur + kualitas log uji. Anggota yang tidak bisa menjelaskan bagiannya sendiri → catat untuk intervensi.

## Pekan 11 — Build/Test · Walkthrough, Sprint Log & Critique II
**Aktivitas mentor**: `WS10 | Code Walkthrough & Catatan Pengujian` (Rubrik Walkthrough S-03.1) + `WS11 | Sprint Log` (Rubrik Praktikum S-03.5).
- **Selama**: walkthrough seluruh fitur — mahasiswa menjelaskan alur, variabel, keputusan, termasuk **bagian yang dibantu AI + verifikasi manual** (patuhi `ai_policy`). Bantu memperbaiki bug yang ketemu; hasil final disiapkan untuk GATE 2 (Pekan 13).
- **WS11**: pastikan sprint log update ≥ 1×/minggu berisi fitur, PIC, status, hambatan, solusi.
- **Forum**: mentor ikut memantau Forum Bantuan Debugging (bantu saat tim lain saling membalas dengan saran yang spesifik).
- **Setelah**: nil WS10 + WS11; skor sprint log jadi bahan verifikasi kontribusi individu di D4.

## Pekan 12 — Test · Validasi Pengguna & Uji Penerimaan
**Aktivitas mentor**: `WS12 | Validasi Pengguna & Uji Penerimaan` — Rubrik Walkthrough S-03.1.
- **Sebelum**: siapkan panduan sesi (skenario 3-5 langkah) & log catatan observasi pemilik usaha.
- **Selama**: dampingi tim memandu pemilik mencoba prototipe (minta bertindak sebagai pengguna — jangan menyoroti bug); catat masukan terhadap kriteria penerimaan WS05.
- **Setelah**: pastikan masukan terdokumentasi di Decision Log (E4) & rencana perbaikan tertera. Nil kualitas pelaksanaan validasi + dokumentasi.

## Pekan 13 — GATE 2 · Submit D3 Final + Code Walkthrough (Milestone)
**Aktivitas mentor**: `Gate2-DP | D3 Final + Walkthrough` — Rubrik D3 S-03.5.
- **Sebelum**: bantu dosen menyusun jadwal walkthrough per individu; siapkan lembar verifikasi (kode, log uji, dokumentasi, kesesuaian dengan D2).
- **Selama**: tiap mahasiswa menjelaskan tipe data, kontrol alur, fungsi/modularisasi, dan tes yang dijalankan. Catat bukti kemampuan menjelaskan (per individu).
- **Setelah**: masukan kunci: **TIDAK LULUS jika dokumentasi tidak valid atau mahasiswa gagal menjelaskan kode** — sampaikan rekomendasi lulus/perbaikan ke dosen. Kesamaan GATE 1: mentor tidak menetapkan nilai akhir.
- **Sinkron**: koordinasikan dengan reviewer `KP-GATE2` & `Check-13` (Konsep SI) agar pemeriksaan berdampingan.

## Pekan 14 — Communicate · Finalisasi Kode & Persiapan Demo
**Aktivitas mentor**: `Final-DP | Checkpoint: Finalisasi D3 & Penyiapan Demo` — Rubrik D3 S-03.5.
- **Selama**: pandu perapian akhir: dokumentasi `README`, komentar kode, pembersihan kode mati, uji lintas platform sederhana. Siapkan skenario demo fitur; koordinasikan dengan tim Bahasa Inggris (pitch deck).
- **Setelah**: nilai kualitas final: kebersihan kode, dokumentasi, reproduksibilitas (`python src/main.py` dari repo bersih). Beri catatan untuk skenario demo.

## Pekan 15 — Communicate · Persiapan Skenario Demo
**Aktivitas mentor**: `DemoPrep-DP | Skenario Demo D3 + Q&A` — Rubrik Demo Day / Presentasi / Oral Defense (S-03.5).
- **Selama**: uji tiap skenario (langkah, input, output diharapkan). Adakan sesi **tanya-jawab teknis latihan** dengan pertanyaan menyerupai mitra usaha; pastikan SEMUA anggota bisa mendemokan & menjelaskan fitur (bukan hanya sang pembuat kode).
- **Setelah**: nilai kelengkapan skenario & kesiapan seluruh anggota; laporkan anggota yang belum siap → dampingi rehearse ulang sebelum Demo Day.

## Pekan 16 — Reflect · Postmortem & Refleksi Akhir
**Aktivitas mentor**: `Postmortem-DP | Postmortem & Refleksi Akhir` — Rubrik Learning Journal / Refleksi Akhir (S-03.5).
- **Selama**: pimpin diskusi reflektif: apa yang berjalan baik, apa yang tidak, apa yang akan diubah. Arahkan refleksi individu ke konstruksi pemrograman dasar (tipe data, kontrol alur, fungsi) + kontribusi tim.
- **Setelah**: nilai kualitas refleksi (bukan panjang teks, tapi kedalaman & kejujuran). Selesaikan **Daftar Konsolidasi mentor**: rekap seluruh temuan, skor sementara, dan catatan perkembangan → serahkan final ke dosen sebagai input nilai & verifikasi passport (E7).
- **Penutup**: ucapkan apresiasi untuk tiap tim; berikan umpan balik 1 kalimat untuk tiap mahasiswa (hal terbaik minggu ini).

---

# Bagian 4: Penilaian, Pelaporan & Integritas

## 4.1 Alur Penilaian
1. Nilai tiap aktivitas `| mentor` menggunakan **rubrik resmi dosen** (lihat 2.2).
2. Simpan bukti: screenshot eksekusi, tangkapan walkthrough, catatan verifikasi manual.
3. Isi **Daftar Konsolidasi** (per tim: aktivitas, skor sementara, bukti, catatan).
4. Serahkan ke dosen Dasar Pemrograman per milestone (P7, P8, P13, P16) — **dosen yang menetapkan nilai akhir**.

## 4.2 Integritas & Kebijakan AI
- Terapkan `ai_policy`: kode/arti teks yang dibantu AI wajib ada **verification note**. Tindak lanjut curiga *output AI mentah*: minta mahasiswa menjelaskan baris/konsep secara lisan.
- **Free-rider**: gunakan sprint log (WS11) + walkthrough (CKPT/WS10/GATE) sebagai bukti kontribusi; laporkan ke dosen bila anggota tim tidak berkontribusi.
- Laporkan semua dugaan pelanggaran ke dosen; **jangan menghakimi mahasiswa di depan umum**.

## 4.3 Koordinasi Mentoring
- Mingguan: 5-10 menit dengan dosen (rekap temuan, kendala alat, daftar remedial).
- Gunakan forum/lounge bantuan antar-tim; mentor membuka jam konsultasi selain jam praktikum sesuai arahan dosen.

---

# Bagian 5: Troubleshooting Cepat

| Gejala | Kemungkinan | Tindakan mentor |
|---|---|---|
| `python` tidak dikenali | Python tidak di PATH | Perbaiki PATH / reinstall centang *Add to PATH* |
| `git: command not found` | Git belum terinstal | Instal Git; saat instal pilih *Git from the command line* |
| Push ditolak (auth) | Token/credential salah | Pandu buat **Personal Access Token** (fine-grained, scope repo) |
| `TypeError: can't concatenate str` | `input()` belum di-*cast* | Arahkan cek tipe `type(x)`; jangan tulis perbaikannya |
| Program hang / loop tak berhenti | Infinite loop | Minta tunjukkan kondisi keluar / `break` |
| Struktur repo berantakan | File tak ditaruh folder | Arahkan ikuti struktur 2.4; gunakan `.gitignore` |
| Moodle submisi tidak muncul | File salah nama/besar | Cek ekstensi `.py` (bukan `.txt`), ukuran < batas, tombol *Submit* diklik |

---
*Buku petunjuk ini menjadi acuan kerja mentor tingkat PBL 1. Temuan lapangan/wacana perbaikan disampaikan ke dosen koordinator; bila perlu dirubah, gunakan nomor revisi & tanggal.*