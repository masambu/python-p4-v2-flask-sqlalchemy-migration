"""Add Department table

Revision ID: 2372e52f067b
Revises: 02d2691a95f2
Create Date: 2024-04-03 16:27:48.053787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2372e52f067b'
down_revision = '02d2691a95f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
