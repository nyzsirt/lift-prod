from abstracts.abstract_resource_route import AbstractResourceRoute
from modules.analyzes.machineEngine.volume.controller import ControllerVolume
from modules.user.auth.routers import token_required
from resources import app


class router_volume(AbstractResourceRoute):
    """
         Extends of flask restfull resource
         :param Resource extended class
         """

    def __init__(self):
        self.abstract = super(router_volume, self)
        self.controller = ControllerVolume

    @token_required
    def get(self, mongoid=None):
        app.logger.debug("***{} fired as GET request".format(self.__class__.__name__))
        if mongoid:
            app.logger.debug("get one for id:{}".format(mongoid))
        return self.abstract.get(mongoid)

    @token_required
    def post(self):
        app.logger.debug("***{} fired as POST request".format(self.__class__.__name__))
        return self.abstract.post()

    @token_required
    def put(self, mongoid):
        app.logger.debug("***{} fired as PUT request with id:{}".format(self.__class__.__name__, mongoid))
        return self.abstract.put(mongoid=mongoid)

    @token_required
    def delete(self, mongoid):
        app.logger.debug("***{} fired as DELETE request with id:{}".format(self.__class__.__name__, mongoid))
        return self.abstract.delete(db_id=mongoid)


app.logger.debug("*** Route Volume api")
app.api.add_resource(router_volume,
                     '/api/v1/volume',
                     '/api/v1/volume/<mongoid>',
                     endpoint='api-volume',
                     methods=['GET', 'POST', 'PUT', 'DELETE'])
