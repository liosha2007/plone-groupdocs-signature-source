GroupDocs HTML5 PDF Signature plugin for Plone CMS (Source)
=============================



###Plugin installation steps:

When plugin is available only on GitHub (not released to Pypi) it can be installed with buildout like this:

* Create groupdocs.signature folder under C:\Plone42\src\ folder
* Download files from GitHub and copy all the files into created folder.
* Change buildout.cfg file
* Add groupdocs.signature record into "eggs =" section
* Add src/groupdocs.signature into "develop =" section
* Run buildout .\bin\buildout.exe from Plone installation folder(For example C:\Plone42).
* Restart plone.
* Go to Admin->Site setup (http://localhost:8080/PloneGD/@@overview-controlpanel)
* Open Add-ons section - http://localhost:8080/PloneGD/prefs_install_products_form
* Find GroupDocs Signature 1.0 add-on, check it and activate it.

###Using plugin:
* Modify or create a new page
* Click Mange Portlets link http://screencast.com/t/fbjWrqCJuCfP
* Open Add portlet.. dropbox and choose GroupDocs Signature portlet - http://screencast.com/t/fAAlxv1dL
* Configure portlet's parameters and press Save button - http://screencast.com/t/zJW3kiyMrW
* Open the created page (http://localhost:8080/PloneGD/gd-test)  - GD Viwer will be embeded into portlet region - http://screencast.com/t/VMd3UZc5