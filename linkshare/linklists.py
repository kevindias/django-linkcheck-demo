from linkcheck import Linklist
from linkshare import models


class PostLinklist(Linklist):
    """ Class to let linkcheck app discover fields containing links """
    model = models.Post
    url_fields = ['link',]
    object_filter = {}


linklists = {'Posts': PostLinklist}
