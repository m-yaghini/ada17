from collections import Counter
import pandas as pd

class word_counter:

    counters_program_period = pd.DataFrame()

    def __init__(self, df):
        def list_flatter(values):
            temp = []
            for sublist in values:
                for item in sublist:
                    temp.append(item)
            return ' '.join(temp)
            
        self.counters_program_period = df.groupby([
            df.program,
            df.publicationDate.apply(lambda x: x.year)
        ])[
            'genres', 'thematicCorporations', 'thematicGeographicals',
            'thematicPersons', 'thematicThemes', 'visualCorporations',
            'visualGeographicals', 'visualPersons', 'visualThemes'
        ].agg(lambda x: ', '.join(x))

    def get_df(self):
        return self.counters_program_period

    def get_themes(self, fr, to, theme_type, program=-1, n_top=3):
        rows_selection = ((self.counters_program_period.index.get_level_values('publicationDate') >= fr) &
        (self.counters_program_period.index.get_level_values('publicationDate') <= to))
        
        if program != -1:
            rows_selection = rows_selection & (self.counters_program_period.index.get_level_values('program') == program)
            
        temp_sum = self.counters_program_period.loc[rows_selection][theme_type].apply(lambda x : [word.strip() for word in x.split(',') if word not in [' ', '']]).sum()
        
        # to prevent error if the list is empty
        if not isinstance(temp_sum, list):
            temp_sum = []
        return Counter(temp_sum).most_common(n_top)

    def get_topn_themes(self, fr, to='', theme_type='thematicThemes', program=-1,n_top = 3):
        if not to:
            to = fr
        
        columns_name = ['top' + str(i+1) for i in range(n_top)]
        themes_per_year = pd.DataFrame(columns=columns_name)
        
        for i in range(fr, to+1):
            temp_themes = self.get_themes(
                i,
                i+1,
                theme_type,
                program,
                n_top
            )

            top_themes = [''] * n_top
            for j in range(min(n_top, len(temp_themes))):
                top_themes[j] = (temp_themes[j][0])

            themes_per_year.loc[i] = top_themes
        return themes_per_year