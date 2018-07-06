"""empty message

Revision ID: 4c7f86bbed3d
Revises: 4cce4fe9ede5
Create Date: 2017-08-18 00:23:48.372798

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '4c7f86bbed3d'
down_revision = '4cce4fe9ede5'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('versions')
    op.add_column('orders', sa.Column('cancel_note', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'cancel_note')
    op.create_table('versions',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('event_ver', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('sessions_ver', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('speakers_ver', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tracks_ver', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('sponsors_ver', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('microlocations_ver', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['event_id'], [u'events.id'], name=u'versions_event_id_fkey', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id', name=u'versions_pkey')
    )
    # ### end Alembic commands ###