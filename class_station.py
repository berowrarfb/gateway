import class_doors as doors

class brfb_station:

    def __init__(self):
        self.bay_1 = doors.motor_door(1, 'Closed')
        self.bay_2 = doors.motor_door(2, 'Closed')
        self.bay_3 = doors.motor_door(3, 'Closed')

        self.main_door = doors.regular_door('Closed')
        self.side_door = doors.regular_door('Closed')

