# app/routers/tasks.py
from typing import List
from fastapi import APIRouter, HTTPException, Body, Path, status
from starlette.responses import JSONResponse # Resposta do Starlette

from .. import schemas  # Importa da pasta pai (app)
from .. import services # Importa da pasta pai (app)

# APIRouter funciona como um "mini-FastAPI"
router = APIRouter(
    prefix="/tasks",  # Adiciona /tasks na frente de todas as rotas
    tags=["Tasks"]    # Agrupa na documentação /docs
)

@router.post("/", 
             response_model=schemas.TaskOut, 
             status_code=status.HTTP_201_CREATED,
             summary="Cria uma nova tarefa")
async def create_task(task_in: schemas.TaskIn = Body(...)):
    """Cria uma nova tarefa e a armazena no banco de dados."""
    return services.create_db_task(task_in=task_in)

@router.get("/{task_id}", 
            response_model=schemas.TaskOut,
            summary="Obtém uma tarefa pelo ID")
async def get_task(task_id: int = Path(..., gt=0, description="O ID da tarefa a ser buscada")):
    """Busca uma única tarefa pelo seu ID."""
    task = services.get_db_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Tarefa não encontrada")
    return task

@router.get("/", 
            response_model=List[schemas.TaskOut],
            summary="Lista todas as tarefas")
async def get_all_tasks():
    """Retorna uma lista de todas as tarefas cadastradas."""
    return services.get_all_db_tasks()

@router.put("/{task_id}", 
            response_model=schemas.TaskOut,
            summary="Atualiza uma tarefa existente")
async def update_task(
    task_id: int = Path(..., gt=0),
    task_update: schemas.TaskIn = Body(...)
):
    """Atualiza completamente uma tarefa existente."""
    task = services.update_db_task(task_id, task_update)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Tarefa não encontrada")
    return task

@router.delete("/{task_id}", 
               status_code=status.HTTP_200_OK,
               summary="Deleta uma tarefa")
async def delete_task(task_id: int = Path(..., gt=0)):
    """Deleta uma tarefa pelo seu ID."""
    task = services.delete_db_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Tarefa não encontrada")
    
    # Usando a resposta JSON do Starlette
    return JSONResponse(
        content={"message": "Tarefa deletada com sucesso"},
        status_code=status.HTTP_200_OK
    )