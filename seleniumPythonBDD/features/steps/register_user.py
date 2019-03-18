# coding=utf-8
import sys
sys.path.append("E:/coding/yangqin/pythonAuto")
from behave import *
use_step_matcher("re")
from seleniumPythonBDD.features.lib.pages.register_page import RegisterPage

@When(u'I open the register website "([^"]*)"')
def step_register(context, url):
    RegisterPage(context).get_url(url)


@Then(u'I expect that the title is "([^"]*)"')
def step_register(context, title_name):
    title = RegisterPage(context).get_title()
    assert title_name in title


@When(u'I set with email "([^"]*)"')
def step_register(context, email):
    RegisterPage(context).send_email(email)
    # context.driver.find_element_by_id("register_email").send_keys(email)


@When(u'I set with username "([^"]*)"')
def step_register(context, username):
    # context.driver.find_element_by_id("register_nickname").send_keys(username)
    RegisterPage(context).send_username(username)


@When(u'I set with password "([^"]*)"')
def step_register(context, password):
    RegisterPage(context).send_password(password)
    # context.driver.find_element_by_id("register_password").send_keys(password)


@When(u'I set with code "([^"]*)"')
def step_register(context, code):
    # context.driver.find_element_by_id("captcha_code").send_keys(code)
    RegisterPage(context).send_code(code)

@When(u'I click with registerBtn')
def step_register(context):
    # context.driver.find_element_by_id("register-btn").click()
    RegisterPage(context).click_register_btn()

@Then(u'I expect that text "([^"]*)"')
def step_register(context,expectResult):
    # actual_result=context.driver.find_element_by_id("captcha_code-error").text
    actual_result=RegisterPage(context).get_code_err_text()
    assert actual_result in expectResult
