from django.shortcuts import render

def home _page(request):

	if request.method == 'POST':
		item = request.POST.get('item')
		address = request.POST.get("address")

		return render(request, 'taobao/home_page.html',{'item':item,'address':address})

	return render(request,'taobao/home_page.html')	 		
# Create your views here.
