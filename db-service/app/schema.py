from pydantic import BaseModel


class Dataset_table(BaseModel):
    name: str
    rating: float
    testProperty: str

    class Config:
        orm_mode = True
