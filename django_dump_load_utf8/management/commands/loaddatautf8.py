from django.core.management.commands import loaddata


class Command(loaddata.Command):
    def loaddata(self, fixture_labels):
        super(Command, self).loaddata(fixture_labels)

        def open_with_utf8(*args, **kwargs):
            kwargs.setdefault('encoding', 'utf-8')
            return open(*args, **kwargs)

        self.compression_formats[None] = open_with_utf8
