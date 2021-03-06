from orator.migrations import Migration


class CreateAfricadatasTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('africadatas') as table:
            table.increments('id')

            table.string('dates')
            table.integer('new_cases')
            table.integer('new_deaths')
            table.integer('total_cases')
            table.integer('total_deaths')

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('africadatas')
