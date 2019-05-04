CSV_FIELDS = {'title': 'عنوان درخواست', 'name': 'نام',
              'family': 'نام خانوادگی', 'shoab_code': 'کد شعبه',
              'shoab': 'نام شعبه', 'score': 'امتیاز',
              'request_count': 'تعداد درخواست'}


SERVICE_SCORE_FIELDS = ['category', 'title', 'request_count', 'score']


BRANCH_SCORE_FIELDS = [
    'branch_code',
    'branch_name',
    'category',
    'title',
    'request_count',
    'score'
]

SERVICE_SCORE_TRANSLATION = {
    'category': 'دسته خدمت',
    'title': 'عنوان خدمت',
    'request_count': 'تعداد درخواست',
    'score': 'امتیاز'
}

BRANCH_SCORE_TRANSLATION = {
    'branch_code': 'کد شعبه',
    'branch_name': 'نام شعبه',
    'category': 'دسته خدمت',
    'title': 'عنوان خدمت',
    'request_count': 'تعداد درخواست',
    'score': 'امتیاز',
    'operation_unit': 'کد امور شعب'
}