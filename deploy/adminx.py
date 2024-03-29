# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from models import Deploy
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction

from xadmin.sites import site
from xadmin.views.base import CommAdminView, ModelAdminView, filter_hook, csrf_protect_m
from django.views.decorators.cache import never_cache
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode, smart_unicode
from django import forms

import pprint

from django.utils.safestring import mark_safe
from xadmin.views.page import PageView, FormPage
from django.contrib import messages

import os

class TestPage1(PageView):
    verbose_name = u'PageView1(基本)'
    app_label = 'app'
    menu_group = 'test_group'

    def get_content(self):
        return 'OK'

site.register_page(TestPage1)

class TestPage2(PageView):
    verbose_name = u'PageView2(带ajax页链接)'
    app_label = 'app'
    menu_group = 'test_group'
    
    def get_media(self):
        media = self.vendor('xadmin.plugin.quick-form.js', 'xadmin.form.css')
        return media
    
    def get_content(self):
        return mark_safe('<a data-refresh-url="/page/testpage2/" href="/page/testpage1" class="ajaxform-handler" title="测试AjaxForm">GO</a>') 
site.register_page(TestPage2)


class TestPage3(PageView):
    verbose_name = u'PageView3(bootstrap常用)'
    app_label = 'app'
    menu_group = 'test_group'
    template = 'bootstrap.html'
    
site.register_page(TestPage3)


class MyForm(forms.Form):
    account = forms.IntegerField(label=u'选择账户', required=True)
    charge_time = forms.DateField(label=u'支付时间', required=True, widget=xadmin.widgets.DateWidget)
    test = forms.MultipleChoiceField(choices=[('a','a'),('b','b')],help_text='按住Ctrl键多选')
    #test2 = forms.MultiSelectFormField(choices=[('a','aaaa'),('b','bbbb'),('c','cccc'),('d','dddd')])


class FormPage1(FormPage):
    app_label = 'app'
    menu_group = 'test_group'
    verbose_name = 'FormPage1'
    form = MyForm
    
    def get_nav_btns(self):
        return [
                 '<a href="/xadmin/page/tags/?_q_=id_desc" class="btn btn-primary"><i class="fa fa-refresh"></i> 查看最新标签</a>',
                 '<a href="/xadmin/page/tags/?_q_=vtalk_c_50" class="btn btn-primary"><i class="fa fa-filter"></i> 精华话题大于50</a>',
                 '<a href="/xadmin/page/tags/?_q_=vtalk_c_100" class="btn btn-primary"><i class="fa fa-filter"></i> 精华话题大于100</a>',
                 '<a href="/xadmin/page/addtag/?_redirect=/xadmin/page/tags/" class="btn btn-primary"><i class="fa fa-plus"></i> 新增 标签</a>',
               ]
        
    def save_forms(self):
        print self.form_obj.cleaned_data

site.register_page(FormPage1)


class TForm(forms.Form):
    input = forms.CharField(label='please input', max_length=60)
    res = forms.CharField(widget=forms.HiddenInput(), required=False)
    #res = forms.CharField(label=u'执行结果：', widget=forms.Textarea(attrs={'readonly':'readonly'}), required=False)


class MyAdminView(FormPage):
    app_label = 'app'
    verbose_name = 'MyFormPage1'
    form = TForm
    #form.fields['res'].widget = forms.HiddenInput()
    #print dir(form.hidden_fields)

    #def message_user(self, message, level='info'):
    #    """
    #    Send a message to the user. The default implementation
    #    posts a message using the django.contrib.messages backend.
    #    """
    #    if hasattr(messages, level) and callable(getattr(messages, level)):
    #        getattr(messages, level)(self.request, message)

    def save_forms(self):
        print dir(self.form_obj)
        #print self.form_obj.as_table()
        #print self.form_obj.cleaned_data
        #print self.form_obj.initial
        ss = os.popen("""python scripts/test.py""").read()
        #print ss
        self.form_obj.fields['res'] = forms.CharField(label=u'执行结果', widget=forms.Textarea(attrs={'readonly':'readonly'}))
        self.form_obj.cleaned_data['res'] = 234
        print self.form_obj.files.values()
        print self.form_obj.cleaned_data
        #self.message_user(ss)

site.register_page(MyAdminView)


class Ansible(CommAdminView):
    #verbose_name = 'ansible'
    title = _(u"ansible")
    icon = None

    def get_page_id(self):
        return self.request.path

    def get_portal_key(self):
        return "dashboard:%s:pos" % self.get_page_id()

    @filter_hook
    def get_title(self):
        return self.title

    @filter_hook
    def get_context(self):
        new_context = {
            'title': self.get_title(),
            'icon': self.icon,
            'portal_key': self.get_portal_key(),
            'content': "aaa",
            'breadcrumbs': self.get_breadcrumb(),
            #'columns': [('col-sm-%d' % int(12 / len(self.widgets)), ws) for ws in self.widgets],
            #'has_add_widget_permission': self.has_model_perm(UserWidget, 'add') and self.widget_customiz,
            #'add_widget_url': self.get_admin_url('%s_%s_add' % (UserWidget._meta.app_label, UserWidget._meta.model_name)) +
            #"?user=%s&page_id=%s&_redirect=%s" % (self.user.id, self.get_page_id(), urlquote(self.request.get_full_path()))
        }
        context = super(Ansible, self).get_context()
        context.update(new_context)
        print context
        return context

    @filter_hook
    def get_breadcrumb(self):
        bcs = super(Ansible, self).get_breadcrumb()
        item = {'title': self.get_title()}
        bcs.append(item)
        return bcs

    @never_cache
    def get(self, request, *args, **kwargs):
        return self.template_response('ansible.html', self.get_context())

site.register_view(r'^ansible/$', Ansible, name='ansible')


class DeployAdmin(object):
    list_display = ('name', 'deploy_time', 'version', 'disconf', 'lts', 'mq', 'description')
    list_editable = ('deploy_time', 'version', 'description')
    list_display_links = ('name',)
    show_detail_fields = ("description")
    show_all_rel_details = ("xxxxx")
    relfield_style = 'fk-ajax'
    wizard_form_list = [
        ('First\'s Form', ('name', 'deploy_time', 'version', 'description')),
        ('Second Form', ('db', 'disconf', 'lts', 'mq')),
#        ('Thread Form', ('customer_id',))
    ]

    search_fields = ['name']
    relfield_style = 'fk-ajax'
    reversion_enable = True

#    actions = [BatchChangeAction, ]
#    batch_fields = ('contact', 'create_time')

site.register(Deploy, DeployAdmin)
