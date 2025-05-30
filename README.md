# Bot Telegram Grub/Channel VVIP
Bot ini adalah bot pembayaran otomatis untuk layanan VVIP Grub dengan fitur pembelian, pengecekan status, dan pengelolaan data pelanggan.


## Fitur
- Pembelian akses VVIP dengan pembayaran melalui QRIS.
- Cek status VVIP pelanggan.
- Proses verifikasi pembayaran manual oleh admin.
- Pengelolaan data pelanggan menggunakan file Excel.
- Auto-kick anggota dari grup jika masa berlaku VVIP habis.


## Instalasi
1. Masukan ID admin dan ID grub : Untuk melihat ID Grub silahkan gunakan grub_id.py, dan kirim pesan apapun ke grub.
  
3. Buat file `.env` dengan isi: TELEGRAM_TOKEN=YOUR_BOT_TOKEN
   
4. Instal dependensi yang dibutuhkan:   pip install python-telegram-bot pandas openpyxl python-dotenv



## Cara Menjalankan
1. Jalankan bot dengan perintah:
   
   python main.py
   
2. Pastikan file `user_data.xlsx` tersedia di direktori `user_data/` dengan format kolom:
   - Chat ID
   - Nama Lengkap
   - Username
   - Status VIP
   - Tanggal Kadaluarsa
   - Sisa Waktu


## Struktur File
- `main.py` : File utama bot.
- `.env` : File untuk menyimpan token bot Telegram.
- `user_data/user_data.xlsx` : File penyimpanan data pelanggan.
- `pay/pay.jpeg` : Gambar bukti pembayaran untuk pengguna yang berhasil membayar.


## Cara Menggunakan
1. **Memulai Bot:**
   - Jalankan `/start` untuk memulai bot.
2. **Pembelian VVIP:**
   - Klik tombol `Beli VVIP`.
3. **Verifikasi Pembayaran:**
   - Kirim bukti pembayaran berupa gambar.
   - Admin akan memverifikasi secara manual.
4. **Cek Status VVIP:**
   - Klik tombol `Status` untuk melihat masa aktif VVIP.
5. **Auto Kick Saat Masa Habis:**
   - Saat masa waktu yang ada di speedsheet Excel sudah habis user akan ter-kick otomatis.
6. **Logika Pengurangan Hari Excel:**
   - Pada Line ke-642 setiap 1 jam file xlsx akan otomatis berubah setiap saat untuk pengurangan hari.
7. **Ubah Nominal Harga Perbulan:**
   - Sesuaikan dengan harga perbulan pada line ke-16.


## Lisensi
File dibuat oleh : Imam Syahru.


### Note!!
Untuk File user_data.xlsx tidak perlu di set apapun, karena sudah otomatis terisi sendiri pada line.

##### Penting!!
Jika anda ingin menggunakan API TELEGRAM_TOKEN langsung di .env Sangat tidak disarankan 
karena bisa di lihat oleh siapapun, jadi disarankan untuk menggunakan .env.example dan 
mengisi TELEGRAM_TOKEN di sana.
