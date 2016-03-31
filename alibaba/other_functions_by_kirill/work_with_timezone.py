# -*- coding:utf-8 -*-
__author__ = 'Kirill Korolev'
"""
    Модуль для работы с часовыми поясам(Дополняется)
    31 март. 2016г. v. 1.0.7
"""


timezone_locations = [
    'Europe/Kaliningrad', # Kaliningrad + 2
    'Europe/Moscow',  # west Russia GMT+3
    'Europe/Volgograd',  # Caspian Sea GMT+3
    'Europe/Samara',  # Samara, Udmurtia GMT+4
    'Asia/Yekaterinburg',  # Urals GMT+5
    'Asia/Omsk',  # west Siberia GMT+6
    'Asia/Novosibirsk',  # Novosibirsk GMT+6
    'Asia/Novokuznetsk',  # Kemerovo GMT+7
    'Asia/Krasnoyarsk',  # Yenisei River GMT+7
    'Asia/Irkutsk',  # Lake Baikal GMT+8
    'Asia/Yakutsk',  # Lena River GMT+9
    'Asia/Vladivostok',  # Amur River GMT+10
    'Asia/Sakhalin',  # Sakhalin Island GMT+10
    'Asia/Ust-Nera',  # Oymyakonsky GMT+10
    'Asia/Magadan',  # Magadan GMT+10
    'Asia/Srednekolymsk',  # East Sakha, N Kuril Island GMT+11
    'Asia/Kamchatka',  # Kamchatka GMT+12
    'Asia/Anadyr',  # Bering Sea GMT+12
]

# аббревиатура часового пояса : разница от GMT
timezone_abrs = {
    'USZ1': 2,  # USZ1(+2)
    'EET': 2,  # East Europe(+2)
    'MSK':  3,  # MSK(+3)
    'SAMT': 4,  # SAMT(+4)
    'YEKT': 5,  # YEKT(+5)
    'OMST': 6,  # OMST(+6)
    'NOVT': 6,  # Novosibirsk(+6)
    'KRAT': 7,  # KRAT(+7)
    'IRKT': 8,  # IRKT(+8)
    'YAKT': 9,  # YAKT(+9)
    'VLAT': 10,  # VLAT(+10)
    'SAKT': 10,  # SAKT(+10)
    'MAGT': 10,  # MAGT(+10)
    'SRET': 11,  # SRET(+11)
    'PETT': 12,  # PETT(+12)
    'ANAT': 12,  # ANAT(+12)
}

