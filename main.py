import argparse
from encoder.image_encoder import encode_image
from decoder.image_decoder import decode_image
from utils.file_utils import file_to_bytes, bytes_to_file
from utils.binary_utils import bytes_to_binary, binary_to_bytes
from crypto.hybrid_encrypt import hybrid_encrypt
from crypto.hybrid_decrypt import hybrid_decrypt

def encode(args):
    file_data = file_to_bytes(args.file)

    encrypted_data = hybrid_encrypt(file_data)

    binary_data = bytes_to_binary(encrypted_data)

    encode_image(args.input, binary_data, args.output)

    print("✅ File encrypted and hidden successfully!")

def decode(args):

    extracted_binary = decode_image(args.input)

    if not extracted_binary:
        print("❌ No hidden data found")
        return

    try:
        encrypted_bytes = binary_to_bytes(extracted_binary)

        decrypted_data = hybrid_decrypt(encrypted_bytes)

        bytes_to_file(decrypted_data, args.output)

        print("🔓 File recovered successfully!")

    except Exception as e:
        print("❌ Error:", e)
def main():
    parser = argparse.ArgumentParser(description="StegoVault Tool 📦")

    subparsers = parser.add_subparsers(dest="command")

    # Encode command
    encode_parser = subparsers.add_parser("encode")
    encode_parser.add_argument("-i", "--input", required=True)
    encode_parser.add_argument("-f", "--file", required=True)
    encode_parser.add_argument("-o", "--output", required=True)

    # Decode command
    decode_parser = subparsers.add_parser("decode")
    decode_parser.add_argument("-i", "--input", required=True)
    decode_parser.add_argument("-o", "--output", required=True)

    args = parser.parse_args()

    if args.command == "encode":
        encode(args)
    elif args.command == "decode":
        decode(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()