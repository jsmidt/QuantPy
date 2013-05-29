import unittest

import numpy as np
import quantpy as qp
import pandas as pd


class SmaTest(unittest.TestCase):
    def setUp(self):
        self.series = pd.Series((10, 11, 12, 13, 14, 15))
        self.data_frame = pd.DataFrame({
            'IBM': pd.Series(
                [1., 2., 3.],
                index=['1/1/13', '2/1/13', '3/1/13']
            ),
            'MSFT': pd.Series(
                [1., 1., 2., 8.],
                index=['1/1/13', '2/1/13', '3/1/13', '4/1/13']
            )
        })

    def tearDown(self):
        pass

    def test_wrong_window(self):
        self.assertRaises(ValueError, qp.sma, self.series, None)
        self.assertRaises(ValueError, qp.sma, self.series, '')
        self.assertRaises(ValueError, qp.sma, self.series, 'five')
        self.assertRaises(ValueError, qp.sma, self.series, -5)
        self.assertRaises(ValueError, qp.sma, self.series, -5.5)
        self.assertRaises(ValueError, qp.sma, self.series, 0)
        self.assertRaises(ValueError, qp.sma, self.series, 5.5)

    def test_wrong_data(self):
        import array
        self.assertRaises(ValueError, qp.sma, (1, 2, 3), 2)
        self.assertRaises(ValueError, qp.sma, [1, 2, 3], 2)
        self.assertRaises(ValueError, qp.sma, {1, 2, 3}, 2)
        self.assertRaises(ValueError, qp.sma, array.array('i', (1, 2, 3)), 2)

    def test_data(self):
        np.testing.assert_array_equal(
            pd.Series((np.NaN, np.NaN, 11.0, 12.0, 13.0, 14.0)),
            qp.sma(self.series, 3)
        )

    def test_data_frame(self):
        df = pd.DataFrame({
            'IBM': pd.Series(
                [np.NaN, 1.5, 2.5, np.NaN],
                index=['1/1/13', '2/1/13', '3/1/13', '4/1/13']
            ),
            'MSFT': pd.Series(
                [np.NaN, 1.0, 1.5, 5],
                index=['1/1/13', '2/1/13', '3/1/13', '4/1/13']
            )
        })
        np.testing.assert_array_equal(df, qp.sma(self.data_frame, 2))

if __name__ == '__main__':
    unittest.main()
