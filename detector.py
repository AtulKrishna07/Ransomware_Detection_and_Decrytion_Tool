import os
from utils import calculate_entropy

def scan_directory_for_encrypted_files(folder):
    suspicious = []
    for root, _, files in os.walk(folder):
        for f in files:
            full_path = os.path.join(root, f)
            try:
                with open(full_path, "rb") as file:
                    data = file.read()
                    entropy = calculate_entropy(data)
                    if entropy > 2.0:
                        suspicious.append({"path": full_path, "entropy": round(entropy, 2)})
            except Exception:
                continue
    return suspicious
