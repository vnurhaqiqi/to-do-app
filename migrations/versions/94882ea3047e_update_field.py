"""update field

Revision ID: 94882ea3047e
Revises: 3619f448530a
Create Date: 2021-02-14 20:29:11.477102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94882ea3047e'
down_revision = '3619f448530a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_logged_in', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_logged_in')
    # ### end Alembic commands ###