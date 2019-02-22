from flask import Response

from app.exception import NoContentException
from app.model.account import StudentModel, UnsignedStudentModel
from test import TCBase, check_status_code
from test.request import AccountRequest


class TestSignup(TCBase, AccountRequest):
    def setUp(self):
        super(TestSignup, self).setUp()

        """
        TCBase setUp 안에서 test 계정을 만들어 주는데, 
        Signup TC에서는 test 계정이 존재하면 안됨
        """

        StudentModel.get_student_by_id('test').delete()

        _unsigned_account_data = {
            'uuid': 'test',
            'name': 'test',
            'number': 1101,
            'email': 'test@dsm.hs.kr'
        }

        self.unsigned_account = UnsignedStudentModel(
            uuid=_unsigned_account_data['uuid'],
            name=_unsigned_account_data['name'],
            number=_unsigned_account_data['number'],
            email=_unsigned_account_data['email']
        ).save()

    @check_status_code(201)
    def test_signup_successful(self) -> Response:
        """
        성공적으로 가입 했다면 UnsignedStudentModel 안의 test 계정 값이 삭제됨
        그러므로 test 계정을 회원가입 시키고 UnsignedStudentModel 내에 test 계정이 있는지 검증
        get_unsigned_student 함수 내부에서 값이 존재하지 않는다면 NoContentException 발생
        NoContentException 이 발생하는지 check 해줌
        """
        rv: Response = self.request_signup()

        with self.assertRaises(NoContentException):
            UnsignedStudentModel.get_unsigned_student('test')

        return rv

    @check_status_code(204)
    def test_Invalid_uuid(self) -> Response:
        rv: Response = self.request_signup(uuid='invalid_uuid')

        return rv

    @check_status_code(205)
    def test_duplication_id(self) -> Response:
        # (1) test 계정을 db에 직접 생성
        self.create_test_account()
        # (2) test 계정을 request 를 통한 재생성
        rv: Response = self.request_signup()

        return rv
