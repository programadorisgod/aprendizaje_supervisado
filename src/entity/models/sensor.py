from pydantic import BaseModel


class SensorModel(BaseModel):
    s1: int
    s2: int
    s3: int
    yd1: int
    yd2: int
