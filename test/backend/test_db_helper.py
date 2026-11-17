import backend.db_helper as db_helper


def test_get_expenses():
    summary = db_helper.get_expenses()
    assert len(summary) > 0

def test_get_expenses_invalid_date():
    summary = db_helper.get_expense_by_date("2029-10-08")
    assert len(summary) == 0

def test_get_expense_by_date():
    summary = db_helper.get_expense_by_date("2026-11-03")
    for expense in summary:
        assert expense['amount'] == 700
        assert expense['category'] == "Entertainment"
        assert expense['notes'] == 'Watched Ramayan'

def test_get_expense_summary_by_date():
    summary = db_helper.get_expense_summary_by_date("2024-08-02","2024-08-05")
    assert len(summary) > 0

def test_get_expense_summary_by_invalid_date():
    summary = db_helper.get_expense_summary_by_date("2028-08-02", "2028-08-05")
    assert len(summary) == 0

def test_get_total_expense_summary_by_month():
    total = db_helper.get_expense_total_by_month_year()
    assert total[0]['month_year'] == "August 2024"
    assert total[0]['total_amount'] == 4922.0
    assert total[1]['month_year'] ==  "September 2024"
    assert total[1]['total_amount'] == 4790.0


