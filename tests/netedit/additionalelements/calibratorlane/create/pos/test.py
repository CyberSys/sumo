#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.dev/sumo
# Copyright (C) 2009-2024 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# go to additional mode
netedit.additionalMode()

# select calibratorLane
netedit.changeElement("calibratorLane")

# change center view
netedit.changeDefaultBoolValue(netedit.attrs.calibrator.create.center)

# change position with an invalid value (dummy)
netedit.changeDefaultValue(netedit.attrs.calibrator.create.pos, "dummyValue")

# try to create calibratorLane with an invalid parameter
netedit.leftClick(referencePosition, 312, 250)

# change position with an invalid value (negative)
netedit.changeDefaultValue(netedit.attrs.calibrator.create.pos, "-5")

# try to create calibratorLane with an invalid parameter
netedit.leftClick(referencePosition, 322, 250)

# change position with a valid value
netedit.changeDefaultValue(netedit.attrs.calibrator.create.pos, "10")

# create calibratorLane with an invalid parameter
netedit.leftClick(referencePosition, 332, 250)

# Check undo redo
netedit.checkUndoRedo(referencePosition)

# save netedit config
netedit.saveNeteditConfig(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
