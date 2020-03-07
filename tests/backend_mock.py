class BackendMock(object):
    """BackendMock backend implementation."""

    def __init__(self, ip):
        self._ip = ip

    def geolocate(self):
        """Mock api call"""
        self._raw_data = {
            "continent": "Europe",
            "country_code": "49",
            "name": "Germany",
            "geo": {
                "latitude": 51.165691,
                "longitude": 10.451526
            },
            "currency_code": "EUR"
        }

    def _parse(self):
        """Parse raw data.
        """
        self._continent = self._raw_data.get('continent')
        self._country = {
            'code': self._raw_data.get('alpha2'),
            'name': self._raw_data.get('name')
        }
        self._geo_data = self._raw_data.get('geo')

    def data(self):
        self._parse()

        return {
            'ip': self._ip,
            'continent': self._continent,
            'country': self._country,
            'geo': self._geo_data,
            'raw_data': self._raw_data
        }

