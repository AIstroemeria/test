from PIL import Image

def pic2ascii(pic, asciis, zoom, vscale):
    img = Image.open(pic)
    temp = img.convert("L")
    width, height = temp.size
    temp = temp.resize((int(width * zoom), int(height * zoom * vscale)))
    width, height = temp.size
    chara_len = len(asciis)
    texts = ""

    for row in range(height):
        for col in range(width):
            gray = temp.getpixel((col,row))
            texts += asciis[int(gray / 255 * (chara_len -1))]
        texts += '\n'

    return texts

def main():
    pic = input("请输入图片位置:")
    asciis = "@%#*+=-:. "
    zoom = 0.5
    vscale = 0.5
    texts = pic2ascii(pic, asciis, zoom, vscale)

    with open("C:\\Users\\hn810\\Desktop\\result.txt","w") as file:
        file.write(texts)

if __name__ == "__main__":
    main()
        
