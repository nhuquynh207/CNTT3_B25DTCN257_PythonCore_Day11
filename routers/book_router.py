from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from schemas.book_schema import BookCreateSchema,BookUpdateSchema,BookResponseSchema
from services.book_service import create_book,delete_book,get_all_books,get_book_by_id,update_book
from database import get_db

router = APIRouter(
    prefix="/api/v1/books",
    tags=["Book Controller"]
)

@router.get("/",response_model=list[BookResponseSchema])
def read_all_books(db:Session = Depends(get_db)):
    books = get_all_books(db)
    return books

@router.post("/",response_model=BookCreateSchema)
def create_new_book(book :BookCreateSchema,db:Session = Depends(get_db)):
    return create_book(db,new_book = book)

@router.put("/{book_id}",response_model=BookUpdateSchema)
def update_book_by_id(book_id:int,book_update:BookUpdateSchema,db:Session=Depends(get_db)):
    book = update_book(db,book_id=book_id,book_in=book_update)
    if not book:
        raise HTTPException(status_code=404,detail="Không tìm thấy sách")

    return book

@router.delete("/{book_id}")
def delete_book_by_id(book_id:int,db:Session = Depends(get_db)):
    del_book = delete_book(db,book_id=book_id)
    if not del_book:
        raise HTTPException(status_code=404,detail="Không tìm thấy sách")
    return {"message":"Xóa thành công"}

@router.get("/{book_id}")
def get_book_by_ids(book_id:int,db:Session=Depends(get_db)):
    book = get_book_by_id(db,book_id=book_id)
    if not book :
        raise HTTPException(status_code=404,detail="Khồn tìm thấy sách")
    return book