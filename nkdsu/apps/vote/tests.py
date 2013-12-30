import datetime

from django.test import TestCase
from django.utils import timezone

from models import Show


class ShowTest(TestCase):
    """
    Tests for Show objects. Many of these depend on Neko Desu continuing to be
    broadcast at 11pm.
    """

    def setUp(self):
        Show.objects.all().delete()

    def test_make_show(self, wipe=True):
        # this may seem overly thorough, but it has already found bugs that
        # would otherwise have been missed:
        for hours in xrange(366*24, 0, -1):
            if wipe:
                Show.objects.all().delete()

            starter = (
                timezone.now().replace(tzinfo=timezone.get_current_timezone())
                -
                datetime.timedelta(hours=hours)
            )

            show = Show.at(starter)
            showtime = show.showtime.astimezone(
                timezone.get_current_timezone())
            self.assertEqual(showtime.hour, 21)
            self.assertEqual(showtime.minute, 0)
            self.assertEqual(showtime.second, 0)
            self.assertEqual(showtime.microsecond, 0)
            self.assertEqual(showtime.weekday(), 5)

            self.assertEqual(show.end - show.showtime,
                             datetime.timedelta(hours=2))

            self.assertGreater(show.end, starter)

    def test_get_show(self):
        self.test_make_show(wipe=False)
        show_count = Show.objects.all().count()
        self.assertGreater(show_count, 51)
        self.assertLess(show_count, 55)

    def test_get_show_far_in_future(self):
        make_current = lambda t: timezone.make_aware(
            t, timezone.get_current_timezone())

        for x in xrange(2):
            # these functions do different things depending on if shows already
            # exist, but there should be no visible difference between the
            # results of these different things
            ours = Show.at(make_current(datetime.datetime(3000, 1, 1)))
            self.assertEqual(Show.objects.all().count(), 1)
            self.assertEqual(ours.end.date(), datetime.date(3000, 1, 4))

        for x in xrange(2):
            ours = Show.at(make_current(datetime.datetime(3010, 1, 1)))
            self.assertEqual(Show.objects.all().count(), 523)
            self.assertEqual(ours.end.date(), datetime.date(3010, 1, 6))
