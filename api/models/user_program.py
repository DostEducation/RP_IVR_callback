from api.mixins import TimestampMixin
from api import db
from api import app, models, helpers
from flask_sqlalchemy import BaseQuery
from api.helpers.common_helper import current_ist_time


class UserProgramQuery(BaseQuery):
    def create_user_program(self, data):
        program_id = app.config["DEFAULT_PROGRAM_ID"]
        preferred_time_slot = app.config["DEFAULT_PROGRAM_TIME_CATEGORY"]

        user = models.User.query.filter_by(phone=data["from_number"]).first()

        user_program = models.UserProgram(
            user_id=user.id,
            program_id=program_id,
            status=models.UserProgram.UserProgramStatus.IN_PROGRESS,
            start_date=current_ist_time().date(),
            preferred_time_slot=preferred_time_slot,
        )
        helpers.save(user_program)


class UserProgram(TimestampMixin, db.Model):
    query_class = UserProgramQuery
    __tablename__ = "user_program"

    class UserProgramStatus(object):
        IN_PROGRESS = "in-progress"
        COMPLETE = "complete"
        TERMINATED = "terminated"
        UNSUB = "unsub"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    program_id = db.Column(db.Integer, db.ForeignKey("program.id"))
    preferred_time_slot = db.Column(db.String(50))
    status = db.Column(db.String(50))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
