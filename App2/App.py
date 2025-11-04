class App:
    def __init__(self, name: str, size: int):
        self.name = name      # dastur nomi
        self.size = size      # dastur hajmi (MB)


class Device:
    def __init__(self, memory_size: int):
        self.memory_size = memory_size         # qurilma umumiy xotirasi (MB)
        self.installed_apps: dict[str, App] = {}  # o'rnatilgan dasturlar
        self.used_memory = 0                   # ishlatilgan xotira
        self.run_count = 0                     # ishlatilgan dasturlar soni

    def install(self, app: App) -> bool:
        """Dastur o'rnatish, agar mavjud bo'lmasa va xotira yetarli bo'lsa."""
        if app.name in self.installed_apps:
            print(f"{app.name} allaqachon o'rnatilgan.")
            return False
        if self.used_memory + app.size > self.memory_size:
            print(f"{app.name} dasturini o'rnatish uchun xotira yetarli emas.")
            return False
        self.installed_apps[app.name] = app
        self.used_memory += app.size
        print(f"{app.name} muvaffaqiyatli o'rnatildi.")
        return True

    def show_apps(self):
        """Barcha o'rnatilgan dasturlarni chiqarish."""
        if not self.installed_apps:
            print("Hozircha dastur o'rnatilmagan.")
            return
        print("O'rnatilgan dasturlar:")
        for app in self.installed_apps.values():
            print(f"- {app.name} ({app.size} MB)")

    def uninstall(self, app_name: str) -> bool:
        """Dastur nomi bo'yicha o'chirish."""
        if app_name not in self.installed_apps:
            print(f"{app_name} dasturi o'rnatilmagan.")
            return False
        app = self.installed_apps.pop(app_name)
        self.used_memory -= app.size
        print(f"{app_name} dasturi muvaffaqiyatli o'chirildi.")
        return True

    def run(self, app_name: str):
        """Dastur ishga tushurish."""
        if app_name not in self.installed_apps:
            print(f"{app_name} dasturi o'rnatilmagan.")
            return
        app = self.installed_apps[app_name]
        self.run_count += 1
        print(f"{app.name} ishlamoqda ({app.size} MB)...")

    def info(self):
        """Umumiy ishlatilgan dasturlar soni va o'rnatilgan dasturlarni chiqarish."""
        print(f"Umumiy ishlatilgan dasturlar soni: {self.run_count}")
        self.show_apps()


# ===== Misol ishlatish =====
if __name__ == "__main__":
    app1 = App("Telegram", 7)
    app2 = App("Minecraft", 50)
    device = Device(120)

    device.install(app1)      # True, o'rnatildi
    device.install(app2)      # True, o'rnatildi
    device.install(app1)      # False, allaqachon o'rnatilgan

    device.show_apps()        # barcha dasturlarni ko'rsatish

    device.run("Telegram")    # Telegram ishga tushdi
    device.run("WhatsApp")    # o'rnatilmagan dastur

    device.info()             # ishga tushirilgan dasturlar soni va ro'yxat

    device.uninstall("Telegram")  # True, o'chirildi
    device.uninstall("Telegram")  # False, allaqachon o'chirilgan
