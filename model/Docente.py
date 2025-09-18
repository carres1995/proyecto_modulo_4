from sqlalchemy import Column, String, Integer, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from model.docente_estudiante import docente_estudiante
from data.base import Base

class Docente(Base):
    __tablename__ = "docentes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_identificacion = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    especialidad = Column(String(100), nullable=True)

    cursos = relationship("Curso", back_populates="docente")
    estudiantes = relationship("Estudiante", secondary=docente_estudiante, back_populates="docentes")