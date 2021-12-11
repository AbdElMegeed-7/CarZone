from django.shortcuts import render


def cars(request):
    return render(request, 'cars/cars.html')
  
  
def car_detail(request, id):
    return render(request, 'cars\car_detail.html')