"""changed item_attribute to item_attributes for consistency

Revision ID: e8da5956d6a3
Revises: 07685a4b5061
Create Date: 2023-04-29 04:13:53.683998

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "e8da5956d6a3"
down_revision = "07685a4b5061"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "item_attributes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("item_id", sa.Integer(), nullable=True),
        sa.Column("primary", sa.Boolean(), nullable=True),
        sa.Column("property", sa.String(), nullable=True),
        sa.Column("value", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("item_attribute")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "item_attribute",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("item_id", sa.INTEGER(), nullable=True),
        sa.Column("primary", sa.BOOLEAN(), nullable=True),
        sa.Column("property", sa.VARCHAR(), nullable=True),
        sa.Column("value", sa.INTEGER(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("item_attributes")
    # ### end Alembic commands ###
