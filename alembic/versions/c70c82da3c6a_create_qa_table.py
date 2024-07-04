"""create QA table

Revision ID: c70c82da3c6a
Revises: 
Create Date: 2024-07-04 15:07:30.816153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c70c82da3c6a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
qa_table_name = "qa_table"

def upgrade() -> None:
    op.create_table(
        qa_table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("question", sa.String(200), unique=False,nullable=False),
        sa.Column("answer", sa.String(150), unique=False,nullable=False),
    )


def downgrade() -> None:
    op.drop_table(qa_table_name)
