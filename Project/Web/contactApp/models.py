from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models.signals import post_init, post_save
from django.dispatch import receiver
from django.core.mail import send_mail

import os
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Mm, Inches, Pt


# Create your models here.
# Which worker we need
class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='Recruiting Position')
    description = models.TextField(verbose_name='Position required')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='update date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ADs'
        verbose_name_plural = 'ADs'
        ordering = ('-publishDate', )


class Resume(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    personID = models.CharField(max_length=30, verbose_name='ID')
    sex = models.CharField(max_length=5, default='Male', verbose_name='sex')
    email = models.EmailField(max_length=30, verbose_name='email')
    birth = models.DateField(max_length=20,
                             default=datetime.strftime(datetime.now(),
                                                       "%Y-%m-%d"),
                             verbose_name='date of birth')
    edu = models.CharField(max_length=5, default='bachelor', verbose_name='Education Level')
    school = models.CharField(max_length=40, verbose_name='School')
    major = models.CharField(max_length=40, verbose_name='Major')
    position = models.CharField(max_length=40, verbose_name='Apply')
    experience = models.TextField(blank=True,
                                  null=True,
                                  verbose_name='experience')
    photo = models.ImageField(upload_to='contact/recruit/%Y_%m_%d',
                              verbose_name='personal photo')
    grade_list = (
        (1, 'quering'),
        (2, 'Passed'),
        (3, 'Not passed'),
    )
    status = models.IntegerField(choices=grade_list,
                                 default=1,
                                 verbose_name='Interview result')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='Update time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resume'
        ordering = ('-status', '-publishDate')


@receiver(post_init, sender=Resume)
def before_save_resume(sender, instance, **kwargs):
    instance.__original_status = instance.status


@receiver(post_save, sender=Resume)
def post_save_resume(sender, instance, **kwargs):
    email = instance.email  # Applicator's email
    EMAIL_FROM = 'xxxxxxxx@gmail.com'  # orginazation email

    if instance.__original_status == 1 and instance.status == 2:
        email_title = 'Announcement: H2H recruitment preliminary results'
        email_body = 'Congratulations on your passing the first test of this public welfare organization'
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

        template_path = os.getcwd() + '/media/contact/recruit.docx'  #template file
        template = DocxTemplate(template_path)
        # 从instance实例中获取当前简历字段信息
        # Gets the current resume field information from the instance instance
        name = instance.name
        personID = instance.personID
        sex = instance.sex
        email = instance.email
        birth = instance.birth
        edu = instance.edu
        school = instance.school
        major = instance.major
        position = instance.position
        experience = instance.experience
        photo = instance.photo

        context = {
            'name': name,
            'personID': personID,
            'sex': sex,
            'email': email,
            'birth': birth,
            'edu': edu,
            'school': school,
            'major': major,
            'position': position,
            'experience': experience,
            'photo': InlineImage(template, photo, width=Mm(30), height=Mm(40)),
        }
        template.render(context)
        filename = '%s/media/contact/recruit/%s_%d.docx' % (
            os.getcwd(), instance.name, instance.id)
        template.save(filename)

    elif instance.__original_status == 1 and instance.status == 3:
        email_title = 'Announcement: H2H recruitment preliminary results'
        email_body = 'It is a pity that you failed the initial examination of this public welfare organization. Thank you for your attention'
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])