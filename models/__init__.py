from mongoengine import CASCADE, PULL, signals
from .owl import Owl
from .rating import Rating
from .user import User
import datetime
import logging

#add in all the delete rules now to avoid circular dependency
Owl.register_delete_rule(Rating, 'owl', CASCADE)
Owl.register_delete_rule(User, 'review_owls', PULL)
User.register_delete_rule(Rating, 'user', CASCADE)
Rating.register_delete_rule(Owl, 'ratings', PULL)
Rating.register_delete_rule(User, 'ratings', PULL)

#add in all the post/pre save hooks
def update_modified(sender, document):
	logging.debug("updating update date")
	document.modified = datetime.datetime.now

def update_owl_and_user_from_new_rating(sender, document, **kwargs):
	created = kwargs.get('created', None)
	if created:
		logging.debug("New rating being added...")
		document.owl.ratings.append(document)
		document.owl.save()
		if(document.user):
			document.user.ratings.append(document)
			document.user.save()

signals.pre_save.connect(update_modified, sender=User)
signals.pre_save.connect(update_modified, sender=Owl)
signals.pre_save.connect(update_modified, sender=Rating)
signals.post_save.connect(update_owl_and_user_from_new_rating, sender=Rating)

__all__ = ['Owl', 'Rating', 'User']