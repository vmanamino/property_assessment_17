data = open('assess_17.txt').read().splitlines()
out = open('assessed.txt', 'w')


count = 0
for line in data:
    
    if count == 0:
        column_count = 1
        columns = line.split('|')
        for column in columns:
            print(len(columns))
            if column_count < len(columns):
                # print('tab')
                out.write('%s\t' % (column))
            else: 
                # print('newline')
                out.write('%s\n' % (column))
            column_count += 1
            print(column_count)
    processed = []
    columns = []
    if count > 0 and count < 2:
        columns = line.split('|')
        pid = columns[0]
        gid = columns[1]
        cmid = columns[2]
        zipid = columns[7]
        columns[0] = pid+"_"
        columns[1] = repr(gid)
        columns[2] = repr(cmid)
        columns[7] = repr(zipid)
        
        for column in columns:
            out.write("%s\t" % (column))
        out.write("\n")
    
    
    count += 1
    
print(count)