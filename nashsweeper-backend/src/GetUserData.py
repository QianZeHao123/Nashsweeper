from flask import Blueprint

bp = Blueprint('GetUserData', __name__, url_prefix='/GetUserData')


@bp.route('/test')
def get_user_rank():
    user_rank = [
        {'index': 1, 'PlayerID': 'CIEG',
            'TotalStrategies': 64, 'Time': 200},
        {'index': 2, 'PlayerID': 'Linyuan',
            'TotalStrategies': 72, 'Time': 220},
        {'index': 3, 'PlayerID': 'QianZehao',
            'TotalStrategies': 38, 'Time': 230},
        {'index': 4, 'PlayerID': 'Test1',
            'TotalStrategies': 96, 'Time': 240},
        {'index': 5, 'PlayerID': 'Test2',
            'TotalStrategies': 27, 'Time': 250},
        {'index': 6, 'PlayerID': 'Test3',
            'TotalStrategies': 15, 'Time': 260},
        {'index': 7, 'PlayerID': 'Test4',
            'TotalStrategies': 45, 'Time': 270},
        {'index': 8, 'PlayerID': 'Test5',
            'TotalStrategies': 27, 'Time': 280},
        {'index': 9, 'PlayerID': 'Test6',
            'TotalStrategies': 89, 'Time': 290},
        {'index': 10, 'PlayerID': 'Test7',
            'TotalStrategies': 56, 'Time': 300},
        {'index': 11, 'PlayerID': 'Test8',
            'TotalStrategies': 75, 'Time': 310},
        {'index': 12, 'PlayerID': 'Test9',
            'TotalStrategies': 100, 'Time': 320},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},

    ]
    return user_rank
