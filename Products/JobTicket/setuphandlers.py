from Products.CMFCore.utils import getToolByName
from Products.JobTicket import config

def setupVarious(context):
    """ Setup preferred default_member_type """
    if context.readDataFile('jobticket-setup-plugins.txt') is None:
        return
    portal = context.getSite()
