from collections import OrderedDict

from datetime import datetime, timedelta
from vip_admin.utils.query_statements import AccountOfficerStatement
from .constants import ReportAttributeList


class DatabaseReporter:

    def __init__(self, database_handler, start_time_delta, end_time_delta):
        self.handler = database_handler
        self.start_time_delta = start_time_delta
        self.end_time_delta = end_time_delta
        (start_time_delta, end_time_delta) = (
            self.start_time_delta, self.end_time_delta) \
            if self.start_time_delta > self.end_time_delta \
            else (self.end_time_delta, self.start_time_delta)

        start_base_time = datetime.today()-timedelta(start_time_delta)
        end_base_time = datetime.today()-timedelta(end_time_delta)
        self.start_date = start_base_time.strftime('%Y-%m-%d') + ' 00:00:00'
        self.end_date = end_base_time.strftime('%Y-%m-%d') + ' 23:59:00'
        self.account_officer_statement = AccountOfficerStatement(
            self.start_date,
            self.end_date
        )

    def create_branch_score_data(self, branch_code=None):
        branch_score_final_result = []
        account_officer_statement = AccountOfficerStatement(
            self.start_date,
            self.end_date,
            branch_code=branch_code
        )
        branch_score = self.handler.fetch_statement_data(
            account_officer_statement.branch_scores_statement
        )
        for item in branch_score:
            branch_score_final_result.append(self.fix_dictionary_order(
                item,
                ReportAttributeList.branch_score_attribute_list
            ))

        return branch_score_final_result

    def create_service_score_data(self):
        service_score_final_result = []
        service_score = self.handler.fetch_statement_data(
            self.account_officer_statement.service_score_statement
        )
        for item in service_score:
            service_score_final_result.append(self.fix_dictionary_order(
                item,
                ReportAttributeList.service_score_attribute_list
            ))

        return service_score_final_result

    def create_branch_request_data(self):
        branch_request = self.handler.fetch_statement_data(
            self.account_officer_statement.branch_request_statement
        )
        return branch_request

    def create_officer_score_data(self):
        officer_score_final_result = []

        officer_score = self.handler.fetch_statement_data(
            self.account_officer_statement.officers_score_statement
        )
        for item in officer_score:
            officer_score_final_result.append(self.fix_dictionary_order(
                item,
                ReportAttributeList \
                    .officer_supervisor_collaborator_attribute_list
            ))

        return officer_score_final_result

    def create_collaborator_score_data(self):
        collaborator_score_final_result = []
        collaborator_score = self.handler.fetch_statement_data(
            self.account_officer_statement.collaborators_score_statement
        )
        for item in collaborator_score:
            collaborator_score_final_result.append(self.fix_dictionary_order(
                item,
                ReportAttributeList \
                    .officer_supervisor_collaborator_attribute_list
            ))

        return collaborator_score_final_result

    def create_supervisor_score_data(self):
        supervisor_score_final_result = []
        supervisor_score = self.handler.fetch_statement_data(
            self.account_officer_statement.supervisor_score_statement
        )
        for item in supervisor_score:
            supervisor_score_final_result.append(self.fix_dictionary_order(
                item,
                ReportAttributeList \
                    .officer_supervisor_collaborator_attribute_list
            ))

        return supervisor_score_final_result

    def create_weak_score_data(self, branch_code=None):
        weak_score_final_result = []

        account_officer_statement = AccountOfficerStatement(
            self.start_date,
            self.end_date,
            branch_code=branch_code
        )
        weak_score = self.handler.fetch_statement_data(
            account_officer_statement.weak_score_statement
        )
        for item in weak_score:
            weak_score_final_result.append(self.fix_dictionary_order(
                item,
                ReportAttributeList.weak_score_attribute_list
            ))

        return weak_score_final_result

    def create_customer_search_data(self, personnel_id=None,
                                    social_number=None, phone_number=None):
        customer_search_final_result = []

        account_officer_statement = AccountOfficerStatement(
            self.start_date,
            self.end_date,
            personnel_id=personnel_id,
            social_number=social_number,
            phone_number=phone_number
        )
        customer_list = self.handler.fetch_statement_data(
            account_officer_statement.customer_search_statement
        )

        for item in customer_list:
            customer_search_final_result.append(self.fix_dictionary_order(
                item,
                ReportAttributeList.customer_atrribute_list
            ))

        return customer_search_final_result

    def create_officer_search_data(self, personnel_id=None,
                                    social_number=None, phone_number=None):

        officer_search_final_result = []

        account_officer_statement = AccountOfficerStatement(
            self.start_date,
            self.end_date,
            personnel_id=personnel_id,
            social_number=social_number,
            phone_number=phone_number
        )
        officer_list = self.handler.fetch_statement_data(
            account_officer_statement.officer_search_statement
        )

        for officer in officer_list:
            officer_search_final_result.append(self.fix_dictionary_order(
                officer,
                ReportAttributeList.officer_search_attribute_list
            ))

        return officer_search_final_result

    @staticmethod
    def fix_dictionary_order(data, attribute_list):
        result_with_fixed_order = OrderedDict()
        for item in attribute_list:
            result_with_fixed_order.setdefault(item)

        for key, value in data.items():
            result_with_fixed_order[key] = value

        return result_with_fixed_order

