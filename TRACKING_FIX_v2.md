# 🔧 Perbaikan Tracking System v2

## ❌ Masalah Lama
Kentang terdeteksi ulang setiap kali posisinya berubah sedikit, membuat counter akumulasi terus bertambah.

## ✅ Solusi yang Diterapkan

### 1. **Increase Distance Threshold**
- **Sebelum**: 50 pixel
- **Sesudah**: 150 pixel ✨
- Artinya: Kentang yang bergerak sampai 150 pixel masih dianggap **SAMA**

### 2. **Add Size-Based Matching**
Sekarang tracking tidak hanya lihat **posisi** (centroid), tapi juga **ukuran** bounding box:
```
Jika width dan height berbeda >50%, kemungkinan bukan object yang sama
```

Contoh:
- Kentang A: 100x80 pixel
- Deteksi baru: 95x85 pixel → **MATCH** (mirip, same object) ✅
- Deteksi baru: 30x25 pixel → **NO MATCH** (terlalu kecil, berbeda object) ❌

### 3. **Increase Timeout**
- **Sebelum**: 2 detik
- **Sesudah**: 3 detik
- Kentang yang hilang dari frame akan tetap diingat selama 3 detik

## 📊 Cara Kerja Baru

```
Frame 1: Deteksi kentang A di (200, 300), ukuran 100x80
  → Track baru, counter = 1 ✓

Frame 2: Kentang A bergeser ke (250, 320), ukuran 102x82
  → Jarak dari (200,300) = 50 pixel < 150 ✓
  → Ukuran mirip (102/100 = 1.02) ✓
  → **MATCH** → Update track, counter tetap 1 ✓

Frame 3: Kentang baru masuk di (100, 100), ukuran 95x75
  → Jarak dari (250,320) = 260 pixel > 150 ❌
  → **NO MATCH** → Track baru, counter = 2 ✓
```

## 🎯 Hasil yang Diharapkan

- ✅ Kentang bergerak halus tidak akan dihitung 2x
- ✅ Kentang yang benar-benar berbeda akan dihitung sekali saja
- ✅ Akumulasi counter akan lebih akurat

---

**Status**: ✅ Perbaikan sudah diterapkan, coba test sekarang!
