from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bot_template.models.employee import Employee, EmployeeSexEnum,\
    AccountOfficer, AccountOfficerStatusEnum
from bot_template.models.customer import Customer, IndevidualCustomer, LegalCustomer
from bot_template.models.branch import Branch
from bot_template.database.databasemanager import DatabaseManager


class TestGetAndWriteStatementData:

    def test_get_and_write_statement_data(self):
        with DatabaseManager() as dbmanager:
            dbmanager.drop_schema()
            dbmanager.setup_schema()
            engine = dbmanager.engine

        Session = sessionmaker(bind=engine)
        session = Session()
        employee = Employee(
            name='Example',
            family='Example',
            personnel_id=12,
            sex=EmployeeSexEnum.آقا)
        officer = AccountOfficer(
            name='Officer',
            family='Officer',
            personnel_id=13,
            sex=EmployeeSexEnum.آقا,
            status=AccountOfficerStatusEnum.ACTIVE
        )
        legal_customer = LegalCustomer(name='company', family='example')
        indevidual_customer = IndevidualCustomer(
            name='company',
            family='example'
        )
        branch = Branch(
            name='sadad',
            code=12,
            employees=[employee, officer],
            customers=[legal_customer, indevidual_customer]
        )
        session.add(branch)
        session.flush()
        assert officer.branch_id == 1
        assert employee.branch_id == 1
        assert len(branch.employees) == 2
        session.flush()
        officer1 = AccountOfficer(
            name='officer1',
            family='example',
            status=AccountOfficerStatusEnum.ACTIVE,
            sex=EmployeeSexEnum.آقا
        )
        session.add(officer1)
        session.flush()
        officer2 = AccountOfficer(
            name='officer2',
            family='example',
            status=AccountOfficerStatusEnum.ACTIVE,
            sex=EmployeeSexEnum.آقا
        )
        session.add(officer2)
        officer2.supervisor_id = officer1.id
        session.flush()
        assert officer2.supervisor_id == officer1.id
        assert officer1.supervisors[0] == officer2
        session.commit()


