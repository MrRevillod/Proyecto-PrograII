import mysql.connector as sql

user = "A2022_nvalenzuela"; host = "db.inf.uct.cl"
pas = "A2022_nvalenzuela" ; db = "A2022_nvalenzuela"

def insert_to_db(lista):
	con = sql.connect(user = "A2022_nvalenzuela",
										password = "A2022_nvalenzuela",
										host = "db.inf.uct.cl",
										database = "A2022_nvalenzuela")
	cursor = con.cursor()
	cursor.execute("DELETE FROM csv_python")
	for x in lista:
		id = int(x[0]); nom_prod = x[1]; tipo_dep = x[2]; masa = x[3]; peso = x[4]
		query = "INSERT INTO csv_python (id, nom_prod, tipo_dep, masa, peso) VALUES ('%s', '%s', '%s', '%s', '%s')" % (id, nom_prod, tipo_dep, masa, peso)
		cursor.execute(query)
		con.commit()
	cursor.close()
	con.close()

def get_list_to_db():
	con = sql.connect(user = "A2022_nvalenzuela",
										password = "A2022_nvalenzuela",
										host = "db.inf.uct.cl",
										database = "A2022_nvalenzuela")
	cursor = con.cursor()
	query = "SELECT * FROM csv_python"
	cursor.execute(query)
	lista = []
	contador = 0
	for (id, nom_prod, tipo_dep, masa, peso) in cursor:
		lista.append([])
		lista[contador].append(id)
		lista[contador].append(nom_prod)
		lista[contador].append(tipo_dep)
		lista[contador].append(masa)
		lista[contador].append(peso)
		contador += 1
	cursor.close()
	con.close()
	return lista
