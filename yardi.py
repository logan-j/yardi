import csv
import argparse
import sys
import lxml.etree as etree
def main():


	parser = argparse.ArgumentParser(description="Mine Yardi files for unit information.")
	parser.add_argument('infile', nargs='?', type=str, default='')
	parser.add_argument('outfile', nargs='?', type=argparse.FileType("w"), default=sys.stdout)
	args = parser.parse_args()
	if args.infile != '':
		try:
			tree = etree.parse(args.infile)


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

			writer = csv.DictWriter(args.outfile, fieldnames=['Property ID', 'Marketing Name', 'Unit ID', 'Leased Status'])
			writer.writeheader()
			writer.writerows(rows)
		except Exception as inst:
			sys.stderr.write("Fatal Error: %s. Aborting\n" % str(inst))

if __name__ == "__main__":
	main()
