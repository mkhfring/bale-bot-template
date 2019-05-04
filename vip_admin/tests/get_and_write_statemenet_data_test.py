import os

from vip_admin import MAIN_DIRECTORY
from vip_admin.utils.result_writer import ResultWriter
from vip_admin.database.create_report_data import DatabaseReporter
from vip_admin.bot.constants import FieldTranslation


RESULT_PATH = os.path.join(MAIN_DIRECTORY, 'tests/data/practice2.xlsx')
SINGLE_BRANCH_RESULT = os.path.join(MAIN_DIRECTORY, 'tests/data/practice3.xlsx')
OFFICER_SCORE_PATH = os.path.join(
    MAIN_DIRECTORY,
    'tests/data/officer_collaborator_supervisor.xlsx'
)
WEAK_SCORE_PATH = os.path.join(MAIN_DIRECTORY, 'tests/data/weakscore.xlsx')


class TestGetAndWriteStatementData:

    def test_get_and_write_statement_data(self, handler):
        reporter = DatabaseReporter(handler, 2, 2)
        total_branch_score = reporter.create_branch_score_data()
        assert total_branch_score is not None
        assert len(total_branch_score) > 0
        single_branch_score = reporter.create_branch_score_data(
            branch_code='0060'
        )
        assert single_branch_score is not None

        service_score = reporter.create_service_score_data()
        assert service_score is not None

        branch_request = reporter.create_branch_request_data()
        assert branch_request is not None

        officer_score = reporter.create_officer_score_data()
        assert officer_score is not None

        collaborator_score = reporter.create_collaborator_score_data()
        assert collaborator_score is not None

        supervisor_score = reporter.create_supervisor_score_data()
        assert supervisor_score is not None

        reporter = DatabaseReporter(handler, 45, 36)
        weak_score = reporter.create_weak_score_data()
        assert weak_score is not None

        weak_score_with_branch = reporter.create_weak_score_data('1011')
        assert weak_score_with_branch is not None
        customer_search = reporter.create_customer_search_data(89406)
        assert customer_search is not None
        officer_search = reporter.create_officer_search_data(89406)
        assert officer_search is not None

        result_writer = ResultWriter(RESULT_PATH)
        result_writer.write_to_excel(
            [
                (service_score, FieldTranslation.SERVICE_SCORE_TRANSLATION),
                (total_branch_score, FieldTranslation.BRANCH_SCORE_TRANSLATION),
                (branch_request, FieldTranslation.BRANCH_REQUEST_TRANSLATIOM)
            ],

            ['main', 'branches', 'requests']
        )
        assert os.path.exists(RESULT_PATH)
        sigle_branch_writer = ResultWriter(SINGLE_BRANCH_RESULT)
        sigle_branch_writer.write_to_excel(
            [(single_branch_score, FieldTranslation.BRANCH_SCORE_TRANSLATION)],
            ['branches']
        )
        assert os.path.exists(SINGLE_BRANCH_RESULT)

        officer_score_writter = ResultWriter(OFFICER_SCORE_PATH)
        officer_score_writter.write_to_excel(
            [
                (officer_score, FieldTranslation.OFFICER_SCORE_TRANSLATION),
                (collaborator_score, FieldTranslation.OFFICER_SCORE_TRANSLATION),
                (supervisor_score,FieldTranslation.OFFICER_SCORE_TRANSLATION),
            ],
            ['officers', 'collaborators', 'supervisors']
        )
        assert os.path.exists(OFFICER_SCORE_PATH)

        weak_score_writter = ResultWriter(WEAK_SCORE_PATH)
        weak_score_writter.write_to_excel(
            [
                (weak_score, FieldTranslation.WEAK_SCORE_TRANSLATION),
                (
                    weak_score_with_branch,
                    FieldTranslation.WEAK_SCORE_TRANSLATION
                )
            ],
            ['weakscore', 'weakscore_with_branch']
        )
        assert os.path.exists(WEAK_SCORE_PATH)
