import class_doors as doors

class brfb_station:

    bay_1 = doors.motor_door(1, 'Closed')
    bay_2 = doors.motor_door(2, 'Closed')
    bay_3 = doors.motor_door(3, 'Closed')

    main_door = doors.regular_door('Closed')
    side_door = doors.regular_door('Closed')

    def __init__(self, name=''):
        self.name = name  # not required
