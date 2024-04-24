from pydantic import BaseModel


class PatronModel(BaseModel):
    s1: int
    s2: int
    s3: int
    yd1: int
    yd2: int


class FileModel(BaseModel):
    weights: list[list[float]]
    thresholds: list[float]


class LayerValues(BaseModel):
    layerValues: list[int]

class NetworkLayer(BaseModel):
    neurons: int
    activationFunction: str

class Configuration(BaseModel):
    weights: list[list[list[float]]]
    thresholds: list[list[float]] 
    networkLayers: list[NetworkLayer]