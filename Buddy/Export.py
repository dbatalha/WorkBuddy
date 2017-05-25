from Collection import Collection
import csv


class Export(object):
    def __init__(self):
        data = Collection()
        csv_file = "export.csv"

        self.collection = data.get_all_data()
        self.file_cursor = open(csv_file, "wb")

    def export_csv(self):
        headers = ["StartWorkTime", "StartWorkEpoch", "LunchTime", "LunchTimeEpoch", "EndWorkTime", "EndWorkTimeEpoch",
                   "StartAfterLunch", "StartAfterLunchEpoch", "Total", "Username"]
        writer = csv.DictWriter(self.file_cursor, fieldnames=headers)

        writer.writeheader()
        self.collection = list(self.collection)
        for row in self.collection:
            writer.writerow({"StartWorkTime": row[0], "StartWorkEpoch": row[1], "LunchTime": row[2],
                             "LunchTimeEpoch": row[3], "EndWorkTime": row[4], "EndWorkTimeEpoch": row[5],
                             "StartAfterLunch": row[6], "StartAfterLunchEpoch": row[7], "Total": row[8],
                             "Username": row[9]})
