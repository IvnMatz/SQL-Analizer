from readF import genTables, getFile, getRelations

file = getFile("ex")

tables = genTables(file)

relations = getRelations(tables)

print(relations)