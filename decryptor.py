def try_basic_decryption(file_path, key=0x42):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        decrypted = bytes([b ^ key for b in data])

        output_file = file_path + ".decrypted"
        with open(output_file, "wb") as f:
            f.write(decrypted)

        return True
    except Exception:
        return False
