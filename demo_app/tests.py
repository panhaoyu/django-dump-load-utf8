import tempfile
from pathlib import Path

from django.core.management import call_command, CommandError
from django.test import TestCase

from demo_app.models import DemoModel


class TestDumpLoadUtf8(TestCase):
    def test_all(self):
        # create a field with special characters
        DemoModel.objects.create(field='�')
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)

            # default dumpdata command will cause error
            with self.assertRaises(CommandError):
                call_command('dumpdata', '--output', directory / 'default.json', 'demo_app')

            # dumpdatautf8 will not cause error and the data will be saved
            call_command('dumpdatautf8', '--output', directory / 'utf8.json', 'demo_app')

            # remove the object just created
            DemoModel.objects.all().delete()
            self.assertEqual(DemoModel.objects.count(), 0)

            # call loaddatautf8, the object appears again
            call_command('loaddatautf8', directory / 'utf8.json')
            self.assertEqual(DemoModel.objects.count(), 1)
            obj: DemoModel = DemoModel.objects.first()
            self.assertEqual(obj.field, '�')
