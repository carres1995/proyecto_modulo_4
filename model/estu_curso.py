from sqlalchemy import Column, Integer, ForeignKey, Table
from data.base import Base

estudiante_curso = Table(
    "estudiante_curso",
    Base.metadata,
    Column("estudiante_id", Integer, ForeignKey("estudiantes.id"), primary_key=True),
    Column("curso_id", Integer, ForeignKey("cursos.id"), primary_key=True)
)