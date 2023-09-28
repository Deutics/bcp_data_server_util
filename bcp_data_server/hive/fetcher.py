from ..fetcher import DataFetcherMain


class DataFetcher:
    class Profile(DataFetcherMain):
        _dates = ['admission_date', 'left_date', 'last_present_date']
        _endpoint = "/profile"

    class EmployeeRole(DataFetcherMain):
        _dates = []
        _endpoint = "/employee_roles"

    class EmployeeProfile(DataFetcherMain):
        _dates = []
        _endpoint = "/employees"

    class Branch(DataFetcherMain):
        _dates = []
        _endpoint = "/branches"

    class Section(DataFetcherMain):
        _dates = []
        _endpoint = "/sections"

    class TeacherGroups(DataFetcherMain):
        _dates = []
        _endpoint = "/teacher_groups"

    class Months(DataFetcherMain):
        _dates = []
        _endpoint = "/months"

    class Priorities(DataFetcherMain):
        _dates = []
        _endpoint = "/priorities"

    class SchoolGroups(DataFetcherMain):
        _dates = []
        _endpoint = "/school_groups"

    class UserWings(DataFetcherMain):
        _dates = []
        _endpoint = "/user_wings"

    class Wings(DataFetcherMain):
        _dates = []
        _endpoint = "/wings"

    class Sections(DataFetcherMain):
        _dates = []
        _endpoint = "/sections"

    class Classes(DataFetcherMain):
        _dates = []
        _endpoint = "/classes"

    class EmergencyContacts(DataFetcherMain):
        _dates = []
        _endpoint = "/emergency_contacts"

    class Employees(DataFetcherMain):
        _dates = []
        _endpoint = "/employees"

    class EmployeeRoles(DataFetcherMain):
        _dates = []
        _endpoint = "/employee_roles"

    class EmployeeScope(DataFetcherMain):
        _dates = []
        _endpoint = "/employee_scope"

    class EmployeeVis(DataFetcherMain):
        _dates = []
        _endpoint = "/employee_vis"

    class GpaInfo(DataFetcherMain):
        _dates = []
        _endpoint = "/gpa_info"

    class Assessments(DataFetcherMain):
        _dates = []
        _endpoint = "/assessments"

    class Summary(DataFetcherMain):
        _dates = []
        _endpoint = "/assessments/summary"

    class Groups(DataFetcherMain):
        _dates = []
        _endpoint = "/groups"

    class Parents(DataFetcherMain):
        _dates = []
        _endpoint = "/parents"

    class Siblings(DataFetcherMain):
        _dates = []
        _endpoint = "/siblings"

    class Subjects(DataFetcherMain):
        _dates = []
        _endpoint = "/subjects"

    class Attendance(DataFetcherMain):
        _dates = []
        _endpoint = "/attendance"

    class Students(DataFetcherMain):
        _dates = []
        _endpoint = "/students"

    class OffDays(DataFetcherMain):
        _dates = []
        _endpoint = "/off_days"

    class Regions(DataFetcherMain):
        _dates = []
        _endpoint = "/regions"

    class Branches(DataFetcherMain):
        _dates = []
        _endpoint = "/branch"

    class Filter:
        class cities_by_region(DataFetcherMain):
            _dates = []
            _endpoint = "/filters/cities_by_region"

        class campuses_by_city(DataFetcherMain):
            _dates = []
            _endpoint = "/filters/campuses_by_city"

        class classes_by_campus(DataFetcherMain):
            _dates = []
            _endpoint = "/filters/classes_by_campus"

        class teacher_by_subject(DataFetcherMain):
            _dates = []
            _endpoint = "/filters/teacher_by_subject"

        class subjects_by_class(DataFetcherMain):
            _dates = []
            _endpoint = "/filters/subjects_by_class"
