"""empty message

Revision ID: 7a5fc83c2718
Revises: 203e516b3809
Create Date: 2024-08-25 01:04:56.931541

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '7a5fc83c2718'
down_revision: Union[str, None] = '203e516b3809'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.drop_table('posts_old')
    op.drop_table('products')
    op.add_column('posts', sa.Column('rating', sa.Integer(), server_default=sa.text('0'), nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("posts_users_fk", 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'rating')
    # op.create_table('products',
    # sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    # sa.Column('price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('is_sale', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    # sa.Column('inventory', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    # sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('id', name='products_pkey')
    # )
    # op.create_table('posts_old',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    # sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False),
    # sa.Column('published', sa.BOOLEAN(), autoincrement=False, nullable=False),
    # sa.Column('rating', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('id', name='posts_pkey')
    # )
    op.drop_table('votes')
    op.drop_table('users')
    # ### end Alembic commands ###