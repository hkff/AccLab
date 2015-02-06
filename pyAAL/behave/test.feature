
Feature: showing off behave

  Scenario: run a simple test
     Given we declare a variable x with a value 5
      And  we declare a variable y with a value 6
      And  we calculate the result of x + y
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
