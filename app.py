from fastapi import FastAPI

app = FastAPI(
    title="HyaUp Bakcend API",
    description="HyaUp Backend API",
    version="0.0.1",
    debug=True
)

@app.get("/healthcheck")
def check_db_connection():
    return {"message": "Database connection successful"}

@app.post("/users")
def create_user():
    return {}