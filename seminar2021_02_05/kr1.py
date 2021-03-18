"""
База данных страховой компании

База состоит из 5 таблиц:
    -Собственники
    -Недвижимость
    -Риэлторы
    -Страховой контракты,
    -Тарифы

Бизнес-требования:
    -Связь между собственниками и недвижимостью один ко многим (у одного собственника может быть много недвижимостей)
    -По одной недвижимости может быть несколько страховых контрактов
    -Аналогично, у одного риэлтора может быть несколько контрактов
    -Несколько контрактов могут использоваться один тариф
"""


from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Float, CheckConstraint
engine = create_engine(f'sqlite:///owners.db')
metadata = MetaData()

user_owner = Table(
    'user_owners', metadata,
    Column('id', Integer()),
    Column('owner_type', String(15), nullable=False),
    Column('first_name', String(25), nullable=False),
    Column('last_name', String(25), nullable=False),
    Column('middle_name', String(25), nullable=False),
    Column('address', String(255), nullable=False),
    Column('phone', String(20), nullable=False, unique=True, index=True),
    Column('passport_number', String(10), nullable=False),
    extend_existing=True
)

own = Table(
    "owns", metadata,
    Column("code", String(20), primary_key=True),
    Column("own_type", String(20), nullable=False),
    Column("square", Float(), nullable=False),
    Column("address", String(255), nullable=False),
    Column("price", Float()),
    Column("user_owners_id", Integer(), ForeignKey("user_owners.id")),
    CheckConstraint('price >= 0', name='unit_cost_positive'),
    extend_existing=True
)

realtor = Table(
    "realtors", metadata,
    Column("id", Integer(), primary_key=True),
    Column("address", String(255), nullable=False),
    Column("phone", String(20), nullable=False, unique=True, index=True),
    Column("insurance_agency", String(50)),
    extend_existing=True
)

insurance_contract = Table(
    "insurance_contracts", metadata,
    Column("code", Integer(), primary_key=True),
    Column("own_code", String(20), ForeignKey("owns.code"), nullable=False),
    Column("realtor_id", Integer(), ForeignKey("realtors.id"), nullable=False),
    Column("rate_code", String(20), ForeignKey("rates.code"), nullable=False),
    extend_existing=True
)

rate = Table(
    "rates", metadata,
    Column("code", String(20), primary_key=True),
    Column("name", String(50)),
    Column("interest6m", Float(), default=3.5),
    Column("interest12m", Float(), nullable=False, default=1.5),
    Column("interest36m", Float(), default=0.47),
    extend_existing=True
)

metadata.create_all(engine)
