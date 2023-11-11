# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TravelingSalesmanProblem
                                 A QGIS plugin
 to solve TSP
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-07-17
        copyright            : (C) 2022 by LTY
        email                : 1643914601@qq.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TravelingSalesmanProblem class from file TravelingSalesmanProblem.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .traveling_salesman_problem import TravelingSalesmanProblem
    return TravelingSalesmanProblem(iface)
