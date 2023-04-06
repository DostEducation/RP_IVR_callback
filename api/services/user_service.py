# This file is treated as service layer
from api import helpers, models, db


class UserService:
    def handle_user_creation(self, data):
        system_phone_data = models.SystemPhone.query.filter_by(
            phone=data["to_number"]
        ).first()

        if not system_phone_data:
            return

        partner = models.PartnerSystemPhone.query.filter_by(
            system_phone_id=system_phone_data.id
        ).first()

        if not partner:
            return

        user = models.User(
            state=system_phone_data.state,
            phone=data["from_number"],
            partner_id=partner.id,
        )
        helpers.save(user)
