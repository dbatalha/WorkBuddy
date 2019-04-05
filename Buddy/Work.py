import WorkSystem
from Timer import Time
from Database import Database
from StateMachine import StateMachine
from Database import BuddyTable

__author__ = 'Daniel Batalha'


class Work(object):
    def __init__(self):
        self.database = Database()
        self.state_machine_instance = StateMachine()
        self.state_machine_instance.run("Void")

        self.start_day_time = None

        # Initialize buddy
        self.buddy = None

    def create_data(self):
        print "No"

    def state(self):
        return self.state_machine_instance.get_state()

    def start(self):
        username = str(WorkSystem.WorkSystem.get_system_username())

        time = Time()
        start_work_time_epoch = int(time.actual())
        start_work_time = time.date_time_format(start_work_time_epoch)

        self.buddy = BuddyTable(start_work_time, start_work_time_epoch, username)

        self.database.create(self.buddy)
        self.database.commit()

        self.start_day_time = start_work_time_epoch

        # Report status to state machine
        self.state_machine_instance.run("Started")

        print "Started"

    def launch(self):
        time = Time()
        launch_work_time_epoch = int(time.actual())
        launch_work_time = time.date_time_format(launch_work_time_epoch)

        self.database.session.query(BuddyTable).filter_by(StartWorkEpoch=self.start_day_time).update(
            {
                "LunchTime": launch_work_time,
                "LunchTimeEpoch": launch_work_time_epoch
            })

        self.database.create(self.buddy)
        self.database.commit()

        # Report status to state machine
        self.state_machine_instance.run("Launch")

        print "Launch"

    def return_from_launch(self):
        time = Time()
        start_after_launch_work_time_epoch = int(time.actual())
        start_after_launch_work_time = time.date_time_format(start_after_launch_work_time_epoch)

        self.database.session.query(BuddyTable).filter_by(StartWorkEpoch=self.start_day_time).update(
            {
                "StartAfterLunch": start_after_launch_work_time,
                "StartAfterLunchEpoch": start_after_launch_work_time_epoch
            })

        self.database.commit()

        # Report status to state machine
        self.state_machine_instance.run("After_Launch")
        print "After Launch"

    def end_day(self):
        time = Time()
        end_launch_work_time_epoch = int(time.actual())
        end_launch_work_time = time.date_time_format(end_launch_work_time_epoch)

        total = int(end_launch_work_time_epoch) - int(self.start_day_time)

        self.database.session.query(BuddyTable).filter_by(StartWorkEpoch=self.start_day_time).update(
            {
                "EndWorkTime": end_launch_work_time,
                "EndWorkEpoch": end_launch_work_time_epoch,
                "Total": int(total)
            })

        self.database.commit()

        # Report status to state machine
        self.state_machine_instance.run("Void")
        print "End Day"
