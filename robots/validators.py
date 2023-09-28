from datetime import datetime


def validate_data(model, version, created):
    errors = []
    if not model or len(model) > 2:
        errors.append('Model is error')
    if not version or len(version) > 2:
        errors.append('Version is error')
    if not created:
        errors.append('Created date is required')
    else:
        try:
            datetime.strptime(created, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            errors.append('Created date should be in format: YYYY-MM-DD HH:MM:SS')
    return errors
