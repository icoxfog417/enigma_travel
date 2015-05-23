import tornado.web


class GroupHandler(tornado.web.RequestHandler):

    def post(self):
        # get group name from request
        group_name = self.get_argument("groupName", "")
        response = {}

        if group_name:
            # create group
            url = '//{0}{1}'.format(self.request.host, "/chat/{0}".format("xxx"))
            response = {"key": "xxx", "url": url}

        return self.write(response)
