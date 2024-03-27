from django.test import Client, TestCase
from countrydata.models import Data, Metadata

class TestModels(TestCase):
    def setUp(self):
        self.client = Client()
        
    @classmethod
    def setUpTestData(cls):
        testData1 = Data.objects.create(
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
        co2_2020 = 555
        )
        testData2 = Data.objects.create(
        countryCode = "EFG",
        countryName = "Test2Name",
        co2_1990 = 234.5,
        co2_1991 = 234.5,
        co2_1992 = 234.5,
        co2_1993 = 12.6,
        co2_1994 = 12.6,
        co2_1995 = 234.5,
        co2_1996 = 12.6,
        co2_1997 = 12.6,
        co2_1998 = 12.6,
        co2_1999 = 999,
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
        co2_2020 = 444
        )
        Metadata.objects.create(countryCode = testData1,region = "testRegion",incomeGroup = "testGroup",specialNotes = "testNotes")
        Metadata.objects.create(countryCode = testData2,region = "testRegion2",incomeGroup = "testGroup2",specialNotes = "testNotes2")
    def testIndexPage(self):
        countries = Data.objects.all()
        response = self.client.get('')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"countrydata/home.html")
        years = range(1990,2021)
        response = self.client.get('',{
        'years': years,
        'selected_year': 1999,
        'countries': countries,})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,999)
    def testComparison(self):
        TestModels.setUpTestData
        response = self.client.post("/comparison/",{"country1" : 1, "country2" : 2},follow=True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"countrydata/comparison.html")
        self.assertContains(response,"TestName")
        self.assertContains(response,"Test2Name")
    def testAbout(self):
        response = self.client.get("/about/",follow=True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"countrydata/about.html")