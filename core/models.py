from sqlalchemy import Column, Integer, String, Float, DateTime, func
from geoalchemy2 import Geometry
from .db import Base

class Fissure(Base):
    __tablename__ = "fissures"

    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(String, nullable=False)
    severity_score = Column(Float, nullable=True)
    # Point géographique en WGS84 (EPSG:4326)
    geom = Column(Geometry(geometry_type="POINT", srid=4326), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
