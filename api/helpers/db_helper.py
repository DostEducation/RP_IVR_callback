from api import db
import traceback
import logging


def save(data):
    try:
        db.session.add(data)
        db.session.commit()
        logging.info("Data saved successfully")
    except Exception as e:
        logging.error("Error: " + str(e))
        print(traceback.format_exc())
        db.session.rollback()
    finally:
        db.session.close()
