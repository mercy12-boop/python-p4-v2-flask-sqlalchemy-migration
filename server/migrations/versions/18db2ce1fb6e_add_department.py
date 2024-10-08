"""add Department

Revision ID: 18db2ce1fb6e
Revises: 850a34fa5d71
Create Date: 2024-08-19 17:22:38.302457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18db2ce1fb6e'
down_revision = '850a34fa5d71'
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
