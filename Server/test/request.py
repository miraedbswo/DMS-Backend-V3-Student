from flask import Response


class AccountRequest:
    def request_auth(self, id='test', password='test') -> Response:
        rv = self.client.post(
            '/account/auth',
            json={'id': id, 'pw': password}
        )
        return rv

    def request_change_pw(self, jwt: str, current_password: str='test', new_password: str='new_pw') -> Response:
        rv = self.client.patch(
            '/account/pw',
            headers={'Authorization': jwt},
            json={'currentPassword': current_password, 'newPassword': new_password}
        )
        return rv

    def request_find_pw(self, id: str='test', email: str='test@dsm.hs.kr') -> Response:
        rv = self.client.post(
            '/account/pw',
            json={'id': id, 'email': email}
        )
        return rv

    def request_signup(self, uuid: str='test', id: str='test', password: str='test'):
        rv = self.client.post(
            '/account/signup',
            json={'uuid': uuid, 'id': id, 'password': password}
        )
        return rv


class InfoRequest:
    def request_basic_info(self, jwt: str) -> Response:
        rv = self.client.get(
            '/info/basic',
            headers={'Authorization': jwt}
        )
        return rv

    def request_extension_info(self, jwt: str) -> Response:
        rv = self.client.get(
            '/info/extension',
            headers={'Authorization': jwt}
        )
        return rv

    def request_point_info(self, jwt: str) -> Response:
        rv = self.client.get(
            '/info/point',
            headers={'Authorization': jwt}
        )
        return rv


class MealRequest:
    def request_meal(self, date: str) -> Response:
        rv = self.client.post(
            '/meal',
            json={'date': date}
        )
        return rv


class NoticeRequest:
    def request_notice_list(self) -> Response:
        rv = self.client.get('/notice')
        return rv

    def request_notice(self, notice_id: str) -> Response:
        rv = self.client.get(f'/notice/{notice_id}')
        return rv

    def request_qna_list(self) -> Response:
        rv = self.client.get('/qna')
        return rv

    def request_qna(self, qna_id: str) -> Response:
        rv = self.client.get(f'/qna/{qna_id}')
        return rv

    def request_rule_list(self) -> Response:
        rv = self.client.get('/rule')
        return rv

    def request_rule(self, rule_id: str) -> Response:
        rv = self.client.get(f'/rule/{rule_id}')
        return rv


class ReportRequest:
    def request_bug_report(self, jwt: str, platform: int, content: str) -> Response:
        rv = self.client.post(
            f'/report/bug/{platform}',
            headers={'Authorization': jwt},
            json={'content': content}
        )
        return rv

    def request_facility_report(self, jwt: str, room: int, content: str) -> Response:
        rv = self.client.post(
            '/report/facility',
            headers={'Authorization': jwt},
            json={'room': room, 'content': content}
        )
        return rv


class SurveyRequest:
    def request_survey_list(self, jwt: str) -> Response:
        rv = self.client.get(
            '/survey',
            headers={'Authorization': jwt}
        )
        return rv

    def request_survey(self, jwt: str, survey_id: str) -> Response:
        rv = self.client.get(
            f'/survey/{survey_id}',
            headers={'Authorization': jwt}
        )
        return rv

    def request_question(self, jwt: str, question_id: str, answer_content: str) -> Response:
        rv = self.client.post(
            f'/survey/question/{question_id}',
            headers={'Authorization': jwt},
            json={'answerContent': answer_content}
        )
        return rv
