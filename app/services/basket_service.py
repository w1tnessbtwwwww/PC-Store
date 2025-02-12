from app.models.models import Basket
from app.database.connector import *

from fastapi import HTTPException
from sqlalchemy import select


class BasketService():
    def __init__(self, session:Session):
        self.session = session

    async def check_basket(self, user_id: int):
        query = select(Basket).filter(Basket.user_id == user_id)

        result = self.session.execute(query)
        basket = result.scalars().all()
        if basket is None:
            raise HTTPException(
                status_code = 404,
                detail = "Ваша корзина пуста"
            )
        return basket
        
    