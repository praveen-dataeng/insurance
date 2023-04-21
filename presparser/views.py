from django.shortcuts import render
from .forms import UploadFileForm
from presparser.extractor import extractor
from django.views import View
import os

# Class Based Views:
class Home(View):
     form_class = UploadFileForm
     initial = {"key": "value"}
     template_name = 'presparser/home.html'
     
     def get(self, request, *args, **kwargs):
         form = self.form_class(initial=self.initial)
         return render(request, self.template_name, {"form": form})         
     
     def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
                handle_uploaded_file(request.FILES["file"])
                if 'prescription' in request.POST:
                    # def prescription(request):    
                    pp = extractor('static/upload/uploaded.pdf', 'prescription')
                    pp = {'prescription': pp}
                    for k,v in pp.items():
                        template_name = 'presparser/prescription.html'
                        prescription = v
                        return render(request, template_name,  {'v': prescription})
                        # return HttpResponse(f"{prescription}\n")
                if 'patientdetail' in request.POST:
                    # def patientdetails(request):
                    patient_details = extractor('static/upload/uploaded.pdf', 'patient_details')
                    patient_details = {'prescription': patient_details}
                    for k,v in patient_details.items():
                        template_name = 'presparser/patientdetails.html'
                        prescription = v
                        return render(request, template_name,  {'v': prescription})
                        # return HttpResponse(f"{prescription}\n")

                    # return render(request, "presparser/home.html", {"form": form})
        else:
            form = UploadFileForm()
            file_path = 'static/upload/'
            if os.path.isfile(file_path):
                os.remove(file_path)       
        return render(request, "presparser/home.html", {"form": form})
         
def handle_uploaded_file(f):
    ext = f.name.split('.')[-1]
    with open("static/upload/"+"%s.%s" % ('uploaded', ext), "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)



# def home(request):
#         if request.method == 'POST':
#             form = UploadFileForm(request.POST, request.FILES)
#             if form.is_valid():
#                 handle_uploaded_file(request.FILES["file"])
#                 if 'prescription' in request.POST:
#                     def prescription(request):    
#                         pp = extractor('static/upload/uploaded.pdf', 'prescription')
#                         pp = {'prescription': pp}
#                         for k,v in pp.items():
#                             prescription = v
#                             return render(request, 'presparser/prescription.html',  {'v': prescription})
#                             # return HttpResponse(f"{prescription}\n")
#                 if 'patientdetail' in request.POST:
#                     def patientdetails(request):
#                         pp = extractor('static/upload/uploaded.pdf', 'patient_details')
#                         pp = {'prescription': pp}
#                         for k,v in pp.items():
#                             prescription = v
#                             return render(request, 'presparser/patientdetails.html',  {'v': prescription})
#                             # return HttpResponse(f"{prescription}\n")

#                     # return render(request, "presparser/home.html", {"form": form})
#         else:
#             form = UploadFileForm()
#             file_path = 'static/upload/'
#             if os.path.isfile(file_path):
#                 os.remove(file_path)       
#         return render(request, "presparser/home.html", {"form": form})
