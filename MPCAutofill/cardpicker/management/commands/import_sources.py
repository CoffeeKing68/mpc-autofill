from django.core.management.base import BaseCommand
from cardpicker.models import Card, Cardback, Token, Source
from bulk_sync import bulk_sync
import csv


def read_sources_csv():
    sources = []

    # read CSV file for drive data
    with open("drives.csv", newline='') as csvfile:
        drivesreader = csv.DictReader(csvfile, delimiter=",")
        # order the sources by row number in CSV
        i = 0
        for row in drivesreader:
            sources.append(
                Source(
                    id=row["key"],
                    username=row["username"],
                    reddit=row["reddit"],
                    drivelink=row["drivelink"],
                    description=row["description"],
                    order=i,
                    drivename=row["drivename"]
                )
            )
            i += 1

    print("Read CSV file and found {} sources.".format(len(sources)))
    return sources


def sync_sources(sources):
    key_fields = ('id', )
    ret = bulk_sync(
        new_models=sources,
        key_fields=key_fields,
        filters=None,
        db_class=Source
    )


class Command(BaseCommand):
    # set up help line to print the available drive options
    help = "Synchronises Google Drives from drives.csv (in root project directory) to database."

    def handle(self, *args, **kwargs):
        sources = read_sources_csv()
        sync_sources(sources)
        print("All sources synchronised from CSV to database.")
