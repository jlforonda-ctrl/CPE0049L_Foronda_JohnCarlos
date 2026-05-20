Feature: Student Enrollment Clearance

Scenario: Student has pending library fees
    Given a student with ID "A20241001" exists
    And the student has a pending "Library" fee of 500 pesos
    When the enrollment clearance system checks the student
    Then the clearance status should be "Rejected"
    And the reason should include "Library"

Scenario: Student has no pending liabilities
    Given a student with ID "A20241002" exists
    And the student has no pending liabilities
    When the enrollment clearance system checks the student
    Then the clearance status should be "Approved"