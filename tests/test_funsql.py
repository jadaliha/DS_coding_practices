"""This module contains tests for the funsql package."""
import unittest
from funsql import Hook, readTemplates



# Set up logging
import logging
logFilePath = "my.log"
file_handler = logging.handlers.TimedRotatingFileHandler(filename=logFilePath, when='midnight', backupCount=30)
logFormatter = logging.Formatter(fmt=' %(name)s :: %(levelname)-8s :: %(message)s')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logFormatter)
log = logging.getLogger("funsql")
log.addHandler(file_handler)



try:
    PH = Hook({
        "host"      : "psql-mock-database-cloud.postgres.database.azure.com",
        "port"      : "5432",
        "user"      : "nxhbvewxsaijdisfftwjgpuw@psql-mock-database-cloud",
        "password"  : "aexcrtmmacdnrmpsomnnsvov",
        "database"  : "booking1666875447372qmebziyvxnskbwrb"
    })
except:
    raise Exception("Please set up a mock database for testing.")

PULL_TEN = 'SELECT * FROM pg_tables LIMIT 10;\n'

class TestTemplate(unittest.TestCase):
    "Here we test the template engine."
    query = readTemplates("./funsql/data/sql_templates.sql")

    def test_read_templates(self):
        "Does readTemplates return a dictionary with expected keys?"
        self.assertTrue('columns' in self.query)

    def test_run_template(self):
        "Does sample10 template produce expected query?"
        my_sample = self.query.sample10('pg_tables')
        self.assertEqual(f'{my_sample}', PULL_TEN)

class TestPghook(unittest.TestCase):
    "Here we test the pghook module."

    def test_run_query(self):
        "Does running query return the result with expected dimension?"
        my_result = PH.get(PULL_TEN)
        self.assertEqual(my_result.shape[0],10)


def test_none():
    "This is a dummy test."
    assert True, "Write some tests!"


if __name__ == '__main__':
    unittest.main()
