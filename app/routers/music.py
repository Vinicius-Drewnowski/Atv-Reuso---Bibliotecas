# app/routers/music.py
from typing import List
from fastapi import APIRouter, HTTPException, Body, Path, status
from starlette.responses import JSONResponse # Resposta do Starlette

from .. import schemas 
from .. import services 

# Criamos um novo roteador.
router = APIRouter(
    prefix="/musicas",
    tags=["Músicas"]
)

@router.post("/", 
             response_model=schemas.MusicOut, 
             status_code=status.HTTP_201_CREATED,
             summary="Cria uma nova música")
async def create_music(music_in: schemas.MusicIn = Body(...)):
    """Cria uma nova música e a armazena no banco de dados."""
    return services.create_db_music(music_in=music_in)

@router.get("/{music_id}", 
            response_model=schemas.MusicOut,
            summary="Obtém uma música pelo ID")
async def get_music(music_id: int = Path(..., gt=0, description="O ID da música a ser buscada")):
    """
    Busca uma única música pelo seu ID.
    (Esta é a rota /musicas/1 que você pediu)
    """
    music = services.get_db_music(music_id)
    if not music:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Música não encontrada")
    return music

@router.get("/", 
            response_model=List[schemas.MusicOut],
            summary="Lista todas as músicas")
async def get_all_music():
    """
    Retorna uma lista de todas as músicas cadastradas.
    (Esta é a rota /musicas/ que você pediu)
    """
    return services.get_all_db_music()

@router.put("/{music_id}", 
            response_model=schemas.MusicOut,
            summary="Atualiza uma música existente")
async def update_music(
    music_id: int = Path(..., gt=0),
    music_update: schemas.MusicIn = Body(...)
):
    """Atualiza completamente uma música existente."""
    music = services.update_db_music(music_id, music_update)
    if not music:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Música não encontrada")
    return music

@router.delete("/{music_id}", 
               status_code=status.HTTP_200_OK,
               summary="Deleta uma música")
async def delete_music(music_id: int = Path(..., gt=0)):
    """Deleta uma música pelo seu ID."""
    music = services.delete_db_music(music_id)
    if not music:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Música não encontrada")
    
    return JSONResponse(
        content={"message": "Música deletada com sucesso"},
        status_code=status.HTTP_200_OK
    )