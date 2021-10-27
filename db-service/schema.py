from pydantic import BaseModel


class Dataset_table(BaseModel):
    url: str
    evaluation: str

    class Config:
        orm_mode = True

class evaluation_model(BaseModel):
    evaluation : str

    class Config:
        orm_mode = True

class Message(BaseModel):
    message: str