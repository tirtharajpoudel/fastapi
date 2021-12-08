"""add foreign-key to posts table

Revision ID: abc4ccb1db3c
Revises: 2793f4d1cbc9
Create Date: 2021-12-08 19:01:33.006660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "abc4ccb1db3c"
down_revision = "2793f4d1cbc9"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
