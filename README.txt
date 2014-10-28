CAS IdP for Authentic2

Install
=======

You just have to install the package in your virtualenv and relaunch, it will
be automatically loaded by the plugin framework.

Settings
========

Name                           Description
=================              =========================

A2_IDP_CAS_SERVICES            A sequence of URL prefixes, any URL starting with this
                               prefix is authorized to request a ticket

A2_IDP_CAS_PROVIDER            Class implementating CAS views, default to
                               `authentic2_idp_cas.views.CasProvider`
A2_IDP_CAS_TICKET_EXPIRATION   Ticket lifetime
