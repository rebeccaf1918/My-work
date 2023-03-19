def do_view(students):
    for student in students:
        print (student["name"])
        for module in student["modules"]:
            print("\t", module["name"], "\t:", module["grade"])
