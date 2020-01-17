"""empty message

Revision ID: 9735c99ea5d9
Revises: 1cde74fcc1a7
Create Date: 2020-01-14 15:12:01.582140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9735c99ea5d9'
down_revision = '1cde74fcc1a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###