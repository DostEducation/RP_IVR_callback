from api import models, db
from datetime import datetime
from sqlalchemy import text

initial_system_phone = {
    "phone": "+918068971703",
}

system_phone_exists = db.session.query(
    db.exists().where(models.SystemPhone.phone == initial_system_phone["phone"])
).scalar()

if not system_phone_exists:
    system_phone = models.SystemPhone(
        phone="+918068971703",
        district="",
        state="UP",
        status="active",
        created_on=datetime.now(),
        updated_on=datetime.now(),
    )
    db.session.add(system_phone)
    db.session.commit()

initial_partner = {"email": "unicef@test.com"}

partner_exist = db.session.query(
    db.exists().where(models.Partner.email == initial_partner["email"])
).scalar()

if not partner_exist:
    partner = models.Partner(
        name="UNICEF",
        email="unicef@test.com",
        created_on=datetime.now(),
        updated_on=datetime.now(),
    )
    db.session.add(partner)
    db.session.commit()

partner = models.Partner.query.filter_by(name="UNICEF").first()

system_phone = models.SystemPhone.query.filter_by(
    phone="+918068971703",
).first()

initial_partner_system_phone = {
    "partner_id": partner.id,
    "system_phone_id": system_phone.id,
}

partner_system_phone_exist = db.session.query(
    db.exists()
    .where(
        models.PartnerSystemPhone.partner_id
        == initial_partner_system_phone["partner_id"]
    )
    .where(
        models.PartnerSystemPhone.system_phone_id
        == initial_partner_system_phone["system_phone_id"]
    )
).scalar()

if not partner_system_phone_exist:
    partner_system_phone = models.PartnerSystemPhone(
        status="active",
        created_on=datetime.now(),
        updated_on=datetime.now(),
        partner_id=partner.id,
        system_phone_id=system_phone.id,
    )
    db.session.add(partner_system_phone)
    db.session.commit()

initial_registration = {"user_phone": "1234567890"}

registration_exist = db.session.query(
    db.exists().where(
        models.Registration.user_phone == initial_registration["user_phone"]
    )
).scalar()

if not registration_exist:
    registration = models.Registration(
        user_phone="1234567890",
        system_phone="+918068971703",
        status="active",
        created_on=datetime.now(),
        updated_on=datetime.now(),
    )

    db.session.add(registration)
    db.session.commit()
