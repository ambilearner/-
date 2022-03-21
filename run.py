from DataCatcher import DataCatcher
from DataVisualize import DataVisualize


data_catcher = DataCatcher()
data_catcher.get_resp()

drawer = DataVisualize(place=data_catcher.place,target=data_catcher.target,updateDate=data_catcher.updateDate,overseas=data_catcher.overseas,local=data_catcher.local,non_symptom=data_catcher.non_symptom,total=data_catcher.total)

drawer.draw()
