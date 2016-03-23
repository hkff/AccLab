[![Version](https://img.shields.io/badge/version-2.0-orange.svg)]()
[![License](https://img.shields.io/badge/license-GPL3-blue.svg)]()
[![Python](https://img.shields.io/badge/python->%3D3.4-green.svg)]()

AccLab Last release : Version 2.0 26/03/2016

What is it?
-----------

AAL tools set. aalc is a part of Acclab tool.
For more information see AccLab home page
AccLab home page: <http://www.emn.fr/z-info/acclab/>


Documentation
-------------

The documentation available as of the date of this release is
included in PDF format in the UserGuide/ directory.  The most
up-to-date documentation can be found at AccLab webpage.

Installation
------------

WARNING : AccLab is designed to run on local machines, DO NOT use it as a web service since
the AAL macros are written in python, which allows arbitrary code execution.

You need PythonX.X.X >= Python3.4.0 installed on your system
To run the main program : python aalc.py

* In order to use LTL based features (compliance/consistency
checking, etc) AccLab needs the following dependency :

    ###### TSPASS prover :
    TSPASS binaries are provided for linux x64 and mac x64 in the
    folder tools/_platformName_/ . For other platforms you have
    to compile tspass source code.
    The last version of TSPASS can be found in :
    <http://lat.inf.tu-dresden.de/~michel/software/tspass/>  
    The source code for TSPASS version 0.95-0.17 is provided
    with this tool.

* In order to use AccMon features AccLab needs the following dependency :

    ###### AccMon >= 1.0 :
        sudo pip3 install accmon

#### Optional : (Under Development)
* In order to use monitor synthetization / simulation features,
AccLab needs the following dependencies :

    You need to install the following dependencies :

            $ sudo pip3 install pykka



AAL Syntax highlighting modes for emacs, intellij, nano and ace,
can be found in tools/utils/.
If you want to run aalc using a symbolic link you need to set the
environment variable ACCLAB_PATH

    $ export ACCLAB_PATH=<AccLab_install_dir>

Licensing
---------

Please see the file called LICENSE.

Contacts
--------

###### Developers :
>   Walid Benghabrit        <Walid.Benghabrit@mines-nantes.fr>

###### Contributors :
>   Pr.Jean-Claude Royer  <Jean-Claude.Royer@mines-nantes.fr>  (Kernel/Theory/UI)  
>   Dr. Hervé Grall       <Herve.Grall@mines-nantes.fr>        (Theory)  
>   Dr. Mohamed Sellami   <Mohamed.Sellami@isep.fr>            (Theory)  
>   Pierre Teilhard    (Kernel)  
>   Anqi Tong          (UI)  
>   Julie Spens         (UI)  

-------------------------------------------------------------------------------
Copyright (C) 2014-2016 Walid Benghabrit  
Ecole des Mines de Nantes - ARMINES  
ASCOLA Research Group  
A4CLOUD Project http://www.a4cloud.eu/

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

