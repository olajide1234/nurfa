from fastapi import APIRouter

from nurfa.v1.routers import news

router = APIRouter(
    prefix="/v1",
)

# router.include_router(auth.router)
router.include_router(news.router)
