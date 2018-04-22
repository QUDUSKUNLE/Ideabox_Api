"""empty message

Revision ID: 5166d10ede44
Revises: 0b4935392f84
Create Date: 2018-03-16 11:29:56.435934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5166d10ede44'
down_revision = '0b4935392f84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('reset_password_link', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'reset_password_link')
    # ### end Alembic commands ###