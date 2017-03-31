import get
import sys

output = open('property_assess_17.txt', 'w')

# headers
output.write('Parcel ID\tAddress\tZipcode\tFull address\tOwner\tLand use\tLot size'
'\tLiving area\tTotal value\tLand value\Building value\tGross tax\n')
if len(sys.argv) == 3:
    the_set = get.parse_data(sys.argv[1], sys.argv[2])
    for s in the_set:
        output.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (s.pid, s.address_one
        , s.address_zip, s.address, s.owner, s.land_use, s.lot_size, s.living_area
        , s.total_value, s.land_value, s.gross_tax ))
else:
    print(get.parse_data())
