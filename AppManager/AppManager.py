class App:
    def __init__(self, name: str, developer: str, version: str):
        self.name = name
        self.developer = developer
        self.version = version

    def __eq__(self, other):
        if not isinstance(other, App):
            return False
        return (self.name, self.developer, self.version) == (other.name, other.developer, other.version)

    def __hash__(self):
        return hash((self.name, self.developer, self.version))

    def __repr__(self):
        return f"App({self.name}, {self.developer}, {self.version})"


class AppManager:
    def __init__(self):
        self.apps = set()  # Set of App objects
        self.app_statuses = {}  # {App: status}
        self.app_usage_stats = {}  # {App: usage_count}

    def add_app(self, app: App) -> bool:
        """Yangi ilovani qo‘shadi, agar mavjud bo‘lsa False qaytaradi"""
        if app in self.apps:
            return False
        self.apps.add(app)
        self.app_statuses[app] = "to‘xtatilgan"  # default status
        self.app_usage_stats[app] = 0
        return True

    def remove_app(self, app: App) -> bool:
        """Ilovani o‘chiradi"""
        if app not in self.apps:
            return False
        self.apps.remove(app)
        self.app_statuses.pop(app, None)
        self.app_usage_stats.pop(app, None)
        return True

    def update_app_status(self, app: App, status: str) -> bool:
        """Ilovaning holatini yangilaydi"""
        valid_statuses = {"faol", "mashg‘ul", "to‘xtatilgan"}
        if app not in self.apps or status not in valid_statuses:
            return False
        self.app_statuses[app] = status
        return True

    def increment_app_usage(self, app: App):
        """Ilova ishlatilganini kuzatadi"""
        if app in self.apps:
            self.app_usage_stats[app] += 1

    def get_most_used_app(self):
        """Eng ko‘p ishlatilgan ilovani qaytaradi"""
        if not self.app_usage_stats:
            return None
        return max(self.app_usage_stats.items(), key=lambda x: x[1])[0]

    def get_apps_by_status(self, status: str):
        """Berilgan holatdagi ilovalar ro‘yxatini qaytaradi"""
        return {app for app, s in self.app_statuses.items() if s == status}


def main():
    app1 = App("Telegram", "Telegram LLC", "1.0.0")
    app2 = App("Instagram", "Meta", "2.5.3")
    app3 = App("Spotify", "Spotify AB", "3.8.1")

    manager = AppManager()

    assert manager.add_app(app1) is True
    assert manager.add_app(app2) is True
    assert manager.add_app(app1) is False  # already exists

    assert manager.update_app_status(app1, "faol") is True
    assert manager.update_app_status(app3, "faol") is False  # app3 not added
    assert manager.update_app_status(app2, "mashg‘ul") is True

    manager.increment_app_usage(app1)
    manager.increment_app_usage(app1)
    manager.increment_app_usage(app2)

    assert manager.get_most_used_app() == app1

    active_apps = manager.get_apps_by_status("faol")
    assert len(active_apps) == 1

    print("All tests passed ✅")

main()
