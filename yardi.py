import csv
import lxml.etree as etree

tree = etree.parse("/home/lejewett/Downloads/yardi (5)")


rows = []

for node in tree.xpath("//Property"):
	propID = unicode(node.xpath(".//Identification[@IDType='managementID']/IDValue/text()")[0]).encode('utf-8', 'ignore')
	m_name = unicode(node.xpath(".//MarketingName/text()")[0]).encode('utf-8', 'ignore')
	unitID = "N/A"
	avail = "N/A"
	for unit in node.xpath(".//ILS_Unit/Units/Unit"):
		unitID = unicode(unit.xpath("Identification[@IDType='UnitID']/IDValue/text()")[0]).encode('utf-8', 'ignore')
		avail = unicode(unit.xpath("UnitLeasedStatus/text()")[0]).encode('utf-8', 'ignore')
		rows.append({"Property ID": propID, "Marketing Name": m_name, "Unit ID": unitID, "Leased Status": avail})

with open('yardi_output.csv', 'w') as w_file:
	writer = csv.DictWriter(w_file, fieldnames=['Property ID', 'Marketing Name', 'Unit ID', 'Leased Status'])
	writer.writeheader()
	writer.writerows(rows)
