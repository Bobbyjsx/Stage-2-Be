from pydantic import BaseModel, validator

class Person(BaseModel):
    name: str

    @validator("name", pre=True, always=True)
    def check_unique_name(cls, value, values):
        existing_names = [p.name for p in values.get("persons", [])]
        if value in existing_names:
            raise ValueError("Name must be unique")
        return value
