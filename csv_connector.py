import csv


class Csv_connector:

    """

    Class for csv file access.
    
    """

    def load_csv_file(self):

        """
        Loads 'episode.csv' file.

        Parameters:
        None

        Returns: 
        'episode.csv' file contents and a Python dictionary.
        """

        with open('episode.csv', newline='') as f:
            episode_db = csv.DictReader(f)
            episode_list = []
            for line in episode_db:
                episode_list.append(line)        
        return episode_list

    def search_date(self, date):
        
        """
        Secaches load_csv_file() by ISO 8601 (YYYY-MM-DDD) format.

        Parametters:
        date (str): This is based on the desired date of the download. Ideally release date. Format "YYYY-MM-DD".

        Return:
        tuple: (series_name, episode_number)
        """

        episode_list = self.load_csv_file()
        series_info = []
        for line in episode_list:
            if line['Date'] == date:
                series_name = line['Series']
                episode_number = line['Episode_Num']
                series_info.append((series_name, episode_number))
        return series_info

    def search_series(self, name):

        """
        Secaches load_csv_file() by series name.

        Parametters:
        name (str): name of the series.

        Return:
        list: of tuple: (series_name, episode_number)
        """

        episode_list = self.load_csv_file()
        series_list = []
        for line in episode_list:
            if line['Series'] == name:
                episode_name = line['Series']
                episode_number = line['Episode_Num']
                series_list.append((episode_name, episode_number))
        return series_list
