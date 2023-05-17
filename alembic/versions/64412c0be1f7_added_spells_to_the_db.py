"""Added spells to the db

Revision ID: 64412c0be1f7
Revises: 1c1df7503576
Create Date: 2023-05-08 08:14:29.454467

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "64412c0be1f7"
down_revision = "1c1df7503576"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "spells",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("character_id", sa.Integer(), nullable=True),
        sa.Column("spell_id", sa.String(), nullable=True),
        sa.Column("slot_id", sa.Integer(), nullable=True),
        sa.Column("sequence_id", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("characters", schema=None) as batch_op:
        batch_op.drop_column("spell0")
        batch_op.drop_column("spell9")
        batch_op.drop_column("spell4")
        batch_op.drop_column("spell5")
        batch_op.drop_column("spell7")
        batch_op.drop_column("spell6")
        batch_op.drop_column("spell8")
        batch_op.drop_column("spell3")
        batch_op.drop_column("spell1")
        batch_op.drop_column("spell2")

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("characters", schema=None) as batch_op:
        batch_op.add_column(sa.Column("spell2", sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column("spell1", sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column("spell3", sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column("spell8", sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column("spell6", sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column("spell7", sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column("spell5", sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column("spell4", sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column("spell9", sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column("spell0", sa.VARCHAR(), nullable=True))

    op.drop_table("spells")
    # ### end Alembic commands ###
