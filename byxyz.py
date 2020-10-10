
def ReadFile(filename):
    lines = open(filename, 'r').readlines()
    natoms = int(lines[0])
    comment = lines[1].rstrip()
    data = []
    for line in lines[2:2+natoms]:
        d = line.split()
        data.append([d[0], float(d[1]), float(d[2]), float(d[3])])

    return natoms, comment, data
        
        
