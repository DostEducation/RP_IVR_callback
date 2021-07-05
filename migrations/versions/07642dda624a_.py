"""empty message

Revision ID: 07642dda624a
Revises:
Create Date: 2021-07-02 18:18:37.987671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "07642dda624a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "call_log_event",
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "updated_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("call_sid", sa.String(length=255), nullable=True),
        sa.Column("account_sid", sa.String(length=255), nullable=True),
        sa.Column("from_number", sa.String(length=255), nullable=True),
        sa.Column("to_number", sa.String(length=255), nullable=True),
        sa.Column("call_status", sa.String(length=255), nullable=True),
        sa.Column("direction", sa.String(length=255), nullable=True),
        sa.Column("parent_call_sid", sa.String(length=255), nullable=True),
        sa.Column("telco_code", sa.String(length=255), nullable=True),
        sa.Column("telco_status", sa.String(length=255), nullable=True),
        sa.Column("dial_time", sa.DateTime(), nullable=True),
        sa.Column("pick_time", sa.DateTime(), nullable=True),
        sa.Column("end_time", sa.DateTime(), nullable=True),
        sa.Column("duration", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "partner",
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "updated_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "program",
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "updated_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "system_phone",
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "updated_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("phone", sa.String(length=50), nullable=True),
        sa.Column("district", sa.String(length=100), nullable=True),
        sa.Column("state", sa.String(length=100), nullable=True),
        sa.Column("status", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "partner_system_phone",
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "updated_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=True),
        sa.Column("partner_id", sa.Integer(), nullable=True),
        sa.Column("system_phone_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["partner_id"],
            ["partner.id"],
        ),
        sa.ForeignKeyConstraint(
            ["system_phone_id"],
            ["system_phone.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "updated_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("phone", sa.String(length=255), nullable=True),
        sa.Column("address_line_1", sa.Text(), nullable=True),
        sa.Column("address_line_2", sa.Text(), nullable=True),
        sa.Column("postal_code", sa.String(length=50), nullable=True),
        sa.Column("partner_id", sa.Integer(), nullable=True),
        sa.Column("city", sa.String(length=100), nullable=True),
        sa.Column("district", sa.String(length=100), nullable=True),
        sa.Column("state", sa.String(length=100), nullable=True),
        sa.Column("country", sa.String(length=50), nullable=True),
        sa.Column("partner", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["partner"],
            ["partner.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "registration",
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "updated_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_phone", sa.String(length=50), nullable=True),
        sa.Column("system_phone", sa.String(length=50), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("partner_id", sa.Integer(), nullable=True),
        sa.Column("program_id", sa.Integer(), nullable=True),
        sa.Column("district", sa.String(length=100), nullable=True),
        sa.Column("state", sa.String(length=100), nullable=True),
        sa.Column("parent_type", sa.String(length=100), nullable=True),
        sa.Column("area_type", sa.String(length=255), nullable=True),
        sa.Column("is_child_between_0_3", sa.Boolean(), nullable=True),
        sa.Column("is_child_between_3_6", sa.Boolean(), nullable=True),
        sa.Column("is_child_above_6", sa.Boolean(), nullable=True),
        sa.Column("has_no_child", sa.Boolean(), nullable=True),
        sa.Column("has_smartphone", sa.Boolean(), nullable=True),
        sa.Column("has_dropped_missedcall", sa.Boolean(), nullable=True),
        sa.Column("has_received_callback", sa.Boolean(), nullable=True),
        sa.Column("status", sa.String(length=100), nullable=True),
        sa.Column("signup_date", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["partner_id"],
            ["partner.id"],
        ),
        sa.ForeignKeyConstraint(
            ["program_id"],
            ["program.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("registration")
    op.drop_table("user")
    op.drop_table("partner_system_phone")
    op.drop_table("system_phone")
    op.drop_table("program")
    op.drop_table("partner")
    op.drop_table("call_log_event")
    # ### end Alembic commands ###
