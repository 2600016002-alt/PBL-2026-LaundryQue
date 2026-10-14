Tags: #type/guidebook #domain/pbl #pbl/level-1 #audience/instructor
# Buku Petunjuk Dosen Project-Based Learning (PjBL) — Level 1

Version : Draft v1.0 | Last Updated : 2026-09-19

## Daftar Isi
1. [Pendahuluan & Peran Dosen](#bagian-1-pendahuluan)
2. [Learning Spine & Fasilitasi per Fase](#bagian-2-learning-spine--fasilitasi-per-fase)
3. [Rotating Phase Lead](#bagian-3-rotating-phase-lead)
4. [Deliverables & Verifikasi](#bagian-4-deliverables)
5. [Asesmen, Rubrik & Passport](#bagian-5-asesmen)
6. [Scaffolding, Coaching & Intervensi](#bagian-6-scaffolding-coaching--intervensi)

---

# Bagian 1: Pendahuluan

## 1.1 Peran Dosen dalam PBL
Dosen bertindak sebagai **fasilitator, coach, dan penilai** — bukan satu-satunya sumber jawaban. Tujuh praktik mengajar PBL: **Design & Plan, Align to Standards, Build the Culture, Manage Activities, Scaffold Student Learning, Assess Student Learning, Engage & Coach**.

| Peran | Siapa | Tanggung Jawab Utama |
|---|---|---|
| Koordinator semester | Dosen koordinator | Jadwal, gate, mitra, konsistensi lintas MK, arsip nilai |
| Pengampu MK project | Dosen per MK | Checkpoint formatif, scaffolding, asesmen per Sub-CPMK, ko-owner D4 |
| Reviewer gate | Reviewer akademik | Verifikasi klaim individu vs bukti artefak; sign-off GATE 1 & 2 |
| Outside expert | Pemilik usaha / dosen tamu | Menilai produk publik (Demo Day) |

> Dokumen ini **khusus dosen** — jangan dibagikan penuh ke mahasiswa. Yang dibagikan: worksheet, modul, template, dan panduan mahasiswa.

## 1.2 Kompetensi Target (SFIA)
| Kemampuan | Level | Bukti Utama | Diukur pada |
|---|---|---|---|
| Business Situation Analysis (BUSA) | L1 | D1, D2, Gate 1 | Rubrik D1, D2 + oral defense |
| Information Management (IRMG) | L1 | Data & bukti D1 | Rubrik D1 |
| Programming/Software Development (PROG) | L1 | D3, Gate 2 | Rubrik D3 + code walkthrough |
| Content Publishing (ICPM) | L2 | D4, executive summary | Rubrik D4 |
| Customer Service Support (CSMG) | L2 | D4, komunikasi tim | Rubrik D4 + peer assessment |

Kriteria kelulusan: klaim **BUSA L1** dan **PROG L1** tercapai + minimal 1 dari 2 skill komunikasi L2 (ICPM, CSMG).

## 1.3 Deskripsi Proyek (yang difasilitasi dosen)
Mahasiswa memilih **satu unit usaha kecil nyata** (kantin kampus, warung, koperasi, unit layanan kampus) sebagai objek studi, lalu: merumuskan masalah → kebutuhan awal terukur (D1–D2) → merancang skema solusi (D2) → membangun & menguji prototipe konsol (D3) → refleksi & portofolio + presentasi publik (D4 + Demo Day).

**Driving Question**: "Bagaimana kita memahami masalah nyata sebuah unit usaha kecil di sekitar kampus, merumuskannya menjadi kebutuhan awal yang terukur, dan membangun prototipe sederhana yang benar-benar membantu mereka?"

**Batasan teknis**: tanpa database; tanpa integrasi sistem lain; tanpa web/mobile; prototipe program konsol (CLI/Python); wajib observasi & wawancara lapangan sebagai bukti.

## 1.4 Distribusi Nilai ke MK (work package)
| MK | Deliverable | Pemilik |
|---|---|---|
| Konsep Sistem Informasi (3 SKS) | D1, D2 | Konsep SI |
| Dasar Pemrograman (4 SKS) | D3 | Dasar Prog |
| Komunikasi Profesional & Kerja Tim (2 SKS) | D4 (co-owner) | Kom. Profesional |
| Bahasa Inggris (2 SKS) | D4 (co-owner) | B. Inggris |

---

# Bagian 2: Learning Spine & Fasilitasi per Fase

## 2.1 Learning Spine (8 Fase)

```
DISCOVER → FRAME → DEFINE → DESIGN → [GATE 1] → BUILD → TEST → [GATE 2] → COMMUNICATE → REFLECT → [DEMO DAY]
```

| Fase | Minggu | Fokus | Worksheet | Fokus Fasilitasi Dosen |
|---|---|---|---|---|
| Discover | 1 | Entry event, tim, norma | WS01, WS02 | Jalankan entry event; bentuk tim; tetapkan rotasi phase lead |
| Frame | 2 | Observasi lapangan, scope | WS03, WS04 | Bimbing wawancara etis; jaga izin & etika lapangan |
| Define | 3–4 | Kebutuhan, metrik sukses | WS05, WS06 | Coaching user story; validasi kebutuhan dengan pemilik |
| Design | 5–7 | Desain solusi + kritik I | WS07, WS08 | Studio desain; fasilitasi kritik antar-tim |
| **GATE 1** | **8** | **D1+D2 sign-off + oral defense** | — | Sign-off; defense individu; verifikasi kontribusi phase lead |
| Build | 9–12 | Pengkodean prototipe | WS09, WS10, WS11 | Work time + teaching teknis; checkpoint formatif mingguan |
| Test | 11–12 | Validasi pengguna + kritik II | WS12, WS13 | Fasilitasi kritik & validasi pemilik |
| **GATE 2** | **13** | **D3 final + code walkthrough** | — | Walkthrough individu; verifikasi bukti uji & AI disclosure |
| Communicate | 14–15 | Executive summary, pitch, rehearsal | WS14 | Bimbing revisi bahasa; selenggarakan rehearsal |
| Reflect | 13–16 | Refleksi, AI disclosure, portfolio | WS15, WS16 | Fasilitasi postmortem; kumpulkan portfolio & passport |
| **DEMO DAY** | **16** | **Presentasi publik; D4 final; passport** | — | Selenggarakan Demo Day dengan pemilik usaha sebagai audiens |

## 2.2 Titik Gate & Checkpoint
| Checkpoint | Kapan | Persyaratan Kelulusan | Tindakan Dosen |
|---|---|---|---|
| **GATE 1** | M8 | D1 + D2 final (TPL-01, TPL-02); **oral defense per individu** | Sign-off + remedial bila perlu |
| **GATE 2** | M13 | D3 final + bukti testing (TPL-03); **code walkthrough per individu**; draf D4 | Sign-off + verifikasi klaim level |
| **DEMO DAY** | M16 | D4 final + supporting evidence + passport; presentasi publik | Penilaian produk publik; postmortem |

Prinsip gate: **exit criteria** harus dipenuhi sebelum lanjut — tidak ada kompromi pada kelengkapan artefak.

---

# Bagian 3: Rotating Phase Lead

Tim **tidak memakai peran permanen** — setiap anggota menjadi **phase lead** bergilir, memimpin minimal satu fase. Dosen memfasilitasi agar rotasi benar-benar berjalan (bukan sekadar label).

| Fase | Phase Lead |
|---|---|
| Discover → Build | Anggota A |
| Frame → Test | Anggota B |
| Define → Communicate | Anggota C |
| Design → Reflect | Anggota D |

Peran dosen:
- Sosialisasikan skema rotasi di minggu 1; berikan template **jadwal rotasi** di WS01.
- **Pantau kepemimpinan tiap fase** (checkpoint mingguan): apakah phase lead menjadwalkan rapat, membagi tugas, melaporkan progres.
- Keputusan penting fase wajib masuk **Decision Log** (lampiran D4) — periksa saat gate.
- Tim 3 orang: dua fase terakhir dikelola bersama; pastikan tetap ada lead yang jelas per fase.
- Intervensi bila phase lead tidak aktif (lihat Bagian 6).

---

# Bagian 4: Deliverables

## 4.1 Core Learning Artifacts (D1–D4)
| Kode | Deliverable | Isi Utama | MK Owner | Deadline | Yang Diverifikasi Dosen/Rubrik |
|---|---|---|---|---|---|
| **D1** | Problem Brief | User/context, bukti, insight, problem statement, impact, scope & non-scope, success metric | Konsep SI | Draf M2 → GATE 1 | Keaslian data lapangan; keterukuran metrik; etika |
| **D2** | System & Solution Design | User story, requirements, acceptance criteria, IPO, data, flowchart, pseudocode, solution concept, validasi | Konsep SI (+ Dasar Prog) | Draf M4 → GATE 1 | Logika desain; kriteria penerimaan terukur; kesiapan implementasi |
| **D3** | Tested Solution Prototype | Prototipe konsol + kode, test cases & results, user validation, improvement, limitation | Dasar Prog | Design GATE 1 → GATE 2 | Kode bisa dijelaskan baris demi baris; bukti uji valid |
| **D4** | Reflection & Portfolio | Summary, decisions, kontribusi individu, AI disclosure, verification, refleksi, dokumentasi portfolio | Kom. Profesional & B. Inggris (co-owner) | Draf GATE 2 → DEMO DAY | Kelengkapan supporting evidence; refleksi autentik |

Format penyerahan: **TPL-01** (D1), **TPL-02** (D2), **TPL-03** (D3), **TPL-04** (D4) plus lampiran — lihat [[output/pbl/level_1/template_pack|template_pack]].

## 4.2 Supporting Evidence (lampiran D4 — diverifikasi saat GATE 2 & DEMO DAY)
| Evidence | Isi | Template | Catatan Verifikasi |
|---|---|---|---|
| Executive Summary & Pitch Deck | Ringkasan eksekutif (EN, 150–250 kata) + pitch maks. 8 slide | TPL-05, TPL-06 | Kualitas bahasa & data |
| AI Usage Disclosure & Verification Note | Tool AI, bagian dibantu, modifikasi, verifikasi manual | TPL-07 | Wajib; tanpa ini artefak dianggap tidak lengkap |
| Decision Log | Keputusan penting + alternatif + alasan (min. 5 entri) | TPL-08 | Cocokkan dengan klaim walkthrough/defense |
| Meeting Log & Peer Assessment | Log pertemuan, kontribusi, umpan balik, refleksi etika | TPL-09 | Bukti anti-free-rider |
| Profil LinkedIn / Portofolio Digital | Foto, headline, about, projects, skills | TPL-10 | Kelengkapan isi |
| Individual Competency Passport | Skor & status klaim 9 kompetensi | TPL-11 | Diisi bertahap; final M16 |

---

# Bagian 5: Asesmen

## 5.1 Skema (default 50/30/20)
| Komponen | Bobot | Bukti |
|---|---|---|
| **Team Evidence** — D1–D4 + kualitas produk | 50% | Rubrik per core artifact |
| **Individual Evidence** — Gate 1 oral defense, Gate 2 code walkthrough | 30% | Rubrik keterampilan per individu |
| **Individual Reflection/Process** — refleksi, kontribusi, decision explanation, journal | 20% | Rubrik Sub-CPMK, passport |

Proporsi default dapat diselaraskan dengan RPS; catat perubahan agar dokumentasi konsisten.

## 5.2 Peran Assessor
- **Dosen pengampu** = teacher assessor: checkpoint formatif, oral/code walkthrough, bukti per Sub-CPMK.
- **Reviewer gate** = verifikator evidence: kecocokan klaim individu vs artefak, AI disclosure, decision log.
- **Pemilik usaha / dosen tamu** = outside expert assessor: menilai produk publik (Demo Day).
- Selalu **asesmen per individu**, bukan hanya nilai kelompok (menghindari free-rider).

## 5.3 Fokus Penilaian
- **Reasoning chain**, bukan hanya artefak akhir: gunakan decision log, oral defense, dan walkthrough sebagai bukti.
- AI bagian mana pun harus bisa dijelaskan & diverifikasi manual oleh mahasiswa.
- Learning journal dinilai per individu, diunggah **per checkpoint** (bukan hanya akhir).

## 5.4 Individual Competency Passport
9 kompetensi: **problem framing, system thinking, computational thinking, programming, testing, communication, collaboration, AI literacy, reflection**. Status klaim: Unggul / Memadai / Berkembang / Belum (rentang 0–100 mengikuti [[output/pbl/level_1/assessment_rubrics|assessment_rubrics]]). Diisi dosen akhir semester dari bukti per Sub-CPMK: S-01.1, S-02.1, S-03.1, S-04.1, S-11.1, S-12.1, S-14.1, S-14.2.

## 5.5 Prosedur Penutupan (Post-Demo Day)
1. **Verifikasi reviewer gate** — klaim individu (score sheet) vs bukti artefak; koreksi bila tidak cocok.
2. **Nilai akhir** — dosen koordinator menetapkan skor per sub-CPMK per mahasiswa.
3. **Passport** — isi status klaim per kompetensi.
4. **Distribusi ke MK** — input nilai per CPMK ke RPS masing-masing MK.
5. **Status** — lulus / remedial per sub-CPMK; remedial = program perbaikan semester berikutnya.
6. **Arsip** — score sheet, bukti, passport, catatan intervensi diarsipkan dosen koordinator.

## 5.6 Rubrik & Referensi
- Rubrik artefak (D1–D4) & per Sub-CPMK: [[output/pbl/level_1/assessment_rubrics|assessment_rubrics]].
- Framework & generic attributes SFIA (L1–L4): [[output/pbl/shared/assessment_framework|assessment_framework]], [[output/pbl/shared/sfia_mapping|sfia_mapping]].
- Score sheet per mahasiswa: [[output/pbl/level_1/instructor_guide|instructor_guide]] 5.1.

---

# Bagian 6: Scaffolding, Coaching & Intervensi

## 6.1 Scaffolding Bertahap (jangan diberikan sekaligus)
| Minggu | Sumber Daya Penopang |
|---|---|
| 1–2 | Template norma + jadwal rotasi phase lead, daftar objek studi aman, contoh need-to-know, panduan wawancara etis |
| 3–4 | Contoh user story & kriteria penerimaan, template metrik, contoh peta komponen SI |
| 5–7 | Template IPO/flowchart, contoh pseudocode, protokol kritik |
| 9–12 | Template log uji, contoh program konsol, checklist walkthrough, hint bertahap |
| 13 | Template AI disclosure, contoh decision log |
| 14–15 | Template executive summary, template slide, rubrik presentasi |
| 16 | Template passport, checklist kelengkapan portfolio |

Prinsip: **fading** — kurangi bantuan saat mahasiswa menunjukkan kemandirian; sesuaikan dukungan agar phase lead mampu memimpin.

## 6.2 Coaching Questions (contoh)
- *"Apa bukti nyata bahwa masalah ini penting bagi pemilik usaha?"*
- *"Kasus input apa yang bisa membuat program ini salah? Bagaimana menanganinya?"*
- *"Jelaskan bagian kode ini baris demi baris — termasuk yang dibantu AI."*
- *"Sebagai phase lead, apa yang kamu rencanakan dan bagaimana kamu menggerakkan anggota?"*
- *"Bagian mana artefak yang dibantu AI, dan bagaimana kalian memverifikasinya (verification note)?"*
- *"Kompetensi apa yang paling berkembang pada dirimu? Apa buktinya?"*

## 6.3 Intervensi Cepat
| Situasi | Tanda | Intervensi |
|---|---|---|
| Tim tidak progres | Tidak ada update checkpoint | Checkpoint mingguan tambahan; breakdown tugas lebih kecil |
| Free-rider | Kontribusi timpang di log | Perkuat log & peer assessment; oral defense individu |
| Phase lead tidak aktif | Fase tidak terkoordinasi | Coaching kepemimpinan; pastikan tiap anggota memimpin satu fase |
| Kode dikerjakan AI penuh | Tidak mampu menjelaskan kode | Ulangi walkthrough; batasi AI sebagai hint |
| Scope melebar | Fitur berlebihan, deliverable molor | Re-negosiasi di GATE 1; dokumentasikan di decision log |
| Konflik tim | Rapat macet | Mediasi; gunakan norma & protokol kritik |
| Masalah etika lapangan | Pemilik keberatan | Hentikan aktivitas; ganti objek studi |
| Bahasa Inggris tertinggal | D4 macet | Peer review & umpan balik bertahap |

## 6.4 Checklist Kesiapan Dosen (Sebelum Semester)
1. [ ] "Do the project yourself": kerjakan D1–D3 singkat untuk memetakan scaffolding & risiko.
2. [ ] Daftar objek studi aman disiapkan.
3. [ ] Entry event direncanakan.
4. [ ] Kalender 16 minggu dibagikan; deadline GATE 1 = 8, GATE 2 = 13, DEMO DAY = 16.
5. [ ] Skema **rotating phase lead** disosialisasikan + template rotasi.
6. [ ] Rubrik & proporsi **50/30/20** dikomunikasikan sejak awal.
7. [ ] Project wall disiapkan (dipasang setelah entry event).
8. [ ] Mitra/pemilik unit usaha dihubungi untuk validasi & Demo Day.
9. [ ] Kebijakan AI + template disclosure & decision log disosialisasikan.
10. [ ] Format **Individual Competency Passport** dibagikan & dijelaskan.