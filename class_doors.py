class motor_door:

    allowed_status_list = ['Open', 'Closed', 'Opening', 'Closing']

    def __init__(self, bay, status):
        self.bay = bay
        self.status = status

    @property
    def bay(self):
        return self.__bay

    @bay.setter
    def bay(self, bay):
        if bay not in [1, 2, 3]:
            self.__bay = 0
        else:
            self.__bay = bay

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if status not in self.allowed_status_list:
            print('Unable to change status')
        else:
            self.__status = status