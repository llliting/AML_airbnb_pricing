import pandas as pd
import os
from sklearn.model_selection import train_test_split

class AirbnbDataloader:
    def __init__(self, data_path = "data/") -> None:
        self.data_path = data_path
        self.data = None
        self.data_per_city = {}
        self.mergeCity()
        pass

    def mergeCity(self):
        cities = ['amsterdam', 'athens', 'barcelona', 'berlin', 'budapest', 'lisbon', 
          'london', 'paris', 'rome', 'vienna']
        days = ['weekdays', 'weekends']

        for city in cities:
            for day in days:
                file_name = os.path.join(self.data_path, f"{city}_{day}.csv")
                data_per_city = pd.read_csv(file_name)
                data_per_city = data_per_city.drop(data_per_city.columns[0], axis=1)
                data_per_city['city'] = city
                if (day == 'weekdays'):
                    data_per_city['weekdays'] = 1
                else:
                    data_per_city['weekdays'] = 0
                self.data_per_city[city] = data_per_city
                if self.data is None:
                    self.data = data_per_city
                else:
                    self.data = pd.concat([self.data, data_per_city])
        
    def split(self, data, test_size):
        X = data.drop(["realSum"], axis = 1)
        y = data["realSum"]
        X_dev, X_test, y_dev, y_test = train_test_split(X, y, test_size=test_size)
        return X_dev, X_test, y_dev, y_test
