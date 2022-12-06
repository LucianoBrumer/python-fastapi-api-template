from fastapi import FastAPI
from uuid import uuid4

import utils.config
from models.Note import *
from utils.database import *

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/note")
async def getAllNotes(id):
    return {
        "id": id,
        "path": "all notes"
    }

@app.get("/api/note/{id}")
async def getNoteByID(id, limit = 0):
    return {
        "id": id,
        "limit": limit,
        "path": "get note"
    }

@app.post("/api/note")
async def createNote(note: Note):
    data = {
        "id": str(uuid4()),
        "title": note.title,
        "description": note.description
    }
    conn.insert('note', data)
    return data

@app.put("/api/note/{id}")
async def updateNoteByID(id):
    return {
        "id": id,
        "path": "update note"
    }

@app.delete("/api/note/{id}")
async def deleteNoteByID(id):
    return {
        "id": id,
        "path": "delete note"
    }

if __name__ == '__main__':
    from uvicorn import run
    from os import getenv

    port = int(getenv('PORT'))

    run(app, host="127.0.0.1", port=port)