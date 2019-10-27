from Database import Database
from Database import TeamsTable


class TeamsFlow(object):
    def __init__(self):
        self.database = Database()

    def add_team(self, team_name, team_elements):
        """
        Create new team
        :param team_name:
        :param team_elements:
        :return:
        """
        teams_table = TeamsTable(team_name, 3)

        self.database.create(teams_table)
        self.database.commit()

    def delete_project(self, team_id):
        """
        Delete team
        :param team_id:
        :return:
        """
        self.database.session.query(TeamsTable).filter_by(Id=team_id).delete()
        self.database.commit()

    def get_all_data(self):
        """
        Get all data from teams table
        :return:
        """
        data = self.database.session.query(TeamsTable).all()
        self.database.commit()

        return data
