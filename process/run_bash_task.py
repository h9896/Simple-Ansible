from simple_ansible.connection.ssh_connection import SshConnection
from simple_ansible.process.run_bash import RunBash
class RunBashTask(RunBash):
    def __init__(self, ssh_connected: SshConnection):
        self.ssh_connected = ssh_connected
        self.result = dict()
    def run(self, server, user, tasks) -> bool:
        client = self.ssh_connected.connected(server, user)
        if (client):
            for mission in tasks:
                if "bash" in mission and "name" in mission:
                    mission_result = super().run_remote(mission["bash"], client)
                    if(mission_result["Result"] == "Success"):
                        print("-"*50)
                        print("{task} -> Success on {host}".format(task = mission["name"], host = server))
                        print("-"*50)
                    else:
                        print("-"*50)
                        print("{task} -> Fail {host}".format(task = mission["name"], host = server))
                        print("-"*50)
                    self.result[mission["name"]] = mission_result
            client.close()
            return True
        else:
            for mission in tasks:
                if "bash" in mission and "name" in mission:
                    mission_result = {"Result": "Fail", "Output": None, "Error": "The server {host} connection fail, Please check user and password".format(host = server)}
                    self.result[mission["name"]] = mission_result
            return False