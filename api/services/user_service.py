# This file is treated as service layer
from api import helpers, models, db
from utils.loggingutils import logger


class UserService:
    def handle_user_creation(self, data):
        system_phone_data = models.SystemPhone.query.filter_by(
            phone=data["to_number"]
        ).first()

        if not system_phone_data:
            return

        partner_system_phone_data = models.PartnerSystemPhone.query.filter_by(
            system_phone_id=system_phone_data.id
        ).first()

        if not partner_system_phone_data:
            logger.error(
                f"Failed to get partner system phone details for system phone {data['to_number']}."
            )
            return

        user_exists = db.session.query(
            db.exists().where(models.User.phone.endswith(data["from_number"][-10:]))
        ).scalar()

        if user_exists:
            return

        user = models.User(
            state=system_phone_data.state,
            phone=data["from_number"],
            partner_id=partner_system_phone_data.partner_id,
        )
        helpers.save(user)
