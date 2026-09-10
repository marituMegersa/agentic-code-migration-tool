from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.code_migration_tool.schemas import AgenticCodeMigrationToolSessionCreate, AgenticCodeMigrationToolSessionResponse
from app.domain.code_migration_tool.service import AgenticCodeMigrationToolService

router = APIRouter(prefix="/api/v1/code_migration_tool", tags=["Agentic Code Migration Tool Domain"])

@router.post("/sessions", response_model=AgenticCodeMigrationToolSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticCodeMigrationToolSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Code Migration Tool.
    """
    return AgenticCodeMigrationToolService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticCodeMigrationToolSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticCodeMigrationToolService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
