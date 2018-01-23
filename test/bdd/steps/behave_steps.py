from behave import *
from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp
from bank.account import Account
from bank_app import app, BANK


@given(u'I create account "{account_number}" with balance of "{balance}"')
def step_impl(context, account_number, balance):
    a = Account(account_number, balance)
    BANK.add_account(a)
    
@given(u'I visit homepage')
def step_impl(context):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)

@when(u'I enter the account number "{account_number}"')
def step_impl(context, account_number):
    form = world.response.forms['account-form']
    form['account_number'] = account_number
    world.form_response = form.submit()
    assert_equal(world.form_response.status_code, 200)

@then(u'I see a balance of "{expected_balance}"')
def step_impl(context, expected_balance):
    assert_in("Balance: {}".format(expected_balance), world.form_response.text)

@given(u'I create the following account')
def step_impl(context):
        for row in context.table:
    		a = Account(row['account_number'], row['balance'])
    		BANK.add_account(a)