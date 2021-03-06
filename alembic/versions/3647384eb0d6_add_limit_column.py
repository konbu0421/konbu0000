"""Add limit column

Revision ID: 3647384eb0d6
Revises: 08c928325482
Create Date: 2021-04-16 12:44:18.420693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3647384eb0d6'
down_revision = '08c928325482'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guild_voice_preference', sa.Column('limit', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('guild_voice_preference', 'limit')
    # ### end Alembic commands ###
