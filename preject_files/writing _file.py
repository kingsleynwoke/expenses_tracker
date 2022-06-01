list_of_entries = [{ "Name": "David", 'Date': '22-3-2022', 'Description': 'concert ticket', 'Amount': 195.01, 'Category': 'fun'},
                   { "Name": "Peter", 'Date': '23-3-2022', 'Description': 'lipstick', 'Amount': 80.09, 'Category': 'cosmetic', "Name": "Peter"},
                   { "Name": "Grace", 'Date': '24-3-20222', 'Description': 'Aldi shopping Diverse', 'Amount': 350.15, 'Category': 'grocery'},
                   { "Name": "Grace", 'Date': '22-3-2022', 'Description': 'concert ticket', 'Amount': 195.01, 'Category': 'fun'},
                   { "Name": "Peter", 'Date': '23-3-2022', 'Description': 'lipstick', 'Amount': 80.09, 'Category': 'cosmetic'},
                   { "Name": "David", 'Date': '24-3-20222', 'Description': 'Aldi shopping Diverse', 'Amount': 350.15, 'Category': 'grocery'}]


import json

with open("dict_new", "w") as new_dict:
    for line in list_of_entries:
        json.dump(line, new_dict, indent=2)
        
      
    

#writing_to_file("my_first_grocery_dictionary", list_of_entries)

 
def reading_from_file(saved_file_name):
    with open(saved_file_name) as saved_file:
        file_result = json.load(saved_file)
    
    return file_result

reading_from_file("dict_new")