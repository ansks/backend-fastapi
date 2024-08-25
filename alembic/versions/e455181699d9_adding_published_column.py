"""adding published column

Revision ID: e455181699d9
Revises: 6896f8518d03
Create Date: 2024-08-25 05:35:03.852557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e455181699d9'
down_revision: Union[str, None] = '6896f8518d03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.String(), nullable=False, server_default="true"))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    pass
