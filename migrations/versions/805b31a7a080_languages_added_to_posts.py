"""languages added to posts

Revision ID: 805b31a7a080
Revises: 0a4fa6aeebd0
Create Date: 2020-09-14 13:07:32.118551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '805b31a7a080'
down_revision = '0a4fa6aeebd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=6), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
