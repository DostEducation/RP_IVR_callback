from api import db
import traceback


def save(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print("Error: " + str(e))
        print(traceback.format_exc())
        db.session.rollback()
