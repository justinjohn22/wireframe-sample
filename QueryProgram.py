class QueryProgram:
    __sets = {}
    __themes = {}

    # QueryProgram constructor
    def __init__(self) -> None:
        self.read_sets()
        self.read_themes()
        # self.query('10030-1')

    # Reads and processes data from sets.csv
    def read_sets(self) -> None:
        try:
            sets = open('sets.csv', encoding='utf8')
            line = sets.readline()

            # check length to see if additional processing is required
            if len(line.split(",")) != 5:
                self.process_unusual_length(line)
            else:
                self.process_usual_length(line)

            while line != '':
                line = sets.readline()
                if len(line.split(",")) != 5:
                    self.process_unusual_length(line)
                else:
                    self.process_usual_length(line)

        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Input Output Error.")
        finally:
            # print("Operation completed - sets processed.")
            pass

    def read_themes(self) -> None:
        try:
            themes = open('themes.csv', encoding='utf8')
            line = themes.readline()

            while line != ['']:
                line = themes.readline()
                line = line.split(",")
                self.__themes[line[0]] = line[1:]

        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Input Output Error.")
        finally:
            # print("Operation completed - themes processed.")
            pass

    def process_usual_length(self, line: str) -> None:
        line = line.strip('\n')
        content = line.split(',')
        self.__sets[content[0]] = content[1:]

    def process_unusual_length(self, line: str) -> None:
        value = []
        line = line.strip('\n')
        content = line.split('"')

        if len(content) == 3:
            filtered_content = (content[2])[1:]
            value = filtered_content.split(",")
            value.insert(0, content[1])

        id_filtered = content[0].strip(',')
        self.__sets[id_filtered] = value

    def query(self, query_id: str) -> None:
        try:
            print("Name: " + self.__sets[query_id][0])
            print("Year released: " + self.__sets[query_id][1])
            print("Theme name: " + (self.__themes[self.__sets[query_id][2]][0]).strip('\n'))
            print("Number of parts: " + self.__sets[query_id][3])
        except KeyError:
            print("Invalid ID - Please try again.")



