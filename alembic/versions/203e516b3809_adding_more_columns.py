"""adding more columns

Revision ID: 203e516b3809
Revises: c5aa16627678
Create Date: 2024-08-25 00:53:49.191841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '203e516b3809'
down_revision: Union[str, None] = 'c5aa16627678'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(table_name = "posts", 
                  column=sa.Column('published', 
                                   sa.Boolean(), 
                                   nullable=False, 
                                   server_default="True"))
    
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    pass
