from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.BigM.routers import BigM_routes

# Init the fastAPI app
app = FastAPI()

# registering the modules routers
app.include_router(BigM_routes.router)

# Configuring CORSMiddleware
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)