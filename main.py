from fastapi import FastAPI
from fastapi.exceptions import HTTPException
# Импортируем uvicorn
import uvicorn
from pydantic import BaseModel

app = FastAPI()  # Создание экземпляра приложения

class Book(BaseModel):
	title: str
	author: str

books = [
	{
		"id": 1,
		"title": "Название 1",
		"author": "Автор 1"
	},
	{
		"id": 2,
		"title": "Название 2",
		"author": "Автор 2"
	}
]

@app.get("/books", summary="Все книги",tags=["books"])
def get_books():
	return books

@app.get("/books/{book_id}", summary="Конкретная книга", tags=["books"])
async def get_book(book_id: int):
	for book in books:
		if book["id"] == book_id:
			return book
	raise HTTPException(status_code=404, detail="Книга не найдена")

@app.post("/books", summary="Создание книги",tags=["books"])
async def create_book(new_book: Book):
	new_book_id = len(books) + 1
	books.append({
		"id": new_book_id,
		"title": new_book.title,
		"author": new_book.author
	})
	return {"success": True}



# Эндпоинт GET-запрос
@app.get("/", summary="Root - эндпоинт", tags=["Главное"])
def root():
	return "Hello, World!"

# Добавляем следующие строчки
if __name__ == "__main__":
	uvicorn.run(app, reload=True)