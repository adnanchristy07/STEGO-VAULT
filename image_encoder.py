from PIL import Image

DELIMITER = "1111111111111110"

def encode_image(image_path, binary_data, output_path):
    img = Image.open(image_path).convert("RGB")

    binary_text = binary_data + DELIMITER

    data = []
    for y in range(img.height):
        for x in range(img.width):
            data.append(img.getpixel((x, y)))
    new_data = []
    binary_index = 0

    for pixel in data:
        r, g, b = pixel

        if binary_index < len(binary_text):
            r = (r & ~1) | int(binary_text[binary_index])
            binary_index += 1

        if binary_index < len(binary_text):
            g = (g & ~1) | int(binary_text[binary_index])
            binary_index += 1

        if binary_index < len(binary_text):
            b = (b & ~1) | int(binary_text[binary_index])
            binary_index += 1

        new_data.append((r, g, b))

    for i, pixel in enumerate(new_data):
        x = i % img.width
        y = i // img.width
        img.putpixel((x, y), pixel)
    img.save(output_path)

    print("✅ Encoding complete")