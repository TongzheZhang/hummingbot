import unittest
import logging
from hummingbot.test_logger import LoggerMixinForTest

# python

class TestLoggerMixinForTestHandle(unittest.TestCase):
    def setUp(self):
        self.mixin = LoggerMixinForTest()
        self.mixin._initialize()

    def test_handle_single_record(self):
        record = logging.LogRecord("test", logging.INFO, "", 0, "test message", (), None)
        self.mixin.handle(record)
        self.assertEqual(len(self.mixin.log_records), 1)
        self.assertIs(self.mixin.log_records[0], record)

    def test_handle_multiple_records(self):
        records = [
            logging.LogRecord("test", logging.INFO, "", 0, "msg1", (), None),
            logging.LogRecord("test", logging.WARNING, "", 0, "msg2", (), None),
            logging.LogRecord("test", logging.ERROR, "", 0, "msg3", (), None),
        ]
        for rec in records:
            self.mixin.handle(rec)
        self.assertEqual(len(self.mixin.log_records), 3)
        self.assertListEqual(self.mixin.log_records, records)

    def test_handle_different_levels(self):
        info_record = logging.LogRecord("test", logging.INFO, "", 0, "info", (), None)
        error_record = logging.LogRecord("test", logging.ERROR, "", 0, "error", (), None)
        self.mixin.handle(info_record)
        self.mixin.handle(error_record)
        self.assertIn(info_record, self.mixin.log_records)
        self.assertIn(error_record, self.mixin.log_records)