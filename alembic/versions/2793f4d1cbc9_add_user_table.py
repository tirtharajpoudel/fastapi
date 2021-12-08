"""add user table

Revision ID: 2793f4d1cbc9
Revises: 1499dc26b155
Create Date: 2021-12-08 18:48:42.001384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2793f4d1cbc9"
down_revision = "1499dc26b155"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade():
    op.drop_table("users")
