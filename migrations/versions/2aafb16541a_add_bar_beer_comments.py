"""Add bar/beer comments

Revision ID: 2aafb16541a
Revises: 379a369c64e
Create Date: 2015-07-26 15:19:53.578587

"""

# revision identifiers, used by Alembic.
revision = '2aafb16541a'
down_revision = '379a369c64e'

from alembic import op
import sqlalchemy_utils
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bar_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bar_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('date', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['bar_id'], ['bars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('beer_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('beer_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('date', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['beer_id'], ['beers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('beer_comments')
    op.drop_table('bar_comments')
    ### end Alembic commands ###
