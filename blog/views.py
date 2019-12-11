from django.shortcuts import render


def post_list(request):
    # Template을 찾을 경로에서
    #  post_list.html을 찾아서
    #  그 파일을 text로 만들어서 HttpResponse형태로 돌려준다
    # 위 기능을 하는 shortcut함수

    # content = loader.render_to_string('post_list.html', None, request)
    # return HttpResponse(content)
    return render(request, 'post_list.html')
