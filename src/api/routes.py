from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def index():
   return {"message": "Estou participando do processo seletivo BTG! 🚀"}