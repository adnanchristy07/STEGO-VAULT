def file_to_bytes(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def bytes_to_file(data, output_path):
    with open(output_path, 'wb') as file:
        file.write(data)