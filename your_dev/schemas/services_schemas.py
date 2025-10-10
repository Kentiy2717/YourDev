from pydantic import BaseModel, EmailStr, Field, ConfigDict


class ServiceCreate(BaseModel):
    pass


class Service(BaseModel):
    pass

    model_config = ConfigDict(from_attributes=True)