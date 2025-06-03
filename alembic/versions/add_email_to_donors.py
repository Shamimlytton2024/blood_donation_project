"""Add email column to donors table

Revision ID: add_email_to_donors
Revises: 
Create Date: 2024-06-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_email_to_donors'
down_revision = '0001'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('donors', sa.Column('email', sa.String(), nullable=True))

def downgrade():
    op.drop_column('donors', 'email')
