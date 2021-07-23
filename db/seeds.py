from api.services import call_log_event_service
from api.models import call_log_event
from api import models, db
from datetime import datetime
from sqlalchemy import text

test_system_phone = {
    "phone": "+918068971703",
}

system_phone_exists = db.session.query(
    db.exists().where(models.SystemPhone.phone == test_system_phone["phone"])
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

test_partner = {"email": "unicef@test.com"}

partner_exist = db.session.query(
    db.exists().where(models.Partner.email == test_partner["email"])
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

test_partner_system_phone = {
    "partner_id": partner.id,
    "system_phone_id": system_phone.id,
}

partner_system_phone_exist = db.session.query(
    db.exists()
    .where(
        models.PartnerSystemPhone.partner_id == test_partner_system_phone["partner_id"]
    )
    .where(
        models.PartnerSystemPhone.system_phone_id
        == test_partner_system_phone["system_phone_id"]
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

test_registration = {"user_phone": "1234567890"}

registration_exist = db.session.query(
    db.exists().where(models.Registration.user_phone == test_registration["user_phone"])
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

test_call_log_event = {"call_sid": "9182161650233761"}
call_log_event_exist = db.session.query(
    db.exists().where(models.CallLogEvent.call_sid == test_call_log_event["call_sid"])
).scalar()

if not call_log_event_exist:
    call_log_event = models.CallLogEvent(
        call_sid="9182161650233761",
        account_sid="123456789123",
        from_number="0970467665087",
        to_number="+918068971703",
        call_status="Missed",
        direction="inbound-api",
        parent_call_sid="9182161650233761",
        telco_code=None,
        telco_status=None,
        dial_time=None,
        pick_time=None,
        end_time=None,
        duration=None,
        created_on=datetime.now(),
        updated_on=datetime.now(),
    )

    db.session.add(call_log_event)
    db.session.commit()
