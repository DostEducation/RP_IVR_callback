from api import db
import traceback
from utils.loggingutils import logger


def save(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        logger.error(
            f"Error occurred while commiting data into database. Error Message:  {e}"
        )
        logger.debug(traceback.format_exc())
        db.session.rollback()
    finally:
        db.session.close()
