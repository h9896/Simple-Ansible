import os
class ReadHosts:
    def __init__(self, path):
        self.path = path
        self.data = dict()
    def read(self) -> bool:
        if os.path.isfile(self.path):
            with open(self.path, 'r') as stream:
                group = None
                server_list = list()
                context = stream.read().split("\n")
                for item in context:
                    temp = item.rstrip()
                    if temp == "":
                        if server_list:
                            self.data[group] = server_list
                        group = None
                    else:
                        if temp[0] == "[" and temp[-1] == "]":
                            if(group):
                                self.data[group] = server_list
                            group = temp[1:-1]
                            server_list = list()
                        else:
                            if(group):
                                server_list.append(temp)
                            else:
                                self.data[temp] = temp
                if(group):
                    self.data[group] = server_list
        if (self.data):
            return True
        else:
            return False