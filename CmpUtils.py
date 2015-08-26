

from suds.client import Client


class CmpUtils(object):

    @staticmethod
    def _get_url(url, host, port):
        return url.format(host=host, port=port)

    @staticmethod
    def _load_client_using_basic_authentication(username, password, url, timeout=None):
        if timeout:
            return Client(url, username=username, password=password, timeout=int(timeout))

        return Client(url, username=username, password=password)

    @staticmethod
    def _escape_xml_string(xml_string):
        data = xml_string
        data = data.replace('&lt', '&amp;lt')
        data = data.replace('&gt', '&amp;gt')
        data = data.replace('&amp', '&amp;gt')
        data = data.replace('&apos', '&amp;apos')
        data = data.replace('&quot', '&amp;quot')
        return data





