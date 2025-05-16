import json

json_file = ""
with open("bus_routes/1.json", "r") as f:
    json_file = json.loads(f.read())

# print(json_file['data'][0])
    
def extract_stops_info(route_json):
    dispatch_dict = {}
    for dispatch in route_json["data"]:
        # each dispatch is a DICT with format:
        '''
            direction: (some direction, string)
            line:
                res: {number}
            stops:
                [
                    idx:
                        altId:
                            id
                        name:
                            name
                        lon: lon
                        lat: lat
                        depTime: "23:37:00"
                        depDate: "2025-05-16"
                ]
        
        
        '''
        if dispatch["direction"] not in dispatch_dict:
            # then we will fill in the dispatch dict.
            stops