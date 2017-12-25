from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def keyboard(request):

    return JsonResponse(
        {
            'type': 'buttons',
            'buttons': ['학식', '내일의 학식', '시간별 학식']
        }
    )

@csrf_exempt
def message(request):

    #button = ['학식', '내일의 학식', '시간별 학식']

    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)
    content_name = received_json['content']
    user_name = received_json['user_key']
    type_name = received_json['type']

    if content_name == "학식":
        return JsonResponse(
            {
                'message': {
                    'text': '학식 버튼을 눌렀습니다.'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['학식', '내일의 학식', '시간별 학식']
                }
            }
        )
    elif content_name == "내일의 학식":
        return JsonResponse(
            {
                'message': {
                    'text': '내일의 학식  버튼을 눌렀습니다'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['학식', '내일의 학식', '시간별 학식']
                }
            }
        )
    elif content_name == '시간별 학식':
        return JsonResponse(
            {
                'message': {
                    'text': '시간별 학식을 눌렀습니다'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['학식', '내일의 학식', '시간별 학식']
                }
            }
        )