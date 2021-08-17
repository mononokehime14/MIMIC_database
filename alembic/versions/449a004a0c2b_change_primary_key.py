"""change primary key

Revision ID: 449a004a0c2b
Revises: eb202c5f3e26
Create Date: 2021-08-17 11:05:04.878044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '449a004a0c2b'
down_revision = 'eb202c5f3e26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('ALTER TABLE core_transfers ALTER COLUMN subject_id DROP NOT NULL')
    op.alter_column('core_transfers', 'subject_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('core_transfers', 'transfer_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.drop_index('ix_core_transfers_subject_id', table_name='core_transfers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_core_transfers_subject_id', 'core_transfers', ['subject_id'], unique=False)
    op.alter_column('core_transfers', 'transfer_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.alter_column('core_transfers', 'subject_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
