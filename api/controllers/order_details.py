from sqlalchemy.orm import Session
from ..models import models, schemas
from fastapi import HTTPException

def create_order_detail(db: Session, order_detail: schemas.OrderDetailCreate):
    db_order_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        amount=order_detail.amount
    )
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def read_all_order_details(db: Session):
    return db.query(models.OrderDetail).all()

def read_order_detail(db: Session, order_detail_id: int):
    order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if order_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return order_detail

def update_order_detail(db: Session, order_detail_id: int, order_detail: schemas.OrderDetailUpdate):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if db_order_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    for key, value in order_detail.dict(exclude_unset=True).items():
        setattr(db_order_detail, key, value)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def delete_order_detail(db: Session, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if db_order_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    db.delete(db_order_detail)
    db.commit()
    return {"detail": "Order detail deleted successfully"}