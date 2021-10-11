import sqlite3

class Database:
    def __init__(self):
        self._initConnectionCursor()

    def _initConnectionCursor(self):
        print ("Connexion à la base")
        self._connection = sqlite3.connect("dbCours.db3")
        self._connection.row_factory = sqlite3.Row
        self._cursor = self._connection.cursor()

    def closeConnection(self):
        self._connection.commit()
        self._connection.close()
        print("Déconnexion de la base")
    
    def getTrucs(self):
        sql = "select * from Truc"
        self._cursor.execute(sql) 
        res = self._cursor.fetchall()
        return res
    
    def getCategories(self):
        sql = "select * from Categorie"
        self._cursor.execute(sql) 
        res = self._cursor.fetchall()
        return res

    def getTrucsByCategorie(self,codeCategorie):
        sql = "select * from Truc where categorie=?"
        self._cursor.execute(sql,(codeCategorie,)) 
        res = self._cursor.fetchall()
        return res

    def insertTruc(self,libelle,codeCategorie):
        sql = "insert into Truc(libelle,categorie) values (?,?)"
        self._cursor.execute(sql, (libelle,codeCategorie))
        self._connection.commit()
        return self._cursor.lastrowid

    def insertCategorie(self,libelle):
        sql = "insert into Categorie(libelle) values (?)"
        self._cursor.execute(sql, (libelle,))
        self._connection.commit()
        return self._cursor.lastrowid

    def updateTruc(self,truc):
        libelle = truc.libelle
        codeCategorie = truc.categorie
        code = truc.code
        sql = "update Truc set libelle = ? , categorie = ? where code = ?"
        self._cursor.execute(sql, (libelle,codeCategorie,code))
        self._connection.commit()
        return self._cursor.lastrowid

    def delTruc(self,code):
        print(code)
        sql = "delete from Truc where code=?"
        self._cursor.execute(sql, (code))
        self._connection.commit()
        return self._cursor.lastrowid
