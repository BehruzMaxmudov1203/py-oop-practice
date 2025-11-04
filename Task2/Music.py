class Music:
    def __init__(self, name: str, album: str, time: str, title: str, text: str):
        self.name = name
        self.album = album
        self.time = time
        self.title = title
        self.text = text

    def play(self):
        """Musiqa ijro etilmoqda"""
        print(f"Musiqa '{self.title}' ijro etilmoqda...")


m = Music("SongName", "Album1", "3:45", "MySong", "Lyrics")
m.play()