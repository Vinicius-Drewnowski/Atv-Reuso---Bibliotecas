# app/schemas.py
from typing import Optional
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    """Modelo base da tarefa."""
    title: str = Field(..., min_length=3, max_length=100, description="O título da tarefa")
    description: Optional[str] = Field(None, max_length=500, description="A descrição da tarefa")
    completed: bool = False

class TaskIn(TaskBase):
    """Modelo para criar uma nova tarefa (entrada)."""
    pass

class TaskOut(TaskBase):
    """Modelo para retornar uma tarefa (saída)."""
    id: int
    
    class Config:
        orm_mode = True

class MusicBase(BaseModel):
    """Modelo base da Música."""
    nome_musica: str = Field(..., min_length=1, max_length=100)
    nome_cantor: str = Field(..., min_length=1, max_length=100)
    genero_musical: str = Field(..., min_length=2, max_length=50)

class MusicIn(MusicBase):
    """Modelo para criar uma nova música (entrada)."""
    pass

class MusicOut(MusicBase):
    """Modelo para retornar uma música (saída)."""
    id: int
    
    class Config:
        orm_mode = True