"""empty message

Revision ID: 56d63842dbba
Revises: ff4af17def81
Create Date: 2020-02-11 14:02:04.733527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56d63842dbba'
down_revision = 'ff4af17def81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'seeking_venue')
    op.drop_column('artist', 'seeking_description')
    # ### end Alembic commands ###