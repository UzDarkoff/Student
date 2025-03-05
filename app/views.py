from django.shortcuts import render,redirect
import qrcode
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from .models import Student , Fan
from .forms import *
def home(request):
    students=Student.objects.all()
    fanlar=Fan.objects.all()
    context={
        "students":students,
        "fanlar":fanlar,
        "title":"Title"
    }
    return render(request,'home.html',context=context)

def fan(request,fan_id):
    students=Student.objects.filter(fan_id=fan_id)
    fanlar=Fan.objects.all()
    context={
        "students":students,
        "fanlar":fanlar
    }
    return render(request,'fan.html',context=context)




def student_about(request, student_id):
    student = Student.objects.get(pk=student_id)


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.full_name}.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)


    width, height = A4


    p.setFont("Helvetica-Bold", 18)
    p.drawString(100, height - 100, f"Talaba: {student.full_name}")

    p.setFont("Helvetica", 14)
    p.drawString(100, height - 130, f"Email: {student.email}")
    p.drawString(100, height - 160, f"Manzil: {student.address}")


    qr_data = "https://t.me/NajotTalim"
    qr = qrcode.make(qr_data)

    qr_buffer = BytesIO()
    qr.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)

    qr_image = ImageReader(qr_buffer)


    p.drawImage(qr_image, width - 180, height - 250, width=100, height=100)

    p.showPage()
    p.save()
    buffer.seek(0)
    response.write(buffer.read())

    return response


def add_student(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            students=Student.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form=StudentForm()
    return render(request,'add_student.html',{'form':form})

def add_fan(request):
    if request.method=='POST':
        form=FanForm(request.POST)
        if form.is_valid():
            fan=Fan.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form=FanForm()
    return render(request,'add_fan.html',{'form':form})