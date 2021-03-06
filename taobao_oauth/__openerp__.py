# -*- coding: utf-8 -*-
##############################################################################
#    Taobao OpenERP Connector
#    Copyright 2012 wangbuke <wangbuke@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Taobao Oauth",
    'version': '1.0',
    'category': 'Web',
    'description': """
    """,
    'author': 'wangbuke@gmail.com',
    'website': 'http://my.oschina.net/wangbuke',
    'license': 'AGPL-3',
    'depends': ['web', 'taobao'],
    'data': [],
    'auto_install': False,
    'web_preload': True,
    'js': ['static/src/js/taobao_oauth.js'],
    'update_xml': [
            'taobao_shop_view.xml',
        ],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
