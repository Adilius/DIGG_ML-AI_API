from pydantic import BaseModel


class Dataset_table(BaseModel):
    url: str
    hash: str
    evaluation: str

    class Config:
        orm_mode = True
