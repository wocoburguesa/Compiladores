class CSVTableReader(object):
    def __init__(self):
        pass

    @staticmethod
    def dict_from_table(filename):
        """
        First row should be separated by ', '
        with a space after the comma, so .split() can't miss
        a comma element
        """
        _file = open(filename, 'r')
        lines = _file.readlines()
        _file.close()

        column_list = lines[0].strip().split(', ')[1:]
        columns = {key:None for key in column_list}
        raw_rows = [line.strip().split(',') for line in lines][1:]
        table_dict = {row[0]:columns.copy() for row in raw_rows}

        counter = 0
        for row in raw_rows:
            counter = 0
            print row
            print row[1:]
            for element in row[1:]:
                if element != '':
                    print '!!!!!!', row[0], column_list[counter], element
                    table_dict[row[0]][column_list[counter]] = int(element)
                counter += 1
            print table_dict[row[0]]

        return table_dict
