# 🥔 Fitur Tracking & History

## ✨ Fitur Baru yang Ditambahkan

### 1. **Tracking System**
- Setiap kentang yang terdeteksi akan di-track menggunakan centroid (titik pusat bounding box)
- Jika kentang yang sama muncul di frame berikutnya, sistem akan **mengenali** bahwa itu adalah kentang yang sama (tidak dihitung 2x)
- Threshold jarak: 50 pixel - jika centroid baru dalam jarak 50 pixel dari track lama, dianggap sama

### 2. **Detection History (Akumulasi)**
- Setiap deteksi baru akan disimpan ke `potato_history` 
- Counter akumulasi otomatis bertambah untuk setiap deteksi unik:
  - `TotalFresh` - Total kentang segar yang pernah terdeteksi
  - `TotalRotten` - Total kentang busuk yang pernah terdeteksi
- Berbeda dengan `Fresh` dan `Rotten` yang hanya menampilkan deteksi di frame saat ini

### 3. **Halaman History**
Klik tombol **"📊 Detection History"** untuk melihat:
- 📊 Statistik total deteksi
- 🟢 Total Segar yang terdeteksi
- 🔴 Total Busuk yang terdeteksi
- 📋 Tabel lengkap dengan waktu dan posisi setiap deteksi
- 🗑️ Tombol untuk clear history

## 📊 Tampilan di Webcam

Frame live webcam sekarang menampilkan 2 set angka:
```
Frame: X               ← Deteksi pada frame saat ini
Fresh: X              ← Segar pada frame saat ini
Rotten: X             ← Busuk pada frame saat ini

Total Fresh (Accumulated): X    ← TOTAL SEGAR (akumulasi)
Total Rotten (Accumulated): X   ← TOTAL BUSUK (akumulasi)
```

## 🔧 Cara Kerja Tracking

1. **Deteksi baru** → Hitung centroid (x, y)
2. **Cek dalam history** → Apakah centroid mirip dengan track lama?
3. **Jika mirip** → Update posisi, jangan increment counter
4. **Jika baru** → Tambah ke history dan increment counter
5. **Cleanup** → Hapus track yang sudah 2 detik tidak terlihat

## 📝 API Endpoints

### GET `/api/history`
Ambil semua data history
```json
{
  "total_detections": 15,
  "fresh_count": 10,
  "rotten_count": 5,
  "history": [...]
}
```

### GET `/api/history/clear`
Reset semua counter dan history

### GET `/api/count`
Ambil count real-time (termasuk accumulated)
```json
{
  "potato": 5,
  "fresh": 3,
  "rotten": 2,
  "total_fresh": 25,
  "total_rotten": 18,
  "total_all": 43
}
```

## 🎯 Contoh Penggunaan

**Skenario:** Anda melintas 10 kentang di depan kamera
- Frame 1-5: Deteksi 5 kentang (3 segar, 2 busuk)
  - `total_fresh = 3, total_rotten = 2`
- Frame 6-10: Sama 5 kentang bergeser posisi (tracking mengenali)
  - **Tidak ada increment**, tetap `total_fresh = 3, total_rotten = 2`
- Frame 11: Kentang baru masuk (5 baru, 4 segar, 1 busuk)
  - `total_fresh = 7, total_rotten = 3` ✓ Increment hanya untuk kentang baru

---

**Status:** ✅ Semua fitur sudah diintegrasikan dan siap digunakan!
