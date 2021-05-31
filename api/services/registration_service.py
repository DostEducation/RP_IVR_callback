# This file is treated as service layer
import requests
from flask import request
from api import models, db


class RegistrationService:
    # Create a registration
    def create_registration(self, data):

        url_decoded_system_phone = requests.utils.unquote(data["to_number"])
        system_phone_exists = db.session.query(
            db.exists().where(models.SystemPhone.phone == url_decoded_system_phone)
        ).scalar()

        if not system_phone_exists:
            return

        system_phone_data = models.SystemPhone.query.filter_by(
            phone=url_decoded_system_phone
        ).first()

        partner = models.PartnerSystemPhone.query.filter_by(
            system_phone_id=system_phone_data.id
        ).first()

        user_exists = db.session.query(
            db.exists().where(models.Registration.user_phone == data["from_number"])
        ).scalar()

        if user_exists:
            return

        registration = models.Registration(
            user_phone=data["from_number"],
            system_phone=url_decoded_system_phone,
            status="pending",
            partner_id=partner.id,
            state=system_phone_data.state,
            has_dropped_missedcall=1,
        )
        db.session.add(registration)
        db.session.commit()
