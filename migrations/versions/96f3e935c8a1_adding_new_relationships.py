"""Adding new relationships

Revision ID: 96f3e935c8a1
Revises: 44fc18b3d8cf
Create Date: 2022-04-09 14:29:36.957565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96f3e935c8a1'
down_revision = '44fc18b3d8cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('merchant_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'categories', 'merchants', ['merchant_id'], ['id'])
    op.alter_column('merchants', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('merchants', 'password',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.create_unique_constraint(None, 'merchants', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'merchants', type_='unique')
    op.alter_column('merchants', 'password',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('merchants', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_constraint(None, 'categories', type_='foreignkey')
    op.drop_column('categories', 'merchant_id')
    # ### end Alembic commands ###
