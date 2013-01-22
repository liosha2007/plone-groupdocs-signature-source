from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import groupdocs.signature


GROUPDOCS_VIEWER = PloneWithPackageLayer(
    zcml_package=groupdocs.signature,
    zcml_filename='testing.zcml',
    gs_profile_id='groupdocs.signature:testing',
    name="GROUPDOCS_VIEWER")

GROUPDOCS_VIEWER_INTEGRATION = IntegrationTesting(
    bases=(GROUPDOCS_VIEWER, ),
    name="GROUPDOCS_VIEWER_INTEGRATION")

GROUPDOCS_VIEWER_FUNCTIONAL = FunctionalTesting(
    bases=(GROUPDOCS_VIEWER, ),
    name="GROUPDOCS_VIEWER_FUNCTIONAL")
