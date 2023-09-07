from ..fetcher import DataFetcherMain


class DataFetcher:
    class Branch(DataFetcherMain):
        _endpoint = "/branches"

    class Region(DataFetcherMain):
        _endpoint = "/regions"

    class City(DataFetcherMain):
        _endpoint = "/cities"

    class Student(DataFetcherMain):
        _endpoint = "/students"

        @classmethod
        def fetch_visitor_registration_system_id_using_email_for_non_bss(cls, email):
            return cls.list(
                endpoint="/students/fetch_visitor_registration_system_id_using_email_for_non_bss",
                single=True,
                params={
                    "email": email
                }
            )

    class TeacherSubject(DataFetcherMain):
        _endpoint = "/teacher_subjects"

    class VMRegister(DataFetcherMain):
        _endpoint = "/vm_register"

    class StudentSubject(DataFetcherMain):
        _endpoint = "/students_subject"

    class Role(DataFetcherMain):
        _endpoint = "/roles"

    class Employee(DataFetcherMain):
        _endpoint = "/employees"

    class User(DataFetcherMain):
        _endpoint = "/users"

    class RegistrationFee(DataFetcherMain):
        _endpoint = "/registration_fee"

    class Invoice(DataFetcherMain):
        _endpoint = "/invoices"

    class Registration(DataFetcherMain):
        _endpoint = "/registrations"

    class Package(DataFetcherMain):
        _endpoint = "/packages"
