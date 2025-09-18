from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from model.estu_curso import estudiante_curso
from model.docente_estudiante import docente_estudiante
from data.base import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_identificacion = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)

    cursos = relationship("Curso", secondary=estudiante_curso, back_populates="estudiantes")
    inscripciones = relationship("Inscripcion", back_populates="estudiante")
    docentes = relationship("Docente", secondary=docente_estudiante, back_populates="estudiantes")