def setup():
    size(600, 400)
    yCoordinate = 50
    xCoordinate = 50
    yspeed = 6
    xspeed = 8
    ellipseSize = 50
global ellipSize

def brick(topRight, topLeft, bWidth, bHeight):
    fill(255,0,0)
    rect(topRight, topLeft, bWidth, bHeight)
    rect(topRight + 50, topLeft, bWidth, bHeight)
    rect(topRight + 100, topLeft, bWidth, bHeight)
    rect(topRight + 150, topLeft, bWidth, bHeight)
    rect(topRight + 200, topLeft, bWidth, bHeight)
    rect(topRight + 250, topLeft , bWidth, bHeight)
    rect(topRight + 300, topLeft, bWidth, bHeight)
    rect(topRight + 350, topLeft, bWidth, bHeight)
    rect(topRight + 400, topLeft, bWidth, bHeight)
    rect(topRight + 450, topLeft, bWidth, bHeight)
    rect(topRight + 500, topLeft, bWidth, bHeight)
    rect(topRight + 550, topLeft, bWidth, bHeight)
def draw():
    
    k=random(23, 50)
    background(0)
    brick(0, 0, 50, 60)
    global xCoordinate, yCoordinate, xspeed, yspeed, ellipseSize
    yCoordinate = 50
    xCoordinate = 50
    yspeed = 6
    xspeed = 8
    yCoordinate = 50
    xCoordinate = 50
    ellipseSize = 50
    
    leftBoundary = ellipseSize / 2
    rightBoundary = 600 - ellipseSize / 2
    topBoundary = ellipseSize / 2
    bottomBoundary = 400 - ellipseSize / 2
    xCoordinate += xspeed
    yCoordinate += yspeed

    if xCoordinate >= rightBoundary or xCoordinate <= leftBoundary:
        xspeed = -xspeed
    
    if yCoordinate >= bottomBoundary or yCoordinate <= topBoundary:
        yspeed = - yspeed
    fill(57, 100, 130)
    ellipse(xCoordinate, yCoordinate, ellipseSize,ellipseSize)

    rect(mouseX, 375, 40, 20)
