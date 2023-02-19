import re
import sys

COLLECTIBLES = [
    {'name': 'Coffee Thermoses', 'config_name': b'THERMOS', 'amount': 100},
    {'name': 'Can Pyramids', 'config_name': b'CANPYRAMIDS', 'amount': 12},
    {'name': 'Chests', 'config_name': b'CHESTS', 'amount': 30},
    {'name': 'Radio Shows', 'config_name': b'RADIOSHOWS', 'amount': 11},
    {'name': 'TV Shows', 'config_name': b'TVSHOWS', 'amount': 14},
    {'name': 'Signs', 'config_name': b'SIGNS', 'amount': 25},
    {'name': 'Coconut Song played on Jukebox', 'config_name': b'COCONUTSONGS', 'amount': 2},
    {'name': 'Alarm Clocks', 'config_name': b'DLC1_ALARMCLOCKS', 'amount': 10},
    {'name': 'Cardboard Standees', 'config_name': b'DLC1_CARDBOARDCUTOUTS', 'amount': 6},
    {'name': 'Night Springs Video Games', 'config_name': b'DLC2_NIGHTSPRINGSVIDEOGAMES', 'amount': 10},
]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid number of Arguments.\nUsage: python alan_find.py "/path/to/config"', file=sys.stderr)
        sys.exit(1)
    alan_wake_config = sys.argv[1]
    with open(alan_wake_config, 'rb') as config:
        config_content = bytearray(config.read())
        for i in COLLECTIBLES:
            config_hunk = re.search(i['config_name']+b'(.)(.*?)(.)\x00\x00\x00', config_content, flags=re.DOTALL)
            # do not crash if user does not have DLCs
            if config_hunk is not None:
                amount_found = int.from_bytes(config_hunk.group(1), 'big')
                found_collectibles = list(str(x) for x in config_hunk.group(2))
                missing_collectibles = [str(x) for x in range(1, i['amount']+1) if str(x) not in found_collectibles]
                print('{}: {}/{}'.format(i['name'], amount_found, i['amount']))
                if len(found_collectibles) != 0:
                    print('\tFound: {}'.format(', '.join(found_collectibles)))
                if len(missing_collectibles) != 0:
                    print('\tMissing: {}'.format(', '.join(missing_collectibles)))
                print('\tDecimal value of the additional byte is {}'.format(ord(config_hunk.group(3))))
