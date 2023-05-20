"""Added Login Table

Revision ID: 489dbe73a913
Revises: b53c793562c7
Create Date: 2023-05-16 19:03:34.855509

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "489dbe73a913"
down_revision = "b53c793562c7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "logins",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("account_id", sa.Integer(), nullable=False),
        sa.Column("character_id", sa.Integer(), nullable=True),
        sa.Column("login_time", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("characters", schema=None) as batch_op:
        batch_op.add_column(sa.Column("last_login", sqlalchemy_utils.types.arrow.ArrowType(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("characters", schema=None) as batch_op:
        batch_op.drop_column("last_login")

    op.drop_table("logins")
    # ### end Alembic commands ###
