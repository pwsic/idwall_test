"""database_structure

Revision ID: 5f84e81951a1
Revises: 
Create Date: 2022-04-26 22:46:26.409542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f84e81951a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Text(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer',
    sa.Column('id', sa.Text(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase_history',
    sa.Column('id', sa.Text(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('category_id', sa.String(length=36), nullable=False),
    sa.Column('purchase_id', sa.String(), nullable=False),
    sa.Column('money_spent', sa.Float(), nullable=False),
    sa.Column('purchase_date', sa.DateTime(), nullable=False),
    sa.Column('customer_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('request_history',
    sa.Column('id', sa.Text(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('customer_id', sa.String(length=36), nullable=False),
    sa.Column('initial_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request_history')
    op.drop_table('purchase_history')
    op.drop_table('customer')
    op.drop_table('category')
    # ### end Alembic commands ###
