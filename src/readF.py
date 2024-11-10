def getFile(filename):
    with open(f"uploads/{filename}.sql", "r") as file:
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
    table['primary_key'] = ""
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
            table['primary_key'] = ""
            intoTab = True
        elif intoTab == True: #leemos los campos
            for char in Pline:
                if char == ',':
                    print(f" New Camp {campN}")
                    camp = readCamp(campN)
                    table['camps'].append(camp)
                    if "primary key" in campN:
                            table['primary_key'] = camp
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

def getRelations(tables):
    tables2 = tables
    relations = []
    for table in tables:
        ActualTable = table['name']
        PK = table['primary_key']
        print(PK)
        for table2 in tables2:
            print(f"{ActualTable} : {table2['name']} ")
            if table2['name'] == ActualTable:
                print("SameTable")
            else:
                for camp in table2['camps']:
                    if PK == camp:
                        print("entra al if")
                        if PK == table2['primary_key']:
                            relations.append([f"{ActualTable}.{PK[0]}", f"{table2['name']}.{table2['primary_key'][0]}"], "1:1")
                        else:
                            relations.append([f"{ActualTable}.{PK[0]}", f"{table2['name']}.{PK[0]}", "1:M"])
    return relations


        