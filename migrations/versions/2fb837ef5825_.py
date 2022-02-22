"""empty message

Revision ID: 2fb837ef5825
Revises: b8757591cdf9
Create Date: 2022-02-22 15:47:29.918316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fb837ef5825'
down_revision = 'b8757591cdf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('home')
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
    op.add_column('home2', sa.Column('details', sa.Text(), nullable=True))
    op.add_column('home4', sa.Column('headings', sa.String(), nullable=True))
    op.add_column('home4', sa.Column('details', sa.Text(), nullable=True))
    op.drop_column('home4', 'details3')
    op.add_column('home5', sa.Column('headings', sa.String(), nullable=True))
    op.add_column('home5', sa.Column('details', sa.Text(), nullable=True))
    op.drop_column('home5', 'headings6')
    op.drop_column('home5', 'details6')
    op.drop_column('home5', 'headings5')
    op.drop_column('home5', 'details5')
    op.drop_column('home5', 'headings4')
    op.drop_column('home5', 'details4')
    op.alter_column('post', 'author',
               existing_type=sa.INTEGER(),
               nullable='True')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('home5', sa.Column('details4', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('home5', sa.Column('headings4', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('home5', sa.Column('details5', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('home5', sa.Column('headings5', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('home5', sa.Column('details6', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('home5', sa.Column('headings6', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('home5', 'details')
    op.drop_column('home5', 'headings')
    op.add_column('home4', sa.Column('details3', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('home4', 'details')
    op.drop_column('home4', 'headings')
    op.drop_column('home2', 'details')
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
    op.create_table('home',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('headings', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('details', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='home_pkey')
    )
    # ### end Alembic commands ###
