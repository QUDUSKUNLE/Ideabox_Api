"""Create category table

Revision ID: 4ae276d824af
Revises: 12f9869b9c05
Create Date: 2018-03-18 09:00:47.499790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ae276d824af'
down_revision = '12f9869b9c05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('category_type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('idea', sa.Column('category_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'idea', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'idea', type_='foreignkey')
    op.drop_column('idea', 'category_id')
    op.drop_table('category')
    # ### end Alembic commands ###
