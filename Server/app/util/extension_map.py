# 0: 벽, 1: 빈 자리

# EXTENSION_MAP_CHARTS = {
#     '가온실': [
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1]
#     ],
#     '나온실': [
#         [1, 0, 1, 0, 1, 0, 1],
#         [1, 0, 1, 0, 1, 0, 1],
#         [1, 0, 1, 0, 1, 0, 1],
#         [1, 0, 0, 1, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 1],
#         [0, 0, 1, 1, 1, 0, 0]
#     ],
#     '다온실': [
#         [1, 1, 1, 1],
#         [1, 1, 1, 1],
#         [1, 1, 1, 1],
#         [1, 1, 1, 1],
#         [1, 1, 1, 1]
#     ],
#     '라온실': [
#         [1, 1, 0, 0, 1, 1],
#         [1, 1, 0, 0, 1, 1],
#         [0, 0, 1, 1, 0, 0],
#         [0, 0, 1, 1, 0, 0],
#         [1, 1, 0, 0, 1, 1],
#         [1, 1, 0, 0, 1, 1]
#     ],
#     '2층 여자 자습실': [
#         [1, 1, 1, 1, 0, 0],
#         [0, 0, 0, 0, 0, 1],
#         [1, 0, 1, 1, 0, 1],
#         [1, 0, 1, 1, 0, 1],
#         [1, 0, 1, 1, 0, 1],
#         [1, 0, 1, 1, 0, 1],
#         [1, 0, 0, 0, 0, 1]
#     ],
#     '3층 학교측': [
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1]
#     ],
#     '3층 기숙사측': [
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0],
#         [1, 1, 0, 0, 0],
#         [1, 1, 0, 0, 0]
#     ],
#     '4층 학교측': [
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1]
#     ],
#     '4층 기숙사측': [
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1],
#         [1, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0],
#         [1, 1, 0, 0, 0],
#         [1, 1, 0, 0, 0]
#     ],
#     '5층 열린교실': [
#         [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
#         [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
#         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
#         [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
#         [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
#         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
#     ],
#     '3층 쇼파': [
#         [1, 1, 1, 1],
#         [1, 1, 1, 1]
#     ],
# }

EXTENSION_MAP_CHARTS = {
    '가온실': [
        [-1, 1, 0, -1, 1],
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1],
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1]
    ],
    '나온실': [
        [1, 0, 1, 0, -1, 0, 1],
        [-1, 0, -1, 0, 1, 0, -1],
        [1, 0, 1, 0, -1, 0, 1],
        [-1, 0, 0, -1, 0, 0, -1],
        [1, 0, 0, 0, 0, 0, 1],
        [0, 0, -1, 1, -1, 0, 0]
    ],
    '다온실': [
        [-1, 1, -1, 1],
        [1, -1, 1, -1],
        [-1, 1, -1, 1],
        [1, -1, 1, -1],
        [-1, 1, -1, 1]
    ],
    '라온실': [
        [-1, 1, 0, 0, -1, 1],
        [1, -1, 0, 0, 1, -1],
        [0, 0, 1, -1, 0, 0],
        [0, 0, -1, 1, 0, 0],
        [-1, 1, 0, 0, -1, 1],
        [1, -1, 0, 0, 1, -1]
    ],
    '2층 여자 자습실': [
        [1, -1, 1, -1, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [-1, 0, -1, 1, 0, -1],
        [1, 0, 1, -1, 0, 1],
        [-1, 0, -1, 1, 0, -1],
        [1, 0, 1, -1, 0, 1],
        [-1, 0, 0, 0, 0, -1]
    ],
    '3층 학교측': [
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1],
        [0, 0, 0, 0, 0],
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1],
        [0, 0, 0, 0, 0],
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1]
    ],
    '3층 기숙사측': [
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1],
        [0, 0, 0, 0, 0],
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1],
        [0, 0, 0, 0, 0],
        [1, -1, 0, 0, 0],
        [-1, 1, 0, 0, 0]
    ],
    '4층 학교측': [
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1],
        [0, 0, 0, 0, 0],
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1],
        [0, 0, 0, 0, 0],
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1]
    ],
    '4층 기숙사측': [
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1],
        [0, 0, 0, 0, 0],
        [1, -1, 0, 1, -1],
        [-1, 1, 0, -1, 1],
        [0, 0, 0, 0, 0],
        [1, -1, 0, 0, 0],
        [-1, 1, 0, 0, 0]
    ],
    '5층 열린교실': [
        [-1, -1, 1, 0, -1, 1, 0, 1, -1, -1],
        [1, -1, -1, 0, 1, -1, 0, -1, -1, 1],
        [0, 0, 0, 0, -1, 1, 0, 0, 0, 0],
        [-1, -1, 1, 0, 1, -1, 0, 1, -1, -1],
        [1, -1, -1, 0, -1, 1, 0, -1, -1, 1],
        [0, 0, 0, 0, 1, -1, 0, 0, 0, 0],
        [-1, -1, 1, 0, 0, -1, 0, 0, 0, 0],
        [1, -1, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1, -1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, -1, -1, 0, 0, 0, 0, 0, 0, 0]
    ],
    '3층 쇼파': [
        [1, 1, 1, 1],
        [1, -1, -1, -1]
    ],
}

map_metadata = {
    1: '가온실',
    2: '나온실',
    3: '다온실',
    4: '라온실',
    5: '2층 여자 자습실',
    6: '3층 학교측',
    7: '3층 기숙사측',
    8: '4층 학교측',
    9: '4층 기숙사측',
    10: '5층 열린교실',
    11: '3층 쇼파'
}


def get_map_chart(class_num: int) -> list:
    return EXTENSION_MAP_CHARTS[map_metadata[class_num]]
