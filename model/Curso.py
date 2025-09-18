from sqlalchemy import Column, String, Integer, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from model.estu_curso import estudiante_curso
from data.base import Base

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    fecha_inicio = Column(Date, nullable=True)
    fecha_fin = Column(Date, nullable=True)
    docente_id = Column(Integer, ForeignKey("docentes.id"), nullable=False)


    estudiantes = relationship("Estudiante", secondary=estudiante_curso, back_populates="cursos")
    docente = relationship("Docente", back_populates="cursos")
    inscripciones = relationship("Inscripcion", back_populates="curso")