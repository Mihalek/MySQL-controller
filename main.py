from modules.Data_Base import PythonDB
import mysql.connector

def main():
    conn = mysql.connector.connect(user='root', password='password', host='localhost')
    mycursor = conn.cursor()
    mycursor.execute("SHOW DATABASES")
    databases = mycursor.fetchall()
    print("Istniejace bazy danych: ")
    print(databases)  
    obiekt = PythonDB()
    print("Podaj nazwe bazy danych: ")
    name_of_database = input()
    menu=0
    while menu == 0:
        print("Podaj operacje ktora chcesz wykonac: ")
        print("1) Utworz tabele")
        print("2) Usun tabele")
        print("3) Dodaj rekord do tabelu")
        print("4) Usun rekord do tabeli")
        print("5) Wyswietl tabele")
        print("6) Zakoncz program")
        zmienna = input()
        if zmienna == '1':
            obiekt.CreateTable(name_of_database)
            zmienna=0
            continue
        elif zmienna == '2':
            obiekt.DeleteTable(name_of_database)
            zmienna=0
            continue
        elif zmienna == '3':
            obiekt.Insert(name_of_database)
            zmienna=0
            continue
        elif zmienna == '4':
            obiekt.DeleteElement(name_of_database)
            zmienna=0
            continue
        elif zmienna == '5':
            obiekt.ShowTable(name_of_database)
            zmienna=0
            continue
        elif zmienna == '6':
            print("Koniec programu")
            menu=1
        else:
            print("Podaj cyfre od 1 do 6 !")
            continue


if __name__ == '__main__':
    main()
