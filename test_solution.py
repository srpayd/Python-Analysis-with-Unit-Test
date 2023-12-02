import unittest
from solution import read_encode_csv, read_decode_json, filter_and_count_2021_clicks

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.encode_csv_path = 'encodes.csv'
        self.decode_json_path = 'decodes.json'

    def test_read_encode_csv(self):
        encode_dict = read_encode_csv(self.encode_csv_path)
        
        self.assertTrue(isinstance(encode_dict, dict)) 
        self.assertEqual(len(encode_dict), 6) 

    def test_read_decode_json(self):
        decode_data = read_decode_json(self.decode_json_path)
        
        self.assertTrue(isinstance(decode_data, list))
        self.assertEqual(len(decode_data), 10000) 

    def test_filter_and_count_2021_clicks(self):
        encode_dict = read_encode_csv(self.encode_csv_path)
        decode_data = read_decode_json(self.decode_json_path)
        result = filter_and_count_2021_clicks(decode_data, encode_dict)
        
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(len(result), 6)  

        for _,clicks in result.items():
            self.assertGreater(clicks,0) 

if __name__ == '__main__':
    unittest.main()
