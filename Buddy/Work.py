from Timer import Time
from Database import Database
from StateMachine import StateMachine

# App imports
import getpass

__author__ = 'Daniel Batalha'


class Work(object):
    def __init__(self):
        self.database = Database()
        self.state_machine_instance = StateMachine()
        self.state_machine_instance.run("Void")

        self.start_day_time = None

    def create_data(self):
        self.database.create("CREATE TABLE buddy (StartWorkTime, StartWorkEpoch INT, LunchTime, LunchTimeEpoch INT,"
                             " EndWorkTime, EndWorkEpoch INT, StartAfterLunch, StartAfterLunchEpoch INT, Total,"
                             " Username)")

    def state(self):
        return self.state_machine_instance.get_state()

    def start(self):
        username = str(getpass.getuser())

        time = Time()
        start_work_time_epoch = int(time.actual())
        start_work_time = time.date_time_format(start_work_time_epoch)

        self.database.insert("INSERT INTO buddy (StartWorkTime, StartWorkEpoch, Username)VALUES ('%s', '%d', '%s')"
                             % (start_work_time, start_work_time_epoch, username))

        self.database.save()

        self.start_day_time = start_work_time_epoch

        # Report status to state machine
        self.state_machine_instance.run("Started")

        print "Started"

    def launch(self):
        time = Time()
        launch_work_time_epoch = int(time.actual())
        launch_work_time = time.date_time_format(launch_work_time_epoch)

        self.database.update("UPDATE buddy SET LunchTime='%s', LunchTimeEpoch='%d' WHERE StartWorkEpoch='%d'"
                             % (launch_work_time, launch_work_time_epoch, self.start_day_time))

        self.database.save()

        # Report status to state machine
        self.state_machine_instance.run("Launch")

        print "Launch"

    def return_from_launch(self):
        time = Time()
        start_after_launch_work_time_epoch = int(time.actual())
        start_after_launch_work_time = time.date_time_format(start_after_launch_work_time_epoch)

        self.database.update("UPDATE buddy SET StartAfterLunch='%s', StartAfterLunchEpoch='%d' WHERE StartWorkEpoch='%d'"
                             % (start_after_launch_work_time, start_after_launch_work_time_epoch, self.start_day_time))

        self.database.save()

        # Report status to state machine
        self.state_machine_instance.run("After_Launch")
        print "After Launch"

    def end_day(self):
        time = Time()
        end_launch_work_time_epoch = int(time.actual())
        end_launch_work_time = time.date_time_format(end_launch_work_time_epoch)

        total = int(end_launch_work_time_epoch) - int(self.start_day_time)

        self.database.update("UPDATE buddy SET EndWorkTime='%s', EndWorkEpoch='%d' WHERE StartWorkEpoch='%d'"
                             % (end_launch_work_time, end_launch_work_time_epoch, self.start_day_time))

        self.database.update("UPDATE buddy SET Total='%d' WHERE StartWorkEpoch='%d'" % (total, self.start_day_time))

        self.database.save()

        # Report status to state machine
        self.state_machine_instance.run("Void")
        print "End Day"
