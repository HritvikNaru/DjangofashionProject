from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ContactForm,Stocks,Cart,Orders
from .serializers import contactformSerializer
from rest_framework.renderers import JSONRenderer
import json
from django.views import View



# Create your views here.

# variables for testing
nm="manvi"
idn=6 

class Shopping(View):
    def get(self,request):
        all_objects= Stocks.objects.all()
        list=all_objects.values()
        return render(request,"coursetemplates/shopping.html",{'list1':list,'name':nm})

    def post(self,request):
        post=Cart()
        stock_idval= request.POST.get('addcart')
        post.stock= Stocks.objects.get(id=stock_idval)
        post.cus= ContactForm.objects.get(id=idn)
        post.save()
                
        return redirect('/shopping')  



#adding the stocks to cart



class Cartpage(View):
    def get(self,request):
        id_set=[]
        allcartobjects= Cart.objects.filter(cus_id=idn)
        list=allcartobjects.values()
        for i in list:
            id_set.append(i['stock_id'])
        # print("ser::", list[0]['id'])
        print("set::",id_set)
        objects = Stocks.objects.filter(id__in=id_set)
        list1=objects.values()
        print(list1)
        # print("data::", data)
    
        return render(request,"coursetemplates/cart.html",{'list1':list1,'name':nm})




    def post(self,request):
        if request.POST.get("placeorder") == "placeorder":
            post=Orders()
            allobj=Cart.objects.filter(cus_id=idn)
            for i in allobj.values():
                post=Orders()
                print(i)
                post.stock= Stocks.objects.get( id=i['stock_id'])
                post.cus= ContactForm.objects.get(id=idn) 
                post.save()
            Cart.objects.filter(cus_id=idn).delete()
            return redirect("/orders")
         
            #Handle Elements from first Form
        else:
            delid=request.POST.get('deletecart')
            print(delid)
            Cart.objects.filter(stock_id=delid).delete()
            return redirect('/cart')  
        # return redirect('/shopping') 
    
            #Handle Elements from second Form



#Deleting the cart

class Registerpage(View):
    def get(self,request):
        return render(request,"coursetemplates/register.html")
    def post(self,request):
        post=ContactForm()
        post.fname= request.POST.get('Fname')
        post.lname= request.POST.get('Lname')
        post.number= request.POST.get('Mobileno')
        post.email= request.POST.get('email')
        post.password= request.POST.get('Password')
        post.Address= request.POST.get('address')

        post.save()
                
        return redirect('/register')  

        


#Displaying the orders
class Orderspage(View):
    def get(self,request):
        id_set=[]
        allorderedobjects= Orders.objects.filter(cus_id=idn)
        list=allorderedobjects.values()
        for i in list:
            id_set.append(i['stock_id'])
        # print("ser::", list[0]['id'])
        print("set::",id_set)
        objects = Stocks.objects.filter(id__in=id_set)
        list1=objects.values()
        print(list1)
        # print("data::", data)
        return render(request,"coursetemplates/orders.html",{'list1':list1,'name':nm})
        




def learn_django (request):
    return HttpResponse("<h1> hello django course</h1>")


# contact details fetched here and can be used for signin


class Details(View):
    def get(self,request):
         return render(request,"coursetemplates/signin.html")



    def post(self,request):
        emaildata= request.POST.get('email')
        stu=ContactForm.objects.get(email=emaildata)   #model object created(complex) 
        serializer = contactformSerializer(stu) #converted to python object
        json_data = JSONRenderer().render(serializer.data) #python to json 
        resp = json.loads(json_data)
        print(resp['fname'])
        global nm
        global idn
        print(stu.id)
        nm=resp['fname']
        idn=stu.id
        return render(request,"coursetemplates/index.html",{'name':nm})






