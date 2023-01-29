from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc





app = Dash(external_stylesheets=[dbc.themes.DARKLY])
application = app.server





data = {'class':['no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','no-recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events','recurrence-events'],
        'age':['30-39','40-49','40-49','60-69','40-49','60-69','50-59','60-69','40-49','40-49','40-49','50-59','60-69','50-59','40-49','60-69','40-49','50-59','60-69','50-59','50-59','60-69','30-39','50-59','50-59','40-49','50-59','60-69','40-49','60-69','50-59','50-59','50-59','50-59','50-59','30-39','50-59','50-59','40-49','40-49','50-59','60-69','60-69','40-49','50-59','50-59','40-49','50-59','40-49','40-49','50-59','30-39','50-59','70-79','70-79','70-79','50-59','50-59','60-69','60-69','40-49','40-49','50-59','20-29','40-49','40-49','40-49','50-59','50-59','60-69','60-69','40-49','60-69','50-59','30-39','50-59','50-59','30-39','50-59','40-49','50-59','60-69','60-69','50-59','40-49','50-59','60-69','70-79','50-59','40-49','30-39','50-59','50-59','60-69','50-59','40-49','60-69','60-69','40-49','30-39','40-49','50-59','50-59','40-49','40-49','40-49','40-49','30-39','40-49','60-69','50-59','50-59','40-49','40-49','40-49','50-59','30-39','40-49','30-39','60-69','60-69','50-59','50-59','50-59','60-69','70-79','30-39','30-39','50-59','40-49','40-49','40-49','40-49','50-59','60-69','30-39','30-39','40-49','30-39','40-49','50-59','50-59','60-69','40-49','60-69','40-49','60-69','50-59','30-39','50-59','50-59','60-69','50-59','60-69','30-39','60-69','50-59','50-59','50-59','40-49','40-49','40-49','60-69','60-69','60-69','40-49','40-49','40-49','50-59','40-49','30-39','30-39','60-69','50-59','50-59','40-49','40-49','60-69','50-59','40-49','40-49','40-49','40-49','50-59','50-59','40-49','50-59','60-69','40-49','50-59','40-49','40-49','50-59','30-39','50-59','50-59','50-59','40-49','50-59','50-59','60-69','50-59','40-49','50-59','50-59','30-39','50-59','50-59','50-59','40-49','40-49','50-59','40-49','50-59','60-69','40-49','50-59','40-49','60-69','30-39','40-49','30-39','60-69','60-69','30-39','40-49','40-49','50-59','60-69','60-69','50-59','40-49','30-39','70-79','60-69','50-59','40-49','40-49','30-39','40-49','60-69','40-49','50-59','50-59','40-49','30-39','30-39','50-59','60-69','30-39','40-49','40-49','30-39','60-69','40-49','40-49','40-49','40-49','50-59','50-59','60-69','40-49','60-69','50-59','50-59','30-39','40-49','60-69','30-39','40-49','50-59','50-59','40-49','60-69','60-69','40-49','30-39','60-69','50-59','50-59','50-59','30-39','30-39','60-69','40-49','50-59'],
        'menopause':['premeno','premeno','premeno','ge40','premeno','ge40','premeno','ge40','premeno','premeno','premeno','ge40','lt40','ge40','premeno','lt40','premeno','premeno','ge40','ge40','ge40','ge40','premeno','premeno','premeno','premeno','premeno','ge40','premeno','ge40','ge40','premeno','premeno','ge40','ge40','premeno','ge40','ge40','premeno','premeno','ge40','ge40','ge40','premeno','ge40','ge40','premeno','premeno','premeno','premeno','lt40','premeno','premeno','ge40','ge40','ge40','ge40','ge40','ge40','ge40','premeno','premeno','ge40','premeno','premeno','premeno','premeno','ge40','ge40','ge40','ge40','premeno','ge40','premeno','premeno','ge40','ge40','premeno','premeno','premeno','ge40','ge40','ge40','ge40','premeno','ge40','ge40','ge40','ge40','premeno','premeno','ge40','ge40','ge40','premeno','premeno','ge40','ge40','premeno','premeno','ge40','ge40','premeno','premeno','premeno','premeno','premeno','premeno','premeno','ge40','ge40','ge40','premeno','premeno','premeno','ge40','premeno','ge40','premeno','ge40','ge40','ge40','ge40','ge40','ge40','ge40','premeno','premeno','premeno','premeno','premeno','premeno','premeno','ge40','ge40','premeno','premeno','premeno','premeno','premeno','ge40','premeno','ge40','premeno','ge40','premeno','ge40','premeno','premeno','lt40','ge40','ge40','ge40','ge40','lt40','ge40','ge40','premeno','ge40','premeno','premeno','premeno','ge40','ge40','ge40','premeno','premeno','ge40','premeno','ge40','premeno','premeno','ge40','ge40','premeno','premeno','ge40','ge40','premeno','premeno','premeno','premeno','premeno','ge40','ge40','premeno','ge40','ge40','premeno','ge40','premeno','premeno','ge40','premeno','premeno','ge40','premeno','premeno','ge40','premeno','ge40','premeno','premeno','ge40','premeno','premeno','ge40','premeno','premeno','premeno','premeno','ge40','premeno','premeno','ge40','ge40','ge40','premeno','ge40','premeno','premeno','premeno','ge40','ge40','premeno','ge40','premeno','premeno','ge40','ge40','premeno','premeno','premeno','ge40','ge40','premeno','premeno','premeno','premeno','premeno','ge40','premeno','ge40','ge40','premeno','premeno','premeno','ge40','ge40','premeno','premeno','premeno','premeno','ge40','premeno','premeno','premeno','premeno','ge40','ge40','ge40','ge40','ge40','lt40','lt40','premeno','premeno','ge40','premeno','premeno','ge40','premeno','premeno','ge40','ge40','premeno','premeno','ge40','premeno','ge40','ge40','premeno','premeno','ge40','ge40','ge40'],
        'tumour_size':['30-34','20-24','20-24','15-19','0-4','15-19','25-29','20-24','50-54','20-24','0-4','25-29','10-14','25-29','30-34','30-34','15-19','30-34','30-34','30-34','40-44','15-19','25-29','40-44','35-39','25-29','20-24','25-29','40-44','30-34','40-44','15-19','10-14','10-14','10-14','30-34','0-4','15-19','10-14','30-34','20-24','25-29','5-9','10-14','50-54','30-34','25-29','25-29','20-24','20-24','15-19','20-24','15-19','20-24','40-44','40-44','0-4','5-9','30-34','15-19','20-24','10-14','0-4','35-39','25-29','10-14','25-29','20-24','35-39','50-54','10-14','25-29','20-24','15-19','5-9','10-14','10-14','25-29','25-29','25-29','10-14','10-14','15-19','15-19','20-24','35-39','25-29','0-4','20-24','40-44','0-4','20-24','25-29','20-24','10-14','30-34','30-34','15-19','30-34','25-29','20-24','30-34','25-29','20-24','10-14','30-34','20-24','40-44','30-34','30-34','25-29','15-19','20-24','10-14','35-39','20-24','15-19','20-24','10-14','15-19','20-24','15-19','40-44','30-34','10-14','10-14','30-34','25-29','25-29','35-39','35-39','40-44','30-34','40-44','30-34','20-24','40-44','5-9','40-44','30-34','40-44','20-24','10-14','45-49','45-49','25-29','50-54','30-34','20-24','30-34','25-29','30-34','35-39','15-19','15-19','40-44','25-29','30-34','30-34','35-39','25-29','30-34','10-14','25-29','25-29','20-24','20-24','40-44','10-14','30-34','20-24','15-19','30-34','20-24','25-29','30-34','25-29','10-14','25-29','20-24','35-39','35-39','25-29','30-34','30-34','20-24','25-29','15-19','10-14','20-24','15-19','25-29','30-34','10-14','50-54','35-39','10-14','10-14','15-19','25-29','25-29','15-19','40-44','35-39','25-29','0-4','30-34','25-29','30-34','35-39','20-24','20-24','30-34','25-29','40-44','20-24','20-24','15-19','30-34','15-19','25-29','30-34','25-29','20-24','25-29','20-24','30-34','30-34','40-44','45-49','50-54','30-34','30-34','15-19','30-34','25-29','25-29','25-29','35-39','20-24','20-24','15-19','25-29','20-24','30-34','30-34','15-19','30-34','35-39','20-24','25-29','50-54','40-44','50-54','30-34','30-34','30-34','20-24','30-34','30-34','25-29','25-29','25-29','20-24','20-24','35-39','30-34','20-24','35-39','25-29','30-34','25-29','15-19','30-34','30-34','25-29','25-29','10-14','35-39','40-44','40-44','30-34','20-24','20-24','30-34','30-34'],
        'inv_nodes':['0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','6-8','6-8','0-2','9-11','9-11','3-5','6-8','0-2','0-2','3-5','3-5','0-2','0-2','0-2','3-5','3-5','0-2','0-2','6-8','0-2','0-2','3-5','0-2','0-2','15-17','3-5','15-17','0-2','0-2','3-5','3-5','0-2','0-2','0-2','0-2','3-5','0-2','3-5','3-5','3-5','3-5','15-17','0-2','0-2','3-5','0-2','6-8','3-5','3-5','0-2','0-2','0-2','3-5','0-2','0-2','0-2','0-2','9-11','9-11','6-8','0-2','0-2','0-2','0-2','12-14','0-2','6-8','0-2','0-2','0-2','3-5','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','0-2','3-5','3-5','15-17','0-2','3-5','0-2','9-11','3-5','3-5','9-11','0-2','3-5','0-2','0-2','0-2','3-5','3-5','15-17','6-8','3-5','12-14','9-11','6-8','9-11','6-8','3-5','0-2','0-2','0-2','0-2','0-2','6-8','0-2','3-5','6-8','3-5','3-5','12-14','0-2','0-2','0-2','9-11','3-5',24-26,'0-2','0-2','6-8','0-2','0-2','0-2','3-5','9-11','6-8','6-8','15-17','6-8','6-8','0-2','0-2','0-2','3-5','3-5'],
        'node_caps':['no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','yes','yes','yes','yes','yes','yes','no','no','no','no','no','no','no','no','yes','yes','no','no','yes','?','no','yes','no','no','yes','yes','no','no','no','no','yes','no','no','no','no','yes','no','?','?','no','no','yes','no','no','yes','no','yes','yes','yes','no','no','no','no','no','yes','yes','no','?','?','no','no','no','no','yes','no','no','yes','no','yes','no','no','no','yes','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','yes','no','yes','no','yes','no','yes','no','no','?','no','yes','no','no','no','yes','no','yes','no','yes','yes','no','yes','yes','yes','yes','no','no','no','no','yes','yes','no','yes','yes','no','no','yes','no','?','?','yes','yes','yes','no','no','yes','no','yes','yes','yes','yes','yes','yes','yes','yes','yes','no','no','no','no','no'],
        'deg_malig':[3,2,2,2,2,2,2,1,2,2,3,2,1,3,3,1,2,3,3,1,2,2,2,2,2,2,1,3,2,2,3,2,3,1,1,2,2,1,2,1,1,2,1,2,1,1,2,1,1,1,2,2,1,3,1,1,1,2,1,1,2,1,1,2,1,1,1,3,3,2,1,2,2,2,2,1,2,1,2,2,2,1,2,2,1,3,2,1,3,1,2,3,2,2,1,2,2,2,1,2,3,3,2,2,2,1,2,2,3,1,1,1,2,1,2,2,1,3,1,1,1,2,3,1,1,2,2,2,2,2,2,3,2,3,2,2,3,1,2,2,2,2,1,2,3,2,2,2,3,3,3,3,3,3,3,2,3,1,1,1,3,2,2,1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,2,3,3,3,1,3,3,2,1,2,2,2,3,2,2,2,2,2,1,2,2,1,3,2,1,2,2,2,3,2,3,1,2,2,3,1,2,2,2,2,3,1,3,1,3,3,3,3,3,3,3,1,2,2,3,1,3,3,2,2,3,2,2,3,3,3,3,2,3,3,3,2,3,2,1,3,3,3,1,2,2,3,2,3,3,1,1,3,2,3,3,2,3,3,3,2,2,3,3,3,3,3,3,2,3,1,3,3],
        'breast':['left','right','left','right','right','left','left','left','left','right','left','left','left','left','left','left','left','left','left','right','left','left','right','left','right','left','left','right','right','left','right','right','left','right','left','left','left','right','left','left','right','left','left','left','right','left','right','right','right','right','left','left','left','left','right','right','right','right','left','right','left','right','left','right','left','right','right','left','left','left','left','right','left','right','left','left','left','left','left','right','right','left','right','right','left','left','right','left','right','right','right','left','right','right','left','right','left','right','left','left','left','right','right','left','right','right','left','right','right','right','left','right','right','right','right','right','left','left','right','left','left','right','left','right','right','left','right','right','left','right','right','right','left','left','left','right','right','left','left','left','left','left','left','left','left','left','right','left','left','right','right','left','left','right','right','right','right','left','right','left','right','right','right','right','right','right','right','right','right','left','right','left','right','right','left','right','left','left','right','right','right','right','right','left','left','right','left','left','right','right','right','left','left','left','right','left','right','left','left','left','right','left','left','left','left','right','left','left','left','right','left','right','right','right','right','right','left','left','right','right','left','right','left','right','left','right','left','right','right','right','right','right','right','left','right','left','right','right','left','right','left','left','left','right','left','right','left','left','left','left','left','right','left','right','right','right','left','left','left','right','right','left','left','left','left','left','left','left','left','left','left','right','right','right','left','right','left','left','right','left','left','left','left','right','left','left'],
        'breast_quad':['left_low','right_up','left_low','left_up','right_low','left_low','left_low','left_low','left_low','left_up','central','left_low','right_up','right_up','left_up','left_low','left_low','left_low','left_low','right_up','left_low','left_low','left_low','left_up','left_up','left_up','left_low','left_up','left_low','left_low','left_up','left_low','left_low','left_up','left_up','left_up','central','central','left_low','left_low','left_low','left_low','central','left_up','right_up','left_up','left_low','left_up','right_up','left_low','left_low','right_low','left_low','left_up','left_up','right_up','central','right_up','left_up','left_up','central','right_low','left_low','right_up','right_low','left_up','right_low','left_up','left_low','left_low','left_low','left_up','left_up','right_low','right_low','left_low','left_low','central','left_low','central','left_low','left_up','left_low','left_low','right_low','left_up','left_low','right_low','left_up','left_up','central','left_up','left_up','left_up','left_low','right_low','left_up','left_up','right_up','left_low','left_low','left_low','right_low','right_low','left_low','left_up','left_up','right_up','right_up','left_up','left_low','central','left_up','left_up','right_up','left_up','left_low','left_up','left_low','right_low','left_low','right_up','left_up','left_low','left_low','central','right_up','left_up','left_up','left_up','right_up','left_up','left_up','right_up','left_low','central','right_up','left_low','left_low','right_low','left_low','left_low','left_up','left_low','central','right_low','left_up','left_low','central','left_up','left_up','left_low','left_low','left_up','left_up','left_up','left_up','central','central','left_low','left_up','left_low','left_up','left_up','left_low','left_up','left_low','left_up','left_up','left_up','left_up','left_low','right_up','left_up','left_low','right_up','left_low','left_low','left_up','left_low','left_up','left_low','left_low','left_up','left_low','left_low','right_low','left_up','left_up','left_up','right_low','left_up','left_low','right_low','left_up','left_up','left_up','left_low','central','left_low','left_low','left_low','left_low','left_low','right_up','central','?','right_up','right_up','left_up','left_low','central','right_up','left_up','left_low','left_up','left_up','left_up','central','left_low','right_up','left_up','right_low','left_low','left_low','left_low','left_low','left_up','left_low','right_up','left_up','left_up','left_up','left_low','left_up','left_low','left_low','left_low','left_low','right_up','left_low','left_low','left_low','right_up','left_up','left_up','left_low','right_low','left_low','left_low','left_up','left_low','left_up','left_up','right_up','left_up','left_low','left_low','right_low','left_up','right_up','right_low','left_up','left_up','left_low','left_low','right_up','left_low','left_low','left_low','right_low','left_low','left_up','right_up','central','left_up','right_low','left_up','right_up','left_low','left_low','left_up','left_up','left_up','left_low','left_low'],
        'irrad':['no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','yes','no','yes','yes','yes','no','no','yes','no','yes','yes','yes','no','no','no','no','yes','no','yes','yes','yes','no','no','no','no','no','yes','no','yes','no','no','no','no','yes','no','yes','yes','yes','no','no','yes','no','yes','yes','no','no','no','yes','yes','no','no','yes','yes','yes','yes','yes','yes','yes','yes','no','yes','no','no','yes','yes','no','no','yes','no','no','yes','yes','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','no','yes','no','yes','yes','no','yes','no','yes','no','no','yes','yes','yes','yes','no','no','no','yes','yes','no','yes','no','yes','yes','yes','yes','no','no','no','yes','no','no','no','no','yes','yes','yes','no','no','yes','no','no','no','no','no','yes','no','yes','no','yes','no','yes','yes','no','yes','yes','no','yes','yes','no','yes','no','no','no']}

data = pd.DataFrame(data)









class_dropdown = dcc.Dropdown(options=data['class'].unique(),
                            value='recurrence-events',
                            style={"background-color":"#999999", "color": "black"})










app.layout = dbc.Row([
    dbc.Col([
        html.Div(children=[
            html.Div(children=[
                class_dropdown,
                html.H5(children='Recurrence Event by Age group and Menopause state of the Patient'),
                dcc.Graph(id='first-graph')
            ]),
            html.Div(children=[
                html.H5(children='Recurrence Event by Nb. of Invaded Lymph Nodes and Lymph Nodes with Pierced Capsule'),
                dcc.Graph(id='sixth-graph')
            ])
        ])
    ], width=5),
    dbc.Col([
        html.Div(children=[
            html.Div(children=[
                html.H6(children='Recurrence Event by Degree of Malignancy and Size of the Tumour'),
                dcc.Graph(id='second-graph')
            ]),
            html.Div(children=[
                html.H6(children='Recurrence Event by Radiation Therapy and Degree of Malignancy fo the Tumor'),
                dcc.Graph(id='third-graph')
            ])
        ])
    ], width=3),
    dbc.Col([
        html.Div(children=[
            html.Div(children=[
                html.H6(children='Recurrence Event by Breast Location and Tumour Size'),
                dcc.Graph(id='fourth-graph')
            ]),
            html.Div(children=[
                html.H6(children='Recurrence Event by Radiation Therapy and Nb. of Invaded Lymph Nodes'),
                dcc.Graph(id='fifth-graph')
            ])
        ])
    ], width=3)
], justify='center')






@app.callback(
    Output(component_id='first-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='age',
                       color='menopause',
                       nbins=6,
                       labels={
                        "age": "Age Group of the Patient",
                        "menopause": "Menopause State of the Patient"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig









@app.callback(
    Output(component_id='second-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='deg_malig',
                       color='tumour_size',
                       nbins=6,
                       labels={
                        "deg_malig": "Degree of Malignancy",
                        "tumour_size": "Size of the Tumour (mm)"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig









@app.callback(
    Output(component_id='third-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='deg_malig',
                       color='irrad',
                       nbins=6,
                       labels={
                        "deg_malig": "Degree of Malignancy",
                        "irrad": "Radiation as a Therapy"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig








@app.callback(
    Output(component_id='fourth-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='tumour_size',
                       color='breast',
                       nbins=6,
                       labels={
                        "tumour_size": "Size of the Tumour (mm)",
                        "breast": "Location of the Breast"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig








@app.callback(
    Output(component_id='fifth-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='inv_nodes',
                       color='irrad',
                       nbins=6,
                       labels={
                        "irrad": "Radiation as a Therapy",
                        "inv_nodes": "Nb. of Invaded Lymph Nodes"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig







@app.callback(
    Output(component_id='sixth-graph', component_property='figure'),
    Input(component_id=class_dropdown, component_property='value')
)
def update_graph(selected_class):
    filtered_class = data[data['class'] == selected_class]
    bar_fig = px.histogram(filtered_class,
                       x='inv_nodes',
                       color='node_caps',
                       nbins=6,
                       labels={
                        "inv_nodes": "Nb. of Invaded Lymph Nodes",
                        "node_caps": "Lymph Node Capsules Perforated"
                       },
                       title=f'Watching the filtered Class_: {selected_class}')
    bar_fig.update_layout({
        'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
    }, font_color = 'white', barmode='overlay')
    return bar_fig















if __name__ == '__main__':
    application.run(debug=True)