from rest_framework.throttling import AnonRateThrottle

class ProductAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'