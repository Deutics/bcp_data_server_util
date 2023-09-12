from ..fetcher import DataFetcherMain


class DataFetcher:
    class Branch(DataFetcherMain):
        _dates = ['close_date']
        _endpoint = "/branches"

    class Region(DataFetcherMain):
        _dates = []
        _endpoint = "/regions"

    class City(DataFetcherMain):
        _dates = []
        _endpoint = "/cities"

    class Student(DataFetcherMain):
        _dates = ['updt_time', 'rcrd_status_dt']
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
        _dates = ['updt_time', 'rcrd_status_dt']
        _endpoint = "/teacher_subjects"

    class VMRegister(DataFetcherMain):
        _dates = []
        _endpoint = "/vm_register"

    class StudentSubject(DataFetcherMain):
        _dates = ['vis_date', 'updt_time', 'time_out', 'time_in', 'entered_on', 'close_date','rcrd_status_dt']
        _endpoint = "/students_subject"

    class Role(DataFetcherMain):
        _dates = []
        _endpoint = "/roles"

    class Employee(DataFetcherMain):
        _dates = []
        _endpoint = "/employees"

    class User(DataFetcherMain):
        _dates = []
        _endpoint = "/users"

    class RegistrationFee(DataFetcherMain):
        _dates = []
        _endpoint = "/registration_fee"

    class Invoice(DataFetcherMain):
        _dates = ['paid_date','invo_canc_date']
        _endpoint = "/invoices"

    class Registration(DataFetcherMain):
        _dates = ['date_of_birth','registration_date','admission_date','updt_time','deposit_date','reg_canc_date','interview_date','entered_on']
        _endpoint = "/registrations"

    class Package(DataFetcherMain):
        _dates = []
        _endpoint = "/packages"
