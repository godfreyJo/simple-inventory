from rest_framework import renderers


class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data):
        response = ''

        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors': data})
        else:
            response = json.dumps({'data': data})
        return response
