"""readding table

Revision ID: c5aa16627678
Revises: 44ec38799d8b
Create Date: 2024-08-25 00:42:12.800518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5aa16627678'
down_revision: Union[str, None] = '44ec38799d8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts", 
                    sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
                    sa.Column("title", sa.String(), nullable=False),
                    sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
