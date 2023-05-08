import requests
import json


URL = "http://127.0.0.1:7452/studentapi"

# function Definition. Show data.
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    # convert python dic into Json Data.
    json_data = json.dumps(data)
    # send data after converting into json.
    res = requests.get(url = URL, data=json_data)
    data = res.json()
    print(data)
    # for dic in data:
    #     for key,value in dic.items():
    #         print(f"{key} : {value}")

# function Calling.
# get_data(4)

# function calling without argument. In this case return all data based on logic.
# get_data()
    

# send data by thirdparty app.
# function definition.
def post_data():
    data = {
        'name':'Arav',
        'sr_no':'105',
        'city':'Noida'
    }
    # convert python data into json data.
    json_data = json.dumps(data)
    res = requests.post(url = URL, data=json_data )
    data = res.json()
    print(data)

# function calling.
# post_data()


# Update data in Database.
# func deifnition 
def update_data():
    data= {
        'id':4, 
        'name':'Gopal lucky',
        'city':'Hydrabad'
    }

    json_data = json.dumps(data)
    res = requests.put(url = URL , data=json_data)
    data = res.json()
    print(data)

# func calling.
# update_data()


# delete data in database.
# function definition
def delete_data():
    data = {
        'id':5,
        }

    json_data = json.dumps(data) # python dict convert into json.
    res = requests.delete(url= URL , data=json_data)
    data = res.json()
    print(data)

# func calling.
# delete_data()

