from fastapi import FastAPI
from pydantic import BaseModel

class TranslateRequest(BaseModel):
    text : str
    source_language : str
    target_language : str
    

app = FastAPI()

@app.get("/")
def route():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def item(item_id: int, q:str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/translate")
def post(request: TranslateRequest):
    return {
        "text": request.text,
        "source_language": request.source_language,
        "target_language": request.target_language
    }