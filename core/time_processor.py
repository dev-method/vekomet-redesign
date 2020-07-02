import datetime

def get_current_year(request):
    current_datetime = datetime.datetime.now()
    return {
        'current_year': current_datetime.year
    }