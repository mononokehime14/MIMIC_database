"""create core_admission

Revision ID: d0a502a9d0fc
Revises: 
Create Date: 2021-08-14 22:29:08.408036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0a502a9d0fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('core_admission',
    sa.Column('ROW_ID', sa.Integer(), nullable=True),
    sa.Column('SUBJECT_ID', sa.Integer(), nullable=True),
    sa.Column('HADM_ID', sa.Integer(), nullable=False),
    sa.Column('ADMITTIME', sa.String(), nullable=True),
    sa.Column('DISCHTIME', sa.String(), nullable=True),
    sa.Column('DEATHTIME', sa.String(), nullable=True),
    sa.Column('ADMISSION_TYPE', sa.String(), nullable=True),
    sa.Column('ADMISSION_LOCATION', sa.String(), nullable=True),
    sa.Column('DISCHARGE_LOCATION', sa.String(), nullable=True),
    sa.Column('INSURANCE', sa.String(), nullable=True),
    sa.Column('LANGUAGE', sa.String(), nullable=True),
    sa.Column('RELIGION', sa.String(), nullable=True),
    sa.Column('MARITAL_STATUS', sa.String(), nullable=True),
    sa.Column('ETHNICITY', sa.String(), nullable=True),
    sa.Column('EDREGTIME', sa.String(), nullable=True),
    sa.Column('EDOUTTIME', sa.String(), nullable=True),
    sa.Column('DIAGNOSIS', sa.String(), nullable=True),
    sa.Column('HOSPITAL_EXPIRE_FLAG', sa.Integer(), nullable=True),
    sa.Column('HAS_CHARTEVENTS_DATA', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('HADM_ID')
    )
    op.create_index(op.f('ix_core_admission_HADM_ID'), 'core_admission', ['HADM_ID'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_core_admission_HADM_ID'), table_name='core_admission')
    op.drop_table('core_admission')
    # ### end Alembic commands ###