"""add phone number

Revision ID: 2abd1ac114f2
Revises: 727055ad04fe
Create Date: 2024-08-25 01:20:03.039067

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2abd1ac114f2'
down_revision: Union[str, None] = '727055ad04fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("phone_number",
                            sa.String(), 
                            nullable=False, 
                            server_default=""))
    pass


def downgrade() -> None:
    op.drop_column("posts", "phone_number")
    pass
