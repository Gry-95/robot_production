import json

from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

from .creating_excel_file import generate_rep
from .validators import validate_data
from .models import Robot



def download_excel(request):
    generate_rep()
    response = FileResponse(open('report.xlsx', 'rb'), as_attachment=True)
    return response


@csrf_exempt
def validate_request(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        model = data.get('model')
        version = data.get('version')
        created = data.get('created')

        errors = validate_data(model, version, created)

        if errors:
            return JsonResponse({'error': errors})
        else:
            robot = Robot(
                model=model,
                version=version,
                created=created
            )
            robot.save()
            return JsonResponse({'its ok': 'Robot created'}, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, safe=False)
