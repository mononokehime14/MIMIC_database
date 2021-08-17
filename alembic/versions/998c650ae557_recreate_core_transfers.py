"""recreate core_transfers

Revision ID: 998c650ae557
Revises: eb202c5f3e26
Create Date: 2021-08-17 14:58:34.152874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '998c650ae557'
down_revision = 'eb202c5f3e26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('core_transfers',
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('hadm_id', sa.String(), nullable=True),
    sa.Column('transfer_id', sa.Integer(), nullable=False),
    sa.Column('eventtype', sa.String(), nullable=True),
    sa.Column('careunit', sa.String(), nullable=True),
    sa.Column('intime', sa.DateTime(), nullable=False),
    sa.Column('outtime', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('transfer_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('core_transfers')
    # ### end Alembic commands ###