from datetime import datetime, timedelta

# format is the desired format the date should be returned as
# ex: 'YYYY-MM-DD' format = '%Y-%m-%d'
# if no format is given, then a datetime object is returned
def get_date_week_ago(format=None):
    week_ago = datetime.now() - timedelta(days=7)
    if format is None:
        return week_ago
    return week_ago.strftime(format)

# Check if a date is from a week ago
def check_week_ago(created_at):
    now = datetime.now()
    week_ago = now - timedelta(days=7)
    if week_ago <= created_at <= now:
        return True
    else:
        return False
