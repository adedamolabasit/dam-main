"""empty message

Revision ID: 015954272231
Revises: 32e9e69d5f6b
Create Date: 2022-02-22 15:12:43.801884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '015954272231'
down_revision = '32e9e69d5f6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('blog', 'author',
               existing_type=sa.INTEGER(),
               nullable='True')
    op.alter_column('comment', 'author',
               existing_type=sa.INTEGER(),
               nullable='True')
    op.alter_column('comment', 'post_id',
               existing_type=sa.INTEGER(),
               nullable='True')
    op.alter_column('comment', 'blog_id',
               existing_type=sa.INTEGER(),
               nullable='True')
    op.add_column('home', sa.Column('headings1', sa.String(), nullable=True))
    op.add_column('home', sa.Column('details1', sa.Text(), nullable=True))
    op.add_column('home', sa.Column('headings2', sa.String(), nullable=True))
    op.add_column('home', sa.Column('details2', sa.Text(), nullable=True))
    op.add_column('home', sa.Column('headings3', sa.String(), nullable=True))
    op.add_column('home', sa.Column('details3', sa.Text(), nullable=True))
    op.add_column('home', sa.Column('headings4', sa.String(), nullable=True))
    op.add_column('home', sa.Column('details4', sa.Text(), nullable=True))
    op.add_column('home', sa.Column('headings5', sa.String(), nullable=True))
    op.add_column('home', sa.Column('details5', sa.Text(), nullable=True))
    op.add_column('home', sa.Column('headings6', sa.String(), nullable=True))
    op.add_column('home', sa.Column('details6', sa.Text(), nullable=True))
    op.drop_column('home', 'details')
    op.drop_column('home', 'headings')
    op.alter_column('post', 'author',
               existing_type=sa.INTEGER(),
               nullable='True')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('home', sa.Column('headings', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('home', sa.Column('details', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('home', 'details6')
    op.drop_column('home', 'headings6')
    op.drop_column('home', 'details5')
    op.drop_column('home', 'headings5')
    op.drop_column('home', 'details4')
    op.drop_column('home', 'headings4')
    op.drop_column('home', 'details3')
    op.drop_column('home', 'headings3')
    op.drop_column('home', 'details2')
    op.drop_column('home', 'headings2')
    op.drop_column('home', 'details1')
    op.drop_column('home', 'headings1')
    op.alter_column('comment', 'blog_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comment', 'post_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comment', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('blog', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
