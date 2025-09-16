from pathlib import Path
from PIL import Image

def rotate_45_clockwise(img: Image.Image) -> Image.Image:
    return img.rotate(-45, expand=True, fillcolor=0)

def shrink_half(img: Image.Image) -> Image.Image:
    w, h = img.size
    return img.resize((w // 2, h // 2), resample=Image.Resampling.BOX)

def binarize_128(img: Image.Image) -> Image.Image:
    return img.point(lambda p: 255 if p >= 128 else 0, mode='1').convert('L')

def processImage(img: Image.Image) -> None:
    rotated = rotate_45_clockwise(img)
    shrunk = shrink_half(img)
    binarized = binarize_128(img)

    rotated.save('./images/rotated-45.bmp')
    shrunk.save('./images/shrink-half.bmp')
    binarized.save('./images/binarize-128.bmp')

if __name__ == '__main__':
    lena = Image.open('./images/lena.bmp').convert('L')
    processImage(lena)
