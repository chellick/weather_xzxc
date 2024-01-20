import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split


class Pipeline:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.data = None
        
    def prelude(self): # обработка данных для обучения модели 
        data = pd.read_csv(self.filepath,  na_values=np.nan)
        data = data.fillna(method='bfill')
        
        tempreture_y = data['Температура воздуха по сухому термометру'].to_numpy(np.int64)
        precipitation_y = data['Сумма осадков за период между сроками'].to_numpy(np.int64)
        humidity_y = data['Относительная влажность воздуха'].to_numpy(np.int64)
        wind_y = data['Средняя скорость ветра'].to_numpy(np.int64)
        
        data = data.drop(columns=['Средняя скорость ветра',
                           'Относительная влажность воздуха',
                           'Сумма осадков за период между сроками',
                           'Температура воздуха по сухому термометру'])
        
        X = data.to_numpy(np.int64)[:]
        return X, tempreture_y, precipitation_y, humidity_y, wind_y
    
    def train_test_split(self, mode="sklearn"):
        if mode == "sklearn":
            X, tempreture_y, precipitation_y, humidity_y, wind_y = self.prelude()
            
            X_temp_train, X_temp_test, y_temp_train, y_temp_test = train_test_split(X, tempreture_y,
                                                                        test_size=0.2,
                                                                        random_state=10,
                                                                        shuffle=True)

            X_precipitation_train, X_precipitation_test, y_precipitation_train, y_precipitation_test = train_test_split(X, precipitation_y,
                                                                                                                        test_size=0.2,
                                                                                                                        random_state=10,
                                                                                                                        shuffle=True)

            X_humidity_train, X_humidity_test, y_humidity_train, y_humidity_test = train_test_split(X, humidity_y,
                                                                                                    test_size=0.2,
                                                                                                    random_state=10,
                                                                                                    shuffle=True)

            X_wind_train, X_wind_test, y_wind_train, y_wind_test = train_test_split(X, wind_y,
                                                                                    test_size=0.2,
                                                                                    random_state=10,
                                                                                    shuffle=True)
            
            self.data = [[X_temp_train, X_temp_test, y_temp_train, y_temp_test],
                    [X_precipitation_train, X_precipitation_test, y_precipitation_train, y_precipitation_test],
                    [X_humidity_train, X_humidity_test, y_humidity_train, y_humidity_test],
                    [X_wind_train, X_wind_test, y_wind_train, y_wind_test]]
                
            return 'Successfull split'
        else:
            raise 'No such mode!'
    
    def models_compile(self, fit: bool, save_path='data/tf_models/'):
        if fit:
            index = 1
            for current_dataset in self.data:
                
                model = tf.keras.models.Sequential([
                    tf.keras.layers.Input((86)),
                    tf.keras.layers.Flatten(),
                    tf.keras.layers.Dense(86*3),
                    tf.keras.layers.ReLU(),
                    tf.keras.layers.Dense(86*3),
                    tf.keras.layers.ReLU(),
                    tf.keras.layers.Dense(1)
                ])
                 
                
                model.compile(optimizer='adam',
                            loss='mean_absolute_error')
                
                model.fit(current_dataset[0], 
                          current_dataset[2],
                          epochs=20,
                          validation_split=0.1)
                
                loss = model.evaluate(current_dataset[1], current_dataset[3])
                
                print(loss, f'<- Model {index} Loss')
                
                if save_path:
                    model.save_weights(filepath=save_path+'model_weights_'+f'{index}.h5')
                    model.save(filepath=save_path+'model_'+f'{index}.h5')
                    print('Model saved')
                    
                index += 1
                
        return 'Compiled'
    

                    

file = Pipeline(filepath="data/srock8/23463.dat")
file.filepath
file.prelude()
file.train_test_split()
print(file.models_compile(fit=True))



        