from xml.parsers.expat import ParserCreate
from urllib import request
class WeatherSaxHandler(object):
    def __init__(self):
        self.data={}
        self.isPubDate=False
    def start_element(self,name,attrs):
        if name=='yweather:location':
            self.data['city']=attrs['country']
        elif name=='pubDate':
            self.isPubDate=True
        elif name=='yweather:forecast':
            if attrs['day']==self.today:
                self.initDayInfo(attrs,'today')
            elif attrs['day']==self.tommrrow:
                self.initDayInfo(attrs, 'tommorrow')
    def end_element(self, name):
        pass

    def char_data(self,text):
        if self.isPubDate:
            self.isPubDate=False
            self.today=text.split(',')[0]
            self.tommrrow=self.getTomorrow(self.today)

    def initDayInfo(self,attrs,dayName):
         self.data[dayName]={}
         self.data[dayName]['text']=attrs['text']
         self.data[dayName]['low']=int(attrs['low'])
         self.data[dayName]['high']=int(attrs['high'])

    def getTomorrow(self,dayOfWeek):
        if dayOfWeek == 'Sun':
            return 'Mon'
        if dayOfWeek == 'Mon':
            return 'Tue'
        if dayOfWeek == 'Tue':
            return 'Wed'
        if dayOfWeek == 'Wed':
            return 'Thu'
        if dayOfWeek == 'Thu':
            return 'Fri'
        if dayOfWeek == 'Fri':
            return 'Sat'
        if dayOfWeek == 'Sat':
            return 'Sun'

def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    return handler.data

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()
result = parse_weather(data.decode('utf-8'))
print(result)

