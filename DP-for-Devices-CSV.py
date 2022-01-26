#
# Script created by Thaya Nagarajah
#

# Library to send HTTP Requests:
import requests
# Library to read XML Documents:
import xml.etree.ElementTree as ET
# Library to read CSV Documents:
import csv

# To disble the Certificate SubjectAlternateName Warning
requests.packages.urllib3.disable_warnings()

# To Trust the CUCM Tomcat Certificate - Download from CUCM and save it in the following location 
TomcatCertLocation = 'C:/Users/Admin/Documents/tomcat.pem'

# Open the CSV file contains the Device Name list if the Devices - Each row of the CSV file should be the Device-Name, SEP or CSF, etc
with open('C:/Users/Admin/Documents/Phone-List.csv', 'r') as csv_file:
    inputDevNames = csv.reader(csv_file)
    for DevName in inputDevNames:
        # Capture the Device Name from the CSV File Location "0"
        Device = str(DevName[0])
        
        # From SoapUI getPhone Code <<Copy and Paste from SoapUI>>
        # Split into two seperate sections with """ """ + Device + """ """
        soapReq = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/12.5">
        <soapenv:Header/>
        <soapenv:Body>
            <ns:getPhone>
            <name>""" + Device + """</name>
            </ns:getPhone>
        </soapenv:Body>
        </soapenv:Envelope>"""

        # Send HTTP Post request to CUCM with AXL API User 
        # Replace <<CUCM-FQDN>> with the Call Manager FQDN, axluser and axlpassword as needed
        r = requests.post('https://<<CUCM-FQDN>>/axl/',verify=TomcatCertLocation,auth=('axluser','axlpassword'),data=soapReq)

        # Write to XML File if the r.contetn
        XMLDoc = ET.fromstring(r.content)
        #print(r.content)
        # Serach for Device Pool Info and Print Device Name, Device Pool for the CSV Device List
        # with other /xxxxxxxxxx instead of the devicePoolName, you could display other configuration data for the devices in the list 
        print(Device+"," + XMLDoc.find(".//devicePoolName").text)
