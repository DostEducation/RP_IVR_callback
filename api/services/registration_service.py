# This file is treated as service layer
import requests
from flask import request
from api import models, db


class RegistrationService:
    # Create a registartion
    def create_registration(self, data):

        url_decoded_system_phone = requests.utils.unquote(data["to_number"])

        system_phone = models.SystemPhone.query.filter_by(
            phone=url_decoded_system_phone
        ).first()

        if system_phone is None:
            return

        partner = models.PartnerSystemPhone.query.filter_by(
            system_phone_id=system_phone.id
        ).first()

        registration_exists = db.session.query(
            db.exists().where(models.Registration.user_phone == data["from_number"])
        ).scalar()

        if registration_exists:
            return

        registration = models.Registration(
            user_phone=data["from_number"],
            system_phone=url_decoded_system_phone,
            status="pending",
            partner_id=partner.id,
            state=system_phone.state,
            has_dropped_missedcall=1,
        )
        db.session.add(registration)
        db.session.commit()
