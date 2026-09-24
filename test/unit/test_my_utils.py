import my_utils
import unittest
import random


class TestMyUtils(unittest.TestCase):

    def test_get_column(self):
        file_name = "test/func/Agrofood_co2_emissions_test_file.csv"
        result = my_utils.get_column(file_name, 0,
                                     'Canada', 2)
        self.assertEqual(result, [329, 683, 608, 627, 1546, 813,
                                  1249, 3236, 1337, 222])

    def test_get_column_doesnt_output_wrong_country(self):
        file_name = "test/func/Agrofood_co2_emissions_test_file.csv"
        result = my_utils.get_column(file_name, 0,
                                     'Canada', 2)
        # note that none of these emission values should appear in
        # the Canada emissions list, though it is poissble that
        # other countries would have overlap
        Spain_emmissions = [15, 27, 5, 7, 22, 23, 62, 4, 18, 6]
        for s in Spain_emmissions:
            self.assertNotIn(s, result)

    def test_get_column_doesnt_output_wrong_column(self):
        file_name = "test/func/Agrofood_co2_emissions_test_file.csv"
        result = my_utils.get_column(file_name, 0,
                                     'Canada', 2)
        # note that none of these emission values should appear in
        # the Canada fires emissions list, though it is poissble that
        # other emissions would have overlap
        crop_emmissions = [3164, 3416, 4283, 3497, 3678,
                           3876, 3839, 3944, 4031, 4246]
        for c in crop_emmissions:
            self.assertNotIn(c, result)

    def test_get_column_random(self):
        file_name = "test/func/Agrofood_co2_emissions_test_file.csv"
        for i in range(100):
            result_column = random.randint(1, 3)
            country_list = ['Canada', 'Spain', 'United Republic of Tanzania']
            country = country_list[random.randint(0, 2)]
            result = my_utils.get_column(file_name, 0, country,
                                         result_column)
            self.assertTrue(len(result) > 0)
            for r in result:
                self.assertTrue(r >= 0)
                self.assertTrue(r <= 11000)

    def test_get_column_file_not_found(self):
        file_name = "test/func/Agrofood_co2_emisions_test_file.csv"
        self.assertRaises(SystemExit, my_utils.get_column,
                          file_name, 0,
                          'Canada', 2)

    def test_query_index_out_of_bounds(self):
        file_name = "test/func/Agrofood_co2_emissions_test_file.csv"
        self.assertRaises(SystemExit, my_utils.get_column,
                          file_name, 13,
                          'Canada', 2)

    def test_result_index_out_of_bounds(self):
        file_name = "test/func/Agrofood_co2_emissions_test_file.csv"
        self.assertRaises(SystemExit, my_utils.get_column,
                          file_name, 0,
                          'Canada', 9)

    def test_non_number_error(self):
        file_name = "test/func/Agrofood_co2_emissions_test_file.csv"
        self.assertRaises(SystemExit, my_utils.get_column,
                          file_name, 0,
                          'Canada', 0)

    def test_country_not_found(self):
        file_name = "test/func/Agrofood_co2_emissions_test_file.csv"
        self.assertRaises(SystemExit, my_utils.get_column,
                          file_name, 0,
                          'Gondor', 2)

    def test_mean_one_array(self):
        array = [1, 5, -3, 19]
        m = my_utils.mean(array)
        self.assertAlmostEqual(m, 5.5)

    def test_mean_random_arrays_within_bounds(self):
        for i in range(10000):
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            c = random.randint(0, 10)
            d = random.randint(0, 10)
            array = [a, b, c, d]
            m = my_utils.mean(array)
            self.assertTrue(m <= 10)
            self.assertTrue(m >= 0)

    def test_mean_large_random_arrays_about_5(self):
        array = []
        for k in range(10000):
            array.append(random.randint(0, 10))
        m = my_utils.mean(array)
        self.assertAlmostEqual(m, 5, delta=0.1)

    def test_mean_not_incorrect(self):
        array = [7, -1, -2, 9, 7]
        m = my_utils.mean(array)
        self.assertNotAlmostEqual(m, -4)

    def test_mean_not_ints(self):
        array = ["hi", 4, 5]
        self.assertRaises(SystemExit, my_utils.mean, array)

    def test_mean_empty_array(self):
        array = []
        self.assertRaises(SystemExit, my_utils.mean, array)

    def test_median_odd_array(self):
        array = [-3, 20, -1, 2, 4]
        med = my_utils.median(array)
        self.assertAlmostEqual(med, 2)

    def test_median_even_array(self):
        array = [-3, 20, -1, 2, 4, -2]
        med = my_utils.median(array)
        self.assertAlmostEqual(med, 0.5)

    def test_median_random_arrays_within_bounds(self):
        for i in range(10000):
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            c = random.randint(0, 10)
            d = random.randint(0, 10)
            array = [a, b, c, d]
            med = my_utils.median(array)
            self.assertTrue(med <= 10)
            self.assertTrue(med >= 0)

    def test_median_large_random_arrays_5(self):
        array = []
        for k in range(100000):
            array.append(random.randint(0, 10))
        med = my_utils.median(array)
        self.assertAlmostEqual(med, 5)

    def test_median_random_arrays_modulo_one_half(self):
        for i in range(10000):
            length = random.randint(1, 10)
            array = [random.randint(0, 10) for k in range(length)]
            med = my_utils.median(array)
            self.assertAlmostEqual(med % 0.5, 0)

    def test_median_not_incorrect(self):
        array = [7, -1, -2, 9, 7]
        med = my_utils.median(array)
        self.assertNotAlmostEqual(med, 8)

    def test_median_not_ints(self):
        array = [3.5, 4, 5]
        self.assertRaises(SystemExit, my_utils.median, array)

    def test_median_empty_array(self):
        array = []
        self.assertRaises(SystemExit, my_utils.median, array)

    def test_sd_one_array(self):
        array = [-1, 2, 3, -2, 0, -3, 1]
        sd = my_utils.sd(array)
        self.assertAlmostEqual(sd, 2.160246899)

    def test_sd_uniform_distribution(self):
        array = [random.randint(0, 10) for k in range(100000)]
        sd = my_utils.sd(array)
        self.assertAlmostEqual(sd, 3.162277660, delta=0.1)

    def test_sd_random_arrays_within_bounds(self):
        for i in range(10000):
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            c = random.randint(0, 10)
            d = random.randint(0, 10)
            array = [a, b, c, d]
            sd = my_utils.sd(array)
            self.assertTrue(sd <= 5.8)
            self.assertTrue(sd >= 0)

    def test_sd_not_incorrect(self):
        array = [7, -1, -2, 9, 7]
        sd = my_utils.sd(array)
        self.assertNotAlmostEqual(sd, 10)

    def test_sd_not_ints(self):
        array = [True, 4, 5]
        self.assertRaises(SystemExit, my_utils.sd, array)

    def test_sd_empty_array(self):
        array = []
        self.assertRaises(SystemExit, my_utils.sd, array)


if __name__ == '__main__':
    unittest.main()
