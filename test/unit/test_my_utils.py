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


if __name__ == '__main__':
    unittest.main()
