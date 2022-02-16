from graphene import String
from mysqlx import Column
import sqlalchemy
from database import metadata

notes = sqlalchemy.Table (
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)