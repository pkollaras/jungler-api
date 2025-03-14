from django.test import TestCase, override_settings


class DebugToolbarURLsTestCase(TestCase):
    @override_settings(DEBUG=False, ENABLE_DEBUG_TOOLBAR=True)
    def test_no_debug_toolbar_url_when_debug_false(self):
        response = self.client.get("/__debug__/", follow=True)
        self.assertEqual(response.status_code, 404)
