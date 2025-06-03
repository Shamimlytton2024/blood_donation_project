"""Initial migration

Revision ID: 0001
Revises: 
Create Date: 2024-06-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'donors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False)
    )
    op.create_table(
        'staff',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False)
    )
    op.create_table(
        'donations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('donor_id', sa.Integer, sa.ForeignKey('donors.id'), nullable=False),
        sa.Column('staff_id', sa.Integer, sa.ForeignKey('staff.id'), nullable=False)
    )
    op.create_table(
        'tests',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('donation_id', sa.Integer, sa.ForeignKey('donations.id'), nullable=False)
    )

def downgrade():
    op.drop_table('tests')
    op.drop_table('donations')
    op.drop_table('staff')
    op.drop_table('donors')
