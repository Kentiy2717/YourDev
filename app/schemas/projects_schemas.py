from pydantic import BaseModel, EmailStr, Field, ConfigDict


class ProjectCreate(BaseModel):
    pass


class Project(BaseModel):
    pass

    model_config = ConfigDict(from_attributes=True)