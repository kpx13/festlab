# -*- coding: utf-8 -*-

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': 'libfic.db',   # Or path to database file if using sqlite3.
        #'USER': 'libfic',                      # Not used with sqlite3.
        #'PASSWORD': 'libfic',                  # Not used with sqlite3.
        #'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        #'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    #}
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'festlab.db',                      # Or path to database file if using sqlite3.
        #'USER': 'myloot',                      # Not used with sqlite3.
        ##'PASSWORD': 'myloot',                  # Not used with sqlite3.
        #'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        #'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        #'OPTIONS': {
         #"init_command": "SET foreign_key_checks = 0;",
        #},
    }
}



DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if DEBUG:
    DEBUG_TOOLBAR = False
    if DEBUG_TOOLBAR:
        MIDDLEWARE_CLASSES  += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
        INSTALLED_APPS      += ('debug_toolbar',)
        DEBUG_TOOLBAR_PANELS = (
            'debug_toolbar.panels.version.VersionDebugPanel',
            'debug_toolbar.panels.timer.TimerDebugPanel',
            'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
            'debug_toolbar.panels.headers.HeaderDebugPanel',
            'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
            'debug_toolbar.panels.template.TemplateDebugPanel',
            'debug_toolbar.panels.sql.SQLDebugPanel',
            'debug_toolbar.panels.signals.SignalDebugPanel',
            'debug_toolbar.panels.logger.LoggingPanel',
        )

        def custom_show_toolbar(request):
            return True # Always show toolbar, for example purposes only.

        DEBUG_TOOLBAR_CONFIG = {
            'INTERCEPT_REDIRECTS': False,
            'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
            #'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
            'HIDE_DJANGO_SQL': False,
            'TAG': 'div',
        }
