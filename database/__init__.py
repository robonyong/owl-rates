from datetime import datetime
import logging

from sqlalchemy import event

from database.schemas import *

def receive_before_update(mapper, connection, target):
	target.updated = datetime.now()

event.listen(Owl, 'before_update', receive_before_update)
event.listen(Reviewer, 'before_update', receive_before_update)
event.listen(Rating, 'before_update', receive_before_update)

__all__ = ['Owl', 'OwlDescription', 'Rating', 'Reviewer']