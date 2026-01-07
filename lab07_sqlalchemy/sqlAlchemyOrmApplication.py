import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import Session

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"

    # Atributos
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    fullname = sa.Column(sa.String)

    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"

    # Atributos
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email_address = sa.Column(sa.String(30), nullable=False)
    user_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("user_account.id"),
        nullable=False,
    )

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


# Conexão com o banco de dados
engine = sa.create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)


with Session(engine) as session:
    joao = User(
        name="joao",
        fullname="João Silva",
        addresses=[Address(email_address="joao@email.com")],
    )
    maria = User(
        name="maria",
        fullname="Maria Silva",
        addresses=[
            Address(email_address="maria@email.com"),
            Address(email_address="marias@email.org"),
        ],
    )

    # Enviando dados para o banco de dados
    session.add_all([joao, maria])
    session.commit()


session_show_results = lambda stmt: [result for result in session.scalars(stmt)]
connection_show_results = lambda results: [result for result in results]

stmt = sa.select(User).where(User.name.in_(["maria"]))
print(session_show_results(stmt))

stmt = sa.select(User).order_by(User.id.desc())
print(session_show_results(stmt))

# stmt por sessão
stmt = sa.select(User.fullname, Address.email_address).join_from(Address, User)
print(session_show_results(stmt))

# stmt por conexão
connection = engine.connect()
results = connection.execute(stmt).fetchall()
print(connection_show_results(results))
