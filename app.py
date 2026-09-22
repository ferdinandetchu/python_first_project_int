from fastapi import FastAPI

app = FastAPI(
    title="HyaUp Bakcend API",
    description="HyaUp Backend API",
    version="0.0.1",
    debug=True
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}