from services.weather_service import get_weather

My_API_KEY = "1995e34eb0fa4d69877111718251906"
TARGET_CITY = "Thailand"
info = get_weather(TARGET_CITY,My_API_KEY)

print(info)