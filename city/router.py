from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from . import crud, schemas

router = APIRouter()


@router.get("/cities/", response_model=list[schemas.CityRead])
async def get_cities(db: AsyncSession = Depends(get_db)):
    return await crud.get_city_list(db=db)


@router.post("/cities/", response_model=schemas.CityCreate)
async def create_city(city: schemas.CityCreate,
                      db: AsyncSession = Depends(get_db)):
    return await crud.create_city(db=db, city=city)


@router.get("/cities/{city_id}/", response_model=schemas.CityReadDetails | None)
async def get_city(city_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_city(db=db, city_id=city_id)


@router.put("/cities/{city_id}/", response_model=schemas.CityUpdate | None)
async def update_city(city_id: int, city: schemas.CityUpdate,
                      db: AsyncSession = Depends(get_db)):
    return await crud.update_city(db=db, city_id=city_id, city=city)


@router.delete("/cities/{city_id}/", response_model=schemas.CityDelete | None)
async def delete_city(city_id: int, db: AsyncSession = Depends(get_db)):
    await crud.delete_city(db=db, city_id=city_id)
    return {"message": "City deleted successfully"}