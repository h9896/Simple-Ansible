import getpass
import paramiko
import os

class SshPrivateKey:
    def __init__(self, private_key_file):
        self.private_key_file = private_key_file
        self.pkey = None
    def read(self) -> bool:
        if os.path.isfile(self.private_key_file):
            pwd = getpass.getpass("Please enter the ssh private key password if necessary:")
            if len(pwd.rstrip()) != 0:
                self.pkey = paramiko.RSAKey.from_private_key_file(self.private_key_file, password= pwd)
            else:
                self.pkey = paramiko.RSAKey.from_private_key_file(self.private_key_file)
        if (self.pkey):
            return True
        else:
            return False