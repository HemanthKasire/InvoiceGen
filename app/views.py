from django.shortcuts import render
from .models import producat, seller, buyer
import datetime
import time

def index(request):
    pro = producat.objects.all()
    slr = seller.objects.all()
    return render(request, 'index.html', {'products': pro, 'seller': slr})

def buy(request, pk):
    print(pk)
    pro = producat.objects.get(pk=pk)

    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        quantity = int(request.POST['quantity'])
        
        by = buyer(name=name, address=address, phone=phone)
        by.save()

        # Fetch the relevant seller associated with the product
        relevant_seller = pro.seller

        amount = float(pro.price)
        bid = int(round(time.time() * 1000))
        pn = pro.name
        dis = pro.dis
        current_time = datetime.datetime.now()
        price = amount
        pro_quantity = quantity
        gst = (amount * quantity)*0.05
        pro_total = (amount * quantity) + gst

        data = {
            'pname': pn,
            'pprice': price,
            'bname': name,
            'baddress': address,
            'bphone': phone,
            'pdis': dis,
            'pquantity': pro_quantity,
            'ptotal': pro_total,
            'tax': gst,
            'product_date': current_time,
            'id': bid,
        }

        return render(request, 'pdf.html', {'data': data, 'seller': [relevant_seller]})

    return render(request, 'buy.html')

def pdf(request):
    slr = seller.objects.all()
    return render(request, 'pdf.html', {'seller': slr})
