# This file is treated as service layer
from api import helpers, models, db
from datetime import datetime
from utils.loggingutils import logger


class RegistrationService:
    # Create a registartion
    def create_registration(self, data):
        system_phone_data = models.SystemPhone.query.filter_by(
            phone=data["to_number"]
        ).first()

        if not system_phone_data:
            logger.error(
                "No system phone data found for phone number {}".format(
                    data["to_number"]
                )
            )
            return

        partner = models.PartnerSystemPhone.query.filter_by(
            system_phone_id=system_phone_data.id
        ).first()

        if not partner:
            logger.error(
                "No partner found for system phone with id {}".format(
                    system_phone_data.id
                )
            )
            return

        registration_exists = db.session.query(
            db.exists().where(
                models.Registration.user_phone.endswith(data["from_number"][-10:])
            )
        ).scalar()

        if registration_exists:
            logger.warning(
                "Registration already exists for user phone {}".format(
                    data["from_number"]
                )
            )
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
        helpers.save(registration)
        logger.info(
            "New registration created for user phone {}".format(data["from_number"])
        )
