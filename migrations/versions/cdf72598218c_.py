"""empty message

Revision ID: cdf72598218c
Revises: 1d533f74b8af
Create Date: 2021-12-25 01:22:15.915300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdf72598218c'
down_revision = '1d533f74b8af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('posts', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'posts')
    # ### end Alembic commands ###