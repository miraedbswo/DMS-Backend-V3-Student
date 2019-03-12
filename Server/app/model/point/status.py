import random

from app.extension import db
from app.model.mixin import BaseMixin


message_dict = {
    0: [
        "이 또한 지나가리 -손승용",
        "아니ㅜㅜ 라면 좀 먹고 살아라ㅠ",
        "라면을 5번 먹을 수 있겠네요!",
        "배는 산으로."
    ],
    1: [
        "티끌 모아 1차 봉사",
        "기리보이 앨범을 듣자.",
        "김준우가 비웃고 있습니다.",
    ],
    2: [
        "2주동안 집 못가겠네요!",
        "벌점은 높게 상점은 낮게!",
        "소 잃고 외양간 고친다.",
        "긴장타세요. 퇴사가 코앞입니다."
    ],
    3: [
        "2주동안 집 못가겠네요!",
        "벌점은 높게 상점은 낮게!",
        "소 잃고 외양간 고친다.",
        "긴장타세요. 퇴사가 코앞입니다."
    ],
    4: [
        "2주동안 집 못가겠네요!",
        "벌점은 높게 상점은 낮게!",
        "소 잃고 외양간 고친다.",
        "긴장타세요. 퇴사가 코앞입니다."
    ],
    5: [
        "퇴사가 오늘 내일한다.",
        "치킨 먹으러 갈래요?",
        "집이 더 좋죠?",
        "다음에 또 만나요!",
        "너 자신을 알라!"
    ]
}


def get_advice(bad_point: int):
    if bad_point <= 0:
        advice_num = 0

    elif bad_point < 10:
        advice_num = 1

    elif bad_point < 20:
        advice_num = 2

    elif bad_point < 25:
        advice_num = 3

    elif bad_point < 30:
        advice_num = 4

    else:
        advice_num = 5

    advice = random.choice(message_dict[advice_num])
    return advice


class PointStatusModel(db.Model, BaseMixin):
    __tablename__ = 'point_status'

    student_id: str = db.Column(db.String, db.ForeignKey('student.id', ondelete='CASCADE'), primary_key=True)
    good_point: int = db.Column(db.Integer, default=0)
    bad_point: int = db.Column(db.Integer, default=0)
    penalty_level: int = db.Column(db.Integer, default=0)
    penalty_status: bool = db.Column(db.Boolean, default=False)

    def __init__(self, student_id: str):
        self.student_id = student_id

    @staticmethod
    def get_point_status(student_id: str):
        point_status: PointStatusModel = PointStatusModel.query.filter_by(student_id=student_id).first()
        if point_status is None:
            point_status = PointStatusModel(student_id).save()

        return {
            'badPoint': point_status.bad_point,
            'goodPoint': point_status.good_point,
            'penaltyLevel': point_status.penalty_level,
            'penaltyStatus': point_status.penalty_status,
            'advice': get_advice(point_status.bad_point)
        }
