class TestApiReport:
    def test_get_api_report_should_return_result(self, client, fixture_report):

        request = client.get(
            f"/report/{fixture_report.id}",
        )

        assert request.status_code == 200
        assert request.json == {
            "id": fixture_report.customer_id,
            "expenses": [
                {
                    "categoryId": "3f1dbe6b-fddd-40e6-bfc4-aaf6e6cda430",
                    "categoryName": "Categoria muito suspeita",
                    "purchaseId": "5852769a-9e1e-41cb-8d26-9a8bfb33fcd4",
                    "moneySpent": 150,
                    "purchaseDate": "25/12/2021",
                }
            ],
        }

    def test_get_report_should_not_found_due_invalid_report(self, client):
        request = client.get(
            "/report/dont-exist",
        )
        assert request.status_code == 404
        assert request.json == {
            "message": "Report not found. You have requested this URI [/report/dont-exist] but did you mean /report/<report_id> ?"
        }
