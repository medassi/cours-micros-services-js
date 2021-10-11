from pydantic import BaseModel

class Categorie(BaseModel):
	code: int
	libelle: str

class Truc(BaseModel):
	code: int
	libelle: str
	categorie: int

class PostTruc(BaseModel):
	libelle: str
	categorie: int

class PostCategorie(BaseModel):
	libelle: str