import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from countrydata.models import Data, Metadata

class Command(BaseCommand):
    help = "Load data from CSVs"

    def handle(self, *args, **options):

        # clear out teh database in order to avoid redundancy
        Data.objects.all().delete()
        print("Data cleared")
        # create table again

        # open the CSV and begin to read it
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        print(base_dir)
        with open(str(base_dir) + '/countrydata/data/CO2_data.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader) # skip the header, single row
            for row in reader:
                print(row)

                try:
                    data = Data(
                        countryCode=row[0],
                        countryName=row[1],
                        co2_1990=row[2],
                        co2_1991=row[3],
                        co2_1992=row[4],
                        co2_1993=row[5],
                        co2_1994=row[6],
                        co2_1995=row[7],
                        co2_1996=row[8],
                        co2_1997=row[9],
                        co2_1998=row[10],
                        co2_1999=row[11],
                        co2_2000=row[12],
                        co2_2001=row[13],
                        co2_2002=row[14],
                        co2_2003=row[15],
                        co2_2004=row[16],
                        co2_2005=row[17],
                        co2_2006=row[18],
                        co2_2007=row[19],
                        co2_2008=row[20],
                        co2_2009=row[21],
                        co2_2010=row[22],
                        co2_2011=row[23],
                        co2_2012=row[24],
                        co2_2013=row[25],
                        co2_2014=row[26],
                        co2_2015=row[27],
                        co2_2016=row[28],
                        co2_2017=row[29],
                        co2_2018=row[30],
                        co2_2019=row[31],
                        co2_2020=row[32]
                    )
                    data.save()
                    print("Data saved to database")
                except Exception as e:
                    print(e)
                    print("Error creating DATA database object...")


        # do the same as above but for the metadata
        with open(str(base_dir) + '/countrydata/data/CO2_metadata.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                print(row)

                try:
                    metadata = Metadata(
                        countryCode=Data.objects.get(countryCode=row[0]),
                        region=row[1],
                        incomeGroup=row[2],
                        specialNotes=row[3]
                    )
                    metadata.save()
                    print("Metadata saved to database")
                except Exception as e:
                    print(e)
                    print("Error creating METADATA database object...")

