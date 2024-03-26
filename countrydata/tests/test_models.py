from django.test import TestCase
from countrydata.models import Data,Metadata
# Create your tests here.

class TestModels(TestCase):

    def buildTestData(cls):
        testData = Data.objects.create(
        countryCode = "ABC",
        countryName = "TestName",
        co2_1990 = 12.6,
        co2_1991 = 12.6,
        co2_1992 = 12.6,
        co2_1993 = 12.6,
        co2_1994 = 12.6,
        co2_1995 = 12.6,
        co2_1996 = 12.6,
        co2_1997 = 12.6,
        co2_1998 = 12.6,
        co2_1999 = 12.6,
        co2_2000 = 12.6,
        co2_2001 = 12.6,
        co2_2002 = 12.6,
        co2_2003 = 12.6,
        co2_2004 = 12.6,
        co2_2005 = 12.6,
        co2_2006 = 12.6,
        co2_2007 = 12.6,
        co2_2008 = 12.6,
        co2_2009 = 12.6,
        co2_2010 = 12.6,
        co2_2011 = 12.6,
        co2_2012 = 12.6,
        co2_2013 = 12.6,
        co2_2014 = 12.6,
        co2_2015 = 12.6,
        co2_2016 = 12.6,
        co2_2017 = 12.6,
        co2_2018 = 12.6,
        co2_2019 = 12.6,
        co2_2020 = 12.6
        )
        Metadata.objects.create(
        countryCode = testData,
        region = "testRegion",
        incomeGroup = "testGroup",
        specialNotes = "testNotes"
        )

    def confirmTestData(self):
        data = Data.objects.get(id=1)
        self.assertEqual(data.countryCode,"ABC222")
        self.assertEqual(data.countryName,"TestName")
        all_data = data.objects.all()
        self.assertEqual(all_data.count(),2)
        