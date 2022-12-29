import uuid


class BaseRequest(object):
    def __init__(self):
        self.__request_id = uuid.uuid1()

    @property
    def request_id(self):
        """ Get 请求ID

        :return: str, dealer_id
        """
        if self.__request_id is None or self.__request_id == "":
            self.__request_id = uuid.uuid1()
        return self.__request_id.__str__()

    @request_id.setter
    def request_id(self, request_id):
        """ Set 请求ID

        :type request_id: str
        :param request_id: 请求ID
        """
        self.__request_id = request_id
