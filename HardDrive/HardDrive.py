class File:
    def __init__(self, name, size):
        self.name = name     # Fayl nomi
        self.size = size     # Fayl hajmi (MB)


# HardDrive (Qattiq disk) sinfi
class HardDrive:
    def __init__(self, capacity):
        self.capacity = capacity   # Umumiy xotira hajmi (MB)
        self.used = 0              # Band qilingan joy
        self.files = []            # Diskdagi fayllar ro'yxati

    # Fayl yozish
    def write(self, file):
        if self.used + file.size > self.capacity:
            print(f"❌ '{file.name}' faylini yozib bo‘lmaydi! Xotira yetarli emas.")
            return False
        
        # Bunday fayl nomi allaqachon bormi?
        for f in self.files:
            if f.name == file.name:
                print(f"⚠️ '{file.name}' nomli fayl allaqachon mavjud.")
                return False

        self.files.append(file)
        self.used += file.size
        print(f"✅ '{file.name}' ({file.size} MB) fayli yozildi. Band joy: {self.used}/{self.capacity} MB")
        return True

    # Belgilangan miqdorda joyni tozalash
    def remove(self, amount):
        """amount MB joyni tozalaydi (fayllardan kamaytiradi)"""
        if amount <= 0:
            print("⚠️ Tozalash miqdori 0 dan katta bo‘lishi kerak.")
            return False

        if amount > self.used:
            amount = self.used  # Faqat mavjud joyni tozalaydi

        self.used -= amount
        print(f"🧹 {amount} MB joy tozalandi. Qoldi: {self.used}/{self.capacity} MB")
        return True

    # Butun xotirani tozalash
    def clear(self):
        self.files.clear()
        self.used = 0
        print("🗑️ Disk to‘liq tozalandi.")

    # Disk bo‘shligini tekshirish
    def isEmpty(self):
        empty = self.used == 0
        print(f"📀 Disk bo‘sh: {empty}")
        return empty

    # Disk to‘lganligini tekshirish
    def isFull(self):
        full = self.used >= self.capacity
        print(f"💾 Disk to‘lgan: {full}")
        return full

    # Band joyni olish
    def getUsedSpace(self):
        print(f"📊 Band joy: {self.used} MB")
        return self.used

    # Bo‘sh joyni olish
    def getFreeSpace(self):
        free = self.capacity - self.used
        print(f"📉 Bo‘sh joy: {free} MB")
        return free


# ==== Dasturni tekshirish ====
# Qattiq disk 2000 MB
disk = HardDrive(2000)

file1 = File("photo.jpg", 500)
file2 = File("video.mp4", 1200)
file3 = File("doc.pdf", 400)

disk.write(file1)
disk.write(file2)
disk.write(file3)     # Bu yozilmaydi, joy yetmaydi

disk.getUsedSpace()
disk.getFreeSpace()

disk.isFull()
disk.isEmpty()

disk.remove(300)      # 300 MB joy tozalash
disk.getFreeSpace()

disk.clear()          # Diskni to‘liq tozalash
disk.isEmpty()
