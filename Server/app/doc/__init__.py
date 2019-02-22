def parameter(name: str, description: str, in_: str = 'json', type_: str = 'str', required: bool = True) -> dict:
    return {
        'name': name,
        'description': description,
        'in': in_,
        'type': type_,
        'required': required
    }


JWT_ACCESS_TOKEN = {
    'name': 'Authorization',
    'description': 'jwt access token',
    'in': 'header',
    'type': 'str',
    'required': 'true'
}

SAMPLE_OBJECT_IDS = [
    '5acddc2bc2a93f68ce96f5c4',
    '5acddc2bc2a93f68ce96f5c9',
    '5acddc2bc2a93f68ce96f5ce'
]
