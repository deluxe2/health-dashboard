from datetime import datetime
from beanie import Document, Link

from health_dashboard.models.user import User


class Weight(Document):
    date: datetime
    weight: float
    user: Link[User]
