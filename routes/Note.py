# from uuid import uuid4

import sys
sys.path.append("..")
from models.Note import Note, NoteSchema
from utils.database import conn

def initNoteRoutes(app):
    @app.get("/api/note")
    async def getAll():
        try:
            data = []
            cursor = conn.execute_sql('SELECT * FROM note')
            for row in cursor.fetchall():
                table = dict()

                for column, value in zip(cursor.description, row):
                    column_name = column[0]
                    table[column_name] = value

                data.append(table)

            return {"__data__": data}
        except Exception as e:
            return {"__data__": ""}

    @app.get("/api/note/{id}")
    async def getByID(id):
        try:
            return Note.select().where(Note.id == id).get()
        except Exception as e:
            return {"__data__": ""}

    @app.post("/api/note")
    async def create(note: NoteSchema):
        data = {
            # "id": str(uuid4()),
            "title": note.title,
            "description": note.description
        }

        Note.create(
            # id=data.get('id'),
            title=data.get('title'),
            description=data.get('description'),
        )

        return {"__data__": data}

    @app.put("/api/note/{id}")
    async def updateByID(note: NoteSchema, id):
        data = {
            "id": id,
            "title": note.title,
            "description": note.description
        }

        Note.update({
            Note.title: data.get('title'),
            Note.description: data.get('description'),
        }).where(Note.id == id).execute()

        return {"__data__": data}

    @app.delete("/api/note/{id}")
    async def deleteByID(id):
        data = {
            "__data__": {
                "id": id,
            }
        }

        Note.delete().where(Note.id == id).execute()

        return data