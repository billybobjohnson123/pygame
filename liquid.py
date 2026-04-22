


class Liquid:
    def __init__(self, x, y, scale):
        self.flowDistance = 0
        self.flowSpeed = 0
        self.source = [x, y]
        self.liquidPosition = [self.source]
        self.scale = scale
        self.directions = [[0,1*scale], [1*scale,0], [-1*scale, 0], [0,-1*scale]]

    def flow(self):
        newLiquidPositions = []
        newLiquidPositionsSet = set()
        for x, y in self.liquidPosition:
            if (x, y) not in newLiquidPositionsSet:
                newLiquidPositions.append([x,y])
                newLiquidPositionsSet.add((x,y))
            for dx, dy in self.directions:
                if (x+dx, y+dy) not in newLiquidPositionsSet:
                    newLiquidPositions.append([x+dx, y+dy])
                    newLiquidPositionsSet.add((x+dx, y+dy))

        self.liquidPosition = newLiquidPositions