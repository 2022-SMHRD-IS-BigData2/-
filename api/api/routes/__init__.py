from fastapi import APIRouter

from .patient_route import router as patient_router
from .record_route import router as record_router
from ..core import Security

router = APIRouter()

router.include_router(Security)
router.include_router(patient_router)
router.include_router(record_router)