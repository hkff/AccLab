
Feature: showing off behave

  Scenario: run a simple test
    Given a clause r1
    And allow bob to use read service provided by alice on data
    And allow bob to read data on alice
    When we finish the program
    Then we run it


#  Scenario: kim preference
#      Given permit kim to write d on cloudX
#      And permit sandra to write d on cloudX
#      And permit sandra to write d on cloudX
#      Then we calculate the result of 5 + 5
#    FORALL d:data WHERE d.subject == kim
#    FORALL a:agent
#    PERMIT kim.read[cloudX](d)
#    AND PERMIT kim.read[cloudX](d)
#    AND PERMIT kim.write[cloudX](d)
#    AND PERMIT kim.delete[cloudX](d)
#    AND PERMIT cloudX.sensors[kim](d)
#    AND cloudX.delete[d]() BEFORE "2 Years"
#    AND IF(a.read[cloudX](d)) THEN (MUST(cloudX.notify[kim]()))
#    AUDITING leslie.audit[cloudS]()
#    IF_VIOLATED_THEN MUST(leslie.sanction[cloudX]() AND cloudX.delete[d]())
