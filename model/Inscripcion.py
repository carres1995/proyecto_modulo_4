from sqlalchemy import Column, String, Text, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from data.base import Base


class Inscripcion(Base):
    __tablename__ = "inscripciones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    estudiante_id = Column(Integer, ForeignKey("estudiantes.id"), nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    fecha_inscripcion = Column(Date, nullable=False)

    estudiante = relationship("Estudiante", back_populates="inscripciones")
    curso = relationship("Curso", back_populates="inscripciones")
    
    def __repr__(self):
        return f"<Inscripcion(id={self.id}, estudiante_id={self.estudiante_id}, curso_id={self.curso_id}, fecha_inscripcion={self.fecha_inscripcion})>"