from abstracts.abstract_resource_route import AbstractResourceRoute
from modules.user.auth.routers import token_required
from .controller import ControllerAnalysisCategory as MainController


__all__ = ['route_analysiscategory']


class route_analysiscategory(AbstractResourceRoute):

    def __init__(self):
        self.abstract = super(route_analysiscategory, self)
        self.controller = MainController

    @token_required
    def get(self, db_id=None):
        return self.abstract.get(db_id)

    @token_required
    def post(self):
        return self.abstract.post()

    @token_required
    def put(self, db_id=None):
        return self.abstract.put(db_id)

    @token_required
    def delete(self, db_id=None):
        return self.abstract.delete(db_id)
