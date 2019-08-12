SQLALCHEMY_DATABASE_PASSWORD = 'yasmin04'
SQLALCHEMY_DATABASE_URI = 'postgresql:///planilha_gastos_dev'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

DEBUG_TB_INTERCEPT_REDIRECTS = False

SECRET_KEY = 'jshdaga\sjkhfuhweugrweuklasd83764208iqohd73i2jduu89472902ojdaaçei2'

DEBUG = True

DEBUG_TB_PANELS = [
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
    'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
    'flask_debugtoolbar.panels.sqlalchemy'
    ]