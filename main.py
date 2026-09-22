import uvicorn
# from config.config import settings
from config.config import settings


if __name__ == '__main__':
    uvicorn.run("app:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=True)