from datetime import datetime
from pytz import timezone

data = datetime.now(timezone('US/Pacific'))

print(data)
print(data.timestamp())
print(datetime.fromtimestamp(1721184338.893685))
