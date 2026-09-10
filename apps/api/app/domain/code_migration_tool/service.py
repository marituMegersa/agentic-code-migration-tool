from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.code_migration_tool.models import AgenticCodeMigrationToolSession, AgenticCodeMigrationToolItem
from app.domain.code_migration_tool.schemas import AgenticCodeMigrationToolSessionCreate, AgenticCodeMigrationToolItemCreate

class AgenticCodeMigrationToolService:
    @staticmethod
    def create_session(db: Session, data: AgenticCodeMigrationToolSessionCreate) -> AgenticCodeMigrationToolSession:
        db_obj = AgenticCodeMigrationToolSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticCodeMigrationToolSession:
        return db.query(AgenticCodeMigrationToolSession).filter(AgenticCodeMigrationToolSession.id == session_id).first()
