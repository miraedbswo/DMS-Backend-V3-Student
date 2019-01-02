class AccountRequest:

    def requst_auth(self, id='test', password='test'):
        rv = self.client.post(
            '/account/auth',
            json={'id': id, 'pw': password}
        )
        return rv

    def request_change_pw(self, jwt, current_password='test', new_password='testtest'):
        rv = self.client.patch(
            '/account/pw',
            headers={'Authorization': jwt},
            json={'currentPassword': current_password, 'newPassword': new_password}
        )
        return rv

    def request_find_pw(self, id='test', email='test@dsm.hs.kr'):
        rv = self.client.post(
            '/account/pw',
            json={'id': id, 'email': email}
        )
        return rv

    def request_signup(self, uuid='test', id='test', password='test'):
        rv = self.client.post(
            '/account/signup',
            json={'uuid': uuid, 'id': id, 'password': password}
        )
        return rv
