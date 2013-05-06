# File: Job_Ticket.py
#
# Copyright (c) 2006 by []
# Generator: ArchGenXML Version 1.4.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import base
from Products.ATContentTypes.interfaces import IATContentType
from Products.JobTicket.config import *
from DateTime.DateTime import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='customer_name',
	required=1,
	default_method="setCustomerText",
	searchable=1,
        widget=StringWidget(
            label='Customer Name',
            label_msgid='JobTicket_label_customer_name',
            i18n_domain='JobTicket',
        )
    ),

    StringField(
        name='locale',
	searchable=1,
        widget=StringWidget(
            label='Customer Location',
            label_msgid='JobTicket_label_customer_locale',
            i18n_domain='JobTicket',
        )
    ),

    DateTimeField(
        name='date_of_service',
	required=1,
	searchable=1,
        default_method = DateTime,
        widget=CalendarWidget(
            label='Date of Service',
            format="%Y%m%d",
	    description=("Enter the starting date, or click "
                     "the calendar icon and select it. "),
            show_hm=False,
            label_msgid='JobTicket_label_date_of_service',
            i18n_domain='JobTicket',
        )
    ),

    StringField(
        name='consultant_name',
	vocabulary=['DKT','HS', 'JDD', 'RG', 'BR', 'RO',],
	required=1,
	searchable=1,
	default_method="setConsultantText",
        widget=StringWidget(
            label='Consultant Name',
            label_msgid='JobTicket_label_consultant_name',
            i18n_domain='JobTicket',
        )
    ),

    TextField(
        name='job_ticket_summary',
	searchable=1,
	default_content_type='text/plain',
        default_output_type='text/plain',
	allowable_content_types=(
		'text/plain',),
        widget=TextAreaWidget(
            label='Job Ticket Summary',
	    label_msgid='JobTicket_label_job_ticket_summary',
	    rows=2,
            i18n_domain='JobTicket',
        )
    ),

    TextField(
        name='job_ticket_detail',
	searchable=1,
	default_content_type='text/html',
        default_output_type='text/html',
	allowable_content_types=(
	    'text/html','text/plain'),
	widget=RichWidget(
            label='Job Ticket Detail',
	    columns=70,
	    rows=10,
            label_msgid='JobTicket_label_job_ticket_detail',
            i18n_domain='JobTicket',
        )
    ),

    FloatField(
        name='onsite_time',
	read_permission='Manage portal',
        widget=DecimalWidget(
	    label='Onsite Time (as a decimal)',
            label_msgid='JobTicket_label_onsite_time',
            i18n_domain='JobTicket',
        )
    ),

    FloatField(
        name='one_way_travel',
	read_permission='Manage portal',
        widget=DecimalWidget(
            label='One Way Travel Time',
            label_msgid='JobTicket_label_one_way_travel',
            i18n_domain='JobTicket',
        )
    ),

    TextField(
        name='billing_notes',
	read_permission='Manage portal',
	default_content_type='text/plain',
	allowed_content_types=(
		'text/plain','text/html'),
        default_output_type='text/html',
        widget=TextAreaWidget(
            label='Billing Notes',
	    rows=2,
            label_msgid='JobTicket_label_billing_notes',
            i18n_domain='JobTicket',
        )
    ),

    TextField(
        name='private_comments',
	read_permission='Manage portal',
	default_content_type='text/plain',
	allowed_content_types=(
		'text/plain','text/html'),
        default_output_type='text/html',
        widget=TextAreaWidget(
            label='Private Comments',
	    rows=2,
            label_msgid='JobTicket_label_private_comments',
            i18n_domain='JobTicket',
        )
    ),

    FloatField(
        name='tolls_and_parking',
	read_permission='Manage portal',
        widget=DecimalWidget(
            dollars_and_cents=True,
	    label='Tolls and Parking',
	    label_msgid='JobTicket_label_tolls_and_parking',
            i18n_domain='JobTicket',
        )
    ),

    IntegerField(
        name='mileage',
	read_permission='Manage portal',
        widget=IntegerWidget(
            label='Mileage',
            label_msgid='JobTicket_label_mileage',
            i18n_domain='JobTicket',
        )
    ),

    LinesField(
        name='special_items',
        required=0,
        default='',
        searchable=1,
        multiValued=1,
        vocabulary=['Server','Network','How-to',],
    	read_permission='Manage portal',
        widget=MultiSelectionWidget(
            format='checkbox',
            description="""Check item where appropriate""",
            description_msgid='JobTicket_help_special_items',
            label='Special',
            label_msgid='JobTicket_label_special_items',
                  i18n_domain='JobTicket',
        )
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Job_Ticket_schema = schemata.ATContentTypeSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

Job_Ticket_schema['description'].widget.visible = {'edit':'invisible', 'view':'invisible'}

class Job_Ticket(base.ATCTContent):
    # Huh? //regebro
    #__implements__ = (base.ATCTContent.__implements__, IATContentType) 

    meta_type = 'Job_Ticket'
    portal_type = 'Job_Ticket'

    #DKT added 1/4/07 for jobticket shortname rename BUT WILL NOT WORK UNTIL Job_Ticket is changed to JobTicket per "santized short name" google this
    _at_rename_after_creation = True

    schema = Job_Ticket_schema




    def setCustomerText(self):
        """determines the default text for the 
	    function """
        return self.getFolderWhenPortalFactory().id
 
    def setConsultantText(self):
        """determines the default text for the 
	    function """
        return self.Creator()
    
    def start(self):
        return self.getDate_of_service()

    def end(self):
        return self.getDate_of_service()


    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Job_Ticket,PROJECTNAME)
# end of class Job_Ticket

##code-section module-footer #fill in your manual code here
##/code-section module-footer



