from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import List
from database import Database
from models import Truc,Categorie,PostTruc,PostCategorie



app = FastAPI()
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', response_model=str)
async def index():
    msg = "Bienvenue au cours de B1 SLAM SIO2"
    return msg

@app.get('/trucs/', response_model=List[Truc])
async def get_getTrucs():
    database = Database()
    res = database.getTrucs() 
    database.closeConnection()
    return res

@app.get('/trucs/{categorie}', response_model=List[Truc])
async def get_getTrucs(categorie):
    database = Database()
    res = database.getTrucsByCategorie(categorie) 
    database.closeConnection()
    return res


@app.get('/categories/', response_model=List[Categorie])
async def get_getCategorie():
    database = Database()
    res = database.getCategories() 
    database.closeConnection()
    return res

@app.post('/trucs/', status_code=201)
async def post_addTruc( payload : PostTruc ):
    dictPost = payload.dict()
    libelle = dictPost['libelle']
    codeCategorie = dictPost['categorie']
    database = Database()
    res = database.insertTruc(libelle,codeCategorie)
    database.closeConnection()
    return res

@app.post('/categories/', status_code=201)
async def post_addCategorie( payload : PostCategorie ):
    dictPost = payload.dict()
    libelle = dictPost['libelle']
    database = Database()
    res = database.insertCategorie(libelle)
    database.closeConnection()
    return res

@app.put('/trucs/', status_code=200)
async def put_updateTruc( truc : Truc ):
    database = Database()
    res = database.updateTruc(truc)
    database.closeConnection()
    return res

@app.delete('/trucs/{code}', status_code=201)
async def delete_delTruc(code):
    database = Database()
    res = database.delTruc(code)
    database.closeConnection()
    return res

uvicorn.run(app, host="0.0.0.0", port="8080")