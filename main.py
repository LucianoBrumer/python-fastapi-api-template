from fastapi import FastAPI

from models.Note import *

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
    return note

@app.update("/api/note/{id}")
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