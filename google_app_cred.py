# Path to Google BigQuery credential JSON
CREDENTIAL_PATH = ""

# Try importing key from private, if available
try:
    from private import *
except Exception:
    pass
