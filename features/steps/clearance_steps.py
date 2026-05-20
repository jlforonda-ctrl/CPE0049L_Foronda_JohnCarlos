from behave import given, when, then

# Rapid Prototype Data Store
mock_database = {}
current_student_id = None
clearance_result = None

@given('a student with ID "{student_id}" exists')
def step_impl(context, student_id):
    global current_student_id
    current_student_id = student_id
    mock_database[student_id] = {"liabilities": []}

@given('the student has a pending "{dept}" fee of {amount} pesos')
def step_impl(context, dept, amount):
    mock_database[current_student_id]["liabilities"].append(dept)

@given('the student has no pending liabilities')
def step_impl(context):
    mock_database[current_student_id]["liabilities"] = []

@when('the enrollment clearance system checks the student')
def step_impl(context):
    global clearance_result
    liabilities = mock_database[current_student_id]["liabilities"]
    
    if len(liabilities) > 0:
        clearance_result = {"status": "Rejected", "reason": liabilities}
    else:
        clearance_result = {"status": "Approved", "reason": []}

@then('the clearance status should be "{expected_status}"')
def step_impl(context, expected_status):
    assert clearance_result["status"] == expected_status

@then('the reason should include "{expected_reason}"')
def step_impl(context, expected_reason):
    assert expected_reason in clearance_result["reason"]