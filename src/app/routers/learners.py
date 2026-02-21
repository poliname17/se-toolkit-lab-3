"""Router for learner endpoints."""

from fastapi import APIRouter

from datetime import datetime
from typing import Optional
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.learners import read_learners, create_learner
from app.models.learner import Learner, LearnerCreate

router = APIRouter()

# ===
# PART A: GET endpoint
# ===

# UNCOMMENT AND FILL IN
#
@router.get("/learners", response_model=list[Learner])
async def read_learners_endpoint(
    enrolled_after: Optional[datetime] = None,
    session: AsyncSession = Depends(get_session),
):
    """<docstring>"""
    return await read_learners(session, enrolled_after)



# ===
# PART B: POST endpoint
# ===

# UNCOMMENT AND FILL IN
#
@router.post("/learners", response_model=Learner, status_code=201)
async def create_learner_endpoint(
    learner: LearnerCreate,
    session: AsyncSession = Depends(get_session),
):
    """Create a new learner"""
    return await create_learner(session, name=learner.name, email=learner.email)