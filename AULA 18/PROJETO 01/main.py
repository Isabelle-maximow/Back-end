
# main.py
from fastapi import FastAPI
from controller import router

#iniciar o fastapi
app = FastAPI(title="Projetinho MVC com fastapi")

#incluir as rotas do controller
app.include_router(router)

#python -m uvicorn main:app --reload
