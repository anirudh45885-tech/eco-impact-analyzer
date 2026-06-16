import requests

def get_live_air_quality():

  """
  Fetches real-time air quality data for Dubai from the Open-Meteo API
  """
  #Latitude and Longitude for Dubai
  url= "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=25.2048&longitude=55.2708&current=european_aqi,pm2_5,pm10"
  try:
    response=requests.get(url)
    #Convert the incoming JSON data into a python dictionary
    data=response.json()
    return data
  except Exception as e:
    print(f"Error fetching data:{e}")
    return None
def print_daily_report(data):
  """ Parses the live API dictionary and prints a clean report """
  if not data:
    print("No data available to print")
    return
  #Extract the current data dictionary from the API response
  current=data.get("current",{})

  print("\n--LIVE DUBAI ENVIRONMENTAL REPORT---")
  print(f"European Air Quality Index(AQI):{current.get('european_aqi')}(Lower is better)")
  print(f"PM2.5 (Fine Particulate Matter):{current.get('pm2_5)} µg/m³")
  print(f"PM10 (Coarse Particulate Matter): {current.get('pm10')} µg/m³")
  print("----------------------------------------")
 if __name__=="__main__":
    print("Connceting to environmental API...")
    live_data=get_live_air_quality()
    print_daily_report(live_data)

  #connect to live open meteo api
