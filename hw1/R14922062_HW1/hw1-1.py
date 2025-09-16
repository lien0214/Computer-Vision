from PIL import Image

def getUpSideDown(img: Image.Image) -> Image.Image:
    column, row = img.size
    newImg = Image.new('L', (column, row))
    [newImg.putpixel((c, r), img.getpixel((c, row - 1 - r))) for r in range(row) for c in range(column)]
    return newImg

def getRightSideLeft(img: Image.Image) -> Image.Image:
    column, row = img.size
    newImg = Image.new('L', (column, row))
    [newImg.putpixel((c, r), img.getpixel((column - 1 - c, r))) for r in range(row) for c in range(column)]
    return newImg

def getDiagonallyMirrored(img: Image.Image) -> Image.Image:
    column, row = img.size
    newImg = Image.new('L', (row, column))
    [newImg.putpixel((c, r), img.getpixel((r, c))) for r in range(column) for c in range(row)]
    return newImg

def processImage(img: Image.Image) -> None:
    upSideDown = getUpSideDown(img)
    rightSideLeft = getRightSideLeft(img)
    diagonallyMirrored = getDiagonallyMirrored(img)

    upSideDown.save('./images/up-side-down.bmp')
    rightSideLeft.save('./images/right-side-left.bmp')
    diagonallyMirrored.save('./images/diagonally-mirrored.bmp')

if __name__ == '__main__':
    lena = Image.open('./images/lena.bmp')
    processImage(lena)
