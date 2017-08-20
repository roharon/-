from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .db_to import db_to_views
import json



def keyboard(request):

    return JsonResponse({
            'type': 'buttons',
            'buttons': ['달걀 검사하기', '살충제 달걀이 위험한 이유', '국내 상황']
    })

@csrf_exempt
def message(request):
    json_str = (request.body).decode('utf-8')
    received_json_data = json.loads(json_str)
    content_name = received_json_data['content']
    content_type = received_json_data['type']

    button_info = ['달걀 검사하기', '살충제 달걀이 위험한 이유', '국내 상황']

    if content_name == '달걀 검사하기':
        return JsonResponse({
            'text': {
                'type': 'text'
            },
            'message': {
                'text': '달걀에 쓰여진 문자를 입력해주세요!(꺄아)'
            }
        })
    elif content_name == '살충제 달걀이 위험한 이유':
        return JsonResponse({
            'keyboard': {
            'type': 'buttons',
            'buttons': button_info
        },
            'message': {
                'text': '국립직업안전보건연구소(NIOSH)는 피프로닐에 장기간 또는 반복적으로 노출됐을 경우 간에 병변이 생길 수 있다고 밝혔다.'
                        '\n국제보건기구(WHO) 역시 유럽에서 ‘살충제 계란’ 파문이 일자 피프로닐을 과다 섭취할 경우 간장·신장 등 장기가 손상될 가능성이 있다고 경고한 바 있다.'
                        '\n가장 흔한 증상은 두통, 현기증, 감각 이상과 같은 신경 증상(50%)이었고 다음으로는 안구(44%), 위장관(28%), 호흡기(27%), 피부 증상(21%) 등이었다.'
            }
        })
    elif content_name == '국내 상황':
        return JsonResponse({
            'keyboard': {
            'type': 'buttons',
            'buttons': button_info
        },
            'message': {
            'text': '현재 정부의 조사가 진행 중이어서 정확한 발생 원인은 드러나지 않았지만, '
                    '산란계 농가가 닭을 키우는 케이지(철재 우리)에 살충제를 뿌리는 과정에서 '
                    '닭의 몸속으로 살충제가 들어갔을 가능성이 제기되고 있다.\n '
                    '살충제를 흡입한 닭이 나은 계란에 피프로닐이 넘어갔을 수 있다는 것이다.\n'
                    '또 케이지에 계란을 둔 채 살충제를 사용한 경우에도 살충제 성분이 계란 속으로 스며들었을 수 있다.\n'
                    '원칙적으로 케이지에 살충제를 뿌릴 때 닭과 계란을 빼내야 하지만 이를 따르지 않는 농가도 있는 것으로 전해졌다.\n'
                    '밀집 사육을 하는 양계장 특성상 관행적으로 닭이 들어 있는 케이지 안에 살충제를 뿌리는 경우가 있고,\n'
                    '이때 피프로닐이 닭의 피부 표면을 통해 체내로 흡수될 수 있다는 것이다.\n[한국일보 발췌]'
        }
        })

    egg_list = db_to_views()
    all_list = []
    #print((egg_list))

    consonant_vowel = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ',
                       'ㅜ','ㅠ','ㅡ','ㅣ']

    content_name = str(content_name).upper()
    #사용자입력 값 소문자->대문자
    content_name = str(content_name).replace(' ', '')
    #사용자입력 값 공백 삭제

    for ch in consonant_vowel:
        if ch in content_name:
            content_name = content_name.replace(ch, '')
            #사용자 값 자모음 오타 삭제

    for i in range(0, len(egg_list)):
        all_list.append(egg_list[i][0].replace('\n', ''))
    print(all_list)

    temp = 0
    for i in range(0, len(egg_list)):
        egg = egg_list[i][0].replace('\n', '')
        if content_name == '':
            answer = '다시 입력해주세요.'
            break
            
        if egg in content_name:
            print(content_name + '  ' + egg)
            answer = '살충제 달걀 상품입니다.'
            break
        elif content_name in egg:
            print(content_name + '  ' + egg)
            answer = '살충제 달걀 상품입니다.'
            break
        else:
            temp = i + 1
    if temp == len(egg_list):
        answer = '안전한 달걀 상품입니다.'



    if content_type == 'photo':
        answer = '사진기능은 지원하지 않아요'
    elif content_type == 'video':
        answer = '영상기능은 지원하지 않아요'
    elif content_type == 'audio':
        answer = '녹음파일은 지원하지 않아요'
    else:
        pass

    return JsonResponse({
        'message': {
            'text': answer
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': button_info
        }

    })





