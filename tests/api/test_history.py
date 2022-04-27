from unittest.mock import Mock, patch

from app.services.request_history import RequestHistoryService


class TestApiHistory:
    @patch.object(RequestHistoryService, "create")
    def test_post_history_should_work_properly(
        self, mock_create, client, fixture_customer
    ):
        id_ = "39289834-303f-434a-ba29-3eb078f029a7"
        mock_create.return_value = Mock(id=id_)

        request = client.post(
            "/history/",
            json={
                "id": fixture_customer.id,
                "initialDate": "01/01/2001",
                "finalDate": "01/01/2005",
            },
        )

        assert request.status_code == 200
        assert mock_create.call_count == 1

    def test_post_history_should_not_found_due_invalid_customer(self, client):
        request = client.post(
            "/history/",
            json={"id": "aaa", "initialDate": "01/01/2001", "finalDate": "01/01/2005"},
        )
        assert request.status_code == 404
        assert request.json == {
            "message": "Customer not found. You have requested this URI [/history/] but did you mean /history/ ?"
        }
