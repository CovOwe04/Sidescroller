from Tile import Tile
class World():
    def __init__(self, data):
        self.data = data
        self.frame = 0

    def draw(self, win):
        
        row_count = 0
        for row in self.data:
            col_count = 0
            for tile in row:
                if(tile.image != None):
                    tile.rect.x -= 10
                    win.blit(tile.image, (tile.x - self.frame, tile.y))       
                col_count += 1

            row_count +=1

        self.frame += 10
        if self.frame > 90:
            self.frame = 0
            self.shiftWorld()
        
    
    def shiftWorld(self):
        for y in range(0, len(self.data)):
            for x in range(0, len(self.data[y])):
                if x < len(self.data[y])-1 :
                    self.data[y][x].convertTile(self.data[y][x+1])
                else:
                    self.data[y][x].convertTile(Tile(0, None, x,y))