class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.name} ({self.size} MB)"


class HardDrive:
    def __init__(self, capacity):
        self.capacity = capacity
        self.files = []

    def write(self, file):
        if self.getUsedSpace() + file.size > self.capacity:
            print("❌ Joy yetarli emas!")
            return False
        self.files.append(file)
        print(f"✅ {file.name} yozildi ({self.getUsedSpace()}/{self.capacity} MB)")
        return True

    def remove(self, size):
        removed = 0
        while self.files and removed < size:
            f = self.files.pop()
            removed += f.size
        print(f"🗑️ {removed} MB o‘chirildi")

    def clear(self):
        self.files.clear()
        print("🧹 Hard disk tozalandi")

    def isEmpty(self):
        return len(self.files) == 0

    def isFull(self):
        return self.getUsedSpace() >= self.capacity

    def getUsedSpace(self):
        return sum(f.size for f in self.files)

    def getFreeSpace(self):
        return self.capacity - self.getUsedSpace()


# 🔹 Test
h = HardDrive(100)
h.write(File("photo.jpg", 20))
h.write(File("video.mp4", 50))
h.write(File("game.exe", 40))
print("Bo‘sh joy:", h.getFreeSpace())
h.remove(30)
h.clear()
