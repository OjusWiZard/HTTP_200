from .models import EmailDetail
from profiles.models import StudentDetail, FacultyDetail
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin
from django.views.generic import View
from django.core.urlresolvers import reverse
from notices.decorators import student_profile_complete, default_password_change
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmailForm

import xlsxwriter


class StudentEmailForm(LoginRequiredMixin, View):

    @method_decorator(default_password_change)
    @method_decorator(student_profile_complete)
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        details = StudentDetail.objects.get(user=user)
        try:
            email_data = EmailDetail.objects.get(user=user)
            if email_data:
                return render(request, 'email/studentemailform.html', {"user": user, "details": details, "email_data": email_data})
        except BaseException:
            return render(request, 'email/studentemailform.html', {"user": user, "details": details})

    def post(self, request):
        user = User.objects.get(username=request.user.username)

        try:
            email_data = EmailDetail.objects.get(user=user)
            email_form = EmailForm(request.POST, request.FILES, instance=email_data)
        except BaseException:
            email_form = EmailForm(request.POST, request.FILES)

        if email_form.is_valid():
            email_form = email_form.save(commit=False)
            email_form.user = user
            email_form.save()
            messages.success(request, "Successfully Registered for Email")
            return HttpResponseRedirect(reverse("relevent-notice-list"))
        else:
            print email_form.errors
            messages.error(request, "Enter Valid data in the form.")
            return HttpResponseRedirect(reverse("student-email"))


class email_excel_writer(LoginRequiredMixin, View):
    def get(self, request):
        '''
        Custom class to download Xls File .
        '''

        workbook = xlsxwriter.Workbook("email_details.xls")
        worksheet = workbook.add_worksheet()
        email = EmailDetail.objects.all()
        bold = workbook.add_format({'bold': True})
        worksheet.set_column(1, 160, 7)
        columns = ["Username", "First Name", "Last Name", "Course", "Branch", "Year", "Purpose for Email", "Attachment", "Date Applied"]
        row = 0
        for i, elem in enumerate(columns):
            worksheet.write(row, i, elem, bold)

        row += 1
        for users in email:
            print users
            date_registered = str(users.created).split(' ')[0]
            try:
                user = User.objects.get(username=users.user)
                student = StudentDetail.objects.get(user=user)
                worksheet.write(row, 0, user.username)
                worksheet.write(row, 1, user.first_name)
                worksheet.write(row, 2, user.last_name)
                worksheet.write(row, 3, student.course)
                worksheet.write(row, 4, student.branch)
                worksheet.write(row, 5, student.year)
                worksheet.write(row, 6, users.email_purpose)
                worksheet.write(row, 7, users.attachment.url)
                worksheet.write(row, 8, date_registered)
                row += 1
            except BaseException:
                user = User.objects.get(username=users.user)
                faculty = FacultyDetail.objects.get(user=user)
                worksheet.write(row, 0, user.username)

        workbook.close()
        response = HttpResponse(file("email_details.xls"))
        response['Content-Type'] = "application/vnd.ms-excel"
        response['Content-Disposition'] = 'attachment; filename="email_details.xls"'
        return response