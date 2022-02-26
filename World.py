class World():
    def __init__(self, data):
        self.data = data

    def draw(self, win):
        row_count = 0
        for row in self.data:
            col_count = 0
            for tile in row:
                if(tile.image != None):
                    win.blit(tile.image, tile.rect)       
                col_count += 1

            row_count +=1