"""add content column to posts table

Revision ID: 1499dc26b155
Revises: 0eba4a1c464d
Create Date: 2021-12-08 18:41:46.014271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1499dc26b155"
down_revision = "0eba4a1c464d"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")

