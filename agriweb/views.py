from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    context={
        'title' : 'Farmer'
    }
    return render(request, 'pages/index.html', context)
# Create your views here.
def supplier(request):
    context={
        'title' : 'Supplier'
    }
    return render(request, 'pages/business.html', context)
# Create your views here.
def blog(request):
    context={
        'title' : 'Blog'
    }
    return render(request, 'pages/business.html', context)
# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail

def send_test_email(email_message, email):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # SMTP sunucusuna bağlan
    server = smtplib.SMTP('mail.kurumsaleposta.com', 587)
    server.starttls()  # TLS'yi başlat

    # Giriş yap
    server.login('info@agriknow.com.tr', 'PApatyam.3578')

    # Mesajı oluştur
    msg = MIMEMultipart()
    msg['From'] = 'info@agriknow.com.tr'
    msg['To'] = email
    msg['Subject'] = 'Agriknow'

    # Mesaj içeriği
    body = email_message
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # E-postayı gönder
    server.send_message(msg)

    # Bağlantıyı kapat
    server.quit()

def contact(request):
    context = {'title': 'Contact'}

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")  # Mesaj verisini alın

        try:
            # İletişim kaydını oluştur
            Contact.objects.create(full_name=name, email=email, phone=phone, message=message, sender="Business")

            success_message = "Başarıyla kaydedildiniz!"
            context['success_message'] = success_message

            email_message = f'Sn. {name} Mesajınız bize ulaştı. Gerekli incelemeleri yapıp en kısa sürede size ulaşacağız.'
            send_test_email(email_message, email)

        except Exception as e:
            context['error_message'] = "Kayıt işlemi sırasında bir hata oluştu. Lütfen daha sonra tekrar deneyin."

    return render(request, 'pages/contact.html', context)

def farmercontact(request):
    context = {'title': 'Contact'}

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")  # Mesaj verisini alın

        try:
            # İletişim kaydını oluştur
            Contact.objects.create(full_name=name, email=email, phone=phone, message=message, sender="Farmer")

            success_message = "Başarıyla kaydedildiniz!"
            context['success_message'] = success_message

            email_message = f'Sn. {name} Mesajınız bize ulaştı. Gerekli incelemeleri yapıp en kısa sürede size ulaşacağız.'
            send_test_email(email_message, email)
            return redirect('index')
        except Exception as e:
            context['error_message'] = "Kayıt işlemi sırasında bir hata oluştu. Lütfen daha sonra tekrar deneyin."


    return render(request, 'pages/contact.html', context)


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Subscribe

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:  # Emailin boş olup olmadığını kontrol et
            Subscribe.objects.create(email=email)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))  # Geri döneceği URL

