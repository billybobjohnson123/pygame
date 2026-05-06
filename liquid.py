


class Liquid:
    def __init__(self, x, y, scale, start_tick, maxDistance):
        self.maxDistance = maxDistance
        self.flowSpeed = 0
        self.source = [(x // scale) * scale, (y // scale) * scale]
        self.liquidPosition = [self.source]
        self.scale = scale
        self.directions = [[0,1*scale], [1*scale,0], [-1*scale, 0], [0,-1*scale]]
        self.start_tick = start_tick
        self.numberTimesFlowed = 0
        self.dryPositions = []
        self.pickuptime = 0
        self.numberTimesDryed = 0

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

    def pickUp(self, pickuptime):
        self.pickuptime = pickuptime

        print(self.liquidPosition)
        self.dryPositions.append(self.source)
        self.liquidPosition.remove(self.source)
        self.source = []
        print(self.liquidPosition)

    def unflow(self):
        newDryPositions = []
        newDryPositionsSet = set()
        for x, y in self.dryPositions:
            if (x, y) not in newDryPositionsSet:
                newDryPositions.append([x,y])
                newDryPositionsSet.add((x,y))
            for dx, dy in self.directions:
                if (x+dx, y+dy) not in newDryPositionsSet:
                    newDryPositions.append([x+dx, y+dy])
                    newDryPositionsSet.add((x+dx, y+dy))
        self.removeLiquidFromDry()

    def removeLiquidFromDry(self):
        for i in range(len(self.dryPositions)):
            if self.dryPositions[i] in self.liquidPosition:
                self.liquidPosition.remove(self.dryPositions[i])

    def tick(self, current_tick):
        if (current_tick - self.start_tick) // 500 > self.numberTimesFlowed:
            if self.numberTimesFlowed < self.maxDistance - 1:
                self.numberTimesFlowed += 1
                self.flow()
        if self.pickuptime != 0:
            if (current_tick - self.pickuptime) // 500 > self.numberTimesDryed:
                self.numberTimesDryed += 1
                self.unflow()

                print("ran")  