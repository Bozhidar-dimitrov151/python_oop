class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics

song = Music("Shape of you", "Ed Sheeran", "I am in love with the shape of you!")
print(song.print_info())
print(song.play())