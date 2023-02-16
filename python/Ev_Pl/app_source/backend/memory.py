# Memory object

# ______________

class Memory(dict):

    def listProcesses(self):
        return list(self.keys())

    def addProcess(self,process,data):
        if process not in self.listProcesses():
            self[process] = data
        else:
            self.updateProcessData(process,data)

    def init_processes(self, *processes):
        for process in processes:
            self.addProcess(process, None)

    def updateProcessData(self,process,data):
        if type(self[process]) == list:
            if type(data) == list:
                for item in data:
                    self[process].append(item)
            else:
                self[process].append(data)
        else:
            self[process] = data

    def removeProcess(self,process):
        del self[process]

    def clearProcess(self,process):
        if type(self[process]) == list:
            self[process] = []
        else:
            self[process] = None

    def removeSpecificProcessData(self,process,data):
        try:
            if type(self[process]) == list:
                index = self[process].index(data)
                del self[process][index]
            else:
                self[process] = None
        except AttributeError:
            pass
        except ValueError:
            pass

    def getProcessData(self,process):
        return self[process]

    def shiftData(self,data,orig_process,new_process):
        if data is not None:
            self.removeSpecificProcessData(orig_process, data)
            self.addProcess(new_process,data)

# ______________
