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
    # user_name = received_json['user_key']
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
    else:
        mess = "이걸 보고계시다면 오류입니다, 개발자에게 알려주세요"
        if type_name == 'photo':
            mess = "사진은 기능이 없어요, 버튼을 눌러주세요!"
        elif type_name == 'video':
            mess = "영상은 기능이 없어요, 버튼을 눌러주세요!"
        elif type_name == 'audio':
            mess = "녹음파일은 기능이 없어요, 버튼을 눌러주세요!"

        return JsonResponse({
            'message': {
                'text': mess
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['학식', '내일의 학식', '시간별 학식']
            }
        })