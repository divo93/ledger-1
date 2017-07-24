from django.shortcuts import render, HttpResponseRedirect


def home(request):
    try:
        if request.user.is_authenticated():
            return render(request, 'base.html')
        else:
            return HttpResponseRedirect('/login')
    except Exception as e:
        print('Exception:', e)
        return render(request, '500.html')
