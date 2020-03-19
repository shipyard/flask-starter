from src.models.base import BaseModel, db


class Counter(BaseModel):

    count = db.Column(db.Integer, default=0, nullable=False)
    label = db.Column(db.String(), nullable=False)

    def increment(self, amount=1):
        self.count += amount
        self.save()
