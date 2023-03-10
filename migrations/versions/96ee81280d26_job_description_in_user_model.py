"""job description in user model

Revision ID: 96ee81280d26
Revises: 530ca4c3c5d0
Create Date: 2023-03-13 10:44:54.769564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96ee81280d26'
down_revision = '530ca4c3c5d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('job_description', sa.String(length=100), nullable=True))
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.drop_column('job_description')

    # ### end Alembic commands ###
