from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
	for code,names in COUNTRIES.items():
		if names == country_name:
			return code
	return None