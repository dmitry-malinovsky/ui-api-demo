from pydantic import BaseModel, HttpUrl
from typing import List

class Person(BaseModel):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: HttpUrl
    films: List[HttpUrl]
    species: List[HttpUrl]
    vehicles: List[HttpUrl]
    starships: List[HttpUrl]
    created: str
    edited: str
    url: HttpUrl


class PlanetResponse(BaseModel):
    name: str
    rotation_period: str
    orbital_period: str
    diameter: str
    climate: str
    gravity: str
    terrain: str
    surface_water: str
    population: str
    residents: List[HttpUrl]
    films: List[HttpUrl]
    created: str
    edited: str
    url: HttpUrl


class FilmResponse(BaseModel):
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: str
    characters: List[HttpUrl]
    planets: List[HttpUrl]
    starships: List[HttpUrl]
    vehicles: List[HttpUrl]
    species: List[HttpUrl]
    created: str
    edited: str
    url: HttpUrl


class SpeciesResponse(BaseModel):
    name: str
    classification: str
    designation: str
    average_height: str
    skin_colors: str
    hair_colors: str
    eye_colors: str
    average_lifespan: str
    homeworld: HttpUrl
    language: str
    people: List[HttpUrl]
    films: List[HttpUrl]
    created: str
    edited: str
    url: HttpUrl