# Standard Library
import time

# Third Party
from client.api_requests.constants.status_codes import RATE_LIMIT, SUCCESS
from requests import Response


class RequestsStatusChecker:

    @staticmethod
    def check_response_status(response: Response) -> bool:
        if response.status_code == SUCCESS:
            return True
        if response.status_code == RATE_LIMIT:
            print("Timed out rate limit reached")
            time.sleep(1)
        return False
