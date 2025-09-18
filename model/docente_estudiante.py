from sqlalchemy import Table, Column, Integer, ForeignKey
from data.base import Base

docente_estudiante = Table(
    "docente_estudiante",
    Base.metadata,
    Column("docente_id", Integer, ForeignKey("docentes.id"), primary_key=True),
    Column("estudiante_id", Integer, ForeignKey("estudiantes.id"), primary_key=True)
)