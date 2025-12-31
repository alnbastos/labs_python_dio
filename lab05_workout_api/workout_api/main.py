from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_hello_word():
    return {"message": "Hello World!"}
