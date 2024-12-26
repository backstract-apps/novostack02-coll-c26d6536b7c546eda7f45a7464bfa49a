from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - novostack02-coll-c26d6536b7c546eda7f45a7464bfa49a',debug=False,docs_url='/great-hugle-b52eeb94c38c11ef8e680242ac12000360/docs',openapi_url='/great-hugle-b52eeb94c38c11ef8e680242ac12000360/openapi.json')

app.include_router(router, prefix='/great-hugle-b52eeb94c38c11ef8e680242ac12000360/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()