import json
import yaml


def json_to_yaml(inp_file, out_file):

    
    try:
        with open(inp_file,"r") as json_data:
            data = json.load(json_data)
 

    except FileNotFoundError:
        return F"Cannot find JSON file with name {inp_file}. "

    except json.JSONDecodeError:
        return "The JSON file is configured incorrectly."

    except:
        return "Something wrong happened"

    elsse:
        with open(yaml_file, "w") as yaml_data:
            yaml.dump(data, yaml_data, sort_keys=False)
            
        return "Success"

                
json_file_name = input('Enter JSON file name: ')
yaml_file_name = input('Enter YAML file name: ')


if __name__ == "__main__":

    print(json_to_yaml(json_file_name,yaml_file_name))

    





