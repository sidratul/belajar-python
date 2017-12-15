from json import dumps,loads

class DmzConfig:
	
	# CONF = loads(open("./config.json").read())
	CONF = loads(open("./config_test.json").read())
	DOMAIN_NAME = CONF['domain_name']
	FORCE_CHECK = CONF['force_check']
	SLEEP_FINISHED = CONF['sleep_hour_after_finished'] * 60 * 60
	SLEEP_MAX_REQUEST = CONF['sleep_hour_max_request'] * 60 * 60
	MAX_REQUEST = CONF['daily_max_request']
	SLEEP_AFTER_REQUEST = CONF['sleep_second_after_request']
	LANGUAGES = CONF['languages']
