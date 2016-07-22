from openpyxl import load_workbook

from django.http import *
from django.shortcuts import render,redirect
from django.template import RequestContext

def new_user_account(request):
    username = password = ''
    form = UserCreationForm
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']

        try:
            validate_email(email)
            valid_email = True
        except:
            valid_email = False
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            wg = Workgroup.objects.get(name="Demonstration Workgroup")
            wg.viewers.add(new_user)
            
            from django.core.mail import send_mail

            send_mail(
                "New Aristotle registry user!",
                "A new user [%s] has signed up on the Aristotle Demo Registry" % (username),
                "Aristotle Accounts <account-creation@mg.aristotlemetadata.com>",
                ["theodore.therone@gmail.com",
                #"Michael.Cohen@thinkplace.com.au"
                ]
            )

            email_context = {
                'link': request.build_absolute_uri('/'),
                'user':new_user
            }
            print email_context
            body_html = render_to_string("registration_new/password_reset_email.html", email_context)
            body_txt = render_to_string("registration_new/password_reset_email.txt", email_context)

            email = EmailMultiAlternatives(
                "Welcome to the Aristotle Metadata Registry",
                body_txt,
                reply_to=["Lauren Eickhorst <lauren@aristotlemetadata.com>"],
                from_email="Lauren Eickhorst <lauren@mg.aristotlemetadata.com>",
                to=[new_user.email],
            )
            email.attach_alternative(body_html, "text/html")
            email.send()

            return redirect("/new_account/success")
            return password_reset(request, is_admin_site=False, 
                template_name='registration_new/new_account.html',
                email_template_name='registration_new/password_reset_email.txt',
                html_email_template_name='registration_new/password_reset_email.html',
                subject_template_name='registration_new/password_reset_subject.txt',
                post_reset_redirect="/new_account/success")

    return render(request, 'registration_new/new_account.html', {
        'form': form,
    })
