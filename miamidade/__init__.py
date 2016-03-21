# encoding=utf-8
from pupa.scrape import Jurisdiction, Organization
from .events import MiamidadeEventScraper
from .bills import MiamidadeBillScraper
from .people import MiamidadePersonScraper


class Miamidade(Jurisdiction):
    division_id = "ocd-division/country:us/state:fl/county:miami-dade"
    classification = "legislature"
    name = "Miami-Dade County Government"
    url = "http://miamidade.gov/wps/portal/Main/government"
    parties = []

    scrapers = {
        "events": MiamidadeEventScraper,
        "bills": MiamidadeBillScraper,
        "people": MiamidadePersonScraper,
    }

    legislative_sessions = [{"identifier":"2014",
            "name":"2014 Regular Session",
            "start_date": "2014-11-20",
            "end_date": "2016-11-20"},
            ]


    def get_organizations(self):
        org = Organization(
            name="Miami-Dade County Commission",
            classification="legislature")
        
        #label=human readable
        #role=what we can pull with the scraper
        org.add_post(label="Clerk, Circuit and County Courts",
            role="Clerk, Circuit and County Courts",
            division_id=self.division_id)
        
        org.add_post(role="Mayor",label="Office of the Mayor",
            division_id=self.division_id)

        org.add_post("Property Appraiser","Property Appraiser",
            division_id=self.division_id)

        for x in range(1,14):
            org.add_post(label="District {dist} Commissioner".format(dist=x),
                role="Commissioner",
                division_id=self.division_id)
        
        yield org

        # Unbelievably, the only source of committees is hard coded in a PDF:
        # http://www.miamidade.gov/commission/library/committee-structure-member-assignments.pdf

        org = Organization(
            name="Metropolitan Services Committee",
            classification="committee")
        org.add_post(label="chair", role="chair")
        org.add_post(label="vice-chair", role="vice-chair")  
        org.add_source(
            "www.miamidade.gov/govaction/agendas.asp?Action=Agendas&Oper=DisplayAgenda&Agenda=MSC&AgendaName=Metropolitan+Services+Committee",
            note="web")
        yield org

        org = Organization(name="UMSA Committee", classification="committee")
        org.add_post(label="chair", role="chair")
        org.add_post(label="vice-chair", role="vice-chair")  
        org.add_source("www.miamidade.gov/govaction/agendas.asp?Action=Agendas&Oper=DisplayAgenda&Agenda=UMSC&AgendaName=Unincorporated+Municipal+Service+Area+(UMSA)+Cmte",
                       note="web")
        yield org        

        org = Organization(name="Strategic Planning and Government Operations Committee", classification="committee")
        org.add_post(label="chair", role="chair")
        org.add_post(label="vice-chair", role="vice-chair")  
        org.add_source("www.miamidade.gov/govaction/agendas.asp?Action=Agendas&Oper=DisplayAgenda&Agenda=SPGO&AgendaName=Strategic+Planning+%26+Government+Operations+Cmte",
                       note="web")
        yield org  

        org = Organization(
            name="Trade and Tourism Committee",
            classification="committee")
        org.add_post(label="chair", role="chair")
        org.add_post(label="vice-chair", role="vice-chair")  
        org.add_source("www.miamidade.gov/govaction/agendas.asp?Action=Agendas&Oper=DisplayAgenda&Agenda=TTC&AgendaName=Trade+and+Tourism+Committee",
                       note="web")
        yield org  

        org = Organization(
            name="Transit and Mobility Services Committee",
            classification="committee")
        org.add_post(label="chair", role="chair")
        org.add_post(label="vice-chair", role="vice-chair")  
        org.add_source("www.miamidade.gov/govaction/agendas.asp?Action=Agendas&Oper=DisplayAgenda&Agenda=TMSC&AgendaName=Transit+and+Mobility+Services+Committee",
                       note="web")
        yield org  

        org = Organization(name="Economic Prosperity Committee", classification="committee")
        org.add_post(label="chair", role="chair")
        org.add_post(label="vice-chair", role="vice-chair")  
        org.add_source("www.miamidade.gov/govaction/agendas.asp?Action=Agendas&Oper=DisplayAgenda&Agenda=EPC&AgendaName=Economic+Prosperity+Committee",
                       note="web")
        yield org  
