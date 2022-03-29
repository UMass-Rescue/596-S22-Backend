"""create interview tables

Revision ID: 674d8bbbeba9
Revises: 1ed3dfe8c024
Create Date: 2022-03-28 17:13:38.828790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '674d8bbbeba9'
down_revision = '1ed3dfe8c024'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "interviews",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("blob_id", sa.Integer),
        sa.Column("first_name", sa.String, index=True),
        sa.Column("last_name", sa.String, index=True),
        sa.Column("date_uploaded", sa.TIMESTAMP(), nullable=False, index=True),
        sa.Column("address", sa.String),
        sa.Column("case_id", sa.Integer),
        sa.ForeignKeyConstraint(('case_id',), ['cases.id'], ),
        sa.ForeignKeyConstraint(('blob_id',), ['blobs.id'], ),
    )
    op.create_table(
        "interview_answers",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("answer", sa.String),

        sa.Column("question_id", sa.Integer),
        sa.ForeignKeyConstraint(('question_id',), ['questions.id'], ),

        sa.Column("interview_id", sa.Integer),
        sa.ForeignKeyConstraint(('interview_id',), ['interviews.id'], ),
    )
    op.create_table(
        "interview_answer_ners",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("label", sa.String, index=True),
        sa.Column("start_index", sa.String),
        sa.Column("end_index", sa.String),
        sa.Column("interview_answer_id", sa.Integer),
        sa.ForeignKeyConstraint(('interview_answer_id',), ['interview_answers.id'], ),
    )


def downgrade():
    op.drop_table("interviews")
    op.drop_table("interview_answers")
    op.drop_table("interview_answer_ners")
