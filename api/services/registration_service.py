# This file is treated as service layer
from api import models, db
from datetime import datetime


class RegistrationService:
    # Create a registartion
    def create_registration(self, data):
        system_phone_data = models.SystemPhone.query.filter_by(
            phone=data["to_number"]
        ).first()

        partner = models.PartnerSystemPhone.query.filter_by(
            system_phone_id=system_phone_data.id
        ).first()

        registration_exists = db.session.query(
            db.exists().where(
                models.Registration.user_phone.endswith(data["from_number"][-10:])
            )
        ).scalar()

        if registration_exists:
            return

        registration = models.Registration(
            user_phone=data["from_number"],
            system_phone=data["to_number"],
            status="pending",
            partner_id=partner.partner_id,
            state=system_phone_data.state,
            has_dropped_missedcall=True,
            created_on=data["log_created_on"]
            if data.get("log_created_on", None)
            else datetime.now(),
        )
        db.session.add(registration)
        db.session.commit()
