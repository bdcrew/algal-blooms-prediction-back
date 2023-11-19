import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(version="0.0.1", title="Remake Ocean Project", description="Remake Ocean Project API")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {"message": "Remake Ocean Project"}


@app.get('/health')
async def health():
    return {"message": "health checking"}


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    uvicorn.run(app, reload=True, host='0.0.0.0', port=8000)
