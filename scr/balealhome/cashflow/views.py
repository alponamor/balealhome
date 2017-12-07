from django.shortcuts import render, render_to_response, redirect


# Create your views here.
def hi_page(request):
    LANGUAGE_CODE = 'pt'
    if request.user.is_authenticated():
        return redirect('account_profile')
    return render_to_response('cashflow/index.html') #стартовая страница

def account_profile(request):
    if not request.user.is_authenticated(): # если не авторизован - нах!
        return redirect('hi_page')
    am = request.user.email
#    accomodations=Accomodation.objects.filter(admin = admin_name).order_by('name')
#    accomodations=Accomodation.objects.filter().order_by('name')
#def post_list(request):
#    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/post_list.html', {'posts':posts})
#    return render_to_response('account_controls.html', {'am': am, 'accomodations': accomodations,} ) #стартовая страница администратора
    return render_to_response('cashflow/account_profile.html', {'am': am} ) #стартовая страница администратора
