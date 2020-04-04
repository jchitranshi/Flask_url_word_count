import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG=False
	TESTING=False
	CSRF_ENABLED=True
	SECRET_KEY='THIS-NEED-TO-BE-CHANGED'

class ProductionConfig(Config):
	DEBUG=False

class DevelopmentConfig(Config):
	DEBUG=True
	DEVELOPMENT=True

class StagingConfig(Config):
	DEBUG=True
	DEVELOPMENT=True

class Testingconfig(Config):
	TESTING=True