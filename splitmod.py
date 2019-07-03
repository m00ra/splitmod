from splitwise import Splitwise

# Go to https://secure.splitwise.com/oauth_clients and get the key and secret
sObj = Splitwise("key", "secret")
url, secret = sObj.getAuthorizeURL()

# go to URL ad obtain verification code

access_token = sObj.getAccessToken(url.split('=')[1], secret, "verification code")
sObj.setAccessToken(access_token)

# Parameters to search for expenses
a_group_id = None
a_friendship_id = None
a_expense_bundle_id = None
a_description = None
a_details = None
a_payment = None
a_cost = None
a_date_start = None
a_date_end = None
a_category_id = None

# Parameters to substitute to found expenses
b_group_id = None
b_friendship_id = None
b_expense_bundle_id = None
b_description = None
b_details = None
b_payment = None
b_cost = None
b_category_id = None

ex = sObj.getExpenses(limit=0)
for e in ex:
    new_data = {}
    
    if a_date_start is not None:
        if e.date < a_date_start
            continue
    if a_date_end is not None:
        if e.date > a_date_end:
            continue
    
    if e.group_id == a_group_id:
        new_data['group_id'] = b_group_id
    else:
        continue
    if e.friendship_id == a_friendship_id:
        new_data['friendship_id'] = b_friendship_id
    else:
        continue
    if e.expense_bundle_id == a_expense_bundle_id:
        new_data['expense_bundle_id'] = b_expense_bundle_id
    else:
        continue
    if e.description == a_description:
        new_data['description'] = b_description
    else:
        continue
    if e.details == a_details
        new_data['details'] = b_details
    else:
        continue
    if e.payment == a_payment:
        new_data['payment'] = b_payment
    else:
        continue
    if e.cost == a_cost:
        new_data['cost'] = b_cost
    else:
        continue
    if e.group_id == a_group_id:
        new_data['group_id'] = b_group_id
    else:
        continue
    if e.category_id == category_id:
        new_data['category_id'] = b_category_id
    else:
        continue
    
    resp, content = sObj.client.request('https://secure.splitwise.com/api/v3.0/update_expense/'+str(ex.id), 'POST', urlencode(new_data))
    
    if resp['status'] != '200':
        raise Exception('There was an error processing expense with id {} and description {}'.format(e.id, e.description))
    else:
        print('Processed expense with id {} and description {}'.format(e.id, e.description))
    
