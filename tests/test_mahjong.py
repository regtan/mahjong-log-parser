import unittest
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.meld import Meld
from mahjong.hand_calculating.yaku_list import Tanyao

class MahjongTestCase(unittest.TestCase):
    
    def test_40符1飜は1300点(self):
        calculator = HandCalculator()
        tiles = TilesConverter.string_to_136_array(man='22567', pin='234567', sou='444')
        win_tile = TilesConverter.string_to_136_array(sou='4')[0]

        result = calculator.estimate_hand_value(tiles, win_tile)
        self.assertEqual(result.han, 1)
        self.assertEqual(result.fu, 40)
        self.assertEqual(result.cost['main'], 1300)
        self.assertEqual(result.yaku[0].name, "Tanyao")


if __name__ == '__main__':
    unittest.main()