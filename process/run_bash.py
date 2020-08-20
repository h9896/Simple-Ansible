import subprocess
from paramiko import SSHClient
class RunBash:
    def __init__(self):
        pass
    def run(self, cmd) -> dict:
        process = subprocess.Popen(cmd.split(), stdout = subprocess.PIPE)
        output, error = process.communicate()
        if (output):
            print(r'{}'.format(output))
        if (error):
            return {"Result": "Fail", "Output": output, "Error": error}
        else:
            return {"Result": "Success", "Output": output, "Error": None}
    def run_remote(self, cmd, client:SSHClient) -> dict:
        stdin, stdout, stderr = client.exec_command(cmd)
        stdout = stdout.readlines()
        if (stdout):
            for output in stdout:
                print(r'{}'.format(output.rstrip()))
        stderr = stderr.readlines()
        if (stderr):
            return {"Result": "Fail", "Output": stdout, "Error": stderr}
        else:
            return {"Result": "Success", "Output": stdout, "Error": None}