"""empty message

Revision ID: c400ed1a1f7f
Revises: 8d4b5676b361
Create Date: 2023-10-24 20:34:51.525333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c400ed1a1f7f'
down_revision = '8d4b5676b361'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=25), nullable=False),
    sa.Column('Password', sa.String(length=20), nullable=False),
    sa.Column('Email', sa.String(length=30), nullable=False),
    sa.Column('PhoneNumber', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('upload',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=20), nullable=False),
    sa.Column('Date', sa.DateTime(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user1.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('Mark', sa.VARCHAR(length=25), nullable=False),
    sa.Column('Model', sa.VARCHAR(length=10), nullable=False),
    sa.Column('Year', sa.INTEGER(), nullable=False),
    sa.Column('Description', sa.VARCHAR(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('upload')
    op.drop_table('user1')
    # ### end Alembic commands ###
