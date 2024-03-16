"""Renaming email column to parents_email

Revision ID: dbb6e77798f6
Revises: 791279dd0760
Create Date: 2024-03-16 07:27:06.050137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbb6e77798f6'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name= 'parents_email' )


def downgrade() -> None:
    op.alter_column('students', 'parents_email', new_column_name='email')

