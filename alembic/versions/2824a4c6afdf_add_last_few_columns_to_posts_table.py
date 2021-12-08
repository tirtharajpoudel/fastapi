"""add last few columns to posts table

Revision ID: 2824a4c6afdf
Revises: abc4ccb1db3c
Create Date: 2021-12-08 19:08:52.075349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2824a4c6afdf"
down_revision = "abc4ccb1db3c"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
