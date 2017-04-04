import get
import sys

output = open('property_assess_17.txt', 'w')

# headers
output.write('Parcel ID\tAddress\tZipcode\tFull address\tOwner\tLand use\tLot size'
'\tLiving area\tTotal value\tLand value\tBuilding value\tGross tax\n')

offset = 0
total = get.total(offset)
count = 0
while offset < total:
    the_set = get.parse_data(offset)
    for s in the_set:
        count += 1
        output.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (s.pid, s.address_one.strip()
        , s.address_zip, s.address.strip(), s.owner, s.land_use, s.lot_size, s.living_area
        , s.total_value, s.land_value, s.building_value, s.gross_tax ))
    offset += 100
    print(count)



    
