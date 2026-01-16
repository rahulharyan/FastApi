from fastapi import FastAPI

app = FastAPI(title="TODO Aplication")

@app.get("/")
def root():
    return {'message':'Server are Running!'}