from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
 
class Base(DeclarativeBase):
    pass


class League(Base):
    __tablename__="leagues"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    type: Mapped[Optional[str]]
    logo: Mapped[Optional[str]]
    country_id: Mapped[str] = mapped_column(ForeignKey("countries.name"))

    def __repr__(self) -> str:
        return f"league(id={self.id!r}, name={self.name!r}, type={self.leuague_type!r}, logo={self.logo!r}, country_id={self.country_id!r})"
    

    
class Country(Base):
    __tablename__="countries"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    code: Mapped[Optional[str]]
    flag: Mapped[Optional[str]]
    
    def __repr__(self) -> str:
        return f"country(id={self.id!r}, name={self.name!r}, code={self.code!r}, flag={self.flag!r})"
    


class Season(Base):
    __tablename__="seasons"

    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[Optional[str]]
    start: Mapped[Optional[str]]
    end: Mapped[Optional[str]]
    current: Mapped[Optional[bool]]
    league_id: Mapped[int] = mapped_column(ForeignKey("leagues.id"))


    def __repr__(self) -> str:
        return f"season(id={self.id!r}, year={self.year!r}, start={self.start!r}, end={self.end!r}, current={self.current!r})"