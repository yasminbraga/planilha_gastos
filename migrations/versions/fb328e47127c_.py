"""empty message

Revision ID: fb328e47127c
Revises: 011bd7bedbe2
Create Date: 2019-07-19 17:58:01.639652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb328e47127c'
down_revision = '011bd7bedbe2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categoria', sa.Column('titulo', sa.String(length=20), nullable=False))
    op.drop_column('categoria', 'tittle')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categoria', sa.Column('tittle', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
    op.drop_column('categoria', 'titulo')
    # ### end Alembic commands ###
