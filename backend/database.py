from contextlib import contextmanager
from config import AppSettings
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Annotated, List

#Models
class BaseModel(DeclarativeBase):
    pass

class TrafficLogModel(BaseModel):

    __tablename__ = "taffic_logs"

    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    host: Mapped[str] = mapped_column(nullable=False)
    client_ip: Mapped[str] = mapped_column(nullable=False)
    source_route: Mapped[str] = mapped_column(nullable=False)
    http_verb: Mapped[str] = mapped_column(nullable=False)
    headers: Mapped[str] = mapped_column(nullable=True)
    traffic_date: Mapped[str] = mapped_column(nullable=False)

class VirginiaLandmarkModel(BaseModel):

    __tablename__ = "virginia_landmarks" 

    id: Mapped[int] = mapped_column(primary_key=True, index=True) 
    landmark_name: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=True)  
    city: Mapped[str] = mapped_column(nullable=True)
    state: Mapped[str] = mapped_column(nullable=True)  
    zip: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    url: Mapped[str] = mapped_column(nullable=True)
    latitude: Mapped[float] = mapped_column(nullable=False)
    longitude: Mapped[float] = mapped_column(nullable=False)
    location_type: Mapped[str] = mapped_column(nullable=False, index=True)
    location: Mapped[str] = mapped_column(nullable=False, index=True)


settings: AppSettings = AppSettings()

connect_args = {"check_same_thread": False}

engine = create_engine(
    settings.db_connection_string,
    connect_args=connect_args
)


@contextmanager
def get_context_session():
    with Session(engine) as session:
        yield session

def get_fastapi_session():
    with Session(engine) as session:
        yield session

def ensure_database_created():
    BaseModel.metadata.create_all(engine)

SessionDep = Annotated[Session, Depends(get_fastapi_session)]

class VirginiaLandmarkRepository:

    def __init__(self, session: Session) -> None:
        self.__session = session

    @property
    def db_session(self) -> Session:
        return self.__session
    

    def record_count(self) -> int:
        return self.db_session.query(VirginiaLandmarkModel).count()

    def truncate(self) -> int:
        record_count = self.record_count()
        self.db_session.query(VirginiaLandmarkModel).delete()
        return record_count

    def save_all(self, models: List[VirginiaLandmarkModel]) -> int:
        record_count = len(models)
        self.db_session.add_all(models)
        self.db_session.commit()
        return record_count
    
    def search(self, location_filter: List[str] = None, location_type_filters: List[str] = None) -> List[VirginiaLandmarkModel]:

        query = self.db_session.query(VirginiaLandmarkModel)

        if location_filter:
            query = query.filter(VirginiaLandmarkModel.location.in_(location_filter))

        if location_type_filters:
            query = query.filter(VirginiaLandmarkModel.location_type.in_(location_type_filters))

        return query.all()
    
    def get_locations(self) -> List[str]:
        
        lookup: list[str] = []

        query = self.db_session.query(VirginiaLandmarkModel.location).distinct()
        rows = query.all()

        for row in rows:
            lookup.append(row[0])

        return lookup

    def get_location_types(self) -> List[str]:

        lookup: list[str] = []

        query = self.db_session.query(VirginiaLandmarkModel.location_type).distinct()
        rows = query.all()

        for row in rows:
            lookup.append(row[0])

        return lookup