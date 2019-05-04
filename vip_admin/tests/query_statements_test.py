import os
import unittest
from datetime import datetime, timedelta

from vip_admin.config import BotConfig
from vip_admin.utils.query_statements import AccountOfficerStatement
from vip_admin.database.dbhandler import DB2Handler
from vip_admin import MAIN_DIRECTORY
from vip_admin.utils.result_writer import ResultWriter


start_base_time = datetime.today()-timedelta(2)
end_base_time = datetime.today()-timedelta(2)
start_date = start_base_time.strftime('%Y-%m-%d') + ' 00:00:00'
end_date = end_base_time.strftime('%Y-%m-%d') + ' 23:59:00'
RESULT_PATH = os.path.join(MAIN_DIRECTORY, 'tests/data/practice1.xlsx')
OFFICERS_SCORE_RESULT_PATH = os.path.join(
    MAIN_DIRECTORY,
    'tests/data/officers.xlsx'
)


# TODO: use database mockup
class TestStatements:

    def test_service_score(self, handler):
        account_officer_statement = AccountOfficerStatement(
            start_date,
            end_date
        )
        service_score = handler.fetch_statement_data(
            account_officer_statement.service_score_statement
        )
        assert service_score is not None
        assert 'SERVICE' in service_score[0].keys()
        assert 'CATEGORY' in service_score[0].keys()
        assert 'REQUEST_COUNT' in service_score[0].keys()

        branch_scores = handler.fetch_statement_data(
            account_officer_statement.branch_scores_statement
        )
        assert branch_scores is not None
        assert 'BRANCH_CODE' in branch_scores[0].keys()
        assert 'SCORE' in branch_scores[0].keys()
        assert 'REQUEST_COUNT' in branch_scores[0].keys()

        branch_request = handler.fetch_statement_data(
            account_officer_statement.branch_request_statement
        )
        assert branch_request is not None
        assert 'BRANCH_CODE' in branch_request[0].keys()
        assert 'REQUEST_COUNT' in branch_request[0].keys()

        result_writer = ResultWriter(RESULT_PATH)
        result_writer.write_to_excel(
            [
                (service_score,),
                (branch_scores,),
                (branch_request,)
            ],
            ['main', 'branches', 'requests']
        )
        assert os.path.exists(RESULT_PATH)

        account_officer_statement_with_branch_code = AccountOfficerStatement(
            start_date,
            end_date,
            branch_code='6401'
        )
        branch_scores = handler.fetch_statement_data(
            account_officer_statement_with_branch_code.branch_scores_statement
        )
        assert branch_scores is not None

        officers_score = handler.fetch_statement_data(
            account_officer_statement.officers_score_statement
        )
        assert officers_score is not None

        collaborator_score = handler.fetch_statement_data(
            account_officer_statement.collaborators_score_statement
        )
        assert collaborator_score is not None

        supervisor_score = handler.fetch_statement_data(
            account_officer_statement.supervisor_score_statement
        )
        assert supervisor_score is not None
        result_writer = ResultWriter(OFFICERS_SCORE_RESULT_PATH)
        result_writer.write_to_excel(
            [
                (officers_score,),
                (collaborator_score,),
                (supervisor_score,)
            ],
            ['officers', 'collaborators', 'supervisors']
        )
        assert os.path.exists(RESULT_PATH)

        weak_score = handler.fetch_statement_data(
            account_officer_statement.weak_score_statement
        )
        assert weak_score is not None

        account_officer_statement_with_branch_code = AccountOfficerStatement(
            start_date,
            end_date,
            branch_code='1011'
        )
        weak_score_with_branch_code = handler.fetch_statement_data(
            account_officer_statement_with_branch_code.weak_score_statement
        )
        assert weak_score_with_branch_code is not None
        account_officer_for_customer_search = AccountOfficerStatement(
            start_date,
            end_date,
            personnel_id=89406,
        )
        customer_search = handler.fetch_statement_data(
            account_officer_for_customer_search.customer_search_statement
        )
        assert customer_search is not None
        account_officer_for_officer_search = AccountOfficerStatement(
            start_date='2019-04-17 00:00:00',
            end_date='2019-04-23 23:59:00',
        )
        officer_search = handler.fetch_statement_data(
            account_officer_for_officer_search.officer_search_statement
        )
        assert officer_search is not None
        account_officer_for_officer_search = AccountOfficerStatement(
            start_date='2019-04-17 00:00:00',
            end_date='2019-04-23 23:59:00',
            social_number='0061638005'
        )
        officer_search_with_criteria = handler.fetch_statement_data(
            account_officer_for_officer_search.officer_search_statement
        )
        assert officer_search_with_criteria is not None

