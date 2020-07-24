class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


title = input()
painter = input()
year = int(input())

new_painting = Painting(title, painter, year)

print(f'"{new_painting.title}" by {new_painting.painter} ({new_painting.year}) hangs in the {Painting.museum}.')


