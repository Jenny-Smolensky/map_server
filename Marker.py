import collections
import re

keys = ['name', 'latitude', 'longitude']

class Marker:

    def __init__(self, latitude, longitude, name):

        self.latitude = latitude
        self.longitude = longitude
        self.name = name


    @staticmethod
    def is_valid_double(number):
        if number is None or number is "":
            return False
        try:
            float(number)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_name_valid(name):
        return re.match("[a-zA-Z0-9|-]*", name)

    @staticmethod
    def is_lat_valid(lat):
        if not Marker.is_valid_double(lat):
            return False

        if -90 <= float(lat) <= 90:
            return True

        return False

    @staticmethod
    def is_lng_valid(lng):
        if not Marker.is_valid_double(lng):
            return False

        if -180 <= float(lng) <= 180:
            return True

        return False

    @staticmethod
    def parse_from_json(json_dict):

        if collections.Counter(json_dict.keys()) != collections.Counter(keys):
            return [False, 'wrong format of dictionary']

        if not Marker.is_name_valid(json_dict['name']):
            return [False, 'name value format wrong']

        if not Marker.is_lat_valid(json_dict['latitude']):
            return [False, 'latitude value out of range']

        if not Marker.is_lng_valid(json_dict['longitude']):
            return [False, 'longitude value out of range']

        return [True, Marker(float(json_dict['latitude']),
                      float(json_dict['longitude']),
                      json_dict['name'])]

    def to_str(self):
        str = {
             'latitude': self.latitude,
             'longitude': self.longitude,
             'name': self.name,
         }
        print(str)
        return str
