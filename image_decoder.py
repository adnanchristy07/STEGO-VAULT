from PIL import Image

DELIMITER = "1111111111111110"

def decode_image(image_path):
    img = Image.open(image_path).convert("RGB")
    data = []
    for y in range(img.height):
        for x in range(img.width):
            data.append(img.getpixel((x, y)))

    binary_data = ""

    for pixel in data:
        for value in pixel[:3]:
            binary_data += str(value & 1)

    end_index = binary_data.find(DELIMITER)

    if end_index != -1:
        return binary_data[:end_index]
    else:
        return None