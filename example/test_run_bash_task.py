from simple_ansible.connection.ssh_connection import SshConnection
from simple_ansible.read import read_hosts, read_yaml, read_ssh_private_key
from simple_ansible.process.run_bash_task import RunBashTask
import os

def run_test():
    result = False
    local = os.path.dirname(os.path.abspath(__file__))
    pkey_path = os.path.join(local, "id_rsa")
    sample_yaml = os.path.join(local, "sample.yaml")
    sample_host = os.path.join(local, "sampleHost.txt")
    private_key = read_ssh_private_key.SshPrivateKey(pkey_path)
    private_key.read()
    ssh = SshConnection(private_key.pkey)
    bash_task = RunBashTask(ssh)
    hosts = read_hosts.ReadHosts(sample_host)
    task_yaml = read_yaml.ReadYaml(sample_yaml)
    if(hosts.read()):
        if(task_yaml.read()):
            for item in task_yaml.data:
                if "hosts" in item and "tasks" in item:
                    if item["hosts"] in hosts.data:
                        for host in hosts.data[item["hosts"]]:
                            result = bash_task.run(host, "root", item["tasks"])
    if (result):
        pass
    else:
        print("Error")

if __name__ =='__main__': 
    run_test()