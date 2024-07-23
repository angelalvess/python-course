import secrets
import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits, k=8)))


random = secrets.SystemRandom()

r_range = random.randrange(1, 100)
print(r_range)
