from api.mixins import TimestampMixin
from api import db
import enum


class ParentTypeEnum(enum.Enum):
    FATHER = ("Father",)
    MOTHER = ("Mother",)
    GRANDFATHER = ("Grand Father",)
    GRANDMOTHER = ("Grand Mother",)
    OTHER = ("Other",)


class RegistrationStatusEnum(enum.Enum):
    PENDING = ("Pending",)
    INPROGRESS = ("In-Progress",)
    COMPLETE = ("Complete",)


class Registration(TimestampMixin, db.Model):
    __tablename__ = "registration"
    id = db.Column(db.Integer, primary_key=True)
    user_phone = db.Column(db.String(50))
    system_phone = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    partner_id = db.Column(db.Integer, db.ForeignKey("partner.id"))
    program_id = db.Column(db.Integer, db.ForeignKey("program.id"))
    district = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    parent_type = db.Column(
        db.Enum(ParentTypeEnum),
        # default = ParentTypeEnum.OTHER
    )
    area_type = db.Column(db.String(255), nullable=True)
    is_child_between_0_3 = db.Column(db.Boolean, nullable=True)
    is_child_between_3_6 = db.Column(db.Boolean, nullable=True)
    is_child_between_3_6 = db.Column(db.Boolean, nullable=True)
    is_child_above_6 = db.Column(db.Boolean, nullable=True)
    has_no_child = db.Column(db.Boolean, nullable=True)
    has_smartphone = db.Column(db.Boolean, nullable=True)
    has_dropped_missedcall = db.Column(db.Boolean, nullable=True)
    has_received_callback = db.Column(db.Boolean, nullable=True)
    status = db.Column(
        db.Enum(RegistrationStatusEnum),
        default=RegistrationStatusEnum.PENDING,
    )
    signup_date = db.Column(db.DateTime, nullable=True)
