from json_to_yaml import json_to_yaml
import unittest


class TestConverter(unittest.TestCase):

    
    def test_json_to_yaml_func(self):
        self.assertEqual(json_to_yaml("test.json","test.yaml"),"Success")

        self.assertNotEqual(json_to_yaml("other.json","test.yaml"),"Success")
        

        self.assertEqual(json_to_yaml("bad_json.json","test.yaml"),

                            "The JSON file is configured incorrectly.")

        self.assertEqual(json_to_yaml(".//","test.yaml"),"Something wrong happened")

        self.assertEqual(json_to_yaml("","test.yaml"),F"Cannot find JSON file with name . "),
                                                    

if __name__ == "__main__":
    unittest.main()