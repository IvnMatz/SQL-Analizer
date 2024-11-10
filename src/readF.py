def getFile(filename):
    with open(f"{filename}.sql", "r") as file:
        sqlfile = file.readlines()
    return sqlfile

def readCamp(camp):
    campName = ""
    campType = ""
    charC = 0
    for char in camp:
        charC += 1
        if char == " ":
            break
        else:
            campName += char
    for char in camp[charC:]:
        if char == ' ':
            break
        else:
            campType += char
    return [campName, campType]

    
def genTables(sqlfile):
    tables = []
    table = {}
    table['camps'] = []
    table['primary key'] = ""
    campN = ""
    intoTab = False
    for line in sqlfile:    #Analizamos linea por linea
        Pline = line.strip()    #cortamos los espacios de cada linea
        if Pline == '':     #salta si no hay nada en la linea
            print(" ")
        elif Pline[:12] == 'create table': #detecta si creamos una tabla
            table = {}
            table['name'] = ""
            print("New table")
            for char in Pline[12:]: # leemos el nombre de la tabla
                if char == '(':
                    break
                elif char != " ":
                    table['name'] += char
            table['camps'] = []
            table['primary key'] = ""
            intoTab = True
        elif intoTab == True: #leemos los campos
            for char in Pline:
                if char == ',':
                    print(f" New Camp {campN}")
                    camp = readCamp(campN)
                    table['camps'].append(camp)
                    if "primary key" in campN:
                            table['primary key'] = camp
                    campN = ""
                    break
                else:
                    if Pline == ')': # detecta si cerró la tabla
                        print(f" New Camp {campN}")
                        camp = readCamp(campN)
                        table['camps'].append(camp)
                        if "primary key" in campN:
                            table['primary key'] = camp
                        campN = ""
                        print("close table")
                        intoTab = False
                        print(f"Table Generated: {table}")
                        tables.append(table)
                    else:
                        campN = campN + char
    return tables

        