import arrow

brewing_time = arrow.utcnow()
rome_time = brewing_time.to("Europe/Rome")

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])

print("UTC Time:", brewing_time)
print("Rome Time:", rome_time)
print("Collections:", chaiProfile)

# UTC Time: 2025-12-18T07:21:58.071681+00:00
# Rome Time: 2025-12-18T08:21:58.071681+01:00
# Collections: <class '__main__.chaiProfile'>