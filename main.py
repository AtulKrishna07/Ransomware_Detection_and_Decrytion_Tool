import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from detector import scan_directory_for_encrypted_files
from decryptor import try_basic_decryption
from utils import calculate_entropy

class RansomwareToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ransomware Analysis, Detection, and Decryption Tool")
        self.root.geometry("800x500")

        self.label = tk.Label(root, text="Ransomware Detection and Decryption", font=("Arial", 16))
        self.label.pack(pady=10)

        # Buttons
        self.folder_button = tk.Button(root, text="Scan Folder", width=20, command=self.browse_folder)
        self.folder_button.pack(pady=5)

        self.file_button = tk.Button(root, text="Scan Files", width=20, command=self.browse_files)
        self.file_button.pack(pady=5)

        # Treeview
        self.tree = ttk.Treeview(root, columns=("File", "Entropy"), show="headings")
        self.tree.heading("File", text="Suspicious File")
        self.tree.heading("Entropy", text="Entropy")
        self.tree.column("File", width=600)
        self.tree.column("Entropy", width=100)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        self.decrypt_button = tk.Button(root, text="Attempt Decryption", command=self.decrypt_files, state=tk.DISABLED)
        self.decrypt_button.pack(pady=10)

        self.suspicious_files = []

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return

        self.tree.delete(*self.tree.get_children())
        self.suspicious_files = scan_directory_for_encrypted_files(folder)

        if not self.suspicious_files:
            messagebox.showinfo("Result", "No suspicious files found.")
            return

        for f in self.suspicious_files:
            self.tree.insert("", tk.END, values=(f["path"], f["entropy"]))

        self.decrypt_button.config(state=tk.NORMAL)

    def browse_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("All Files", "*.*")])
        if not file_paths:
            return

        self.tree.delete(*self.tree.get_children())
        self.suspicious_files = []

        for path in file_paths:
            try:
                with open(path, "rb") as f:
                    data = f.read()
                    entropy = calculate_entropy(data)
                    if entropy > 7.5:
                        self.suspicious_files.append({"path": path, "entropy": round(entropy, 2)})
            except Exception:
                continue

        if not self.suspicious_files:
            messagebox.showinfo("Result", "No suspicious files found.")
            return

        for f in self.suspicious_files:
            self.tree.insert("", tk.END, values=(f["path"], f["entropy"]))

        self.decrypt_button.config(state=tk.NORMAL)

    def decrypt_files(self):
        for file_data in self.suspicious_files:
            decrypted = try_basic_decryption(file_data["path"])
            if decrypted:
                messagebox.showinfo("Decryption", f"Decrypted: {file_data['path']}")
            else:
                messagebox.showwarning("Decryption Failed", f"Failed: {file_data['path']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RansomwareToolGUI(root)
    root.mainloop()
