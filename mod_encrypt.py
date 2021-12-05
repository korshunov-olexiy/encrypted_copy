# *-* encoding=utf-8
from pathlib import Path, PosixPath, WindowsPath
import pyAesCrypt, pickle
from typing import Optional, List
from collections import UserDict

# Decorator for file type constants.
def constant(f):
    def fset(self, value): raise TypeError
    def fget(self): return f()
    return property(fget, fset)


# Classes for choosing constants 'all', 'files', 'dirs'
class TypeOfShowObject(object):
    @constant
    def ALL(): return 'all'
    @constant
    def FILES(): return 'files'
    @constant
    def DIRS(): return 'dirs'
    @constant
    def ERROR(): return 'error'


typeObj = TypeOfShowObject()


class EncryptFiles(UserDict):
    def __init__(self, file_name: str, input_dir: str, output_dir: str, pwd: str, extension: str = "*") -> None:
        self.data["input_dir"] = Path(input_dir)
        self.data["output_dir"] = Path(output_dir)
        self.data["extension"] = extension
        self.data["input_files"] = []
        self.data["output_files"] = []
        self.data["password"] = pwd
        if not self.load_data(file_name):
            self.get_files_in_dir()

    def get_files_in_dir(self) -> Optional[List]:
        if self.data["input_dir"].is_dir():
            for os_obj in self.data["input_dir"].rglob(self.data["extension"]):
                if os_obj.is_file():
                    self.data["input_files"].append(os_obj)
                    out_file = Path(str(os_obj).replace(str(self.data["input_dir"]), str(self.data["output_dir"])))
                    self.data["output_files"].append(Path(str(out_file.parent / out_file.stem) + ".aes"))

    def encrypt_files_in_dir(self) -> bool:
        for index in range(len(self.data["input_files"])):
            pyAesCrypt.encryptFile(self.data["input_files"][index], self.data["output_files"][index], self.data["password"] )
            # if self.output_dir.is_dir():
            #     makedirs(dir, exist_ok=True)
            # yield pyAesCrypt.encryptFile(file, self.list_out_path_with_files[i] + self.crypt_ext, self.pwd, self.bufferSize)

    def save_data(self, filename: str) -> None:
        try:
            with open(filename, "wb") as fn:
                pickle.dump(self.data, fn)
            print(f"Saving to file \"{filename}\" is successfully")
        except (FileNotFoundError, AttributeError, MemoryError):
            print(f"An error occurred while saving the file \"{filename}\"")

    def load_data(self, filename: str) -> None:
        try:
            with open(filename, 'rb') as fn:
                self.data = pickle.load(fn)
            print(f"Loading from file \"{filename}\" is successfully")
        except (FileNotFoundError, AttributeError, MemoryError):
            print(f"An error occurred while opening the file \"{filename}\"")


if __name__ == "__main__":
    inp_dir = r"d:\MyProjects\encrypted_copy\test"
    out_dir = r"d:\MyProjects\encrypted_copy\test_enc"
    data_file = Path("data.bin")
    enc_cls = EncryptFiles(data_file, inp_dir, out_dir, "pwd103")
    print(enc_cls.output_files)
    pickle.dump(enc_cls, data_file)
