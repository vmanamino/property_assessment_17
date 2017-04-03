import get
import sys

output = open('property_assess_17.txt', 'w')

# headers
output.write('Parcel ID\tAddress\tZipcode\tFull address\tOwner\tLand use\tLot size'
'\tLiving area\tTotal value\tLand value\tBuilding value\tGross tax\n')

# if sys.argv[1]:
#     total = int(sys.argv[1])
#     print(total)
# else:
#     total = 0

the_set = get.parse_data()
count = 0
for s in the_set:
    count += 1
    print(count)
    output.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (s.pid, s.address_one.lstrip()
    , s.address_zip, s.address.lstrip(), s.owner, s.land_use, s.lot_size, s.living_area
    , s.total_value, s.land_value, s.building_value, s.gross_tax ))
    
