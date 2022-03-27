"""craete case table

Revision ID: 1050b69f3e0b
Revises: b7a58cb0b6e2
Create Date: 2022-03-26 23:05:47.385451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1050b69f3e0b'
down_revision = 'b7a58cb0b6e2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "cases",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("start_date", sa.TIMESTAMP(), nullable=False, index=True),
        sa.Column("end_date", sa.TIMESTAMP(), index=True),
        sa.Column("is_active", sa.Boolean, default=True),
    )


def downgrade():
    op.drop_table("cases")
