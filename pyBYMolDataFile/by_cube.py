
import pyBY

class by_cube:

    def ReadFile(self, moldata, fn):
        fin = open(fn, "r")
        # comment 1
        moldata.SetComment(fin.readline().rstrip())
        # comment 2
        moldata.SetKeyValue('comment2', fin.readline().rstrip())
        # atom count and cell origin
        vars = fin.readline().rstrip().split()
        atomcount = int(vars[0]);
        org = [ float(vars[k]) for k in range(1,4) ]
        moldata.SetCellOrigin(org)
        moldata.SetVDOrigin(org)
        # grid count and lattice vector
        vars = fin.readline().rstrip().split()
        gn1 = int(vars[0])
        lv1 = [ float(vars[k]) for k in range(1,4) ]
        vars = fin.readline().rstrip().split()
        gn2 = int(vars[0])
        lv2 = [ float(vars[k]) for k in range(1,4) ]
        vars = fin.readline().rstrip().split()
        gn3 = int(vars[0])
        lv3 = [ float(vars[k]) for k in range(1,4) ]
        lv = [ float(gn1)*lv1[0], float(gn1)*lv1[1], float(gn1)*lv1[2], \
               float(gn2)*lv2[0], float(gn2)*lv2[1], float(gn2)*lv2[2], \
               float(gn3)*lv3[0], float(gn3)*lv3[1], float(gn3)*lv3[2]]
        # bohr or angstrom
        if gn1 < 0: 
            moldata.SetKeyValue('bohrox', 0)
            gn = [-gn1, -gn2, -gn3]
            bohrox = 0
            lv = [ -lv[k] for k in range(0,9) ]
        else:
            moldata.SetKeyValue('bohrox', 1)
            gn = [gn1, gn2, gn3]
            bohrox = 1
            lv = [ lv[k]*0.52917721092 for k in range(0,9) ]
        moldata.SetVDGridCount(gn)
        moldata.SetLatticeVectors(lv)
        # atom data
        Elem = pyBY.Element()
        for n in range(0, atomcount):
            vars = fin.readline().rstrip().split()
            elem = Elem.GetSymbol(int(vars[0]))
            sf = 1.0
            if bohrox == 1: sf = 0.52917721092
            x = [ sf*float(vars[k]) for k in range(2,5) ]
            moldata.AppendAtom(elem, x)
        count = 0
        nnn = gn[0]*gn[1]*gn[2]
        # volumetric data
        while (1):
            vars = fin.readline().rstrip().split()
            for n in range(0, len(vars)):
                moldata.vd[count] = float(vars[n])
                count = count+1
            if (count >= nnn): break
        fin.close()
        moldata.SetFileName(fn)
        moldata.SetFileType('cubei')
 

    def WriteFile(self, moldata, fn):
        fout = open(fn, "w")
        # comment
        fout.write(moldata.GetComment()+"\n")
        # comment2
        str = ""
        if moldata.KeyValueExists('comment2'):
            str = moldata.GetKeyValue('comment2')
        fout.write(str+"\n")
        # atom count & grid origin
        atomcount = moldata.GetAtomCount()
        org = moldata.GetVDOrigin()
        str = "%d %f %f %f\n" % (atomcount, org[0], org[1], org[2])
        fout.write(str)
        # grid count & lattice vector
        gn = moldata.GetVDGridCount()
        lv = moldata.GetLatticeVectors()
        lv = [ lv[k]/float(gn[k/3]) for k in range(0,9) ]
        str = "%d %f %f %f\n" % (-gn[0], lv[0], lv[1], lv[2])
        fout.write(str)
        str = "%d %f %f %f\n" % (-gn[1], lv[3], lv[4], lv[5])
        fout.write(str)
        str = "%d %f %f %f\n" % (-gn[2], lv[6], lv[7], lv[8])
        fout.write(str)
        # atom elems & positions
        Elem = pyBY.Element();
        for n in range(0,atomcount):
            num =Elem.GetAtomicNumber(moldata.GetAtomElem(n))
            p   = moldata.GetAtomPos(n)
            str  = "%d 0.000 %12.7f %12.7f %12.7f\n" % (num, p[0], p[1], p[2])
            fout.write(str)
        # volumetric data
        for n in range(0, gn[0]*gn[1]*gn[2]):
            fout.write(" %14.7e" % moldata.vd[n])
            if n%5 == 4: fout.write("\n")

 












