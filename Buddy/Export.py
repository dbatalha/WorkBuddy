from Collection import Collection
import csv


class Export(object):
    def __init__(self):
        data = Collection()
        csv_file = "export.csv"

        self.collection = data.get_all_data()
        self.file_cursor = open(csv_file, "wb")

    def export_csv(self):
        headers = [
            "StartWorkTime",
            "StartWorkEpoch",
            "LunchTime",
            "LunchTimeEpoch",
            "EndWorkTime",
            "EndWorkTimeEpoch",
            "StartAfterLunch",
            "StartAfterLunchEpoch",
            "Total",
            "Username"
        ]
        writer = csv.DictWriter(self.file_cursor, fieldnames=headers)

        writer.writeheader()
        self.collection = list(self.collection)
        for row in self.collection:
            writer.writerow({
                "StartWorkTime": row.StartWorkTime,
                "StartWorkEpoch": row.StartWorkEpoch,
                "LunchTime": row.LunchTime,
                "LunchTimeEpoch": row.LunchTimeEpoch,
                "EndWorkTime": row.EndWorkTime,
                "EndWorkTimeEpoch": row.EndWorkEpoch,
                "StartAfterLunch": row.StartAfterLunch,
                "StartAfterLunchEpoch": row.StartAfterLunchEpoch,
                "Total": row.Total,
                "Username": row.Username
            })
