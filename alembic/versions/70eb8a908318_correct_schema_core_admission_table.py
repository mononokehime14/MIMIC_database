"""correct schema core_admission table

Revision ID: 70eb8a908318
Revises: d0a502a9d0fc
Create Date: 2021-08-17 09:23:52.988980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70eb8a908318'
down_revision = 'd0a502a9d0fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('core_admission', sa.Column('subject_id', sa.Integer(), nullable=True))
    op.add_column('core_admission', sa.Column('hadm_id', sa.Integer(), nullable=False))
    op.add_column('core_admission', sa.Column('admittime', sa.DateTime(), nullable=False))
    op.add_column('core_admission', sa.Column('dischtime', sa.String(), nullable=True))
    op.add_column('core_admission', sa.Column('deathtime', sa.String(), nullable=True))
    op.add_column('core_admission', sa.Column('admission_type', sa.String(), nullable=True))
    op.add_column('core_admission', sa.Column('admission_location', sa.String(), nullable=True))
    op.add_column('core_admission', sa.Column('discharge_location', sa.String(), nullable=True))
    op.add_column('core_admission', sa.Column('insurance', sa.String(), nullable=True))
    op.add_column('core_admission', sa.Column('language', sa.String(), nullable=True))
    op.add_column('core_admission', sa.Column('marital_status', sa.String(), nullable=True))
    op.add_column('core_admission', sa.Column('ethnicity', sa.String(), nullable=True))
    op.add_column('core_admission', sa.Column('edregtime', sa.String(), nullable=True))
    op.add_column('core_admission', sa.Column('edouttime', sa.String(), nullable=True))
    op.add_column('core_admission', sa.Column('hospital_expire_flag', sa.Integer(), nullable=True))
    op.drop_index('ix_core_admission_HADM_ID', table_name='core_admission')
    op.create_index(op.f('ix_core_admission_hadm_id'), 'core_admission', ['hadm_id'], unique=False)
    op.drop_column('core_admission', 'EDOUTTIME')
    op.drop_column('core_admission', 'DISCHTIME')
    op.drop_column('core_admission', 'ADMISSION_LOCATION')
    op.drop_column('core_admission', 'EDREGTIME')
    op.drop_column('core_admission', 'HOSPITAL_EXPIRE_FLAG')
    op.drop_column('core_admission', 'LANGUAGE')
    op.drop_column('core_admission', 'RELIGION')
    op.drop_column('core_admission', 'DEATHTIME')
    op.drop_column('core_admission', 'DISCHARGE_LOCATION')
    op.drop_column('core_admission', 'MARITAL_STATUS')
    op.drop_column('core_admission', 'SUBJECT_ID')
    op.drop_column('core_admission', 'ETHNICITY')
    op.drop_column('core_admission', 'ADMISSION_TYPE')
    op.drop_column('core_admission', 'HAS_CHARTEVENTS_DATA')
    op.drop_column('core_admission', 'ROW_ID')
    op.drop_column('core_admission', 'ADMITTIME')
    op.drop_column('core_admission', 'HADM_ID')
    op.drop_column('core_admission', 'INSURANCE')
    op.drop_column('core_admission', 'DIAGNOSIS')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('core_admission', sa.Column('DIAGNOSIS', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('INSURANCE', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('HADM_ID', sa.INTEGER(), server_default=sa.text('nextval(\'"core_admission_HADM_ID_seq"\'::regclass)'), autoincrement=True, nullable=False))
    op.add_column('core_admission', sa.Column('ADMITTIME', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('ROW_ID', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('HAS_CHARTEVENTS_DATA', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('ADMISSION_TYPE', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('ETHNICITY', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('SUBJECT_ID', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('MARITAL_STATUS', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('DISCHARGE_LOCATION', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('DEATHTIME', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('RELIGION', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('LANGUAGE', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('HOSPITAL_EXPIRE_FLAG', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('EDREGTIME', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('ADMISSION_LOCATION', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('DISCHTIME', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('core_admission', sa.Column('EDOUTTIME', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_core_admission_hadm_id'), table_name='core_admission')
    op.create_index('ix_core_admission_HADM_ID', 'core_admission', ['HADM_ID'], unique=False)
    op.drop_column('core_admission', 'hospital_expire_flag')
    op.drop_column('core_admission', 'edouttime')
    op.drop_column('core_admission', 'edregtime')
    op.drop_column('core_admission', 'ethnicity')
    op.drop_column('core_admission', 'marital_status')
    op.drop_column('core_admission', 'language')
    op.drop_column('core_admission', 'insurance')
    op.drop_column('core_admission', 'discharge_location')
    op.drop_column('core_admission', 'admission_location')
    op.drop_column('core_admission', 'admission_type')
    op.drop_column('core_admission', 'deathtime')
    op.drop_column('core_admission', 'dischtime')
    op.drop_column('core_admission', 'admittime')
    op.drop_column('core_admission', 'hadm_id')
    op.drop_column('core_admission', 'subject_id')
    # ### end Alembic commands ###