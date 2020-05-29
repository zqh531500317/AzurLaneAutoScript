from module.campaign.campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger


MAP = CampaignMap('10-2')
MAP.shape = 'H6'
MAP.map_data = '''
    MB -- ME ME -- ++ ME MB
    -- ++ ++ ME ME ++ ME ME
    -- SP ++ ++ __ ME ME ++
    -- SP ++ ++ -- ME ME ++
    -- ++ ++ -- ME ++ ME ME
    -- -- -- -- ME ++ ME MB
'''
# MAP.weight_data = '''
#     10 10 10 10 10 10 10 10
#     10 20 10 10 10 10 10 10
#     10 10 10 10 30 10 10 20
#     10 10 10 10 10 10 10 10
#     10 10 10 10 10 10 10 10
#     10 10 10 10 10 10 10 10
# '''
# MAP.camera_data = ['D3']
# MAP.spawn_data = [
#     {'battle': 0, 'enemy': 3},
#     {'battle': 1, 'enemy': 2, 'mystery': 1},
#     {'battle': 2, 'enemy': 2, 'mystery': 1},
#     {'battle': 3, 'enemy': 1, 'mystery': 2},
#     {'battle': 4, 'enemy': 1},
#     {'battle': 5, 'boss': 1},
# ]

A1, B1, C1, D1, E1, F1, G1, H1, \
A2, B2, C2, D2, E2, F2, G2, H2, \
A3, B3, C3, D3, E3, F3, G3, H3, \
A4, B4, C4, D4, E4, F4, G4, H4, \
A5, B5, C5, D5, E5, F5, G5, H5, \
A6, B6, C6, D6, E6, F6, G6, H6, \
    = MAP.flatten()


class Config:
    pass


class Campaign(CampaignBase):
    MAP = MAP