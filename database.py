# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base  # Importamos la Base y los modelos

# Cambia la URL de la base de datos si es necesario
SQLALCHEMY_DATABASE_URL = "postgresql://sistema_admision:password@localhost/sistema_admision"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para crear las tablas en la base de datos
def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print("Tablas creadas en la base de datos.")