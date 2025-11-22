from src.handlers.metrics_handler import createCustomMetric

# ALL custom metrics are created HERE!
auth_failures = createCustomMetric(
    "auth_failures", "Total number of authentication failures"
)

breached_passwords = createCustomMetric(
    "breached_passwords", "Checks whether the password is breached"
)

auth_success  = createCustomMetric(
    "auth_success", "Total number of successful authentications"
)

auth_logout  = createCustomMetric(
    "auth_logout", "Total number of log out attempts"
)

haveIbeenPwned  = createCustomMetric(
    "haveIbeenPwned", "Total number of log out attempts"
)

