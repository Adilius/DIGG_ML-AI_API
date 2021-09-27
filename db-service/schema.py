from pydantic import BaseModel


class Dataset_table(BaseModel):
    url: str
    checksum: str
    evaluation: str

    class Config:
        orm_mode = True

class evaluation_model(BaseModel):
    evaluation : str

    class Config:
        orm_mode = True