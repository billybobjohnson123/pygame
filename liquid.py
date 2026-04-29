


class Liquid:
    def __init__(self, x, y, scale, start_tick):
        self.flowDistance = 0
        self.flowSpeed = 0
        self.source = [(x // scale) * scale, (y // scale) * scale]
        self.liquidPosition = [self.source]
        self.scale = scale
        self.directions = [[0,1*scale], [1*scale,0], [-1*scale, 0], [0,-1*scale]]
        self.start_tick = start_tick
        self.numberTimesFlowed = 0

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
    
    def tick(self, current_tick):
        if (current_tick - self.start_tick) // 500 > self.numberTimesFlowed:
            self.numberTimesFlowed += 1
            self.flow()



        