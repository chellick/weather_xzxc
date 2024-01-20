import pandas as pd
import numpy as np
import os
import time

class Info:
    def __init__(self) -> None:
        pass
    
    def upload_info(file_path, save_path='file.csv', extension='csv'):
        local_path = 'data/storage/'
        if extension == 'csv' or extension == 'dat': 
            data = pd.read_csv(file_path).fillna(method='ffill')
            data = data.to_csv(local_path + save_path, index=False) # сохраняем в локальную папку storage
        elif extension == 'xlsx':
            data = pd.read_excel(file_path).fillna(method='ffill')
            data = data.to_csv(local_path + save_path, index=False)
    
    def export_info(self):
        pass # чее???

class Location:
    def __init__(self) -> None: # функция парсит .dat; .csv файлы и заполняет пропущенные значения
        self.data = None
        
        
    def set_location(self, station_index):
        # тут короче либо в бд хранить данные климатические и к ним обращаться
        # либо яндекс API юзать
        # написан варик где пока все на локал data/srock8/___.dat
        for i in os.listdir('data/storage/'):
            sin_index = int(i.replace('.dat', '').replace('.csv', '').replace('.xlsx', ''))
            if sin_index == station_index:
                dataframe = pd.read_csv(f'data/storage/{i}', sep=',')
                break

        self.data = dataframe
        self.location = sin_index
    
    def choose_time(self, start: str, end: str) -> pd.DataFrame: # пока ток с годами
        start = start.split('/')
        end = end.split('/')
        choose = self.data.loc[(self.data['Год по Гринвичу'] >= int(start[0]))
                      &(self.data['Год по Гринвичу'] <= int(end[0]))]
        
        return choose # оставлю как есть в зависимости от того что понадобится тебе. Возвращается объект датафрейма там можно медиану найти
    
class Predictions:
    def __init__(self) -> None:
        # input format: широта, долгота, год, месяц, день 
        # TODO: переделать модель на torch
        pass
        
        
d = Info.upload_info(file_path='data/srock8/20069.dat', save_path='20069.csv', extension='csv')
l = Location()
l.set_location(20069)
print(l.choose_time('1966/12/12', '2022/12/12'))

        