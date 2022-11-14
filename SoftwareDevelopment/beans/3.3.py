def InputDetails():
    pupils = int(input("Please enter the number of pupils: "))

    forenames = [""] * pupils
    surnames = [""] * pupils
    SCN = [""] * pupils

    for i in range(pupils):
        forenames[i] = input("Please enter the forename for pupil " + str(i + 1) + " : ")
        surnames[i] = input("Please enter the surname for pupil " + str(i + 1) + " : ")
        SCN[i] = input("Please enter the SCN for pupil " + str(i+1) + " : ")

    return forenames,surnames,SCN

def writeFile(forenames,surnames,SCN):
    with open("SCN.csv", "w") as writefile:
        for i in range(len(forenames)):
            line = forenames[i] + "," + surnames[i] + "," + SCN[i] + "\n"
            writefile.write(line)

    print('Data Outputted to SCN.csv...')

fn,sn,scn = InputDetails()
writeFile(fn,sn,scn)