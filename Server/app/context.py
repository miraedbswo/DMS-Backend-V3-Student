from typing import Optional


class _ContextProperty:
    _request_payload = None

    @property
    def request_payload(self) -> Optional:
        return self._request_payload

    @request_payload.setter
    def request_payload(self, value):
        self._request_payload = value


context_property = _ContextProperty()
