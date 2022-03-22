"""empty message

Revision ID: 5f2d1e8bf3b7
Revises: 
Create Date: 2022-02-27 08:22:36.063735

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5f2d1e8bf3b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('yt_videos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('yt_videos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('video_id', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('kind', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(precision=0), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(precision=0), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='yt_videos_pkey'),
    sa.UniqueConstraint('video_id', name='yt_videos_video_id_key')
    )
    # ### end Alembic commands ###
