import os

# Add this at the end of the file
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'myapp/static')]
