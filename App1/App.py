class App:
    def __init__(self, name, size):
        self.name = name        # Dastur nomi
        self.size = size        # Dastur hajmi (MB)
        self.isRunning = False  # Dastur ishga tushganmi yoki yo'qmi


# Device (Qurilma) sinfi
class Device:
    def __init__(self, memory):
        self.memory = memory            # Qurilmaning umumiy xotirasi (MB)
        self.used_memory = 0            # Band qilingan xotira
        self.installed_apps = []        # O'rnatilgan dasturlar ro'yxati
        self.running_apps = []          # Ishga tushgan dasturlar ro'yxati

  
    def install(self, app):
        # Avval tekshiramiz — bunday nomli dastur allaqachon o‘rnatilganmi?
        for a in self.installed_apps:
            if a.name == app.name:
                print(f"⚠️ '{app.name}' allaqachon o‘rnatilgan.")
                return False
        
        if self.used_memory + app.size > self.memory:
            print(f"❌ '{app.name}' uchun xotira yetarli emas!")
            return False
        
        
        self.installed_apps.append(app)
        self.used_memory += app.size
        print(f"✅ '{app.name}' dasturi o‘rnatildi. Band xotira: {self.used_memory}/{self.memory} MB")
        return True

    def showApps(self):
        if not self.installed_apps:
            print("📱 Qurilmada hech qanday dastur o‘rnatilmagan.")
        else:
            print("📱 Qurilmadagi dasturlar:")
            for app in self.installed_apps:
                print(f" - {app.name} ({app.size} MB)")

    def uninstall(self, app_name):
        for a in self.installed_apps:
            if a.name == app_name:
                self.installed_apps.remove(a)
                self.used_memory -= a.size
                print(f"🗑️ '{a.name}' o‘chirildi. Qolgan xotira: {self.memory - self.used_memory} MB")
                return True
        print(f"⚠️ '{app_name}' topilmadi, o‘chirish amalga oshmadi.")
        return False


    def run(self, app_name):
        for a in self.installed_apps:
            if a.name == app_name:
                if a not in self.running_apps:
                    self.running_apps.append(a)
                a.isRunning = True
                print(f"▶️ '{a.name}' ishga tushirildi.")
                return True
        print(f"❌ '{app_name}' o‘rnatilmagan, ishga tushirib bo‘lmaydi.")
        return False

    
    def info(self):
        print(f"\nℹ️ Ishga tushgan dasturlar soni: {len(self.running_apps)}")
        if not self.running_apps:
            print("Hech qanday dastur hozircha ishga tushmagan.")
        else:
            print("Ishlayotgan dasturlar:")
            for a in self.running_apps:
                print(f" - {a.name} ({a.size} MB)")


app1 = App("Telegram", 200)
app2 = App("Instagram", 300)
app3 = App("PUBG", 1500)
app4 = App("TikTok", 250)

device = Device(2000)

device.install(app1)
device.install(app2)
device.install(app3)
device.install(app4)

print("\n--- O‘rnatilgan dasturlar ---")
device.showApps()

device.run("Telegram")
device.run("PUBG")
device.run("YouTube")  

device.info()

device.uninstall("Instagram")
device.uninstall("YouTube")  
device.showApps()
