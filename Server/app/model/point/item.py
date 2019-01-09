from app.extension import db
from app.model.mixin import BaseMixin


class PointItemModel(db.Model, BaseMixin):
    __tablename__ = 'point_item_model'

    id = db.Column(db.Integer, primary_key=True)
    reason: str = db.Column(db.String)
    point: int = db.Column(db.Integer)
    type: bool = db.Column(db.Boolean)

    def __init__(self, reason: str, point: int, type: bool):
        self.reason: str = reason
        self.point: int = point
        self.type: bool = type

    @staticmethod
    def get_point_item(id: int):
        point_item: PointItemModel = PointItemModel.query.filter_by(id=id).first()

        return {
            'point': point_item.point,
            'pointType': point_item.type,
            'reason': point_item.reason
        }
