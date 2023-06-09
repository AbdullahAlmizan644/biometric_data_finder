from django.shortcuts import render,HttpResponse,redirect
from .forms import PersonDataForm,FaceImageForm
import face_recognition
from .models import PersonData
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"face/index.html",context={

    })


def user_data(request):
    if request.method=="POST":
        form=PersonDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    
    else:
        form =PersonDataForm()

    return render(request,"face/person_data.html",{
        "form":form,
    })



def face_search(request):
    if request.method=="POST":
        form=FaceImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.cleaned_data['image']
            print(image)
            unknown_image = face_recognition.load_image_file(f"/home/rtr/Pictures/{image}",)


            # unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            try:
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

            except IndexError:
                messages.error(request,"Please give a person image not any fictional object")
                return redirect(face_search)

            print(unknown_encoding)

            user_data=PersonData.objects.all()

            for data in user_data:
                print(data.person_face_image.url)
                known_image = face_recognition.load_image_file(f"/home/rtr/biometric_data_finder/{data.person_face_image.url}")
                known_encoding = face_recognition.face_encodings(known_image)[0]
                print(f"known_encoding{data.id}: {known_encoding}")
                results = face_recognition.compare_faces([known_encoding], unknown_encoding)
                print(f"result{data.id}:{results}")

                if results[0]==True:
                    match_data=data
                    messages.success(request,f"The {data.last_name} face matched with your image face")
                    print("Matched")
                    return render(request,"face/person_details.html",{
                                        "match_data":match_data,
                                    })
                    
                
                else:
                    print("not matched")
            
            messages.error(request,"Sorry The person you want is not available in our database")


            return redirect("face_search")
        
    else:
        form=FaceImageForm()
        
    return render(request,"face/face_search.html",{
        'form':form,
    })



def person_details(request):
    return render(request,"face/person_details.html")