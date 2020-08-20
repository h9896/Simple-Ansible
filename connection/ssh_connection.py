import getpass
import paramiko
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException

class SshConnection:
    def __init__(self, pkey):
        self.pkey = pkey
    def connected(self, host, user, port = 22) -> paramiko.SSHClient:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if self.pkey:
            try:
                client.connect(hostname = host, port = port, username = user, pkey = self.pkey, timeout=4)
            except NoValidConnectionsError as err:
                    return None
            except AuthenticationException as err:
                    return None
        else:
            pwd = getpass.getpass("Please enter password of the user:")
            try:
                client.connect(hostname = host, port = port, username = user, password = pwd, timeout=4)
            except NoValidConnectionsError as err:
                    return None
            except AuthenticationException as err:
                    return None
        return client