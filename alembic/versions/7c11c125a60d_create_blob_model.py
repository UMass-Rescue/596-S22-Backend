"""create blob model

Revision ID: 7c11c125a60d
Revises: 1050b69f3e0b
Create Date: 2022-03-27 14:00:46.213326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c11c125a60d'
down_revision = '1050b69f3e0b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "blobs",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("date_uploaded", sa.TIMESTAMP(), nullable=False, index=True),
        sa.Column("description", sa.String, index=True),
        sa.Column("key", sa.String, index=True),
        sa.Column("file_type", sa.String, index=True),
        sa.Column("case_id", sa.Integer),
        sa.ForeignKeyConstraint(('case_id',), ['cases.id'], ),
    )


def downgrade():
    op.drop_table("blobs")
