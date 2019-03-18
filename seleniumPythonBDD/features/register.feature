# coding=utf-8

Feature:Register User

    As a developer
    This is my first bdd project

    Scenario:open register website
        When I open the register website "http://www.5itest.cn/register"
        Then I expect that the title is "注册"

    Scenario:input username
        When I set with email "testBdd@163.com"
        And I set with username "testBdd"
        And I set with password "12345678"
        And I set with code "2222"
        And I click with registerBtn
        Then I expect that text "验证码错误"