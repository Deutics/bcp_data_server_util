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
