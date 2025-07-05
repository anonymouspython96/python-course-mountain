from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
def greet_json():
    return {"Hello": "World!"}
