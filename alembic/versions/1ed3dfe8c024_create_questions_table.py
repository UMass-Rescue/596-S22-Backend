"""create questions table

Revision ID: 1ed3dfe8c024
Revises: 7c11c125a60d
Create Date: 2022-03-28 10:22:28.118861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ed3dfe8c024'
down_revision = '7c11c125a60d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("text", sa.String, index=True),
        sa.Column("case_id", sa.Integer),
        sa.ForeignKeyConstraint(('case_id',), ['cases.id'], ),
    )


def downgrade():
    op.drop_table("questions")
