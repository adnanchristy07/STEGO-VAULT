def bytes_to_binary(data):
    return ''.join(format(byte, '08b') for byte in data)

def binary_to_bytes(binary):
    byte_chunks = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return bytes([int(b, 2) for b in byte_chunks])