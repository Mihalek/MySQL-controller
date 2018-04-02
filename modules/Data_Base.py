import mysql.connector


class PythonDB:

    def CreateTable(self, name_of_base):
        conn = mysql.connector.connect(
        user='root', password='password', host='localhost')
        mycursor = conn.cursor()
        mycursor.execute("USE "+name_of_base)

        name_of_table = input("Wprowadz nazwe tabeli: ")
        a = int(input("Wprowadz ile kolumn chcesz posiadac w bazie: (ID zostanie dodane osobno jako pierwsza kolumna)"))
        list_of_names = []
        list_of_type = []
        list_of_numberschars = []
        list_of_emptytype = []

        for i in range(0, a):
            list_of_names.append(input("wprowadz nazwe kolumny: "))
            print("Podaj typ danego pola: a) INT b) FLOAT c) CHAR : ")
            typ = input()
            if typ == 'a':
                list_of_type.append('INT')
            elif typ == 'b':
                list_of_type.append('FLOAT')
            elif typ == 'c':
                list_of_type.append('CHAR')
            else:
                print("PODAJ TYLKO A B LUB C")
                return

            list_of_numberschars.append(input("ile znakow ma miec to pole: "))
            print("Czy pole moze byc puste? T - tak N - nie: ")
            typ2 = input()
            if(typ2 == 'T'):
                list_of_emptytype.append('NULL')
            elif typ2 == 'N':
                list_of_emptytype.append('NOT NULL')
            else:
                print("PODAJ TYLKO T LUB N")
                return
        loopsize = len(list_of_names)
        word = "CREATE TABLE IF NOT EXISTS "+name_of_table + \
            " (id INT(5) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY, "

        for i in range(0, len(list_of_names)):
            word += list_of_names[i]+" "+list_of_type[i] + \
                " ( "+list_of_numberschars[i] + " ) "+list_of_emptytype[i]
            if i != loopsize-1:
                word = word+","

        word += " )"
        print(word)
        mycursor.execute(word)
        conn.commit()
        

    def Insert(self, name_of_base):
        conn = mysql.connector.connect(user='root', password='password', host='localhost')
        mycursor = conn.cursor(buffered=True)
        mycursor.execute("USE "+name_of_base)
        print("Do jakiej tabeli chcesz wprowadzic rekord: ")
        print("istniejace tabele: ")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()  
        print(tables)
        table = input()
        mycursor.execute("SELECT * FROM "+ table + " LIMIT 0")
        string = mycursor.description
        no_of_columns = len(mycursor.description)
        for i in range(0, no_of_columns):
            print(string[i][0])
        print("Podaj wartosci ktore chcesz wprowadzic: (Pamietaj ze stringi podajemy w apostrofach")
        lista = []
        for i in range(0,no_of_columns):
            print("podaj "+string[i][0]+":")
            value = input()
            lista.append(value)
        string2 = "INSERT INTO "+table+" ("
        for i in range(0,no_of_columns):
            string2+= string[i][0]
            if i != no_of_columns-1:
                string2+=", "
        string2+=") VALUES ("
        for i in range(0,no_of_columns):
            string2+=lista[i]
            if i != no_of_columns-1:
                string2+=", "
        string2+=");"
        print(string2)
        mycursor.execute(string2)
        conn.commit()
        print("TABELA PO DODANIU: ")
        mycursor.execute("SELECT * FROM "+table)
        rows = mycursor.fetchall()
        for row in rows:
            print(row)
        

    def DeleteTable(self, name_of_base):
        conn = mysql.connector.connect(user='root', password='password', host='localhost')
        mycursor = conn.cursor()
        mycursor.execute("USE "+name_of_base)
        print("Podaj nazwe tabeli które chcesz usunąć: ")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()  
        print(tables)
        to_delete = input()
        string = "DROP TABLE IF EXISTS "+to_delete
        mycursor.execute(string)
        print("Po usunieciu: ")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()
        conn.commit()  
        print(tables)

    def DeleteElement(self, name_of_base):
        conn = mysql.connector.connect(user='root', password='password', host='localhost')
        mycursor = conn.cursor()
        mycursor.execute("USE "+name_of_base)
        print("Podaj nazwe tabeli z ktorej chcesz usunac element: ")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()  
        print(tables)
        table = input()
        mycursor.execute("SELECT * FROM "+table)
        rows = mycursor.fetchall()
        for row in rows:
            print(row)
        print("Podaj id elementu ktory chcesz usunac: ")
        id_ = input()
        string = "DELETE FROM "+table+" WHERE ID = "+id_
        mycursor.execute(string)
        print("Po usunieciu elementu: ")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()
        conn.commit()  
        print(tables)
        


    def ShowTable(self, name_of_base):
        conn = mysql.connector.connect(user='root', password='password', host='localhost')
        mycursor = conn.cursor()
        mycursor.execute("USE "+name_of_base)
        print("Podaj nazwe tabeli ktora chcesz wyswietlic: ")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()  
        print(tables)
        string = input()
        mycursor.execute("SELECT * FROM "+string)
        rows = mycursor.fetchall()
        for row in rows:
            print(row)