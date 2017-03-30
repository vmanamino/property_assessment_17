data = open('property-assessment-2015.csv').read().splitlines()
out = open('assessed-15.txt', 'w')


count = 0
for line in data:
    processed = []
    columns = []
    
    if count == 0:
        column_count = 1
        columns = line.split(',')
        for column in columns:
            print(len(columns))
            if column_count < len(columns):
                # print('tab')
                out.write('%s\t' % (column))
            else: 
                # print('newline')
                out.write('%s\n' % (column))
            column_count += 1
            # print(column_count)
    
    else:
        columns = line.split(',')
        pid = columns[0]
        cmid = columns[1]
        gisid = columns[2]
        zipid = columns[7]
        mailzipid = columns[15]
        columns[0] = pid.zfill(10)+"_"
        if cmid:
            columns[1] = cmid.zfill(10)+"_"
        columns[2] = gisid.zfill(10)+"_"
        columns[7] = zipid.zfill(5)+"_"
        columns[15] = mailzipid.zfill(5)+"_"
        
        for column in columns:
            out.write("%s|" % (column))
        out.write("\n")
    
    
    count += 1
    
print(count)