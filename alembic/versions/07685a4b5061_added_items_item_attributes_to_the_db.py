"""Added items/item attributes to the db

Revision ID: 07685a4b5061
Revises: 3316d022ea2c
Create Date: 2023-04-28 21:16:09.949483

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "07685a4b5061"
down_revision = "3316d022ea2c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "item_attribute",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("item_id", sa.Integer(), nullable=True),
        sa.Column("primary", sa.Boolean(), nullable=True),
        sa.Column("property", sa.String(), nullable=True),
        sa.Column("value", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("character_id", sa.Integer(), nullable=True),
        sa.Column("item_id", sa.String(), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=True),
        sa.Column("inventory_id", sa.Integer(), nullable=True),
        sa.Column("slot_id", sa.Integer(), nullable=True),
        sa.Column("ammo_count", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("items")
    op.drop_table("item_attribute")
    # ### end Alembic commands ###
