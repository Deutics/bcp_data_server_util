from ..fetcher import DataFetcherMain


class DataFetcher:
    class Profile(DataFetcherMain):
        _endpoint = "/profile"

    class EmployeeRole(DataFetcherMain):
        _endpoint = "/employee_roles"

    class EmployeeProfile(DataFetcherMain):
        _endpoint = "/employees"

    class Branch(DataFetcherMain):
        _endpoint = "/branches"

    class Section(DataFetcherMain):
        _endpoint = "/sections"

    class TeacherGroups(DataFetcherMain):
        _endpoint = "/teacher_groups"
