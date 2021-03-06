"""empty message

Revision ID: 18d6095002ef
Revises: None
Create Date: 2015-05-02 01:24:24.419718

"""

# revision identifiers, used by Alembic.
revision = '18d6095002ef'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kaharesource',
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=True),
    sa.Column('resource_for', sa.String(length=10), nullable=True),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('district', sa.String(length=150), nullable=True),
    sa.Column('tole', sa.String(length=150), nullable=True),
    sa.Column('contactname', sa.String(length=200), nullable=True),
    sa.Column('contactnumber', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('is_active', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('resource_id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index('created_kr_idx', 'kaharesource', ['created'], unique=False)
    op.create_index('updated_kr_idx', 'kaharesource', ['updated'], unique=False)
    op.create_table('kaharesource_stat',
    sa.Column('key', sa.String(length=20), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['resource_id'], ['kaharesource.resource_id'], ),
    sa.PrimaryKeyConstraint('key', 'resource_id')
    )
    op.create_index('created_ks_idx', 'kaharesource_stat', ['created'], unique=False)
    op.create_index('updated_ks_idx', 'kaharesource_stat', ['updated'], unique=False)
    op.create_table('kaharesource_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_type', sa.String(length=100), nullable=True),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resource_id'], ['kaharesource.resource_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kaharesource_type')
    op.drop_index('updated_ks_idx', table_name='kaharesource_stat')
    op.drop_index('created_ks_idx', table_name='kaharesource_stat')
    op.drop_table('kaharesource_stat')
    op.drop_index('updated_kr_idx', table_name='kaharesource')
    op.drop_index('created_kr_idx', table_name='kaharesource')
    op.drop_table('kaharesource')
    ### end Alembic commands ###
