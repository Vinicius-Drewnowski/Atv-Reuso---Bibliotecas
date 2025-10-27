# app/services.py
from typing import Dict, List, Optional
from . import schemas # Importa os schemas do mesmo pacote

# --- "Banco de Dados" em Memória ---
db_tasks: Dict[int, schemas.TaskOut] = {}
next_task_id = 1

def create_db_task(task_in: schemas.TaskIn) -> schemas.TaskOut:
    """Cria uma tarefa no 'banco de dados'."""
    global next_task_id
    new_task = schemas.TaskOut(id=next_task_id, **task_in.dict())
    db_tasks[next_task_id] = new_task
    next_task_id += 1
    return new_task

def get_db_task(task_id: int) -> Optional[schemas.TaskOut]:
    """Busca uma tarefa no 'banco de dados' pelo ID."""
    return db_tasks.get(task_id)

def get_all_db_tasks() -> List[schemas.TaskOut]:
    """Retorna todas as tarefas do 'banco de dados'."""
    return list(db_tasks.values())

def update_db_task(task_id: int, task_update: schemas.TaskIn) -> Optional[schemas.TaskOut]:
    """Atualiza uma tarefa no 'banco de dados'."""
    if task_id not in db_tasks:
        return None
    
    updated_task = schemas.TaskOut(id=task_id, **task_update.dict())
    db_tasks[task_id] = updated_task
    return updated_task

def delete_db_task(task_id: int) -> Optional[schemas.TaskOut]:
    """Deleta uma tarefa do 'banco de dados'."""
    if task_id not in db_tasks:
        return None
    
    # Retorna o item deletado
    return db_tasks.pop(task_id)

db_music: Dict[int, schemas.MusicOut] = {}
next_music_id = 1

def create_db_music(music_in: schemas.MusicIn) -> schemas.MusicOut:
    """Cria uma música no 'banco de dados'."""
    global next_music_id
    new_music = schemas.MusicOut(id=next_music_id, **music_in.dict())
    db_music[next_music_id] = new_music
    next_music_id += 1
    return new_music

def get_db_music(music_id: int) -> Optional[schemas.MusicOut]:
    """Busca uma música no 'banco de dados' pelo ID."""
    return db_music.get(music_id)

def get_all_db_music() -> List[schemas.MusicOut]:
    """Retorna todas as músicas do 'banco de dados'."""
    return list(db_music.values())

def update_db_music(music_id: int, music_update: schemas.MusicIn) -> Optional[schemas.MusicOut]:
    """Atualiza uma música no 'banco de dados'."""
    if music_id not in db_music:
        return None
    
    updated_music = schemas.MusicOut(id=music_id, **music_update.dict())
    db_music[music_id] = updated_music
    return updated_music

def delete_db_music(music_id: int) -> Optional[schemas.MusicOut]:
    """Deleta uma música do 'banco de dados'."""
    if music_id not in db_music:
        return None
    
    return db_music.pop(music_id)