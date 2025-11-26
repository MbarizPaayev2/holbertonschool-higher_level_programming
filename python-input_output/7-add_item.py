from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file 
import sys
my_list = []
try:
     my_list = load_from_json_file("add_item.json")
except Exception:
     my_list = []

return save_to_json_file(my_list, "add_item.json")