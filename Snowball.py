class Snowball:
    def __init__(self, positionX, positionY):
        self.x = positionX
        self.y = positionY

    def fall(self):
        self.y -= 1